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
color_key = (0, 89, 255)
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

#-----Imagem da explosão
assets['explosion00'] = pygame.image.load('assets/img/EXPLOSAO00.png')
explosao = []
for i in range(6):
    diretorio = 'assets/img/EXPLOSAO0{}.png'.format(i)
    img = pygame.image.load(diretorio).convert()
    img.set_colorkey(color_key)
    explosao.append(img) 
assets['explosao']= explosao

# ----- Inicia estruturas de dados
#------- Definindo novos tipos
class Ninja(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['ninjadireita00']
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH-210 #posicao na direita
        self.rect.y = HEIGHT-150 ###############
        self.speedx = 0
        self.speedy = 0
        self.lado = 'direita'
        self.groups = groups
        self.assets = assets
        self.all_sprites = all_sprites
        self.all_shurikens = all_shurikens
        self.shuriken = assets['shuriken']
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 150
        self.andandodireita = [assets['ninjadireita01'], assets['ninjadireita00']]
        self.andandoesquerda = [assets['ninjaesquerda00'], assets['ninjaesquerda01']]
    
    def move(self, direcao):
        if direcao == 'esquerda':
            self.lado = 'meiodireita'
        if direcao == 'direita':
            self.lado = 'meioesquerda'

    def update(self):
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update
        self.rect.x += self.speedx
        if self.rect.x > WIDTH:
            self.rect.x = 200
        if self.lado == 'direita':
            self.rect.x = WIDTH-210 #posicao na direita
            self.rect.y = HEIGHT-150 ###############
            if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
                self.last_update = now
                self.frame += 1
                if self.frame >= len(self.andandodireita):
                    self.frame = 0
                self.image = self.andandodireita[self.frame]

        if self.lado == 'esquerda':
            player.rect.y = HEIGHT-150
            player.rect.x = WIDTH-490
            if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
                self.last_update = now
                self.frame += 1
                if self.frame >= len(self.andandodireita):
                    self.frame = 0
                self.image = self.andandoesquerda[self.frame]

        if self.lado == 'meiodireita':
            self.image = assets['ninjapulandoe02']
            player.rect.x = WIDTH-352.5
            player.rect.y = HEIGHT-200
            self.lado = 'esquerda'
        if self.lado == 'meioesquerda':
            self.image = assets['ninjapulandod02']
            player.rect.x = WIDTH-352.5
            player.rect.y = HEIGHT-200
            self.lado = 'direita'
        
    
    def shoot(self):
        # A nova bala vai ser criada logo acima e no centro horizontal da nave
        shuriken = Shuriken(self.shuriken, self.rect.top, self.rect.centerx)
        self.all_sprites.add(shuriken)
        self.all_shurikens.add(shuriken)

class Shuriken(pygame.sprite.Sprite):
    def __init__(self, img, bottom, centerx):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['shuriken']
        self.rect = self.image.get_rect()
        self.last_update = pygame.time.get_ticks()

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
        self.speedy = 7
    
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.rect.x = WIDTH-495
            self.rect.y = HEIGHT-(random.randint(1000, 3500))
            self.speedx = 0
            self.speedy = 7

class CanoD(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH-210
        self.rect.y = HEIGHT-(random.randint(2000, 3500))
        self.speedx = 0
        self.speedy = 7

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.rect.x = WIDTH-210
            self.rect.y = HEIGHT-(random.randint(2000, 3500))
            self.speedx = 0
            self.speedy = 7

class AntenaE(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH-210
        self.rect.y = HEIGHT-(random.randint(1000, 3500))
        self.speedx = 0
        self.speedy = 7
    
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.rect.x = WIDTH-210
            self.rect.y = HEIGHT-(random.randint(2000, 3500))
            self.speedx = 0
            self.speedy = 7

class AntenaD(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH-495
        self.rect.y = HEIGHT - (random.randint(1000, 3500))
        self.speedx = 0
        self.speedy = 7
    
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.rect.x = WIDTH-495
            self.rect.y = HEIGHT-(random.randint(1000, 3500))
            self.speedx = 0
            self.speedy = 7

class Explosao(pygame.sprite.Sprite):
    def __init__(self, center, assets):
        pygame.sprite.Sprite.__init__(self)

        self.explosao = assets['explosao']

        self.frame = 0
        self.image = self.explosao[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = center

        self.last_update = pygame.time.get_ticks()

        self.frame_ticks = 50

    def update(self):
        # Verifica o tick atual.
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update

        if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
            self.last_update = now
            self.frame += 1

        
            # Verifica se já chegou no final da animação.
            if self.frame == len(self.explosao):
                # Se sim, tchau explosão!
                self.kill()
            else:
                # Se ainda não chegou ao fim da explosão, troca de imagem.
                center = self.rect.center
                self.image = self.explosao[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

game = True
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30
#criando dicionario de grupos
groups = {}
#criando grupos
#sprites
all_sprites = pygame.sprite.Group()
#obstaculos
all_obstacles = pygame.sprite.Group()
#shurikens
all_shurikens = pygame.sprite.Group()
#grupo para cada obstaculo individual
all_antenae = pygame.sprite.Group()
all_antenad = pygame.sprite.Group()
all_canoe = pygame.sprite.Group()
all_canod = pygame.sprite.Group()

#adicionando no dicionario
groups['all_sprites']=all_sprites
groups['all_obstacles']=all_obstacles
groups['all_shurikens'] = all_shurikens
groups['all_antenae'] = all_antenae
groups['all_antenad'] = all_antenad
groups['all_canoe'] = all_canoe
groups['all_canod'] = all_canod

#criando o jogador
player = Ninja(groups, assets)

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

#adicionando um numero limitado de shurikens
numeroshurikens= 0

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
                if player.lado == 'direita':
                    player.move('esquerda')
               # player.rect.x = WIDTH-352.5
              #  player.rect.y = HEIGHT-200
            if event.key == pygame.K_RIGHT:
                if player.lado == 'esquerda':
                    player.move('direita')
              #  player.rect.x = WIDTH-352.5
              #   player.rect.y = HEIGHT-200
            if event.key == pygame.K_SPACE:
                if numeroshurikens < 3:
                    player.shoot()
                    numeroshurikens += 1
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.rect.y = HEIGHT-150
                player.rect.x = WIDTH-495
            if event.key == pygame.K_RIGHT:
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
        

        explosao = Explosao(colisoes.rect.center, assets)
        all_sprites.add(explosao)

    colidiuae = pygame.sprite.groupcollide(all_shurikens, all_antenae, True, True)
    for colisoes in colidiuae:
        antenae = AntenaE(assets['antenaesquerda'])
        all_sprites.add(antenae)
        all_obstacles.add(antenae)
        all_antenae.add(antenae)

        explosao = Explosao(colisoes.rect.center, assets)
        all_sprites.add(explosao)

    colidiucd = pygame.sprite.groupcollide(all_shurikens, all_canod, True, True)
    for colisoes in colidiucd:
        cd = CanoD(assets['canodireita'])
        all_sprites.add(cd)
        all_obstacles.add(cd)
        all_canod.add(cd)

        explosao = Explosao(colisoes.rect.center, assets)
        all_sprites.add(explosao)
    
    colidiuce = pygame.sprite.groupcollide(all_shurikens, all_canoe, True, True)
    for colisoes in colidiuce:
        ce = CanoE(assets['canoesquerda'])
        all_sprites.add(ce)
        all_obstacles.add(ce)
        all_canoe.add(ce)

        explosao = Explosao(colisoes.rect.center, assets)
        all_sprites.add(explosao)


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