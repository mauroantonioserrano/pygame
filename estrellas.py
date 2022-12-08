import pygame
import sys
import random

pygame.init()
dimension=(700,500)
verde=(0,180,0)
blanco=(255,255,255)
pantalla=pygame.display.set_mode(dimension)
reloj=pygame.time.Clock()

lista_coordenadas=[]
for i in range(60):
    x=random.randint(0,700)
    y=random.randint(9,500)
    lista_coordenadas.append([x,y])
print(lista_coordenadas)
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    pantalla.fill(verde)
    for l in lista_coordenadas:
        x=l[0]
        y=l[1]
        pygame.draw.circle(pantalla,blanco,(x,y),2)
        l[1]=l[1]+1
        if l[1]>500:
            l[1]=0
    
    

    pygame.display.flip()
    reloj.tick(59)


