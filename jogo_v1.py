# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

# ----- Gera tela principal
Width = 600
Height = 800
window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption('Shinobi`s power')
image = pygame.image.load('/Users/caiotieri/Documents/INSPER/DESSOFT/Projeto pygame/Projeto-Dessoft-Ninja/Fundo2.png').convert()
fundo = pygame.transform.scale(image, (Width, Height))
# ----- Inicia estruturas de dados
game = True

# ----- Inicia assets
font = pygame.font.SysFont(None, 48)
text = font.render('Shinobi`s power', True, (255, 0, 0))

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
    window.blit(text, (200, 10))

    #---paredes
    corparede= (100,50,50)
    vertices1 = [(0,0),(100,0),(100,800),(0,800)]
    vertices2= [(500,0),(600,0),(600,800),(500,800)]
    pygame.draw.polygon(window, corparede, vertices1)
    pygame.draw.polygon(window, corparede, vertices2)
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados