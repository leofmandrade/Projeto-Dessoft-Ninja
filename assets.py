import pygame
import os
from config import IMG_DIR, SND_DIR, FNT_DIR
color_key = (0, 89, 255)

BACKGROUND = 'background'
PAREDES = 'paredes'
PLACA = 'placa'
NINJADIREITA00 = 'ninjadireita00'
NINJADIREITA01 = 'ninjadireita01'
NINJAESQUERDA00 = 'ninjaesquerda00'
NINJAESQUERDA01 =  'ninjaesquerda01'
NINJAPULANDOD02= 'ninjapulandod02'
NINJAPULANDOE02 = 'ninjapulandoe02'
CANOESQUERDA = 'canoesquerda'
CANODIREITA = 'canodireita'
ANTENADIREITA = 'antenadireita'
ANTENAESQUERDA = 'antenaesquerda'
SHURIKEN = 'shuriken'
EXPLOSAO = 'explosao'
FONTEPLACAR = 'fonteplacar'
FONTEMENORPUNTUACAO = 'fontemenorpontuacao'
SCORE_FONT = 'scorefont'
MUSIC = 'music'
SHURIKEN_SOUND = 'shuriken_sound'
JUMP_SOUND= 'jump_sound'
COLLISION_SOUND = 'collision_sound'

pygame.init()

def load_assets():
    assets = {}
    assets['fundo'] = pygame.image.load(os.path.join(IMG_DIR, 'FUNDOJOGOFINAL.png'))
    assets['paredes'] = pygame.image.load(os.path.join(IMG_DIR,'PAREDESFINAL.png'))
    assets['placa'] = pygame.image.load(os.path.join(IMG_DIR, 'PLACA.png'))
    #-----Imagens do ninja
    #Logo Ninja
    assets['logoninja'] = pygame.image.load(os.path.join(IMG_DIR,'LOGONINJA.png'))
    #Ninja andando
    assets['ninjadireita00'] = pygame.image.load(os.path.join(IMG_DIR,'NINJAANDANDODIREITA00.png'))
    assets['ninjaesquerda00'] = pygame.image.load(os.path.join(IMG_DIR,'NINJAANDANDOESQUERDA00.png'))
    assets['ninjadireita01'] = pygame.image.load(os.path.join(IMG_DIR,'NINJAANDANDODIREITA01.png'))
    assets['ninjaesquerda01'] = pygame.image.load(os.path.join(IMG_DIR,'NINJAANDANDOESQUERDA01.png'))

    #Ninja Pulando
    assets['ninjapulandod02'] = pygame.image.load(os.path.join(IMG_DIR,'NINJAPULANDODIREITA02.png'))
    assets['ninjapulandoe02'] = pygame.image.load(os.path.join(IMG_DIR,'NINJAPULANDOESQUERDA02.png'))

    #-----Imagens dos obstáculos
    assets['canoesquerda']= pygame.image.load(os.path.join(IMG_DIR,'CANOESQUERDA.png'))
    assets['canodireita']= pygame.image.load(os.path.join(IMG_DIR,'CANODIREITA.png'))
    assets['antenaesquerda']= pygame.image.load(os.path.join(IMG_DIR,'ANTENAESQUERDA.png'))
    assets['antenaesquerda']= pygame.transform.scale(assets['antenaesquerda'], (103, 94))
    assets['antenadireita']= pygame.image.load(os.path.join(IMG_DIR,'ANTENADIREITA.png'))
    assets['antenadireita']= pygame.transform.scale(assets['antenadireita'], (103, 94))
    #-----Imagem do projétil

    assets['shuriken']= pygame.image.load(os.path.join(IMG_DIR,'SHURIKEN.png'))

    #-----Imagem da explosão
    assets['explosion00'] = pygame.image.load(os.path.join(IMG_DIR,'EXPLOSAO00.png'))
    explosao = []
    for i in range(6):
        diretorio = os.path.join(IMG_DIR,'EXPLOSAO0{}.png'.format(i))
        img = pygame.image.load(diretorio)
        img.set_colorkey(color_key)
        explosao.append(img) 
    assets['explosao']= explosao

    # Carrega os sons do jogo

    assets['music'] = pygame.mixer.music.load(os.path.join(SND_DIR, 'Musica2.ogg'))
    assets['music'] = pygame.mixer.music.set_volume(0.2)
    assets['shuriken_sound'] = pygame.mixer.Sound(os.path.join(SND_DIR,'ShurikenSound2.wav'))
    assets['jump_sound'] = pygame.mixer.Sound(os.path.join(SND_DIR,'JumpSound.wav'))
    assets['collision_sound'] = pygame.mixer.Sound(os.path.join(SND_DIR,'CollisionSound.wav'))

    #--------Carrega a fonte do placar
    assets['fonteplacar'] = pygame.font.Font(os.path.join(FNT_DIR,'game_over.ttf'), 100)
    assets['fontemenorpontuacao'] = pygame.font.Font(os.path.join(FNT_DIR,'game_over.ttf'), 60)

    #--------FONTE DAS VIDAS
    assets['score_font'] = pygame.font.Font(os.path.join(FNT_DIR,'PressStart2P.ttf'), 28)
    return assets

