import pygame
import random

from OTTO.Helper import *
from OTTO.StateMachine import *
from OTTO.Dialog import *


class Pet():
    def __init__(self, x, y, font):
        self.pos = [x, y]
        self.size = (200, 200)
        self.sSize = (x * 2, y * 2)

        # Build animations
        idle_frames = [pygame.transform.scale(load_image(
            f"otter/idle/{i}.png"), self.size) for i in range(1, 13)]
        run_frames = [pygame.transform.scale(load_image(
            f"otter/run/{i}.png"), self.size) for i in range(1, 4)]
        sleep_frames = [pygame.transform.scale(load_image(
            f"otter/sleep/{i}.png"), self.size) for i in range(1, 7)]
        spin_frames = [pygame.transform.scale(load_image(
            f"otter/spin/{i}.png"), self.size) for i in range(1, 3)]

        # Create state machine
        self.animations = StateMachine()
        self.animations.add_state("Idle", AnimationState(
            idle_frames, frame_duration=120, loop=True))
        self.animations.add_state("Moving", AnimationState(
            run_frames, frame_duration=80, loop=True))
        self.animations.add_state("Sleeping", AnimationState(
            sleep_frames, frame_duration=200, loop=True))
        self.animations.add_state("Spin", AnimationState(
            spin_frames, frame_duration=200, loop=True))

        self.animations.set_state("Idle")

        self.rect = idle_frames[0].get_rect(center=self.pos)
        self.target_pos = self.pos[:]
        self.dir = 0

        self.isreached = True

        self.Status = {
            "Sleep": 100,
            "Fun": 100,
        }
        self.speed = 100

        self.move_timer = 0
        self.move_time = 10

        self.spin_timer = 0
        self.spin_time = 100

    def Update(self, dt):
        dt_sec = dt / 1000.0

        if self.animations.current == "Spin":
            self.spin_timer += dt_sec
        if self.spin_timer >= self.spin_time:
            self.spin_timer = 0
            self.animations.set_state("Idle")

        if self.move_timer >= self.move_time:
            self.move_timer = 0
            tarpos = (random.randint(
                0, self.sSize[0] - self.size[0]), random.randint(
                0, self.sSize[1] - self.size[1]))
            self.target_pos = tarpos[:]
            self.animations.set_state("Moving")

        if self.animations.current != "Moving":
            self.move_timer += dt_sec

        print(f"{self.move_timer} , {self.animations.current}")

        if self.Status["Sleep"] <= 10 and self.animations.current == "Idle":
            self.animations.set_state("Sleeping")

        if self.animations.current == "Idle":
            self.Status["Sleep"] -= dt_sec * 0.5

        elif self.animations.current == "Moving":
            self.move_timer = 0

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

            self.Status["Sleep"] -= dt_sec * 0.75

        elif self.animations.current == "Sleeping" and self.Status["Sleep"] <= 90:
            self.Status["Sleep"] += dt_sec
            self.State_timer = 0
        # print(self.Status["Sleep"])

        # update animation
        self.animations.update(dt)

    def Check_Mouse_Click(self, mouse_pos):
        if (self.pos[0] <= mouse_pos[0] and self.pos[0] + self.size[0] >= mouse_pos[0]) and (self.pos[1] <= mouse_pos[1] and self.pos[1] + self.size[1] >= mouse_pos[1]):
            return True
        return False

    def Draw(self, screen):
        frame = self.animations.get_frame()
        if self.animations.current == "Moving":
            blitRotateCenter(screen, frame, self.pos, self.dir * 57.2958)
        elif self.animations.current == "Sleeping":
            blitRotateCenter(screen, frame, self.pos, self.dir * 0.0)
        elif self.animations.current == "Spin":
            blitRotateCenter(screen, frame, self.pos, self.dir * 0.0)
        elif self.animations.current == "Idle":
            blitRotateCenter(screen, frame, self.pos, self.dir * 0.0)
