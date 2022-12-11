import pygame

WIDTH, HEIGHT = SCR_DIM = 800, 800
FPS = 10

pygame.init()
screen = pygame.display.set_mode(SCR_DIM)
pygame.display.set_caption("Course - Snake")
clock = pygame.time.Clock()

running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()