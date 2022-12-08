import pygame,sys,random

negro=(0,0,0)
blanco=(255,255,255)
contador=0

class Monito(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("pngwing.com.png").convert()
        self.image.set_colorkey(negro)
        self.rect=self.image.get_rect()

class AmongUs(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("descarga.png").convert()
        self.image.set_colorkey(blanco)
        self.rect=self.image.get_rect()



pygame.init()

dimesion=(900,700)

pantalla = pygame.display.set_mode(dimesion)
reloj=pygame.time.Clock()
fondo=pygame.image.load("fondo-azul-galaxia_125540-99.webp").convert()

lista_monos=pygame.sprite.Group()
lista_personajes=pygame.sprite.Group()

for i in range(40):
    mono=Monito()
    mono.rect.x=random.randrange(900)
    mono.rect.y=random.randrange(700)
    lista_monos.add(mono)
    lista_personajes.add(mono)

among=AmongUs()
lista_personajes.add(among)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    mouse=pygame.mouse.get_pos()
    among.rect.x=mouse[0]
    among.rect.y=mouse[1]

    aplastador_de_monos=pygame.sprite.spritecollide(among,lista_monos,True)
    for i in aplastador_de_monos:
        contador+=1
        print(contador)
        
    pantalla.blit(fondo,[0,0])

    lista_personajes.draw(pantalla)

    pygame.display.flip()
    reloj.tick(40)