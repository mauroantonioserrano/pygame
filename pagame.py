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
cordenada_x=300
velocidad_x=4
reloj=pygame.time.Clock()

while True:
    for i in pygame.event.get():
        print(i)
        if i.type == pygame.QUIT:
            sys.exit()

    if cordenada_x >800 or cordenada_x <0 :
        velocidad_x=velocidad_x *-1
    cordenada_x=cordenada_x+velocidad_x


    ventanita.fill(azul)
    for i in range(100,800,100):
        pygame.draw.rect(ventanita,blanco,(i,20,60,60))
    for c in range(100,400,100):
        pygame.draw.circle(ventanita,blanco,(cordenada_x,c),20)


    
    
    # pygame.draw.line(ventanita,rojo,[50,200], [200,200], 8)
    # pygame.draw.rect(ventanita,negro,(100,100,40,40))
    # pygame.draw.circle(ventanita,blanco,(cordenada_x,100),20)
    # pygame.draw.polygon(ventanita,verde,[(500,100),(550,150),(600,50)])

    pygame.display.flip()
    reloj.tick(40)

