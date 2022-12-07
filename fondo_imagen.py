import pygame

dimension=(1100,700)
negro=(0,0,0)
blanco=(255,255,255)
ventana=pygame.display.set_mode(dimension)

cerrar=False

fondo=pygame.image.load("paisaje.jpg").convert()

while not cerrar:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            cerrar=True
    ventana.blit(fondo,[-20,-200])

    pygame.display.flip()

pygame.quit()
    