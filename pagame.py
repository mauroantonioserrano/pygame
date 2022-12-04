import pygame,sys
pygame.init()
tamanio=(800,400)
ventanita=pygame.display.set_mode(tamanio)

while True:
    for i in pygame.event.get():
        print(i)
        if i.type == pygame.QUIT:
            sys.exit()

