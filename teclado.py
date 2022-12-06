import pygame
import sys

pygame.init()
tamanio=(900,500)
verde=(0,255,0)
negro=(0,0,0)
ventanita=pygame.display.set_mode(tamanio)
reloj=pygame.time.Clock()

x=200
y=100
velocidadx=0
velocidady=0
while True:
    for i in pygame.event.get():
        print(i)
        if i.type == pygame.QUIT:
            sys.exit()

        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                velocidadx=-3
            elif i.key ==pygame.K_RIGHT:
                velocidadx=3
            elif i.key == pygame.K_UP:
                velocidady=-3
            elif i.key == pygame.K_DOWN:
                velocidady=3

        if i.type == pygame.KEYUP:
            if i.key == pygame.K_LEFT:
                velocidadx=0
            elif i.key ==pygame.K_RIGHT:
                velocidadx=0
            elif i.key == pygame.K_UP:
                velocidady=0
            elif i.key == pygame.K_DOWN:
                velocidady=0

        
    

    ventanita.fill(verde)
    x+=velocidadx
    y+=velocidady

    pygame.draw.circle(ventanita,negro,(x,y),20)
    
    pygame.display.flip()
    reloj.tick(49)