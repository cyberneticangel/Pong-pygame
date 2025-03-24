import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 90
BALL_SIZE = 15
PADDLE_SPEED = 5
BALL_SPEED = 7

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pong in Python using Pygame")

# Create game objects
player = pygame.Rect(50, WINDOW_HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
opponent = pygame.Rect(WINDOW_WIDTH - 50 - PADDLE_WIDTH, WINDOW_HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WINDOW_WIDTH//2 - BALL_SIZE//2, WINDOW_HEIGHT//2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE)

# Ball speed (global variables)
ball_speed_x = BALL_SPEED * random.choice((1, -1))
ball_speed_y = BALL_SPEED * random.choice((1, -1))

# Score
player_score = 0
opponent_score = 0
font = pygame.font.Font(None, 74)

def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
    ball_speed_y = BALL_SPEED * random.choice((1, -1))
    ball_speed_x = BALL_SPEED * random.choice((1, -1))

def main():
    global player_score, opponent_score, ball_speed_x, ball_speed_y
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player.top > 0:
            player.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and player.bottom < WINDOW_HEIGHT:
            player.y += PADDLE_SPEED

        # Simple AI for opponent
        if opponent.top < ball.y:
            opponent.y += PADDLE_SPEED
        if opponent.bottom > ball.y:
            opponent.y -= PADDLE_SPEED

        # Ball movement
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # Ball collisions
        if ball.top <= 0 or ball.bottom >= WINDOW_HEIGHT:
            ball_speed_y *= -1

        # Paddle collisions
        if ball.colliderect(player) or ball.colliderect(opponent):
            ball_speed_x *= -1

        # Score points
        if ball.left <= 0:
            opponent_score += 1
            reset_ball()
        if ball.right >= WINDOW_WIDTH:
            player_score += 1
            reset_ball()

        # Drawing
        screen.fill(BLACK)
        
        # Draw paddles and ball
        pygame.draw.rect(screen, WHITE, player)
        pygame.draw.rect(screen, WHITE, opponent)
        pygame.draw.ellipse(screen, WHITE, ball)
        pygame.draw.aaline(screen, WHITE, (WINDOW_WIDTH//2, 0), (WINDOW_WIDTH//2, WINDOW_HEIGHT))

        # Draw score
        player_text = font.render(str(player_score), False, WHITE)
        opponent_text = font.render(str(opponent_score), False, WHITE)

        screen.blit(player_text, (WINDOW_WIDTH//4, 20))
        screen.blit(opponent_text, (3*WINDOW_WIDTH//4, 20))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()


