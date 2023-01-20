import pygame
import random
import os
pygame.init()

WIDTH, LENGTH = 10,10 # x * x amount of mines
MINES = 10 #amount of mines
WIN = pygame.display.set_mode((WIDTH, LENGTH))
pygame.display.set_caption("Minesweeper")

#import files
spr_emptyGrid = pygame.image.load(os.path.join('Sprites', 'empty.png'))
spr_flag = pygame.image.load(os.path.join('Sprites', 'flag.png'))
spr_grid = pygame.image.load(os.path.join('Sprites', 'grid.png'))
spr_grid1 = pygame.image.load(os.path.join('Sprites', 'grid1.png'))
spr_grid2 = pygame.image.load(os.path.join('Sprites', 'grid2.png'))
spr_grid3 = pygame.image.load(os.path.join('Sprites', 'grid3.png'))
spr_grid4 = pygame.image.load(os.path.join('Sprites', 'grid4.png'))
spr_grid5 = pygame.image.load(os.path.join('Sprites', 'grid5.png'))
spr_grid6 = pygame.image.load(os.path.join('Sprites', 'grid6.png'))
spr_grid7 = pygame.image.load(os.path.join('Sprites', 'grid7.png'))
spr_grid8 = pygame.image.load(os.path.join('Sprites', 'grid8.png'))
spr_mine = pygame.image.load(os.path.join('Sprites', 'mine.png'))
spr_mineClicked = pygame.image.load(os.path.join('Sprites', 'mineClicked.png'))
spr_mineFalse = pygame.image.load(os.path.join('Sprites', 'mineFalse.png'))


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