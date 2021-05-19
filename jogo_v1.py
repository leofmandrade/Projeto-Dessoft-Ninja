# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
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
assets['ninjainicio'] = pygame.image.load('assets/img/NINJAINICIO.png')
assets['ninjadireita00'] = pygame.image.load('assets/img/NINJAANDANDODIREITA00.png')
assets['ninjaesquerda00'] = pygame.image.load('assets/img/NINJAANDANDOESQUERDA00.png')

#-----Imagens dos obstáculos
assets['canoesquerda']= pygame.image.load('assets/img/CANOESQUERDA.png')
assets['canodireita']= pygame.image.load('assets/img/CANODIREITA.png')
assets['antenaesquerda']= pygame.image.load('assets/img/ANTENAESQUERDA.png')
assets['antenadireita']= pygame.image.load('assets/img/ANTENADIREITA.png')
#-----Imagem do projétil
assets['shuriken']= pygame.image.load('assets/img/SHURIKEN.png')

# ----- Inicia estruturas de dados
#------- Definindo novos tipos
class CanoE(pygame.sprite.Sprite):
    def __init__(self, img):
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

#----CANOS (POR CLASS)
canoe = CanoE(assets['canoesquerda'])
canod = CanoD(assets['canodireita'])
#----ANTENA (POR CLASS)
antenae = AntenaE(assets['antenaesquerda'])
antenad = AntenaD(assets['antenadireita'])


# ===== Loop principal =====
while game:
    clock.tick(60)

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        # ----- Atualiza estado do jogo
    # ----- Atualiza estado do jogo
    # Atualizando a posição do meteoro
    canoe.update()
    canod.update()
    antenad.update()
    antenae.update()

    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca)
    window.blit(assets['fundo'], (0, 0))
    window.blit(assets['paredes'], (0,0))
    window.blit(assets['placa'], (0, 0))
    window.blit(assets['ninjadireita00'],(0,0))
    window.blit(canoe.image, canoe.rect) 
    window.blit(antenad.image, antenad.rect)
    window.blit(canod.image, canod.rect)
    window.blit(antenae.image, antenae.rect)


    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados