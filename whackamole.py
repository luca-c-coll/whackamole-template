import pygame
import random


def main():
    try:
        pygame.init()


        GRID_COLS = 20
        GRID_ROWS = 16
        CELL_SIZE = 32
        SCREEN_HEIGHT = GRID_ROWS * CELL_SIZE
        SCREEN_WIDTH = GRID_COLS * CELL_SIZE
        BG_COLOR = "light green"
        GRID_COLOR = "black"


        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))

        # initialize screen and clock
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        clock = pygame.time.Clock()

        # load mole image
        mole_image = pygame.image.load("mole.png")
        mole_rect = mole_image.get_rect(topleft=(0,0))


        def draw_grid():
            for x in range(0,SCREEN_WIDTH, CELL_SIZE):
                pygame.draw.line(screen, GRID_COLOR, (x,0), (x, SCREEN_HEIGHT))
            for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
                pygame.draw.line(screen, GRID_COLOR, (0,y), (SCREEN_WIDTH, y))

        def move_mole():
            random_x = random.randrange(0, GRID_COLS)* CELL_SIZE
            random_y = random.randrange(0,GRID_ROWS) * CELL_SIZE
            mole_rect.topleft = (random_x, random_y)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # get the mouse click position
                    mouse_x, mouse_y = event.pos

                    # find the grid column and row where mouse was clicked
                    click_col = mouse_x // CELL_SIZE
                    click_row = mouse_y // CELL_SIZE

                    # find the grid column and row where mole is
                    mole_col = mole_rect.x // CELL_SIZE
                    mole_row = mole_rect.y // CELL_SIZE

                    # checks if clicked cell is equal to the mole's cell
                    if click_col == mole_col and click_row == mole_row:
                        move_mole()

            screen.fill(BG_COLOR)
            draw_grid()
            screen.blit(mole_image, mole_rect)
            pygame.display.flip()
            clock.tick(60)


    finally:
            pygame.quit()


if __name__ == "__main__":
    main() # run main
