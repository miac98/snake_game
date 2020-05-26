import pygame, sys, random

# This module contains various constants used by pygame
from pygame.locals import *

# Background color for game interface
black_color = pygame.Color(0, 0, 0)

# Color for the food
red_color = pygame.Color(255, 0, 0)

# Color for snake
snake_color = pygame.Color(173, 255, 47)

# Height and width for the window
# Standard -> 640w x 480h
w_width = 900
w_height = 700


# End the game
def game_over():
    pygame.quit()
    sys.exit()


def main():
    # Initialize all imported pygame modules
    pygame.init()
    pygame.font.init()

    # Font
    font = pygame.font.SysFont(None, 30)

    # Creates an object to help track time
    fps_clock = pygame.time.Clock()

    # Creates the display screen and set a title
    game_surface = pygame.display.set_mode((w_width, w_height))
    pygame.display.set_caption("Retro Snake")

    snake_position = [140, 100]
    snake_body = [[140, 100], [120, 100], [100, 100]]
    food_position = [300, 300]

    # If the value equals to 0, it means the food was eaten
    food_flag = 1

    # Default direction
    default_direction = 'right'

    direction = default_direction

    score = 0

    # GAME
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                game_over()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    direction = 'right'
                elif event.key == K_LEFT:
                    direction = 'left'
                elif event.key == K_UP:
                    direction = 'up'
                elif event.key == K_DOWN:
                    direction = 'down'
                elif event.key == K_ESCAPE:
                    game_over()

        # Confirm the direction
        if direction == 'right' and not default_direction == 'left':
            default_direction = direction
        elif direction == 'left' and not default_direction == 'right':
            default_direction = direction
        elif direction == 'up' and not default_direction == 'down':
            default_direction = direction
        elif direction == 'down' and not default_direction == 'up':
            default_direction = direction

        # Move snake
        if default_direction == 'right':
            snake_position[0] += 20
        elif default_direction == 'left':
            snake_position[0] -= 20
        elif default_direction == 'up':
            snake_position[1] -= 20
        elif default_direction == 'down':
            snake_position[1] += 20

        # Increase the length of the snake
        snake_body.insert(0, list(snake_position))

        if snake_position == food_position:
            food_flag = 0
            score += 10
        else:
            snake_body.pop()

        # Create new food position
        if food_flag == 0:
            x = random.randrange(1, 32)
            y = random.randrange(1, 24)

            food_position = [int(x)*20, int(y)*20]
            food_flag = 1

        # Creating and filling surface
        game_surface.fill(black_color)

        # Snake body
        for position in snake_body:
            pygame.draw.rect(game_surface, snake_color, Rect(position[0], position[1], 20, 20))

        # Show food
        pygame.draw.rect(game_surface, red_color, Rect(food_position[0], food_position[1], 20, 20))

        # Show points
        game_surface.blit(font.render('Score: ' + str(score), 1, red_color), (0, w_height-20))

        # Display
        pygame.display.flip()

        # Control snake speed
        fps_clock.tick(7)

        # GAME OVER
        if snake_position[0]+20 > w_width or snake_position[0] < 0:
            game_over()
        elif snake_position[1]+20 > w_height or snake_position[1] < 0:
            game_over()
        elif snake_position in snake_body[1:]:
            game_over()


if __name__ == '__main__':
    main()
