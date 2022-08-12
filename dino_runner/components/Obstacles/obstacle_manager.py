from dino_runner.components.Obstacles.Cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.utils.constants import SCREEN_WIDTH
from dino_runner.utils.constants import LIVES

import pygame


class ObstacleManager():
    def __init__(self):
        self.obstacles = []
        self.lives = LIVES


    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    self.lives -= 1
                    self.obstacles.pop()
                    if self.lives <= 0:
                        pygame.time.delay(500)
                        game.playing = False
                        break
                    

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        font = pygame.font.Font('freesansbold.ttf', 18)
        label = 'lives'

        if self.lives == 1:
            label = 'live'

        text = font.render(f'{self.lives} {label}', True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (SCREEN_WIDTH-30,20)
        screen.blit(text, text_rect)