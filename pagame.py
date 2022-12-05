import pygame,sys
pygame.init()

#colores
negro=(0,0,0)
blanco=(255,255,255)
rojo=(255,0,0)
verde=(0,255,0)
azul=(0,0,255)

tamanio=(800,400)
ventanita=pygame.display.set_mode(tamanio)

while True:
    for i in pygame.event.get():
        print(i)
        if i.type == pygame.QUIT:
            sys.exit()

    ventanita.fill(azul)
    pygame.draw.line(ventanita,rojo,[50,200], [200,200], 8)
    pygame.draw.rect(ventanita,negro,(100,100,40,40))
    pygame.draw.circle(ventanita,blanco,(300,100),20)
    pygame.draw.polygon(ventanita,verde,[(500,100),(550,150),(600,50)])

    pygame.display.flip()

