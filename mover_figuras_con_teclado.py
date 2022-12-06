import pygame 
import sys 
pygame.init()

tamanio=(800,500)
blanco=(255,255,255)
azul=(0,0,255)
pantalla=pygame.display.set_mode(tamanio)
reloj=pygame.time.Clock()

cordenada_x=10
cordenada_y=10
velocidad_x=0
velocidad_y=0

while True:
    for i in pygame.event.get():
        print(i)
        if i.type ==pygame.QUIT:
            sys.exit()
        if i.type ==pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                velocidad_x=-3
            elif i.key ==pygame.K_RIGHT:
                velocidad_x=3
            elif i.key == pygame.K_UP:
                velocidad_y=-3
            elif i.key==pygame.K_DOWN:
                velocidad_y=3

        if i.type ==pygame.KEYUP:
            if i.key == pygame.K_LEFT:
                velocidad_x=0
            elif i.key == pygame.K_RIGHT:
                velocidad_x=0
            elif i.key == pygame.K_UP:
                velocidad_y=0
            elif i.key == pygame.K_DOWN:
                velocidad_y=0

        # if i.type == pygame.TEXTINPUT:
        #     if i.key == pygame.K_LEFT:
        #         velocidad_x=-3
        #     elif i.key == pygame.K_RIGHT:
        #         velocidad_x=3
        
            
    pantalla.fill(azul)
    cordenada_x+=velocidad_x
    cordenada_y+=velocidad_y
    pygame.draw.rect(pantalla,blanco,(cordenada_x,cordenada_y,30,30))
    
   
    pygame.display.flip()
    reloj.tick(60)
     