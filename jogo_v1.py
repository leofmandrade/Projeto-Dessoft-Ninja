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

image = pygame.image.load('assets/img/FUNDOJOGOFINAL.png').convert()
paredes = pygame.image.load('assets/img/PAREDESFINAL.png')
placa = pygame.image.load('assets/img/PLACA.png')
ninjainicio = pygame.image.load('assets/img/NINJAINICIO.png')
fundo = pygame.transform.scale(image, (WIDTH, HEIGHT))

# ----- Inicia estruturas de dados
class Ninja(pygame.sprite.Sprite):
    def __init__(self, img): 
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()

game = True


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