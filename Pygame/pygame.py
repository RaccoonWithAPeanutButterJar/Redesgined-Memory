import pygame

WIDTH, LENGTH = 900,500
screen = pygame.display.set_mode((WIDTH, LENGTH))

def main(): 

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.quit:
                run = False
    pygame.quit()

if __name__ == "__main__":
    main()