import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Car Racing Animation")

# Define colors
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
YELLOW = (255, 255, 0)

# Load and scale car image
car_image = pygame.image.load('car1.png')
car_image = pygame.transform.scale(car_image, (80, 160))
car_rect = car_image.get_rect(center=(width // 2, height - 100))

# Define lane and movement variables
lane_width = 200
speed = 5
obstacle_speed = 7
score = 0

# Generate obstacles
def generate_obstacle():
    x_position = random.choice([(width // 2) - lane_width // 2, (width // 2) + lane_width // 2])
    obstacle = pygame.Rect(x_position, -150, 80, 160)
    return obstacle

obstacles = [generate_obstacle()]

# Game loop
running = True
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the car
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_rect.left > (width // 2) - lane_width:
        car_rect.x -= speed
    if keys[pygame.K_RIGHT] and car_rect.right < (width // 2) + lane_width:
        car_rect.x += speed

    # Move and generate obstacles
    for obstacle in obstacles:
        obstacle.y += obstacle_speed
        if obstacle.y > height:
            obstacles.remove(obstacle)
            obstacles.append(generate_obstacle())
            score += 1

    # Check for collisions
    for obstacle in obstacles:
        if car_rect.colliderect(obstacle):
            running = False  # Game over if collision

    # Draw background, road, and lane lines
    screen.fill(GRAY)
    pygame.draw.rect(screen, WHITE, ((width // 2) - lane_width, 0, lane_width * 2, height))
    for i in range(0, height, 80):
        pygame.draw.rect(screen, YELLOW, ((width // 2) - 5, i, 10, 40))

    # Draw car and obstacles
    screen.blit(car_image, car_rect)
    for obstacle in obstacles:
        pygame.draw.rect(screen, (255, 0, 0), obstacle)

    # Draw score
    score_text = font.render(f'Score: {score}', True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
