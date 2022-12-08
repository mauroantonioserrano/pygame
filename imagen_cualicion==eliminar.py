import  pygame,sys
import random
blanco=(255,255,255)
negro=(0,0,0)

class Basura(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("basura.png").convert()
        self.image.set_colorkey(negro)
        self.rect=self.image.get_rect()

class Walle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("pngegg.png")
        self.rect=self.image.get_rect()

    
    
pygame.init()

tamanio=(800,500)
ventana=pygame.display.set_mode(tamanio)
reloj=pygame.time.Clock()
fondo=pygame.image.load("peakpx.jpg")
pygame.mouse.set_visible(0)
contador=0



lista_de_basura=pygame.sprite.Group()
lista_de_imagenes=pygame.sprite.Group()

for i in range(20):
    basura_rango=Basura()
    basura_rango.rect.x=random.randrange(800)
    basura_rango.rect.y=random.randrange(500)
    lista_de_basura.add(basura_rango)
    lista_de_imagenes.add(basura_rango)

walle=Walle()

lista_de_imagenes.add(walle)

   




while True :
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            sys.exit()
    mouse=pygame.mouse.get_pos()
    walle.rect.x=mouse[0]
    walle.rect.y=mouse[1]
    coalision_basura=pygame.sprite.spritecollide(walle,lista_de_basura,True)
    for i in coalision_basura:
        contador+=1
        print(contador)

    
    ventana.blit(fondo,[0,0])
        
    lista_de_imagenes.draw(ventana)


    pygame.display.flip()
    reloj.tick(50)
