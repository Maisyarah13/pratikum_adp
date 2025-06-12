import pygame
import math
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bendera Merah Putih Lebih Lebar dan Berkibar ke Samping")

MERAH = (255, 0, 0)
PUTIH = (255, 255, 255)
TIANG = (105, 105, 105)
LANGIT = (135, 206, 235)

def draw_flag(t):
    flag_width = 240  
    flag_height = 100

    for x in range(flag_width):
        wave = math.sin((x / 15.0) + t) * 10 
        red_rect = pygame.Rect(150 + x, 100 + wave, 1, flag_height)
        white_rect = pygame.Rect(150 + x, 100 + flag_height + wave, 1, flag_height)

        pygame.draw.rect(screen, MERAH, red_rect)
        pygame.draw.rect(screen, PUTIH, white_rect)
clock = pygame.time.Clock()
t = 0 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(LANGIT)
    pygame.draw.rect(screen, TIANG, (130, 100, 10, 400))
    draw_flag(t)
    t += 0.1  
    pygame.display.flip()
    clock.tick(60)

