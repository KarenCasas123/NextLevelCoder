from tabnanny import check
from dino_runner.components.Obstacles.special_attack import Special_attack
from dino_runner.utils.constants import BONE
from dino_runner.utils.constants import BLUE
import random
import pygame


class BoneManager():
    def __init__(self):
        self.Bones = []
        self.blue_time_up = 5000
        self.blue = False

    def update(self, game):
        if len(self.Bones) == 0:
            self.sort = random.randint(0,10000)
            if self.sort == 1:
                self.Bones.append(Special_attack(BONE))

        for bone in self.Bones:
            bone.update(game.game_speed, self.Bones)
            if game.player.dino_rect.colliderect(bone.rect):
                self.Bones.pop()
                pygame.time.delay(500)
                self.start_time = pygame.time.get_ticks()
                    

    def draw(self, screen):
        for bone in self.Bones:
            bone.draw(screen)
        if self.blue:
            self.check_blue(screen)

    def check_blue(self,screen):
        time_to_show = round ((self.blue_time_up - pygame.time.get_ticks()) / 1000, 1)
        if time_to_show >= 0:
             screen.blit(BLUE)
        else:
            self.blue = False