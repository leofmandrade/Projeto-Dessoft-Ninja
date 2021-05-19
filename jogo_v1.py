# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
import time

from pygame.constants import KEYDOWN
pygame.init()

# ----- Gera tela principal
WIDTH = 600
HEIGHT = 750
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Run Shinobi, Run!")

#------Inicia os assets
#------Imagens do fundo
assets = {}
assets['fundo'] = pygame.image.load('assets/img/FUNDOJOGOFINAL.png').convert()
assets['paredes'] = pygame.image.load('assets/img/PAREDESFINAL.png')
assets['placa'] = pygame.image.load('assets/img/PLACA.png')
#-----Imagens do ninja
#Ninja andando
assets['ninjainicio'] = pygame.image.load('assets/img/NINJAINICIO.png')
assets['ninjadireita00'] = pygame.image.load('assets/img/NINJAANDANDODIREITA00.png')
assets['ninjaesquerda00'] = pygame.image.load('assets/img/NINJAANDANDOESQUERDA00.png')
assets['ninjadireita01'] = pygame.image.load('assets/img/NINJAANDANDODIREITA01.png')
assets['ninjaesquerda01'] = pygame.image.load('assets/img/NINJAANDANDOESQUERDA01.png')
#Ninja Pulando
assets['ninjapulandod01'] = pygame.image.load('assets/img/NINJAPULANDODIREITA01.png')
assets['ninjapulandod02'] = pygame.image.load('assets/img/NINJAPULANDODIREITA02.png')
assets['ninjapulandod03'] = pygame.image.load('assets/img/NINJAPULANDODIREITA03.png')
assets['ninjapulandoe01'] = pygame.image.load('assets/img/NINJAPULANDOESQUERDA01.png')
assets['ninjapulandoe02'] = pygame.image.load('assets/img/NINJAPULANDOESQUERDA02.png')
assets['ninjapulandoe03'] = pygame.image.load('assets/img/NINJAPULANDOESQUERDA03.png')

#-----Imagens dos obstáculos
assets['canoesquerda']= pygame.image.load('assets/img/CANOESQUERDA.png')
assets['canodireita']= pygame.image.load('assets/img/CANODIREITA.png')
assets['antenaesquerda']= pygame.image.load('assets/img/ANTENAESQUERDA.png')
assets['antenadireita']= pygame.image.load('assets/img/ANTENADIREITA.png')
#-----Imagem do projétil
assets['shuriken']= pygame.image.load('assets/img/SHURIKEN.png')

# ----- Inicia estruturas de dados
#------- Definindo novos tipos
class Ninja(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        if self.rect.x > WIDTH:
            self.rect.x = 200
        
            

class CanoE(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = -400
        self.speedx = 0
        self.speedy = 5
    
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.rect.x = 0
            self.rect.y = -400
            self.speedx = 0
            self.speedy = 5

class CanoD(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = -100
        self.speedx = 0
        self.speedy = 5

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.rect.x = 0
            self.rect.y = -250
            self.speedx = 0
            self.speedy = 5

class AntenaE(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = -800
        self.speedx = 0
        self.speedy = 5
    
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.rect.x = 0
            self.rect.y = -300
            self.speedx = 0
            self.speedy = 5

class AntenaD(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = -600
        self.speedx = 0
        self.speedy = 5
    
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.rect.x = 0
            self.rect.y = -600
            self.speedx = 0
            self.speedy = 5
   
game = True
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30

#criando um grupo
all_sprites = pygame.sprite.Group()

#criando o jogador

player = Ninja(assets['ninjadireita00'])


#----CANOS (POR CLASS)

canoe = CanoE(assets['canoesquerda'])
canod = CanoD(assets['canodireita'])

#----ANTENA (POR CLASS)
antenae = AntenaE(assets['antenaesquerda'])
antenad = AntenaD(assets['antenadireita'])
#adicionando tudo num grupo só

all_sprites.add(canoe)
all_sprites.add(canod)
all_sprites.add(antenae)
all_sprites.add(antenad)
all_sprites.add(player)



# ===== Loop principal =====
while game:
    clock.tick(60)

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        # ----- Verifica se apertou alguma tecla
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.image = assets['ninjapulandod02']

            if event.key == pygame.K_RIGHT:
                player.image = assets['ninjapulandoe02']

        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.image = assets['ninjaesquerda00']
            if event.key == pygame.K_RIGHT:
                player.image = assets['ninjadireita00']
                
        # ----- Atualiza estado do jogo
    # ----- Atualiza estado do jogo
    # Atualizando a posição do meteoro
    all_sprites.update()

    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca)
    window.blit(assets['fundo'], (0, 0))
    window.blit(assets['paredes'], (0,0))
    window.blit(assets['placa'], (0, 0))
    all_sprites.draw(window)

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados