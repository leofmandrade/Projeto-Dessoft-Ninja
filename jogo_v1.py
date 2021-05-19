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
'''
class Ninja(pygame.sprite.Sprite):
    def __init__(self, groups, img): 
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['ninjadireita00']
        self.rect = self.image.get_rect()
        self.speedx = 0
        self.groups = groups
        self.assets = assets
        self.image = img

    def update(self):
        # Atualização da posição do ninja
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def atirar(self):
        # A nova bala vai ser criada logo acima e no centro horizontal da nave
        novashuriken = Shuriken(self.assets, self.rect.top, self.rect.centerx)
        self.groups['all_sprites'].add(novashuriken)
        self.groups['all_bullets'].add(novashuriken)

class CanoEsquerda(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['canoesquerda']
        self.rect = self.image.get_rect()
        self.speedy = 5

        def update(self):
        # Atualizando a posição do cano
            self.rect.y += self.speedy
        # Se o cano passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT:
            self.speedy = 5

class Shuriken(pygame.sprite.Sprite):
    def __init__(self, assets, bottom, centerx):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['shuriken']
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
'''

game = True
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30
#----CANO DA ESQUERDA PRONTO PORRA IHAAAAAAA
canoe_x = 0
canoe_y = -300
canoe_speedy = 5
#----ANTENA DA DIREITA
antenad_x = 0
antenad_y = -600
antenad_speedy = 5

'''
# Criando um grupo de meteoros
all_sprites = pygame.sprite.Group()
all_obstaculos = pygame.sprite.Group()
all_shurikens = pygame.sprite.Group()
groups = {}
groups['all_sprites'] = all_sprites
groups['all_meteors'] = all_obstaculos
groups['all_bullets'] = all_shurikens

# Criando o jogador
player = Ninja(groups, assets)
all_sprites.add(player)

all_canosesquerdos = pygame.sprite.Group()
#Criando obstáculos
for i in range(10):
    canoesquerda = CanoEsquerda(assets)
    all_canosesquerdos.add(canoesquerda)
'''
# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        # ----- Atualiza estado do jogo
    # ----- Atualiza estado do jogo
    # Atualizando a posição do meteoro
    canoe_y += canoe_speedy
    antenad_y += antenad_speedy
    # Se o meteoro passar do final da tela, volta para cima
    if canoe_y > HEIGHT:
        canoe_y = -300
    if antenad_y > HEIGHT:
        antenad_y = -300
    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca)
    window.blit(assets['fundo'], (0, 0))
    window.blit(assets['paredes'], (0,0))
    window.blit(assets['placa'], (0, 0))
    window.blit(assets['ninjadireita00'],(0,0))
    window.blit(assets['canoesquerda'], (canoe_x, canoe_y))
    window.blit(assets['antenadireita'], (antenad_x, antenad_y))


    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados