import pygame
pygame.init()

negro=(0,0,0)
rojo=(255,0,0)
blanco=(255,255,255)

tamanio=(800,600)
ventana=pygame.display.set_mode(tamanio)
reloj=pygame.time.Clock()

alto=60
ancho=10

jugador_1_x = 100
jugador_1_y=300-(alto/2)
velocidad_jugador_1_y=0

jugador_2_x=700
jugador_2_y=300-(alto/2)
velocidad_jugador_2_y=0

pelotax=400
pelotay=300
velocidad_pelota_x=3
velocidad_pelota_y=3

cerrar=False
while not cerrar:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            cerrar = True
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_w:
                velocidad_jugador_1_y = -3
            elif i.key == pygame.K_s:
                velocidad_jugador_1_y = 3
            elif i.key == pygame.K_UP:
                velocidad_jugador_2_y=-3
            elif i.key == pygame.K_DOWN:
                velocidad_jugador_2_y=3

        if i.type == pygame.KEYUP:
            if i.key == pygame.K_w:
                velocidad_jugador_1_y = 0
            elif i.key == pygame.K_s:
                velocidad_jugador_1_y = 0
            elif i.key == pygame.K_UP:
                velocidad_jugador_2_y=0
            elif i.key == pygame.K_DOWN:
                velocidad_jugador_2_y=0
    if pelotay > 600 or pelotay <0:
        velocidad_pelota_y*=-1
    elif pelotax >800 or pelotax <0:
        velocidad_pelota_x*=-1
        
        

    jugador_1_y+=velocidad_jugador_1_y
    jugador_2_y+=velocidad_jugador_2_y
    pelotax+=velocidad_pelota_x
    pelotay+=velocidad_pelota_y

    ventana.fill(negro)
    maria=pygame.draw.rect(ventana,rojo,(jugador_1_x,jugador_1_y,ancho,alto))
    luis=pygame.draw.rect(ventana,rojo,(jugador_2_x,jugador_2_y,ancho,alto))
    pelota= pygame.draw.circle(ventana,blanco,(pelotax,pelotay),10)
    if pelota.colliderect(maria) or pelota.colliderect(luis):
        velocidad_pelota_x*=-1
        
    pygame.display.flip()
    reloj.tick(80)
    


   
pygame.quit()