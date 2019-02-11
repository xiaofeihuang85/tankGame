import pygame


class MainScreen:
    screen_width = 700
    screen_height = 550

    @classmethod
    def display(cls):
        pygame.init()
        done = False
        my_tank = MyTank("up", (50, 50))

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYUP:
                    print("You released a key!")
                if event.type == pygame.KEYDOWN:
                    print("You pressed a key!")
                    my_tank.move(event.key, (cls.screen_width, cls.screen_height))
            pygame.display.init()
            pygame.display.set_mode((cls.screen_width, cls.screen_height))
            pygame.display.set_caption("Tank Game V2.0")
            pygame.font.init()
            pygame.display.get_surface().blit(
                pygame.font.SysFont("arial", 16, True).render("The amount of the enemy tanks: ", False, [255, 0, 0]),
                (0, 0))
            pygame.display.get_surface().blit(my_tank.image, my_tank.position)
            pygame.display.flip()


class Base(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


class Tank(Base):
    def __init__(self, direction, position):
        self.direction = direction
        self.position = position


class MyTank(Tank):
    speed = 20
    width = 35
    height = 34
    images = (
        pygame.image.load("images/tankU.gif"),
        pygame.image.load("images/tankR.gif"),
        pygame.image.load("images/tankD.gif"),
        pygame.image.load("images/tankL.gif"))

    def __init__(self, direction, position):
        self.direction = direction
        self.position = position
        self.image = MyTank.images[0]

    def move(self, key, screen_size):
        if key == pygame.K_UP:
            print("You pressed UP arrow key!")
            self.image = MyTank.images[0]
            self.position = (
                self.position[0], self.position[1] - MyTank.speed if self.position[1] - MyTank.speed >= 0 else 0)
        elif key == pygame.K_DOWN:
            print("You pressed DOWN arrow key!")
            self.image = MyTank.images[2]
            self.position = (
                self.position[0],
                self.position[1] + MyTank.speed if self.position[1] + MyTank.speed <= screen_size[
                    1] - MyTank.height else screen_size[
                                                1] - MyTank.height)
        elif key == pygame.K_LEFT:
            print("You pressed LEFT arrow key!")
            self.image = MyTank.images[3]
            self.position = (
                self.position[0] - MyTank.speed if self.position[0] - MyTank.speed >= 0 else 0, self.position[1])
        elif key == pygame.K_RIGHT:
            print("You pressed RIGHT arrow key!")
            self.image = MyTank.images[1]
            self.position = (
                self.position[0] + MyTank.speed if self.position[0] + MyTank.speed <= screen_size[0] - MyTank.width else
                screen_size[
                    0] - MyTank.width, self.position[1])


class EnemyTank(Tank):
    pass


class Bullet:
    pass


class Explosion:
    pass


class SoundEffect:
    pass


MainScreen.display()
