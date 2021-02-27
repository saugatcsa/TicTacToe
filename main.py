import pygame
import math

# Initializing Pygame
pygame.init()

# Screen WIDTH in pixels
SCREEN_WIDTH = 300 # I changed the screen size to 300
ROWS = 3

# Individual width of an x/o space
SQUARE_SIZE = SCREEN_WIDTH // ROWS

# Set the size of the game window
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))
pygame.display.set_caption("Hackathon TicTacToe Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (132, 27, 185)
DBlUE =  (0, 0, 102) #  I added color

# Images
X_IMAGE = pygame.transform.scale(pygame.image.load("x.png"), (90, 90)) # I changed X and O images size here
O_IMAGE = pygame.transform.scale(pygame.image.load("o.png"), (90, 90))

# Font to use to display message to players
END_FONT = pygame.font.SysFont('comicsansms', 50)   # I change the font here and font size


def draw_board():
    # SQUARE_SIZE is 200 pixels if WIDTH = 600

    # Draw vertical grid lines
    pygame.draw.line(win, DBlUE, (SQUARE_SIZE, 0), (SQUARE_SIZE, SCREEN_WIDTH), 3)  # I changed color here
    pygame.draw.line(win, DBlUE, (2*SQUARE_SIZE, 0), (2*SQUARE_SIZE, SCREEN_WIDTH), 3)

    # Draw horizontal grid lines
    pygame.draw.line(win, DBlUE, (0, SQUARE_SIZE), (SCREEN_WIDTH, SQUARE_SIZE), 3)
    pygame.draw.line(win, DBlUE, (0, 2*SQUARE_SIZE), (SCREEN_WIDTH, 2*SQUARE_SIZE), 3)


# This function will initialize or setup game board.
# NOTE: The game_board is a list of 3 lists, corresponding to a 3 x 3 grid
# representing the NINE grid squares of tic-tac-toe
def initialize_board():

    print("Executing initialize_board ...")

    # Each element of each list is a tuple defined by: (x, y, "", True)
    # Pixels to center (x,y) of one of the X/O squares
    # The string in the sequence will store "", "o", or "x"
    # True means the slot is currently available
    game_board = [[None, None, None], [None, None, None], [None, None, None]]

    #  Populate the game board with the CENTER of each grid square

    # Middle of each grid square is SQUARE_SIZE // 2
    # The values are 100, 300, 500 pixels, when the board size is 600

    mid_grid_square = SQUARE_SIZE // 2

    for i in range(3):
        # Compute the y-values:  100, 300, 500
        y = mid_grid_square + (i * SQUARE_SIZE)
        for j in range(3):
            # Compute the 3 x-values:  100, 300, 500
            x = mid_grid_square + (j * SQUARE_SIZE)

            game_board[i][j] = (x, y, "", True)
            print(game_board[i][j])
    # Return the game board to main()
    return game_board


def click(game_board):
    global x_turn, o_turn, images

    print("Detected a mouse click ...")
    # Mouse position
    m_x, m_y = pygame.mouse.get_pos()

    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            x, y, char, can_play = game_board[i][j]

            # Distance between mouse and the CENTER of the tic-tac-toe square
            clickpos = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
            # print(clickpos)

            # If it's inside the square AND the square is available,
            # then populate that game_board cell
            # if clickpos < 100 and can_play:
            # Update game_board and return from the function
            if (clickpos < SQUARE_SIZE // 2 and can_play):

                # If it's X's turn, update the square with an X
                if x_turn:
                    images.append((x, y, X_IMAGE))

                    # swap turns
                    x_turn = False
                    o_turn = True
                    game_board[i][j] = (x, y, 'x', False)

                # If it's O's turn, update the square with an O
                elif o_turn:
                    images.append((x, y, O_IMAGE))

                    # swap turns
                    x_turn = True
                    o_turn = False
                    game_board[i][j] = (x, y, 'o', False)
                print()
                print("Copied 3 lines form line 67 - 74 ")
                for i in range(3):
                    for j in range(3):
                        print(game_board[i][j])


                return

# Checking if someone has won
def has_won(game_board):
    print("Checking if there's a winner.")

    # Checking columns
    for row in range(3):
        if game_board[row][0][2] == game_board[row][1][2] and game_board[row][1][2]== game_board[row][2][2] and game_board[row][0][2] != "":
            display_message(game_board[row][0][2].upper() + " WON!!!!")
            return True

    # Checking rows
    for col in range(3):
        print("checking row-based wins ...")
        if game_board[0][col][2] == game_board[1][col][2] and game_board[1][col][2] == game_board[2][col][2] and game_board[0][col][2] != "":
            display_message(game_board[0][col][2].upper() + " WON!!!!")
            return True

    # Checking main diagonal
    # I added this code here
    if (game_board[0][0][2] == game_board[1][1][2] and game_board[2][2][2] == game_board[0][0][2]) and game_board[2][2][2] != "":
        display_message(game_board[0][0][2].upper() + " WON!!!!")
        return True


    # Checking reverse diagonal
    if (game_board[0][2][2] == game_board[1][1][2] and game_board[1][1][2] == game_board[2][0][2]) and game_board[0][2][2] != "":
        display_message(game_board[0][2][2].upper() + " WON!!!!")
        return True

    return False


# If there's no more available squares, then it's a draw if no one has won yet.
def has_drawn(game_board):
    print("Checking if it's a draw ...")
    for i in range(3):
        for j in range(3):
            if game_board[i][j][2] == "":
                return False

    display_message("Draw!")
    return True


# Inform user that there was a winner OR a draw!
def display_message(content):
    pygame.time.delay(500)
    win.fill(WHITE)
    end_text = END_FONT.render(content, 1, BLACK) # I changed the end message color here
    win.blit(end_text, ((SCREEN_WIDTH - end_text.get_width()) // 2, (SCREEN_WIDTH - end_text.get_height()) // 2))
    pygame.display.update()
    pygame.time.delay(3000)


def render():

    # Draw the background
    win.fill(WHITE)

    # Call the user-defined function to draw the initial board
    draw_board()

    # Drawing X's and O's
    for image in images:
        x, y, IMAGE = image
        win.blit(IMAGE, (x - IMAGE.get_width() // 2, y - IMAGE.get_height() // 2))

    pygame.display.update()


def main():
    global x_turn, o_turn, images, draw

    images = []

    x_turn = True # x goes first
    o_turn = False

    game_board = initialize_board()
    render()

    # Run the loop as long as no one has yet won OR still a grid cell unoccupied
    while True:

        pygame.display.flip()
        event = pygame.event.poll()

        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(game_board)
        else: continue

        render()
        # I changed / fliped the draw and won
        if has_won(game_board):
            break

        elif has_drawn(game_board):
            break



#while True:
if __name__ == '__main__':
    main()