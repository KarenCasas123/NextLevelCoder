from dino_runner.components.Obstacles.obstacle import Obstacle
import random
import pygame

class Cactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0,2)
        super().__init__(image, self.type)
        self.rect.y = 325