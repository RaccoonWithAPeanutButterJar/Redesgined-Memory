import pygame

WIDTH, LENGTH = 900,500
WIN = pygame.display.set_mode((WIDTH, LENGTH))
pygame.display.set_caption("Minesweeper", icontitle=None)

def main(): 

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.quit:
                run = False
    pygame.quit()

if __name__ == "__main__":
    main()