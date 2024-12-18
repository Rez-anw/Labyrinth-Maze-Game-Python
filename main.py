from logging import currentframe

import pygame
import sys

# Initialise pygame
pygame.init()

# Screen dimession
width, height = 800, 800

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
maze1 = [
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

maze2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


# Cell and Target setting
cell_size = 40
target_x, target_y = 13 * cell_size, 17 * cell_size
maze = maze2


# Ball setting
ball_x, ball_y = cell_size + 10, cell_size + 10
ball_size = cell_size - 20
speed = 5
current_direction = None


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
# def can_move(x, y):
#     row = y // cell_size
#     col = x // cell_size
#     return maze[row][col] == 0

# def can_move(x, y):
#     # Define balls bounding box based on its size
#     ball_rect = pygame.Rect(x, y, ball_size, ball_size)
#
#     # Check if any part of the ball overlaps a wall
#     for row_index, row in enumerate(maze):
#         for col_index, cell in enumerate(maze):
#             if cell == 1:
#                 wall_rect = pygame.Rect(col_index * cell_size, row_index * cell_size, cell_size, cell_size)
#                 if ball_rect.colliderect(wall_rect):
#                     return False
#     return True

def can_move(x, y):
    # Define the player's bounding box based on its size
    player_rect = pygame.Rect(x, y, ball_size, ball_size)

    # Check if any part of the player overlaps a wall
    for row_index, row in enumerate(maze):
        for col_index, cell in enumerate(row):
            if cell == 1:  # Wall
                wall_rect = pygame.Rect(
                    col_index * cell_size,
                    row_index * cell_size,
                    cell_size,
                    cell_size,
                )
                if player_rect.colliderect(wall_rect):
                    return False  # Player hits a wall
    return True  # Player is not colliding with any walls



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
        elif event.type == pygame.KEYDOWN:
            # Update direction
            directions = {pygame.K_UP: "up", pygame.K_DOWN: "down", pygame.K_LEFT: "left", pygame.K_RIGHT: "right"}
            if event.key in directions:
                current_direction = directions[event.key]


    # Handle continuous movement
    if current_direction == "up" and can_move(ball_x, ball_y - speed):
            ball_y -= speed
    if current_direction == "down" and can_move(ball_x, ball_y + speed):
            ball_y += speed
    if current_direction == "left" and can_move(ball_x - speed, ball_y):
            ball_x -= speed
    if current_direction == "right" and can_move(ball_x + speed, ball_y):
            ball_x += speed



    # Check for collisions
    # if can_move(new_x, ball_y):
    #     ball_x = new_x
    # if can_move(ball_x, new_y):
    #     ball_y = new_y

    # Drawing
    screen.fill(white)
    draw_maze()
    draw_ball()
    draw_target()


    # Win condition
    if is_ball_in_target():
        print("You won!")
        current_direction = None
        # running = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()

