# Draw Lines in Pygame / No Functions

# Pygame game template
import random
import pygame
import sys
import config  # Import the config module

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))  # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False  # Return False to indicate quitting
    return True  # Continue running if no quit event

def draw_rect(screen, color, x, y, width, height):
    pygame.draw.rect(screen, color, (x, y, width, height))


def main():



    screen = init_game()  # Initialize the game and get the screen
    clock = pygame.time.Clock() # Initialize the clock objecct
    running = True
    squares = []
    counter = 0
    # Main game loop
    running = True
    while running:
        running = handle_events()  # Handle events and check if we should continue running

        # Fill the screen with a background color 
        screen.fill(config.WHITE) 
        
        # Square
        for square in squares:
            if not (0 < square['location'][0] < config.WINDOW_WIDTH - square['size']):
                square['speed'][0] *= -1
            if not (0 < square['location'][1] < config.WINDOW_HEIGHT - square['size']):
                square['speed'][1] *= -1

            square['location'][0] += square['speed'][0]
            square['location'][1] += square['speed'][1]

            draw_rect(screen, square['color'], square['location'][0], square['location'][1], square['size'], square['size'])

        counter += 1
        if counter == config.FPS/6:
            counter = 0
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                squares.append({
                    'color' : config.BLUE,
                    'size' : 50,
                    'speed' : [5, 5],
                    'location' : [random.randint(50, 750), random.randint(50, 550)]
                })
            

        



        font = pygame.font.SysFont("Ariel", 50)
        text = font.render('Matthew Hall', True, config.RED)
        screen.blit(text, [0, 50])
        text = font.render('Career Tech', True, config.GREEN)
        screen.blit(text, [0, 90])
        mouse_pos = pygame.mouse.get_pos()
        text = font.render(str(mouse_pos), True, config.BLACK)
        screen.blit(text, mouse_pos)
        pygame.display.flip()  # Update the display

        clock.tick(config.FPS) # Limit frame rate to specified number of frames per second (FPS)

    pygame.quit()  # Quit Pygame
    sys.exit()  # Exit the program

if __name__ == "__main__":
    main()  































