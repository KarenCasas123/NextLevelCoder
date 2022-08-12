from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH

class Special_attack(Sprite): 
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.y = 325
        self.rect.x = -10

    def update(self, game_speed, Bone):
        self.rect.x += game_speed
        if self.rect.x > SCREEN_WIDTH:
            Bone.pop()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
