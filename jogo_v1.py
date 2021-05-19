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

game = True
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30
#----CANO DA ESQUERDA PRONTO PORRA IHAAAAAAA
canoe_x = 0
canoe_y = -400
canoe_speedy = 5
#----ANTENA DA DIREITA
antenad_x = 0
antenad_y = -600
antenad_speedy = 5
#----CANO DA DIREITA
canod_x = 0
canod_y= -100
canod_speedy = 5
#----ANTENA DA ESQUERDA
antenae_x = 0
antenae_y = -800
antenae_speedy = 5

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
    canoe_y += canoe_speedy
    antenad_y += antenad_speedy
    canod_y += canod_speedy
    antenae_y += antenae_speedy
    # Se o objeto passar do final da tela, volta para cima
    if canoe_y > HEIGHT:
        canoe_y = -400
    if antenad_y > HEIGHT:
        antenad_y = -600
    if canod_y > HEIGHT:
        canod_y = -250
    if antenae_y > HEIGHT:
        antenae_y = -300
    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca)
    window.blit(assets['fundo'], (0, 0))
    window.blit(assets['paredes'], (0,0))
    window.blit(assets['placa'], (0, 0))
    window.blit(assets['ninjadireita00'],(0,0))
    window.blit(assets['canoesquerda'], (canoe_x, canoe_y))
    window.blit(assets['antenadireita'], (antenad_x, antenad_y))
    window.blit(assets['canodireita'], (canod_x, canod_y))
    window.blit(assets['antenaesquerda'], (antenae_x, antenae_y))


    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados