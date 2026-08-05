import pygame
import sys

# Pygame-ni ishga tushirish
pygame.init()

# Oyna sozlamalari
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Example")

clock = pygame.time.Clock()

# Ranglar
WHITE = (255, 255, 255)
BLUE = (50, 120, 255)

# O'yinchi
player = pygame.Rect(100, 100, 50, 50)

speed = 5

running = True

while running:

    # Hodisalar
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Tugmalar
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= speed

    if keys[pygame.K_RIGHT]:
        player.x += speed

    if keys[pygame.K_UP]:
        player.y -= speed

    if keys[pygame.K_DOWN]:
        player.y += speed

    # Chegaradan chiqmasin
    player.x = max(0, min(player.x, WIDTH - player.width))
    player.y = max(0, min(player.y, HEIGHT - player.height))

    # Ekranni tozalash
    screen.fill(WHITE)

    # Kvadrat chizish
    pygame.draw.rect(screen, BLUE, player)

    # Ekranni yangilash
    pygame.display.flip()

    # FPS
    clock.tick(60)

pygame.quit()
sys.exit()