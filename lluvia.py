import pygame
import random
import sys
pygame.init()

blanco=(255,255,255)
color=(29,200,56)
negro=(0,0,0)




tamanio=(800,500)
pantalla=pygame.display.set_mode(tamanio)
reloj=pygame.time.Clock()

lista_de_coordenadas=[]
for i in range(70):
    x=random.randint(0,800)
    y=random.randint(0,500)
    lista_de_coordenadas.append([x,y])
    
print(lista_de_coordenadas)

while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            sys.exit()
       
    pantalla.fill(negro)
    
    for l in lista_de_coordenadas:
        x=l[0]
        y=l[1]
        pygame.draw.circle(pantalla,blanco,(x,y),2)
        l[1]+=1
        if l[1]>500 :
            l[1]=0
    
    
    
    pygame.display.flip()
    reloj.tick(30)
