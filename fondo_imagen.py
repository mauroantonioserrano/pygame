import pygame

dimension=(1100,700)
negro=(0,0,0)
blanco=(255,255,255)
ventana=pygame.display.set_mode(dimension)

cerrar=False

fondo=pygame.image.load("paisaje.jpg").convert()
jugador=pygame.image.load("descarga.png")
jugador.set_colorkey(blanco)

pygame.mouse.set_visible(0)

while not cerrar:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            cerrar=True
    mouse=pygame.mouse.get_pos()
    x=mouse[0]
    y=mouse[1]
    ventana.blit(fondo,[-20,-200])
    ventana.blit(jugador,[x,y])

    pygame.display.flip()

pygame.quit()
    