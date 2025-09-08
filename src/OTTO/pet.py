import pygame

from OTTO.Helper import *
from OTTO.StateMachine import *


class Pet():
    def __init__(self, x, y):
        self.pos = [x, y]
        self.size = (200, 200)

        # Build animations
        idle_frames = [pygame.transform.scale(load_image(
            f"otter/idle/{i}.png"), self.size) for i in range(1, 13)]
        run_frames = [pygame.transform.scale(load_image(
            f"otter/run/{i}.png"), self.size) for i in range(1, 4)]
        sleep_frames = [pygame.transform.scale(load_image(
            f"otter/sleep/{i}.png"), self.size) for i in range(1, 7)]

        # Create state machine
        self.animations = StateMachine()
        self.animations.add_state("Idle", AnimationState(
            idle_frames, frame_duration=120, loop=True))
        self.animations.add_state("Moving", AnimationState(
            run_frames, frame_duration=80, loop=True))
        self.animations.add_state("Sleeping", AnimationState(
            sleep_frames, frame_duration=200, loop=True))

        self.animations.set_state("Idle")

        self.rect = idle_frames[0].get_rect(center=self.pos)
        self.target_pos = self.pos[:]
        self.dir = 0

        self.isreached = True

        self.Status = {
            "Sleep": 100,
            "Fun": 100,
            "Hunger": 100,
            "Health": 100
        }
        self.speed = 100

    def Update(self, dt):
        dt_sec = dt / 1000.0

        if self.Status["Sleep"] <= 10 and self.animations.current == "Idle":
            self.animations.set_state("Sleeping")

        if self.animations.current == "Idle":
            self.Status["Sleep"] -= dt * 0.001

        elif self.animations.current == "Moving":

            dx = self.target_pos[0] - self.pos[0]
            dy = self.target_pos[1] - self.pos[1]
            dist = math.hypot(dx, dy)

            if dist > 1:
                # Normalize and move
                dx /= dist
                dy /= dist
                self.pos[0] += dx * self.speed * dt_sec
                self.pos[1] += dy * self.speed * dt_sec

                # Direction for rotation (atan2 expects y flipped)
                self.dir = math.atan2(-dy, dx)
            else:
                # Arrived
                self.animations.set_state("Idle")

            self.Status["Sleep"] -= dt * 0.01

        elif self.animations.current == "Sleeping":
            self.Status["Sleep"] += dt * 0.01
            self.State_timer = 0
            self.pos[0] += dx
            self.pos[1] += dy

        # print(self.Status["Sleep"])

        # update animation
        self.animations.update(dt)

    def Draw(self, screen):
        frame = self.animations.get_frame()
        if self.animations.current == "Moving":
            blitRotateCenter(screen, frame, self.pos, self.dir * 57.2958)
        elif self.animations.current == "Sleeping":
            blitRotateCenter(screen, frame, self.pos, self.dir * 0.0)
        elif self.animations.current == "Idle":
            blitRotateCenter(screen, frame, self.pos, self.dir * 0.0)
