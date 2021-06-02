import random
import pygame
from config import WIDTH, HEIGHT

from assets import load_assets, BACKGROUND, SCORE_FONT, PAREDES, PLACA, NINJADIREITA00, NINJADIREITA01, NINJAESQUERDA00, NINJAESQUERDA01, NINJAPULANDOD02, NINJAPULANDOE02, CANODIREITA, CANOESQUERDA, ANTENADIREITA, ANTENAESQUERDA, SHURIKEN, EXPLOSAO, FONTEMENORPUNTUACAO, FONTEPLACAR, MUSIC, SHURIKEN_SOUND, JUMP_SOUND, COLLISION_SOUND

assets = load_assets()

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
            self.rect.y = HEIGHT-150
            self.rect.x = WIDTH-490
            if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
                self.last_update = now
                self.frame += 1
                if self.frame >= len(self.andandodireita):
                    self.frame = 0
                self.image = self.andandoesquerda[self.frame]

        if self.lado == 'meiodireita':
            self.image = assets['ninjapulandoe02']
            self.rect.x = WIDTH-352.5
            self.rect.y = HEIGHT-200
            self.lado = 'esquerda'

        if self.lado == 'meioesquerda':
            self.image = assets['ninjapulandod02']
            self.rect.x = WIDTH-352.5
            self.rect.y = HEIGHT-200
            self.lado = 'direita'

    def shoot(self):
        # A nova bala vai ser criada logo acima e no centro horizontal da nave
        return Shuriken(self.rect.top, self.rect.centerx, assets['shuriken_sound'])

class Shuriken(pygame.sprite.Sprite):
    def __init__(self, bottom, centerx, shuriken_sound):
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
            self.kill()

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
            self.kill()

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


