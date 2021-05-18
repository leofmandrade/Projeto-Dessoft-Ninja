# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
pygame.init()

# ----- Gera tela principal
Width = 600
Height = 750
window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Run Shinobi, Run!")

#------Inicia os assets

image = pygame.image.load('C:/Users/User/Desktop/INSPER/DESOFT/PYGAME/Projeto-Dessoft-Ninja/assets/FUNDOJOGO.png').convert()
paredes = pygame.image.load('C:/Users/User/Desktop/INSPER/DESOFT/PYGAME/Projeto-Dessoft-Ninja/assets/PAREDES.png')
placa = pygame.image.load('C:/Users/User/Desktop/INSPER/DESOFT/PYGAME/Projeto-Dessoft-Ninja/assets/PLACA.png')
ninjainicio = pygame.image.load('C:/Users/User/Desktop/INSPER/DESOFT/PYGAME/Projeto-Dessoft-Ninja/assets/NINJAINICIO.png')
fundo = pygame.transform.scale(image, (Width, Height))

# ----- Inicia estruturas de dados
game = True

# ----- Inicia assets
font = pygame.font.SysFont(None, 48)

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca

    window.blit(fundo, (0, 0))
    window.blit(paredes, (0,0))
    window.blit(placa, (0, 0))
    window.blit(ninjainicio, (0,0))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados