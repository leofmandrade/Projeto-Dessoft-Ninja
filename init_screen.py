# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from config import WIDTH, HEIGHT
pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((600, 750))

# ----- Inicia estruturas de dados
game = True

# ----- Inicia assets
imageminicio = pygame.image.load('assets/img/TELAINICIAL.png')
# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca
    window.blit(imageminicio, (0, 0))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador