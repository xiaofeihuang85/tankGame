import pygame


class MainGame:

    @classmethod
    def display(cls):
        pygame.init()
        screen = pygame.display.set_mode((400, 300))
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
