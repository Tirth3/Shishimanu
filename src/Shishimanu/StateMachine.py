import pygame

class AnimationState:
    def __init__(self, frames, frame_duration=100, loop=True):
        """
        frames: list of pygame.Surface
        frame_duration: ms per frame
        loop: should the animation repeat
        """
        self.frames = frames
        self.frame_duration = frame_duration
        self.loop = loop
        self.reset()

    def reset(self):
        self.current_frame = 0
        self.timer = 0
        self.finished = False

    def update(self, dt):
        if self.finished:
            return
        self.timer += dt
        if self.timer >= self.frame_duration:
            self.timer -= self.frame_duration
            self.current_frame += 1
            if self.current_frame >= len(self.frames):
                if self.loop:
                    self.current_frame = 0
                else:
                    self.current_frame = len(self.frames) - 1
                    self.finished = True

    def get_frame(self):
        return self.frames[self.current_frame]


class StateMachine:
    def __init__(self):
        self.states = {}
        self.current = None

    def add_state(self, name, state: AnimationState):
        self.states[name] = state
        if self.current is None:
            self.current = name

    def set_state(self, name):
        if name in self.states and name != self.current:
            self.current = name
            self.states[name].reset()

    def update(self, dt):
        if self.current:
            self.states[self.current].update(dt)

    def get_frame(self):
        if self.current:
            return self.states[self.current].get_frame()
        return None
