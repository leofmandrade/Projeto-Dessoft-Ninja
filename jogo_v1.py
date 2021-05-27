# ===== Inicialização =====
# ----- Importa e inicia pacotes
####teste mudanca
import pygame
import random
import time
from pygame.constants import KEYDOWN
pygame.init()
pygame.mixer.init()

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
#Logo Ninja
assets['logoninja'] = pygame.image.load('assets/img/LOGONINJA.png')
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

# Carrega os sons do jogo
pygame.mixer.music.load('assets/snd/Musica2.ogg')
pygame.mixer.music.set_volume(0.2)
shuriken_sound = pygame.mixer.Sound('assets/snd/ShurikenSound2.wav')
jump_sound = pygame.mixer.Sound('assets/snd/JumpSound.wav')
collision_sound = pygame.mixer.Sound('assets/snd/CollisionSound.wav')

#--------Carrega a fonte do placar
assets['fonteplacar'] = pygame.font.Font('assets/font/game_over.ttf', 100)
assets['fontemenorpontuacao'] = pygame.font.Font('assets/font/game_over.ttf', 60)

#--------FONTE DAS VIDAS
assets['score_font'] = pygame.font.Font('assets/font/PressStart2P.ttf', 28)
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
        shuriken = Shuriken(self.shuriken, self.rect.top, self.rect.centerx, shuriken_sound)
        self.all_sprites.add(shuriken)
        self.all_shurikens.add(shuriken)

class Shuriken(pygame.sprite.Sprite):
    def __init__(self, img, bottom, centerx, shuriken_sound):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['shuriken']
        self.rect = self.image.get_rect()
        self.last_update = pygame.time.get_ticks()

        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speedy = -10  # Velocidade fixa para cima
        self.shuriken_sound = shuriken_sound

    def update(self):
        # A bala só se move no eixo y
        self.rect.y += self.speedy
        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom < 0:
            self.kill()  
        self.shuriken_sound.play()   

#------------------ CANOS        
class Cano(pygame.sprite.Sprite):
    def __init__(self, img, spd, lado):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.speedx = 0
        self.speedy = spd
        self.lado = lado
        if self.lado == "esquerdo":
            self.rect.x = WIDTH-495
            self.rect.y = HEIGHT-(random.randint(1000, 3500))

        elif self.lado == "direito":
            self.rect.x = WIDTH-210
            self.rect.y = HEIGHT-(random.randint(2000, 3500))

       # self.frame_ticksCANOE = 10000
       # self.last_updateCANOE = pygame.time.get_ticks()
    
    def update(self):
        self.rect.y += self.speedy
    
        if self.rect.top > HEIGHT:           
            self.speedx = 0
            if self.lado == "esquerdo":
                self.rect.x = WIDTH-495
                self.rect.y = HEIGHT-(random.randint(1000, 3500))
            elif self.lado =="direito":
                self.rect.x = WIDTH-210
                self.rect.y = HEIGHT-(random.randint(2000, 3500))

       # now = pygame.time.get_ticks()
       # elapsed_ticksCANOE = now - self.last_updateCANOE 


#-------------- ANTENAS
class Antena(pygame.sprite.Sprite):
    def __init__(self, img, spd, lado):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH-210
        self.rect.y = HEIGHT-(random.randint(1000, 3500))
        self.speedx = 0
        self.speedy = spd
        self.lado = lado
        if self.lado == 'esquerdo':
            self.rect.x = WIDTH-495
            self.rect.y = HEIGHT-(random.randint(2000, 3500))
        elif self.lado == 'direito':
            self.rect.x = WIDTH-210
            self.rect.y = HEIGHT-(random.randint(1000, 3500))

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.speedx = 0
            if self.lado == 'direito':
                self.rect.x = WIDTH-210
                self.rect.y = HEIGHT-(random.randint(2000, 3500))
            if self.lado == 'esquerdo':
                self.rect.x = WIDTH-495
                self.rect.y = HEIGHT-(random.randint(1000, 3500))

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

#variaveis iniciais velocidade
spdcanoe = 7
spdcanod = 7
spdantenae = 7
spdantenad = 7
#----CANOS (POR CLASS)
canoe = Cano(assets['canoesquerda'],spdcanoe, 'esquerdo')
canod = Cano(assets['canodireita'],spdcanod, 'direito')

#----ANTENA (POR CLASS)
antenae = Antena(assets['antenadireita'],spdantenae, 'esquerdo')
antenad = Antena(assets['antenaesquerda'],spdantenad, 'direito')

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
numeroshurikens= 3

#ESTADOS
DONE = 0
PLAYING = 1
DYING = 2
state = PLAYING

ticks_0 = 0
ticks_1 = 0
ticks_2 = 0
placar = 0
vidas = 3

# ===== Loop principal =====
pygame.mixer.music.play(loops=-1)
while state != DONE:
    #AUMENTANDO PROGRESSIVAMENTE A VELOCIDADE
    if ticks_2 >= 900:
        numeroshurikens = 3
        ticks_2 = 0

    if ticks_1 >= 15:
        placar += 5
        ticks_1 = 0
    
    if ticks_0 >= 600:
        canoe.speedy += 1
        canoe.rect.y += canoe.speedy
        canoe.speedx = 0
        
        canod.speedy += 1
        canod.rect.y += canod.speedy
        canod.speedx = 0

        antenad.speedy += 1
        antenad.rect.y += antenad.speedy
        antenad.speedx = 0
        
        antenae.speedy += 1
        antenae.rect.y += antenae.speedy
        antenae.speedx = 0

        ticks_0 = 0
        
    ticks_0 += 1
    ticks_1 += 1
    ticks_2 += 1
    
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            state = DONE
        # ----- Verifica se apertou alguma tecla
        if state == PLAYING:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if player.lado == 'direita':
                        player.move('esquerda')
                        jump_sound.play()
                # player.rect.x = WIDTH-352.5
                #  player.rect.y = HEIGHT-200
                if event.key == pygame.K_RIGHT:
                    if player.lado == 'esquerda':
                        player.move('direita')
                        jump_sound.play()
                #  player.rect.x = WIDTH-352.5
                #   player.rect.y = HEIGHT-200
                if event.key == pygame.K_SPACE:
                    if numeroshurikens <= 3 and numeroshurikens > 0:
                        player.shoot()
                        numeroshurikens -= 1
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
    if state == PLAYING:
        hits = pygame.sprite.spritecollide(player, all_obstacles, True)
        if len(hits) > 0:
            collision_sound.play()
            player.kill()
            time.sleep(0.5)
            state = DYING
            vidas -= 1
            if vidas == 0:
                state = DONE
            else:
                state = PLAYING
                player = Ninja(groups, assets)
                all_sprites.add(player)

        # Verifica se houve colisão entre os obstáculos e o ninja
        colidiuad = pygame.sprite.groupcollide(all_shurikens, all_antenad, True, True)
        for colisoes in colidiuad:
            antenad = Antena(assets['antenaesquerda'],antenad.speedy,'direito')
            all_sprites.add(antenad)
            all_obstacles.add(antenad)
            all_antenad.add(antenad)

            explosao = Explosao(colisoes.rect.center, assets)
            all_sprites.add(explosao)

        colidiuae = pygame.sprite.groupcollide(all_shurikens, all_antenae, True, True)
        for colisoes in colidiuae:
            antenae = Antena(assets['antenadireita'],antenae.speedy,'esquerdo')
            all_sprites.add(antenae)
            all_obstacles.add(antenae)
            all_antenae.add(antenae)

            explosao = Explosao(colisoes.rect.center, assets)
            all_sprites.add(explosao)

        colidiucd = pygame.sprite.groupcollide(all_shurikens, all_canod, True, True)
        for colisoes in colidiucd:
            cd = Cano(assets['canodireita'],canoe.speedy,'direito')
            all_sprites.add(cd)
            all_obstacles.add(cd)
            all_canod.add(cd)

            explosao = Explosao(colisoes.rect.center, assets)
            all_sprites.add(explosao)
        
        colidiuce = pygame.sprite.groupcollide(all_shurikens, all_canoe, True, True)
        for colisoes in colidiuce:
            ce = Cano(assets['canoesquerda'],canoe.speedy, 'esquerdo')
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

    #---------DESENHANDO O PLACAR
    text_surface1 = assets['fontemenorpontuacao'].render(('PONTOS:'), True, (255,255,255))
    text_surface2 = assets['fonteplacar'].render("{:04d}".format(placar), True, (255, 255, 255))
    text_rect1 = text_surface1.get_rect()
    text_rect2 = text_surface2.get_rect()
    text_rect1.topleft = (HEIGHT - 255, HEIGHT - 750)
    text_rect2.topleft = (HEIGHT - 253, HEIGHT - 725)
    window.blit(text_surface1, text_rect1)
    window.blit(text_surface2, text_rect2)

    #----------DESENHANDO AS VIDAS
    text_surface = assets['score_font'].render(chr(9829) * vidas, True, (255, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.bottomleft = (10, HEIGHT - 10)
    window.blit(text_surface, text_rect)

    #----------DESENHANDO A KUNAI
    kunai = assets['shuriken']
    kunai_rect = kunai.get_rect()
    kunai_rect.bottomleft = (25, HEIGHT - 60)
    qtdkunais = assets['fontemenorpontuacao'].render("= {}".format(numeroshurikens), True, (255, 255, 255))
    qtdkunais_rect = qtdkunais.get_rect()
    qtdkunais_rect.bottomleft = (50, HEIGHT - 70)
    window.blit(kunai, kunai_rect)
    window.blit(qtdkunais, qtdkunais_rect)

    window.blit(text_surface1, text_rect1)
    window.blit(text_surface2, text_rect2)

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados