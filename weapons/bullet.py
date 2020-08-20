import pygame
from configurations.size_configurations import BULLET_SIZE
from configurations.files_configurations import PATH_TO_WEAPONS, LEFT_BULLET_NAME, RIGHT_BULLET_NAME
from configurations.modes_configuration import LEFT, RIGHT, UP, DOWN
from game.game import Game


class Bullet(pygame.sprite.Sprite):
    def __init__(self, owner, game: Game):
        super(Bullet, self).__init__()

        self.owner = owner
        self.game = game

        self.left_bullet = pygame.transform.scale(pygame.image.load(f'{PATH_TO_WEAPONS}/{LEFT_BULLET_NAME}'), BULLET_SIZE)
        self.right_bullet = pygame.transform.scale(pygame.image.load(f'{PATH_TO_WEAPONS}/{RIGHT_BULLET_NAME}'), BULLET_SIZE)
        self.image: pygame.image.Image = self.left_bullet

        self.direction_x = None
        self.direction_y = None
        self.speed_x = None
        self.speed_y = None

        self.rect: pygame.Rect = self.image.get_rect()

    def set_direction_x(self, direction):
        self.direction_x = direction
        self.image = self.left_bullet if direction == LEFT else self.right_bullet

    def set_coord(self, topleft):
        self.rect.topleft = topleft

    def move(self):
        sign_x = 1 if self.direction_x == RIGHT else -1
        sign_y = 1 if self.direction_y == DOWN else -1
        self.rect.x += sign_x * self.speed_x
        self.rect.y += sign_y * self.speed_y

        if pygame.sprite.spritecollide(self, self.game.map_blocks_group, False):
            self.kill()

    def set_bullet_speed_x(self, speed):
        self.speed_x = speed

    def set_bullet_speed_y(self, speed):
        self.speed_y = speed

    def start(self):
        self.game.map_bullets_group.add(self)
