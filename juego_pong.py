import pygame 
pygame.init()
blanco=(255,255,255)
azul=(0,0,255)
negro=(0,0,0)
tamanio=(800,500)
ventana=pygame.display.set_mode(tamanio)
reloj=pygame.time.Clock()

ancho_jugador=15
alto_jugador=90

jugador_1_x=50
jugador_1_y=200
velocidad_jugador_1_y=0

jugador_2_x=700
jugador_2_y=200
velocidad_jugador_2_y=0

pelotaX=400
pelotay=250
velocidad_pelotaY=4
velocidad_pelotax=3



cerrar=False
while not cerrar:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            cerrar=True
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_w:
                velocidad_jugador_1_y=-3
            elif i.key == pygame.K_s:
                velocidad_jugador_1_y=3
        if i.type == pygame.KEYUP:
            if i.key == pygame.K_w:
                velocidad_jugador_1_y=0
            elif i.key == pygame.K_s:
                velocidad_jugador_1_y=0

        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                velocidad_jugador_2_y=-3
            elif i.key == pygame.K_DOWN:
                velocidad_jugador_2_y=3
        if i.type == pygame.KEYUP:
            if i.key == pygame.K_UP:
                velocidad_jugador_2_y=0
            elif i.key == pygame.K_DOWN:
                velocidad_jugador_2_y=0
            
    if pelotay >490 or pelotay <10 :
        velocidad_pelotaY *=-1
    elif pelotaX >790 or pelotaX <10 :
        velocidad_pelotax *=-1
    

    if jugador_1_y <8:
        jugador_1_y=8
    if jugador_1_y>410:
        jugador_1_y=410

    if jugador_2_y <8:
        jugador_2_y = 8
    elif jugador_2_y >410:
        jugador_2_y = 410
        
    
    
    ventana.fill(negro)
    jugador_1_y+=velocidad_jugador_1_y
    jugador_2_y+=velocidad_jugador_2_y
    pelotaX+=velocidad_pelotax
    pelotay+=velocidad_pelotaY

    naomi=pygame.draw.rect(ventana,azul,(jugador_1_x,jugador_1_y,ancho_jugador,alto_jugador))
    mauro=pygame.draw.rect(ventana,azul,(jugador_2_x,jugador_2_y,ancho_jugador,alto_jugador))
    pelotita=pygame.draw.circle(ventana,azul,(pelotaX,pelotay),10)
       #coalisiones 
    if pelotita.colliderect(naomi)or pelotita.colliderect(mauro):
        velocidad_pelotax*=-1
        velocidad_pelotaY*=-1




    pygame.display.flip()
    reloj.tick(90)

pygame.quit()