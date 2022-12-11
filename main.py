import random
import pygame

WIDTH, HEIGHT = SCR_DIM = 800, 800
TILES_DIM = 25, 25
FPS = 6

APPLE_COUNT = 1
GRASS_COLOUR = (89, 108, 55)
SECONDARY_GRASS_COLOUR = (82, 99, 53)

pygame.init()
screen = pygame.display.set_mode(SCR_DIM)
pygame.display.set_caption("Course - Snake")
clock = pygame.time.Clock()

class GameOverException(Exception):
    def __str__(self):
        return "The game has ended!"

class Player:
    def __init__(self):
        self.tiles = []

    def update(self, direction):
        recent = self.tiles[-1]
        new = recent.x + direction[0], recent.y + direction[1]

        for apple in apples:
            if new == (apple.x, apple.y):
                apple.kill()
                Apple()
                break
        else:
            self.tiles[0].kill()

        if new[0] < 0 or new[1] < 0 or new[0] > TILES_DIM[0] or new[1] > TILES_DIM[1]:
            raise GameOverException()

        for tile in self.tiles:
            if new[0] == tile.x and new[1] == tile.y:
                raise GameOverException()

        PlayerTile(*new, recent.idx + 1, self)

tiles = []
class Tile:
    def __init__(self, x, y, colour):
        tiles.append(self)
        self.x = x
        self.y = y
        self.colour = colour

    def draw(self):
        scale = (WIDTH // TILES_DIM[0], HEIGHT // TILES_DIM[1])
        pygame.draw.rect(screen, self.colour, (self.x * scale[0], self.y * scale[1], scale[0], scale[1]))

class PlayerTile(Tile):
    def __init__(self, x, y, idx, player: Player):

        colour = (29, 108, 62) if not idx % 2 else (18, 139, 76)
        super().__init__(x, y, colour)

        self.idx = idx
        self.player = player
        self.player.tiles.append(self)

    def kill(self):
        tiles.remove(self)
        self.player.tiles.remove(self)

apples = []
class Apple(Tile):
    def __init__(self):
        apples.append(self)

        player_positions = [(tile.x, tile.y) for tile in player.tiles]
        while True:
            x, y = random.randint(0, TILES_DIM[0]), random.randint(0, TILES_DIM[1])
            if (x, y) not in player_positions:
                break

        super().__init__(x, y, (206, 56, 45))

    def kill(self):
        tiles.remove(self)
        apples.remove(self)

player = Player()

for x in range(TILES_DIM[0]):
    for y in range(TILES_DIM[1]):
        colour = GRASS_COLOUR if not y // 2 % 2 else SECONDARY_GRASS_COLOUR
        Tile(x, y, colour)

for i in range(5):
    PlayerTile(TILES_DIM[0] // 2, i + 3, i, player)

for i in range(APPLE_COUNT):
    Apple()

direction = (0, 1)
running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pygame.K_d and direction != (-1, 0):
                direction = (1, 0)
            if event.key == pygame.K_w and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_s and direction != (0, -1):
                direction = (0, 1)

    try:
        player.update(direction)
    except:
        running = False

    for tile in tiles:
        tile.draw()
    pygame.display.flip()
    clock.tick(FPS)

print("Game over!")
pygame.quit()
