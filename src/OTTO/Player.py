import pygame

from OTTO.Helper import *


class Spritesheet:
    def __init__(self, filename):
        self.sheet = load_image(filename)

    def get_image(self, frame, width, height, scale, row=0):
        """Extract a frame from the given row and column"""
        image = pygame.Surface((width, height), pygame.SRCALPHA)
        image.blit(self.sheet, (0, 0),
                   (frame * width, row * height, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        return image


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, spritesheet, frame_width, frame_height, ssize, scale=2):
        super().__init__()
        self.sSize = ssize
        self.spritesheet = spritesheet
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.scale = scale

        # Physics
        self.vel_y = 0
        self.speed = 100
        self.jump_power = -1000
        self.on_ground = False

        # Animations dictionary (row index for each action)
        self.animations = {
            "idle": [],
            "run": [],
            "jump": []
        }
        self.load_animations()

        self.action = "idle"
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

        # Sprite setup
        self.image = self.animations[self.action][self.frame_index]
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.direction = 1  # 1 = right, -1 = left

    def load_animations(self):
        # Adjust frame counts & row indices for your spritesheet layout
        for i in range(4):  # idle frames
            self.animations["idle"].append(
                self.spritesheet.get_image(
                    i, self.frame_width, self.frame_height, self.scale, row=0)
            )
        for i in range(6):  # run frames
            self.animations["run"].append(
                self.spritesheet.get_image(
                    i, self.frame_width, self.frame_height, self.scale, row=1)
            )
        for i in range(2):  # jump frames
            self.animations["jump"].append(
                self.spritesheet.get_image(
                    i, self.frame_width, self.frame_height, self.scale, row=2)
            )

    def set_action(self, new_action):
        """Change action and reset frame index to avoid index errors"""
        if self.action != new_action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def update(self, keys, dt, gravity=50):
        dx, dy = 0, 0

        # Movement
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx = -self.speed * dt
            self.direction = -1
            self.set_action("run")
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx = self.speed * dt
            self.direction = 1
            self.set_action("run")
        # Jumping
        elif keys[pygame.K_w] and self.on_ground:
            self.vel_y = self.jump_power
            self.on_ground = False
            self.set_action("jump")
        elif self.on_ground:
            self.set_action("idle")

        # Apply gravity
        self.vel_y += gravity
        dy += self.vel_y * dt

        # Update rect
        self.rect.x += dx
        self.rect.y += dy

        # Simple floor collision
        if self.rect.bottom >= self.sSize[1]:  # Example "ground"
            self.rect.bottom = self.sSize[1]
            self.vel_y = 0
            self.on_ground = True

        # Update animation
        self.update_animation()

    def update_animation(self):
        ANIM_COOLDOWN = 120  # ms per frame
        current_time = pygame.time.get_ticks()

        if current_time - self.update_time > ANIM_COOLDOWN:
            self.update_time = current_time
            self.frame_index += 1
            if self.frame_index >= len(self.animations[self.action]):
                self.frame_index = 0

        # Set current frame
        self.image = self.animations[self.action][self.frame_index]

        # Flip if facing left
        if self.direction == -1:
            self.image = pygame.transform.flip(self.image, True, False)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
