import pygame,sys
pygame.init()



tamanio=(736,414)
azul=(0,0,255)
blanco=(255,255,255)
rojo=(255,0,0)
negro=(0,0,0)
ventana=pygame.display.set_mode(tamanio)

fondo=pygame.image.load("6ea1a3ddc80612b8997fb20bc0223f6a.jpg").convert()
jugador=pygame.image.load("pngegg.png").convert()
jugador.set_colorkey(negro)
reloj=pygame.time.Clock()
x=100
y=200
velocidad=0
pygame.mouse.set_visible(0)

while True :
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            sys.exit()
        if i.type ==pygame.KEYDOWN:
            if i.key==pygame.K_LEFT:
                velocidad=-3
            elif i.key==pygame.K_RIGHT:
                velocidad=3
        if i.type==pygame.KEYUP:
            if i.key==pygame.K_LEFT:
                velocidad=0
            elif i.key==pygame.K_RIGHT:
                velocidad=0
    mouse=pygame.mouse.get_pos()
    x=mouse[0]
    y=mouse[1]


    ventana.blit(fondo,[0,0])
    ventana.blit(jugador,[x,y])
    x+=velocidad
    pygame.draw.circle(ventana,rojo,(x,y),20)


    pygame.display.flip()
    reloj.tick(70)
