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
    def __init__(self, img, all_sprites, all_shurikens, shuriken):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH-210
        self.rect.y = HEIGHT-150
        self.speedx = 0
        self.speedy = 0
        self.speedx = 0
        self.all_sprites = all_sprites
        self.all_shurikens = all_shurikens
        self.shuriken = assets['shuriken']

    def update(self):
        self.rect.x += self.speedx
        if self.rect.x > WIDTH:
            self.rect.x = 200
    
    def shoot(self):
        # A nova bala vai ser criada logo acima e no centro horizontal da nave
        shuriken = Shuriken(self.shuriken, self.rect.top, self.rect.centerx)
        self.all_sprites.add(shuriken)
        self.all_shurikens.add(shuriken)

class Shuriken(pygame.sprite.Sprite):
    def __init__(self, img, bottom, centerx):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()

        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speedy = -10  # Velocidade fixa para cima

    def update(self):
        # A bala só se move no eixo y
        self.rect.y += self.speedy

        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom < 0:
            self.kill()     
            
class CanoE(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH-495
        self.rect.y = HEIGHT-(random.randint(1000, 3500))
        self.speedx = 0
        self.speedy = 5
    
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.rect.x = WIDTH-495
            self.rect.y = HEIGHT-(random.randint(1000, 3500))
            self.speedx = 0
            self.speedy = 5

class CanoD(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH-210
        self.rect.y = HEIGHT-(random.randint(2000, 3500))
        self.speedx = 0
        self.speedy = 5

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.rect.x = WIDTH-210
            self.rect.y = HEIGHT-(random.randint(2000, 3500))
            self.speedx = 0
            self.speedy = 5

class AntenaE(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH-210
        self.rect.y = HEIGHT-(random.randint(1000, 3500))
        self.speedx = 0
        self.speedy = 5
    
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.rect.x = WIDTH-210
            self.rect.y = HEIGHT-(random.randint(2000, 3500))
            self.speedx = 0
            self.speedy = 5

class AntenaD(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH-495
        self.rect.y = HEIGHT - (random.randint(1000, 3500))
        self.speedx = 0
        self.speedy = 5
    
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.rect.x = WIDTH-495
            self.rect.y = HEIGHT-(random.randint(1000, 3500))
            self.speedx = 0
            self.speedy = 5
   
game = True
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30

#criando um grupo
all_sprites = pygame.sprite.Group()
all_obstacles = pygame.sprite.Group()
all_shurikens = pygame.sprite.Group()
all_antenae = pygame.sprite.Group()
all_antenad = pygame.sprite.Group()
all_canoe = pygame.sprite.Group()
all_canod = pygame.sprite.Group()

#criando o jogador

player = Ninja(assets['ninjadireita00'], all_sprites, all_shurikens, assets['shuriken'])

#----CANOS (POR CLASS)
canoe = CanoE(assets['canoesquerda'])
canod = CanoD(assets['canodireita'])

#----ANTENA (POR CLASS)
antenae = AntenaE(assets['antenaesquerda'])
antenad = AntenaD(assets['antenadireita'])

#-----SHURIKEN (POR CLASS)
#shuriken = Shuriken(assets['shuriken'], centerx, bottom=)

#adicionando tudo num grupo só
all_sprites.add(canoe)
all_sprites.add(canod)
all_sprites.add(antenae)
all_sprites.add(antenad)
all_sprites.add(player)

#adicionando os obstaculos num grupo
all_obstacles.add(canoe)
all_obstacles.add(canod)
all_obstacles.add(antenad)
all_obstacles.add(antenae)

#adicionando cada obstaculo no seu grupo
all_antenad.add(antenad)
all_antenae.add(antenae)
all_canod.add(canod)
all_canoe.add(canoe)

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
                player.rect.x = WIDTH-352.5
                player.rect.y = HEIGHT-200
            if event.key == pygame.K_RIGHT:
                player.image = assets['ninjapulandoe02']
                player.rect.x = WIDTH-352.5
                player.rect.y = HEIGHT-200
            if event.key == pygame.K_SPACE:
                player.shoot()
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.image = assets['ninjaesquerda00']
                player.rect.y = HEIGHT-150
                player.rect.x = WIDTH-495
            if event.key == pygame.K_RIGHT:
                player.image = assets['ninjadireita00']
                player.rect.x = WIDTH-210
                player.rect.y = HEIGHT-150
                
        # ----- Atualiza estado do jogo
    # ----- Atualiza estado do jogo
    # Atualizando a posição do objeto
    all_sprites.update()

    #-----Verifica colisão
    hits = pygame.sprite.spritecollide(player, all_obstacles, True)
    if len(hits) > 0:
        game = False

    # Verifica se houve colisão entre a bala e o meteoro
    colidiuad = pygame.sprite.groupcollide(all_shurikens, all_antenad, True, True)
    for colisoes in colidiuad:
        antenad = AntenaD(assets['antenadireita'])
        all_sprites.add(antenad)
        all_obstacles.add(antenad)
        all_antenad.add(antenad)

    colidiuae = pygame.sprite.groupcollide(all_shurikens, all_antenae, True, True)
    for colisoes in colidiuae:
        antenae = AntenaE(assets['antenaesquerda'])
        all_sprites.add(antenae)
        all_obstacles.add(antenae)
        all_antenae.add(antenae)

    colidiucd = pygame.sprite.groupcollide(all_shurikens, all_canod, True, True)
    for colisoes in colidiucd:
        cd = CanoD(assets['canodireita'])
        all_sprites.add(cd)
        all_obstacles.add(cd)
        all_canod.add(cd)
    
    colidiuce = pygame.sprite.groupcollide(all_shurikens, all_canoe, True, True)
    for colisoes in colidiuce:
        ce = CanoE(assets['canoesquerda'])
        all_sprites.add(ce)
        all_obstacles.add(ce)
        all_canoe.add(ce)


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