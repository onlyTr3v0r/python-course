import random
import pygame

SCR_DIM = 800, 800
TILES_DIM = 25, 25
SCALE = (SCR_DIM[0] // TILES_DIM[0], SCR_DIM[1] // TILES_DIM[1])
FPS = 5

APPLE_COLOUR = (206, 56, 45)
APPLE_COUNT = 3

GRASS_COLOUR = (89, 108, 55)
SECONDARY_GRASS_COLOUR = (82, 99, 53)

pygame.init()
screen = pygame.display.set_mode(SCR_DIM)
pygame.display.set_caption("Python Course")
clock = pygame.time.Clock()

def draw_tile(x, y, colour):
    pos = (x * SCALE[0], y * SCALE[1])
    pygame.draw.rect(screen, colour, (*pos, *SCALE))

apples = []
def generate_apple():
    while True:
        x = random.randint(0, TILES_DIM[0] - 1)
        y = random.randint(0, TILES_DIM[1] - 1)
        if (x, y) not in apples:
            break

    apples.append((x, y))

for _ in range(3):
    generate_apple()

running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for x in range(TILES_DIM[0]):
        for y in range(TILES_DIM[1]):
            colour = GRASS_COLOUR if not (y // 2) % 2 else SECONDARY_GRASS_COLOUR
            draw_tile(x, y, colour)

    for x, y in apples:
        draw_tile(x, y, APPLE_COLOUR)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()