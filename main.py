# Draw Lines in Pygame / No Functions

# Pygame game template

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

def main():

    screen = init_game()  # Initialize the game and get the screen
    clock = pygame.time.Clock() # Initialize the clock objecct
    rect_change_x = 160
    rect_change_y = 160
    rect_x = 50
    rect_y = 50
    # Main game loop
    running = True
    while running:
        running = handle_events()  # Handle events and check if we should continue running

        # Fill the screen with a background color 
        screen.fill(config.WHITE) 
        pygame.draw.rect(screen, config.BLACK, [rect_x, rect_y, 50, 50])
        rect_x += rect_change_x
        rect_y += rect_change_y

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            pygame.draw.rect(screen, config.BLUE, [rect_x, rect_y, 50, 50])
            


        #if rect_y > 550:
            #rect_change_y = rect_change_y * -1
        if rect_y > 550 or rect_y < 0:
            rect_change_y = rect_change_y * -1
        if rect_x > 850 or rect_x < 0:
            rect_change_x = rect_change_x * -1

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































