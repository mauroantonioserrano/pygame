import pygame
import sys
pygame.init()

tamanio=(800,500)

rojo=(130,0,0)
verde=(0,140,0)

pantalla=pygame.display.set_mode(tamanio)
pygame.mouse.set_visible(0)

while True :
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            sys.exit()
    mouse_pos=pygame.mouse.get_pos()
    print(mouse_pos)
    x=mouse_pos[0]
    y=mouse_pos[1]

    pantalla.fill(rojo)
    
    pygame.draw.rect(pantalla,verde,(x,y,10,20))
    pygame.display.flip()


