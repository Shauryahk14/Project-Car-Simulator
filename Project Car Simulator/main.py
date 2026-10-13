import pygame
import random

pygame.init()

# Window setup
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Traffic Signal Simulator")

# Custom events
CHANGE_CAR_COLOR = pygame.USEREVENT + 1
CHANGE_SIGNAL = pygame.USEREVENT + 2

# Car sprite
class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((60, 30))
        self.image.fill((0, 0, 255))  # Start blue
        self.rect = self.image.get_rect(center=(100, 250))
        self.velocity = 5

    def update(self):
        self.rect.x += self.velocity
        
        # Check road boundaries
        if self.rect.right >= 500 or self.rect.left <= 0:
            self.velocity = -self.velocity
            pygame.event.post(pygame.event.Event(CHANGE_CAR_COLOR))
            pygame.event.post(pygame.event.Event(CHANGE_SIGNAL))

    def change_color(self):
        random_color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        self.image.fill(random_color)

# Setup sprite group
car = Car()
sprites = pygame.sprite.Group(car)

# Signal state
signal_color = (255, 0, 0)  # Starts RED

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == CHANGE_CAR_COLOR:
            car.change_color()
        elif event.type == CHANGE_SIGNAL:
            signal_color = (0, 255, 0) if signal_color == (255, 0, 0) else (255, 0, 0)

    sprites.update()

    # Draw everything
    screen.fill((50, 50, 50))  # Road background
    
    # Traffic signal (circle at the top)
    pygame.draw.circle(screen, signal_color, (250, 60), 25)
    
    sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()