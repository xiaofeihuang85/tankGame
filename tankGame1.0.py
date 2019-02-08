import pygame


class MainGame:
    screen_width = 700
    screen_height = 550

    @classmethod
    def display(cls):
        pygame.init()
        pygame.display.set_mode((cls.screen_width, cls.screen_height))
        pygame.display.set_caption("Tank Game V1.0")
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            pygame.display.flip()


class Tank:
    pass


class MyTank(Tank):
    pass


class EnemyTank(Tank):
    pass


class Bullet:
    pass


class Explosion:
    pass


class SoundEffect:
    pass


MainGame.display()
