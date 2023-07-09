import pygame
import random

# Initialize Pygame
pygame.init()

# Define color constants using RGB values
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set display width and height
disp_width = 600
disp_height = 400

# Create the game window
dis = pygame.display.set_mode((disp_width, disp_height))
pygame.display.set_caption('Snake Game')

# Set up the clock to control the game speed
clock = pygame.time.Clock()

# Define the size of each block in the game and the speed of the snake
snake_block = 10
initial_snake_speed = 10
snake_speed = initial_snake_speed

# Set up font styles for displaying score and messages
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


# Function to display the player's score
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


# Function to draw the snake on the game window
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


# Function to display messages on the game window
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [disp_width / 6, disp_height / 3])


# Main game loop
def gameLoop():
    global snake_speed  # Declare snake_speed as a global variable
    game_over = False
    game_close = False

    # Initial position of the snake's head
    x1 = disp_width / 2
    y1 = disp_height / 2

    # Variables to control the change in the snake's position
    x1_change = 0
    y1_change = 0

    # Variables to store the snake's body and its length
    snake_List = []
    Length_of_snake = 1

    # Generate initial position of the food randomly
    foodx = round(random.randrange(0, disp_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, disp_height - snake_block) / 10.0) * 10.0

    # Main game loop
    while not game_over:

        # Game over screen
        while game_close:
            dis.fill(blue)
            message("Game Over! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            # Event handling for the game over screen
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Event handling for keyboard input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Check for collision with the boundaries of the game window
        if x1 >= disp_width or x1 < 0 or y1 >= disp_height or y1 < 0:
            game_close = True

        # Update the position of the snake's head
        x1 += x1_change
        y1 += y1_change

        # Fill the game window with the background color
        dis.fill(blue)

        # Draw the food and the snake on the game window
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        # Remove the extra part of the snake if its length exceeds the length of the snake list
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Check for collision with the snake's body
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Draw the snake on the game window
        our_snake(snake_block, snake_List)

        # Display the player's score
        Your_score(Length_of_snake - 1)

        # Update the game window
        pygame.display.update()

        # Check for collision with the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, disp_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, disp_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            snake_speed+=1          # Increase the snake's speed

        # Control the speed of the game
        clock.tick(snake_speed)

    # Quit Pygame and exit the program
    pygame.quit()
    quit()


# Start the game loop
gameLoop()
