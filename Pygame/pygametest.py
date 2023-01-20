import pygame

WIDTH, LENGTH = 900,500
WIN = pygame.display.set_mode((WIDTH, LENGTH))
pygame.display.set_caption("Minesweeper")

BG_COLOUR = (32, 25, 36)
FPS = 60

def draw():

    WIN.fill(BG_COLOUR)
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