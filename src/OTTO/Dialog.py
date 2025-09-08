import pygame


class Dialog:
    def __init__(self, dialog_list, font, box_rect, text_color=(255, 255, 255), box_color=(0, 0, 0)):
        """
        dialog_list: list of strings
        font: pygame.font.Font object
        box_rect: pygame.Rect defining the dialog box position and size
        text_color: text color
        box_color: background color
        """
        self.dialog_list = dialog_list
        self.font = font
        self.box_rect = box_rect
        self.text_color = text_color
        self.box_color = box_color

        self.current_index = 0
        self.active = True if dialog_list else False
        self.cooldown = 200  # ms to avoid multiple triggers on one keypress
        self.last_press = 0

    def advance(self):
        """Go to the next dialog line"""
        if self.current_index < len(self.dialog_list) - 1:
            self.current_index += 1
        else:
            self.active = False  # all dialogs finished

    def handle_input(self, keys):
        """Check if W is pressed to advance"""
        current_time = pygame.time.get_ticks()
        if keys[pygame.K_SPACE] and current_time - self.last_press > self.cooldown:
            self.advance()
            self.last_press = current_time

    def draw(self, screen):
        """Draw current dialog line if active"""
        if not self.active:
            return

        # Draw box
        pygame.draw.rect(screen, self.box_color, self.box_rect)
        pygame.draw.rect(screen, (255, 255, 255), self.box_rect, 2)  # border

        # Render text
        text = self.dialog_list[self.current_index]
        words = text.split(" ")
        lines = []
        current_line = ""

        # Wrap text
        for word in words:
            test_line = current_line + word + " "
            if self.font.size(test_line)[0] < self.box_rect.width - 20:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word + " "
        lines.append(current_line)

        # Draw lines
        for i, line in enumerate(lines):
            txt_surf = self.font.render(line, True, self.text_color)
            screen.blit(txt_surf, (self.box_rect.x + 10,
                        self.box_rect.y + 10 + i*25))
