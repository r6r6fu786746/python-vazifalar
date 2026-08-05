import pygame
import sys

# Simple side-scrolling platformer example using Pygame
# Controls: Left/Right arrows to move, Space to jump, ESC to quit

WIDTH, HEIGHT = 800, 600
FPS = 60
GRAVITY = 0.8

class Player:
    def __init__(self, x, y):
        self.width = 40
        self.height = 60
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.color = (50, 200, 50)
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 6
        self.jump_strength = 16
        self.on_ground = False

    def handle_input(self, keys):
        self.vel_x = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vel_x = -self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vel_x = self.speed
        if (keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]) and self.on_ground:
            self.vel_y = -self.jump_strength
            self.on_ground = False

    def apply_gravity(self):
        self.vel_y += GRAVITY
        if self.vel_y > 25:
            self.vel_y = 25

    def move_and_resolve(self, platforms):
        # Horizontal movement
        self.rect.x += int(self.vel_x)
        for p in platforms:
            if self.rect.colliderect(p):
                if self.vel_x > 0:  # moving right
                    self.rect.right = p.left
                elif self.vel_x < 0:  # moving left
                    self.rect.left = p.right
        # Vertical movement
        self.rect.y += int(self.vel_y)
        self.on_ground = False
        for p in platforms:
            if self.rect.colliderect(p):
                if self.vel_y > 0:  # falling
                    self.rect.bottom = p.top
                    self.vel_y = 0
                    self.on_ground = True
                elif self.vel_y < 0:  # jumping
                    self.rect.top = p.bottom
                    self.vel_y = 0

    def update(self, platforms, keys):
        self.handle_input(keys)
        self.apply_gravity()
        self.move_and_resolve(platforms)

    def draw(self, surface, camera_x):
        draw_rect = self.rect.copy()
        draw_rect.x -= camera_x
        pygame.draw.rect(surface, self.color, draw_rect)


def build_level():
    # Create a simple level with platforms at different positions
    platforms = []
    ground = pygame.Rect(0, HEIGHT - 40, 3000, 40)  # very wide ground
    platforms.append(ground)
    # some floating platforms
    platforms.append(pygame.Rect(300, HEIGHT - 140, 120, 20))
    platforms.append(pygame.Rect(500, HEIGHT - 220, 200, 20))
    platforms.append(pygame.Rect(850, HEIGHT - 180, 140, 20))
    platforms.append(pygame.Rect(1200, HEIGHT - 140, 200, 20))
    platforms.append(pygame.Rect(1600, HEIGHT - 220, 120, 20))
    platforms.append(pygame.Rect(1900, HEIGHT - 180, 200, 20))
    platforms.append(pygame.Rect(2300, HEIGHT - 140, 300, 20))
    return platforms


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Simple Pygame Platformer")
    clock = pygame.time.Clock()

    player = Player(100, HEIGHT - 200)
    platforms = build_level()

    level_width = 3000
    camera_x = 0

    font = pygame.font.SysFont(None, 24)

    while True:
        dt = clock.tick(FPS) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        keys = pygame.key.get_pressed()
        player.update(platforms, keys)

        # Camera follows the player horizontally with margins
        left_margin = WIDTH // 3
        right_margin = WIDTH - left_margin
        if player.rect.centerx - camera_x < left_margin:
            camera_x = max(0, player.rect.centerx - left_margin)
        elif player.rect.centerx - camera_x > right_margin:
            camera_x = min(level_width - WIDTH, player.rect.centerx - right_margin)

        # Drawing
        screen.fill((135, 206, 235))  # sky blue

        # Draw platforms
        for p in platforms:
            draw_p = p.copy()
            draw_p.x -= camera_x
            pygame.draw.rect(screen, (120, 72, 0), draw_p)

        # Draw player
        player.draw(screen, camera_x)

        # HUD
        text = font.render("Left/Right or A/D: move  Space/W/Up: jump  ESC: quit", True, (0, 0, 0))
        screen.blit(text, (10, 10))

        pygame.display.flip()


if __name__ == "__main__":
    main()
