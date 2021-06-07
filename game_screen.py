#---Importando bibliotecas
from random import randint
import pygame
from config import WIDTH, HEIGHT
from assets import load_assets
from sprites import Ninja, Cano, Antena, Explosao, Shuriken
pygame.init()

#---Função da tela e funcionamento do jogo
def game_screen(window):
    clock = pygame.time.Clock()
    assets = load_assets()

    #---Variável para o ajuste de velocidade
    FPS = 30
    #---Criando dicionário de grupos
    groups = {}
    #---Sprites
    all_sprites = pygame.sprite.Group()
    #---Obstáculos
    all_obstacles = pygame.sprite.Group()
    #---Shurikens
    all_shurikens = pygame.sprite.Group()

    #---Adicionando no dicionário
    groups['all_sprites']=all_sprites
    groups['all_obstacles']=all_obstacles
    groups['all_shurikens'] = all_shurikens

    #---Criando o jogador (ninja)
    player = Ninja(groups, assets)

    #---Adicionando tudo em um grupo só
    all_sprites.add(player)

    #---Adicionando um número limitado de shurikens
    numeroshurikens= 3

    #---Criando estados para facilitar o código do jogo e estabelecendo um estado inicial
    game = True
    PLAYING = 1
    INITIAL = 2
    FINISH = 3
    INSTRUCTIONS = 4
    state = INITIAL

    #---Criando variáveis para os ticks 
    ticks_0 = 0
    ticks_1 = 0
    ticks_2 = 0

    #---Criando variáveis para placar, vidas e velocidade inicial dos obstáculos
    placar = 0
    vidas = 3
    speedy = 7

    #---Inicia a música de fundo do jogo
    pygame.mixer.music.play(loops=-1)


    # ===== Loop principal =====
    while game:
        if state == PLAYING:    #Caso o estado seja "PLAYING"...
            clock.tick(FPS)
            #---A cada 900 ticks o número de shurikens irá resetar à 3
            if ticks_2 >= 900:
                numeroshurikens = 3
                ticks_2 = 0
            #---Aumentando o score do jogador no placar
            if ticks_1 >= 15:
                placar += 5
                ticks_1 = 0
            #---Aumentando progressivamente a velocidade dos obstáculos
            if ticks_0 >= 600:
                speedy += 3
                for obs in all_obstacles:
                    obs.speedy = speedy
                print(speedy)
                ticks_0 = 0
            ticks_0 += 1
            ticks_1 += 1
            ticks_2 += 1
            
            #---Trata eventos
            for event in pygame.event.get():
                #---Verifica consequências
                if event.type == pygame.QUIT:
                    game = False
                if state == PLAYING:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:          #Verifica se apertou a -setinha da esquerda-
                            if player.lado == 'direita':        #Caso tenha apertado e ele estiver na direita, o ninja pula pra esquerda
                                player.move('esquerda')
                                assets['jump_sound'].play()
                        
                        if event.key == pygame.K_RIGHT:
                            if player.lado == 'esquerda':       #Verifica se apertou a -setinha da direita-
                                player.move('direita')          #Caso tenha apertado e ele estiver na esquerda, o ninja pula pra direita
                                assets['jump_sound'].play()
                        
                        if event.key == pygame.K_SPACE:         #Verifica se apertou a -barra de espaço-
                            if numeroshurikens <= 3 and numeroshurikens > 0:    #Atira um shuriken para cima
                                assets['shuriken_sound'].play()  
                                shuriken = player.shoot()
                                all_sprites.add(shuriken)
                                all_shurikens.add(shuriken)
                                numeroshurikens -= 1

                    #---Mudança do ninja de posição
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT:
                            player.rect.y = HEIGHT-150
                            player.rect.x = WIDTH-495
                        if event.key == pygame.K_RIGHT:
                            player.rect.x = WIDTH-210
                            player.rect.y = HEIGHT-150
            
            #---Atualizando as sprites do jogo
            all_sprites.update()

            #---Gerador dos obstáculos (usando 'randint' para que o surgimento seja aleatório)
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

            if state == PLAYING:
                hits = pygame.sprite.spritecollide(player, all_obstacles, True)
                if len(hits) > 0:       #Verifica colisão
                    assets['collision_sound'].play()
                    player.kill()
                    vidas -= 1
                    if vidas == 0:
                        state = FINISH      #Se as vidas chegarem à zero, muda o estado para "FINISH" e vai para a tela final
                    else:
                        for obs in all_obstacles:
                            obs.kill()      #Caso ele bata em um obstáculo, todos irão sumir, para que o jogador tenha um pequeno intervalo sem perder vidas
                        state = PLAYING
                        player = Ninja(groups, assets)
                        all_sprites.add(player)

                #---Verifica se houve colisão entre os obstáculos e o ninja, para que a sprite de explosão apareça e o obstáculo suma
                colidiuad = pygame.sprite.groupcollide(all_shurikens, all_obstacles, True, True)
                for colisoes in colidiuad:
                    assets['explosion_sound'].play()
                    explosao = Explosao(colisoes.rect.center, assets)
                    all_sprites.add(explosao)
            
            #---Gera saídas
            window.fill((255, 255, 255))            #Preenche o fundo com a cor branca
            window.blit(assets['fundo'], (0, 0))    #Plano de fundo (cidade)
            window.blit(assets['paredes'], (0,0))   #Paredes
            window.blit(assets['placa'], (0, 0))    #Placar 
            all_sprites.draw(window)
            all_obstacles.draw(window)

            #---Desenhando o placar
            text_surface1 = assets['fontemenorpontuacao'].render(('PONTOS:'), True, (255,255,255))
            text_surface2 = assets['fonteplacar'].render("{:04d}".format(placar), True, (255, 255, 255))
            text_rect1 = text_surface1.get_rect()
            text_rect2 = text_surface2.get_rect()
            text_rect1.topleft = (HEIGHT - 255, HEIGHT - 750)
            text_rect2.topleft = (HEIGHT - 253, HEIGHT - 725)
            window.blit(text_surface1, text_rect1)
            window.blit(text_surface2, text_rect2)

            #---Desenhando as vidas
            text_surface = assets['score_font'].render(chr(9829) * vidas, True, (255, 0, 0))
            text_rect = text_surface.get_rect()
            text_rect.bottomleft = (10, HEIGHT - 10)
            window.blit(text_surface, text_rect)

            #---Desenhando o shuriken (kunai)
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
  
        #---Caso o estado seja "INITIAL"...
        if state == INITIAL:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                
                window.fill((255, 255, 255))                #Preenche o fundo com a cor branca
                window.blit(assets['telainicial'], (0, 0))  #Insere a tela de início
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        assets['watah_sound'].play()
                        state = INSTRUCTIONS                #Muda de tela e vai para a parte das instruções, com a mudança de estado
        
        #---Caso o estado seja "INSTRUCTIONS"...
        elif state == INSTRUCTIONS:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                window.fill((255, 255, 255))                #Preenche o fundo com a cor branca
                window.blit(assets['instrucoes'], (0, 0))   #Insere a tela das instruções
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        assets['watah_sound'].play()
                        state = PLAYING                     #Muda de tela e vai para a parte do jogo em si, com a mudança de estado

        #---Caso o estado seja "FINISH"...
        elif state == FINISH:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                window.fill((255, 255, 255))                #Preenche o fundo com a cor branca
                window.blit(assets['telafinal'], (0, 0))    #Insere a tela final de game over
                text_surface3 = assets['fonteplacar'].render("Seu score foi de: {:04d}".format(placar), True, (255, 255, 255))
                text_rect3 = text_surface3.get_rect()
                text_rect3.bottomright = (WIDTH-110, HEIGHT-200)
                window.blit(text_surface3, text_rect3)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        game = False                        #Caso a tecla "A" seja apertada, o jogo acaba e a tela fecha
                    if event.key == pygame.K_r:
                        state = INSTRUCTIONS                
                        for obs in all_obstacles:
                            obs.kill()
                        speedy = 7
                        vidas = 3
                        placar = 0
                        player = Ninja(groups, assets)
                        all_sprites.add(player)             #Caso a tecla "R" seja apertada, o jogo reinicia totalmente

        #---Mostra o novo frame pro jogador
        pygame.display.update()
        
