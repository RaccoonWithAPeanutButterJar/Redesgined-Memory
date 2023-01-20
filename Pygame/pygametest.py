import pygame
import random
pygame.init()

WIDTH, LENGTH = 10,10 # x * x amount of mines
MINES = 10 #amount of mines
WIN = pygame.display.set_mode((WIDTH, LENGTH))
pygame.display.set_caption("Minesweeper")

#import files
spr_emptyGrid = pygame.image.load("Sprites", "empty.png")
spr_flag = pygame.image.load("Sprites", "flag.png")
spr_grid = pygame.image.load("Sprites", "Grid.png")
spr_grid1 = pygame.image.load("Sprites", "grid1.png")
spr_grid2 = pygame.image.load("Sprites", "grid2.png")
spr_grid3 = pygame.image.load("Sprites", "grid3.png")
spr_grid4 = pygame.image.load("Sprites", "grid4.png")
spr_grid5 = pygame.image.load("Sprites", "grid5.png")
spr_grid6 = pygame.image.load("Sprites", "grid6.png")
spr_grid7 = pygame.image.load("Sprites", "grid7.png")
spr_grid8 = pygame.image.load("Sprites", "grid8.png")
spr_grid7 = pygame.image.load("Sprites", "grid7.png")
spr_mine = pygame.image.load("Sprites", "mine.png")
spr_mineClicked = pygame.image.load("Sprites", "mineClicked.png")
spr_mineFalse = pygame.image.load("Sprites/mineFalse.png")

FPS = 60

def draw():

    WIN.fill((32, 25, 36))
    pygame.display.update()

def main(): 

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw()
    pygame.quit()

if __name__ == "__main__":
    main()