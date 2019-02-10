import pygame


class MainGame:
    screen_width = 700
    screen_height = 550

    @classmethod
    def display(cls):
        pygame.init()
        pygame.display.set_mode((cls.screen_width, cls.screen_height))
        pygame.display.set_caption("Tank Game V2.0")
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYUP:
                    print("You released a key!")
                if event.type == pygame.KEYDOWN:
                    print("You pressed a key!")
                    if event.key == pygame.K_UP:
                        print("You pressed UP arrow key!")
                    if event.key == pygame.K_DOWN:
                        print("You pressed DOWN arrow key!")
                    if event.key == pygame.K_LEFT:
                        print("You pressed LEFT arrow key!")
                    if event.key == pygame.K_RIGHT:
                        print("You pressed RIGHT arrow key!")
            pygame.font.init()
            pygame.display.get_surface().blit(
                pygame.font.SysFont("arial", 16).render("The amount of the enemy tanks: ", False, [255, 0, 0]),
                (0, 0))
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
