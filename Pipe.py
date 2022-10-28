import random
import pygame


from constant import SCREENHEIGHT, PIPE_GAP_SIZE, SCREENWIDTH


class Pipe(pygame.sprite.Sprite):
    def __init__(self, image, position, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.left, self.rect.top = position
        self.used_for_score = False

    @staticmethod
    def randomPipe(image):
        base_y = 0.79 * SCREENHEIGHT
        up_y = int(base_y * 0.2) + random.randrange(
            0, int(base_y * 0.6 - PIPE_GAP_SIZE)
        )
        return {
            "top": (SCREENWIDTH + 10, up_y - image.get_height()),
            "bottom": (SCREENWIDTH + 10, up_y + PIPE_GAP_SIZE),
        }
