import pygame

# TODO: change border detection to use image size instead of constants

# Init pygame
pygame.init()

# Create screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Set title
pygame.display.set_caption("CatMouse")
# Load and set icon
icon = pygame.image.load("images/catlogo.png")
pygame.display.set_icon(icon)
# Keep track of all our feline friends in play
cats = []


class Player:
    image = pygame.image.load("images/mouse.png")
    image = pygame.transform.scale(image, (75, 40))
    deltaX = 0
    deltaY = 0
    vel = 3

    def __init__(self):
        self.direction = 0
        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT / 2

    def show(self):
        # print(f"self.x:{self.x}\nself.y:{self.y}")
        if (self.direction == 0):
            screen.blit(self.image, (self.x, self.y))
        else:
            screen.blit(pygame.transform.flip(Player.image, True, False), (self.x, self.y))

    def updatePosition(self):
        self.x += self.deltaX
        self.y += self.deltaY


class Cat:
    image = pygame.image.load("images/cat.png")
    image = pygame.transform.scale(image, (75, 65))

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        screen.blit(Cat.image, (self.x, self.y))


if __name__ == "__main__":
    running = True
    player = Player()
    while running:

        pygame.time.delay(10)

        screen.fill((0, 200, 120))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for cat in cats:
            cat.show()

        keys = pygame.key.get_pressed()

        if (not keys[pygame.K_LEFT]) or (not keys[pygame.K_RIGHT]):
            player.deltaX = 0
        if (not keys[pygame.K_UP]) or (not keys[pygame.K_DOWN]):
            player.deltaY = 0

        if keys[pygame.K_y]:
            cats.append(Cat(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

        if keys[pygame.K_LEFT]:
            player.direction = 0
            player.deltaX = -1 * player.vel

        if keys[pygame.K_RIGHT]:
            player.direction = 1
            player.deltaX = player.vel

        if keys[pygame.K_UP]:
            player.deltaY = -1 * player.vel

        if keys[pygame.K_DOWN]:
            player.deltaY = player.vel

        if (player.x >= (screen.get_width() - 75)):
            player.x = screen.get_width() - 75
        elif (player.x <= 0):
            player.x = 0
        if (player.y >= screen.get_height() - 40):
            player.y = screen.get_height() - 40
        elif (player.y <= 0):
            player.y = 0

        player.updatePosition()
        player.show()

        pygame.display.update()
