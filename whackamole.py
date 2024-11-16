from itertools import filterfalse

import pygame
import random



def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        grid_size = 32
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()

        mole_position = (0,0)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x,mouse_y = event.pos
                    mole_x,mole_y = mole_position
                    if mole_x <= mouse_x < mole_x + grid_size and mole_y <= mouse_y < mole_y + grid_size:
                        new_x = random.randint(0, 19) * 32
                        new_y = random.randint(0, 15) * 32
                        mole_position = (new_x,new_y)
            screen.fill("light green")
            for y in range(0,512,32):
                pygame.draw.line(screen,"black",(0,y),(640,y))
            for x in range(0,640,32):
                pygame.draw.line(screen,"black",(x,0),(x,512))


            if mole_position:
                x,y = mole_position
                screen.blit(mole_image,mole_image.get_rect(topleft=(x,y)))

            screen.blit(mole_image, mole_image.get_rect(topleft=(x, y)))


            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()

