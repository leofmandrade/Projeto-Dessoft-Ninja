import pygame
from config import FPS, WIDTH, HEIGHT, BLACK, YELLOW, RED
from assets import load_assets, BACKGROUND, SCORE_FONT, PAREDES, PLACA, NINJADIREITA00, NINJADIREITA01, NINJAESQUERDA00, NINJAESQUERDA01, NINJAPULANDOD02, NINJAPULANDOE02, CANODIREITA, CANOESQUERDA, ANTENADIREITA, ANTENAESQUERDA, SHURIKEN, EXPLOSAO, FONTEMENORPUNTUACAO, FONTEPLACAR, MUSIC, SHURIKEN_SOUND, JUMP_SOUND, COLLISION_SOUND
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
    spd = 7

    #----CANOS (POR CLASS)
    canoe = Cano(assets['canoesquerda'], spd, 'esquerdo')
    canod = Cano(assets['canodireita'], spd, 'direito')

    #----ANTENA (POR CLASS)
    antenae = Antena(assets['antenadireita'], spd, 'esquerdo')
    antenad = Antena(assets['antenaesquerda'], spd, 'direito')

    #adicionando tudo num grupo só
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
    game = True
    PLAYING = 1
    INITIAL = 2
    FINISH = 3
    INSTRUCTIONS = 4

    ticks_0 = 0
    ticks_1 = 0
    ticks_2 = 0

    placar = 0
    vidas = 3
    speed = 1

    pygame.mixer.music.play(loops=-1)
    # ===== Loop principal =====
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            window.fill((255, 255, 255))  # Preenche com a cor branca)
            window.blit(assets['telainicial'], (0, 0))
            pygame.display.update()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    print('a')
                    #state == INSTRUCTIONS
                    window.blit(assets['instrucoes'], (0, 0))
                    pygame.display.update()
                if event.key == pygame.K_b:
                    print('b')
                    clock.tick(FPS)
                    #AUMENTANDO PROGRESSIVAMENTE A VELOCIDADE
                    if ticks_2 >= 900:
                        numeroshurikens = 3
                        ticks_2 = 0

                    if ticks_1 >= 15:
                        placar += 5
                        ticks_1 = 0
                    
                    if ticks_0 >= 600:
                        canoe.speedy += 1
                        canoe.rect.y += speed
                        canoe.speedx = 0
                        
                        canod.speedy += 1
                        canod.rect.y += speed
                        canod.speedx = 0

                        antenad.speedy += 1
                        antenad.rect.y += speed
                        antenad.speedx = 0
                        
                        antenae.speedy += 1
                        antenae.rect.y += speed
                        antenae.speedx = 0

                        all_obstacles.update(antenae.speedy)
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
                            all_obstacles.update(canoe.speedy)

                            #-----Verifica colisão
                            hits = pygame.sprite.spritecollide(player, all_obstacles, True)
                            if len(hits) > 0:
                                assets['collision_sound'].play()
                                player.kill()
                                vidas -= 1

                            if vidas == 0:
                                window.blit(assets['telafinal'], (0, 0))
                                pygame.display.update()

                            # Verifica se houve colisão entre os obstáculos e o ninja
                            colidiuad = pygame.sprite.groupcollide(all_shurikens, all_antenad, True, True)
                            for colisoes in colidiuad:
                                antenad = Antena(assets['antenaesquerda'],antenad.speedy,'direito')
                                all_obstacles.add(antenad)
                                all_antenad.add(antenad)

                                explosao = Explosao(colisoes.rect.center, assets)
                                all_sprites.add(explosao)

                            colidiuae = pygame.sprite.groupcollide(all_shurikens, all_antenae, True, True)
                            for colisoes in colidiuae:
                                antenae = Antena(assets['antenadireita'],antenae.speedy,'esquerdo')
                                all_obstacles.add(antenae)
                                all_antenae.add(antenae)

                                explosao = Explosao(colisoes.rect.center, assets)
                                all_sprites.add(explosao)

                            colidiucd = pygame.sprite.groupcollide(all_shurikens, all_canod, True, True)
                            for colisoes in colidiucd:
                                cd = Cano(assets['canodireita'],canoe.speedy,'direito')
                                all_obstacles.add(cd)
                                all_canod.add(cd)

                                explosao = Explosao(colisoes.rect.center, assets)
                                all_sprites.add(explosao)
                            
                            colidiuce = pygame.sprite.groupcollide(all_shurikens, all_canoe, True, True)
                            for colisoes in colidiuce:
                                ce = Cano(assets['canoesquerda'],canoe.speedy, 'esquerdo')
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
                pygame.display.update()
