import pygame,sys
import random

pygame.init()
tamanio=(600,400)
window=pygame.display.set_mode(tamanio)
reloj=pygame.time.Clock()


mono=pygame.image.load("pngwing.com.png").convert()
mono.set_colorkey((0,0,0))

lista_monos=[]
for m in range(10):
        x=random.randrange(500)
        y=random.randrange(300)
        lista_monos.append([x,y])


while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
    mouse=pygame.mouse.get_pos()
    circulo_x=mouse[0]
    circulo_y=mouse[1]

    window.fill((255,255,255))

    for m in lista_monos:
        x=m[0]
        y=m[1]
        imagen=window.blit(mono,(x,y))
    
    
    circulo=pygame.draw.circle(window,(255,0,0),(circulo_x,circulo_y),10)

    coalicion=circulo.colliderect(circulo)

    pygame.display.flip()
    reloj.tick(30)
    

        