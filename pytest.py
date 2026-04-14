import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Game 1")

clock = pygame.time.Clock()

player = pygame.Rect(400, 300, 40, 40)
speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: player.y -= speed
    if keys[pygame.K_s]: player.y += speed
    if keys[pygame.K_a]: player.x -= speed
    if keys[pygame.K_d]: player.x += speed

    screen.fill((20, 20, 30))
    pygame.draw.rect(screen, (0, 200, 255), player)

    pygame.display.flip()
    clock.tick(60)
