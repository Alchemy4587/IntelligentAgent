import pygame
from agent import *

WIDTH = 800
HEIGHT = 600
black = (0,0,0)
white = (255,255,255)
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
obstacle = pygame.image.load("img/stone.png")
obstacle = pygame.transform.scale(obstacle,(35,35))

man = pygame.image.load("img/stick.jpg")
man = pygame.transform.scale(man,(35,35))

agent = Agent(man,0,0)

lastExecutionTime = pygame.time.get_ticks()

target = pygame.image.load("img/laptop.png")
target = pygame.transform.scale(target,(35,35))


grid = [[3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
 [1, 0, 3, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1],
 [0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0],
 [1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
 [1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 2, 0, 1, 0, 1, 0, 0, 1, 1],
 [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
 [0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1],
 [0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
 [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
 [1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0],
 [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1],
 [1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1],
 [1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1],
 [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0]]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((white))
    for x in range (0,HEIGHT,40):
        pygame.draw.line(screen, black,(0,x), (WIDTH,x))
    for y in range (0,WIDTH,40):
        pygame.draw.line(screen, black,(y,0), (y,HEIGHT))
    for i in range(0,15):
        for j in range(0,20):
            x = j * 40
            y = i * 40
            if grid[i][j] == 0:
                screen.blit(obstacle,(x,y))

            elif grid[i][j] == 2:
                screen.blit(target,(x,y))
    currentTime = pygame.time.get_ticks()
    if currentTime - lastExecutionTime > 500 and not agent.foundTarget:
        agent.move(grid)
        lastExecutionTime = pygame.time.get_ticks()
    agent.draw(screen)
    pygame.display.update()
pygame.quit()
