import pygame
import sys

# Initialise pygame
pygame.init()

# Screen dimession
width, height = 800, 600

# Colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Create the game window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Labyrinth Maze Game")

# Game clock
clock = pygame.time.Clock()

# Maze layout: 1 = wall, 0 = Path
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Cell and Target setting
cell_size = 40
target_x, target_y = 10 * cell_size, 7 * cell_size


# Ball setting
ball_x, ball_y = cell_size + 10, cell_size + 10
ball_size = cell_size - 20
speed = 5


# Draw the maze
def draw_maze():
    for row_index, row in enumerate(maze):
        for col_index, cell in enumerate(row):
            x = col_index * cell_size
            y = row_index * cell_size

            if cell == 1:
                pygame.draw.rect(screen, black, (x, y, cell_size, cell_size))
            else:
                pygame.draw.rect(screen, white, (x, y, cell_size, cell_size))



def draw_ball():
    pygame.draw.ellipse(screen, red, (ball_x, ball_y, ball_size, ball_size))

def draw_target():
    pygame.draw.rect(screen, green, (target_x, target_y, cell_size, cell_size))

# Movement control
def can_move(x, y):
    row = y // cell_size
    col = x // cell_size
    return maze[row][col] == 0

# Check if ball is at the target
def is_ball_in_target():
    # Ball's bounding box
    ball_rect = pygame.Rect(ball_x, ball_y, ball_size, ball_size)

    # Target's bounding box
    target_rect = pygame.Rect(target_x, target_y, cell_size, cell_size)

    # check for collision
    return ball_rect.colliderect(target_rect)


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key presses
    keys = pygame.key.get_pressed()
    new_x, new_y = ball_x, ball_y

    if keys[pygame.K_UP]:
        new_y -= speed
    if keys[pygame.K_DOWN]:
        new_y += speed
    if keys[pygame.K_LEFT]:
        new_x -= speed
    if keys[pygame.K_RIGHT]:
        new_x += speed

    # Check for collisions
    if can_move(new_x, ball_y):
        ball_x = new_x
    if can_move(ball_x, new_y):
        ball_y = new_y

    # Drawing
    screen.fill(white)
    draw_maze()
    draw_ball()
    draw_target()


    # Win condition
    if is_ball_in_target():
        print("You won!")
        # running = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()

