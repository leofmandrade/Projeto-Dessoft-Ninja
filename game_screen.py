from random import randint
import pygame
from config import WIDTH, HEIGHT, BLACK, YELLOW, RED
from assets import load_assets
from sprites import Ninja, Cano, Antena, Explosao, Shuriken
pygame.init()

def game_screen(window):

    clock = pygame.time.Clock()

    assets = load_assets()
        # Variável para o ajuste de velocidade
    
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

    #adicionando no dicionario
    groups['all_sprites']=all_sprites
    groups['all_obstacles']=all_obstacles
    groups['all_shurikens'] = all_shurikens

    #criando o jogador
    player = Ninja(groups, assets)

    #adicionando tudo num grupo só
    all_sprites.add(player)

    #adicionando um numero limitado de shurikens
    numeroshurikens= 3

    #ESTADOS
    game = True
    PLAYING = 1
    INITIAL = 2
    FINISH = 3
    INSTRUCTIONS = 4
    state = INITIAL

    ticks_0 = 0
    ticks_1 = 0
    ticks_2 = 0

    placar = 0
    vidas = 3
    speedy = 7

    pygame.mixer.music.play(loops=-1)
    # ===== Loop principal =====
    
    while game:
        if state == PLAYING:
            clock.tick(FPS)
            #AUMENTANDO PROGRESSIVAMENTE A VELOCIDADE
            if ticks_2 >= 900:
                numeroshurikens = 3
                ticks_2 = 0

            if ticks_1 >= 15:
                placar += 5
                ticks_1 = 0
            
            if ticks_0 >= 600:
                speedy += 3
                for obs in all_obstacles:
                    obs.speedy = speedy
                print(speedy)
                ticks_0 = 0
                
            ticks_0 += 1
            ticks_1 += 1
            ticks_2 += 1
            
            # ----- Trata eventos
            for event in pygame.event.get():
                # ----- Verifica consequências
                if event.type == pygame.QUIT:
                    game = False
                # ----- Verifica se apertou alguma tecla
                if state == PLAYING:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            if player.lado == 'direita':
                                player.move('esquerda')
                                assets['jump_sound'].play()
                        # player.rect.x = WIDTH-352.5
                        #  player.rect.y = HEIGHT-200
                        if event.key == pygame.K_RIGHT:
                            if player.lado == 'esquerda':
                                player.move('direita')
                                assets['jump_sound'].play()
                        #  player.rect.x = WIDTH-352.5
                        #   player.rect.y = HEIGHT-200
                        if event.key == pygame.K_SPACE:
                            if numeroshurikens <= 3 and numeroshurikens > 0:
                                shuriken = player.shoot()
                                all_sprites.add(shuriken)
                                all_shurikens.add(shuriken)
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

           # all_obstacles.update(canoe.speedy)
            
            while len(all_obstacles)<=2:
                opc = randint(1,4)
                if opc == 1:
                    obs = Cano(assets['canoesquerda'], speedy , 'esquerdo')
                elif opc == 2:
                    obs = Cano(assets['canodireita'], speedy, 'direito')
                elif opc == 3:
                    obs = Antena(assets['antenadireita'], speedy, 'esquerdo')
                else: 
                    obs = Antena(assets['antenaesquerda'], speedy, 'direito')

                all_obstacles.add(obs)
                all_sprites.add(obs)

            #-----Verifica colisão
            if state == PLAYING:
                hits = pygame.sprite.spritecollide(player, all_obstacles, True)
                if len(hits) > 0:
                    assets['collision_sound'].play()
                    player.kill()
                    vidas -= 1
                    if vidas == 0:
                        state = FINISH
                    else:
                        #all_obstacles.empty()
                        for obs in all_obstacles:
                            obs.kill()
                        state = PLAYING
                        player = Ninja(groups, assets)
                        all_sprites.add(player)

                # Verifica se houve colisão entre os obstáculos e o ninja
                colidiuad = pygame.sprite.groupcollide(all_shurikens, all_obstacles, True, True)
                for colisoes in colidiuad:
                    explosao = Explosao(colisoes.rect.center, assets)
                    all_sprites.add(explosao)
            
            # ----- Gera saídas
            window.fill((255, 255, 255))  # Preenche com a cor branca)
            window.blit(assets['fundo'], (0, 0))
            window.blit(assets['paredes'], (0,0))
            window.blit(assets['placa'], (0, 0))
            all_sprites.draw(window)
            all_obstacles.draw(window)

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
  
        if state == INITIAL:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                #print('estado: {}'.format(state))
                window.fill((255, 255, 255))  # Preenche com a cor branca)
                window.blit(assets['telainicial'], (0, 0))
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        state = INSTRUCTIONS
                        #print('a')

        elif state == INSTRUCTIONS:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                window.fill((255, 255, 255))  # Preenche com a cor branca)
                window.blit(assets['instrucoes'], (0, 0))
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        state = PLAYING

        elif state == FINISH:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                window.fill((255, 255, 255))  # Preenche com a cor branca)
                window.blit(assets['telafinal'], (0, 0))
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        game = False
                    if event.key == pygame.K_r:
                        state = INSTRUCTIONS
                        for obs in all_obstacles:
                            obs.kill()
                        speedy = 7
                        vidas = 3
                        placar = 0
                        player = Ninja(groups, assets)
                        all_sprites.add(player)

        #Mostra o novo frame pro jogador
        pygame.display.update()
        
