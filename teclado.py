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
            if i.key == pygame.K_LEFT or i.key == pygame.K_a:
                velocidadx=-3
            elif i.key ==pygame.K_RIGHT or i.key == pygame.K_d:
                velocidadx=3
            elif i.key == pygame.K_UP or i.key == pygame.K_w:
                velocidady=-3
            elif i.key == pygame.K_DOWN or i.key == pygame.K_s:
                velocidady=3

        if i.type == pygame.KEYUP:
            if i.key == pygame.K_LEFT or i.key == pygame.K_a:
                velocidadx=0
            elif i.key ==pygame.K_RIGHT or i.key == pygame.K_d:
                velocidadx=0
            elif i.key == pygame.K_UP or i.key == pygame.K_w:
                velocidady=0
            elif i.key == pygame.K_DOWN or i.key == pygame.K_s:
                velocidady=0

        
    

    ventanita.fill(verde)
    x+=velocidadx
    y+=velocidady

    pygame.draw.circle(ventanita,negro,(x,y),20)
    
    pygame.display.flip()
    reloj.tick(49)