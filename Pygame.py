import pygame

pygame.init()

WIDTH = 800
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")

clock = pygame.time.Clock()

test_font = pygame.font.Font("assets/Minecraft.ttf", 40)

ground_surface = pygame.image.load("assets/full_game_image.png").convert()
ground_surface = pygame.transform.scale(ground_surface, (WIDTH, HEIGHT))

snail = pygame.image.load('assets/image-removebg-preview.png').convert_alpha()
snail = pygame.transform.scale(snail, (75, 100))


text_surface = test_font.render("My Game", True, "Blue")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(ground_surface, (0, 0))
    screen.blit(text_surface, (300, 50))
    screen.blit(snail, (120,150))

    pygame.display.update()
    clock.tick(60)

pygame.quit()