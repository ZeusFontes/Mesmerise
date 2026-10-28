import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pygame
import json
import controller
import config
import progress
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'




pygame.init()

icone = pygame.image.load("icone.png")
pygame.display.set_icon(icone)
pygame.display.set_caption("Mesmerize")
fonte = pygame.font.SysFont(None,28)

fullscreen_antigo = config.fullscreen_ativo
menu_anterior = None
resolucao_antiga = config.res
destino = 19
fps = 0
alpha = 255
som = ""
texto = ""
rodando = True
apaga = False
acende = True
touch = (19,'','')
mochila_antiga = progress.mochila.copy()
imgicon = ['', '', '', '', '']


def carregar(caminho):
    img = pygame.image.load(caminho).convert()
    if caminho == "./assets/menu.png" or caminho == "./assets/menu1.png":
        return pygame.transform.scale(img, config.resulucao[config.res])
    else:
        return pygame.transform.scale(img, config.imagem)

    
def tocar(caminho):
     pygame.mixer.music.fadeout(500)
     pygame.mixer.music.load(caminho)
     pygame.mixer.music.set_volume(config.volmusica)
     pygame.mixer.music.play(-1, fade_ms=500) 

def carregaricon(caminhoicone,tamanho_slot):
    imgicon = pygame.image.load(caminhoicone).convert()
    return pygame.transform.scale(imgicon, tamanho_slot)


tocarmenu = "assets/sounds/menu.mp3"
tocarjogo = "assets/sounds/jogo.mp3"

tela = pygame.display.set_mode(config.resulucao[config.res])
relogio = pygame.time.Clock()


fundos = [carregar(c) for c in controller.salas]

preta = pygame.Surface((1920,1080))
preta.fill((0,0,0))


caixa = pygame.Surface((config.escalar2(900, 120,config.resulucao,config.res)))
caixa.fill((0, 0, 0))
caixa.set_alpha(255)


tamanho_slot = config.escalar2(50, 50, config.resulucao, config.res)

caminhoicone = [
    "./assets/icons/icon_vazio.png",
    "./assets/icons/icon_vazio.png",
    "./assets/icons/icon_vazio.png",
    "./assets/icons/icon_vazio.png"
]



inicio_icon = pygame.image.load("./assets/icons/icon_vazio.png").convert()
inv1 = pygame.transform.scale(inicio_icon, tamanho_slot)
inv2 = pygame.transform.scale(inicio_icon, tamanho_slot)
inv3 = pygame.transform.scale(inicio_icon, tamanho_slot)
inv4 = pygame.transform.scale(inicio_icon, tamanho_slot)


largura1, altura1 = config.resulucao[config.res]
largura2, altura2 = config.imagem

if config.menu:
    tocar(tocarmenu)

## LOOP DO PROGRAMA 
while rodando: 

    ## ALTERANDO A RESOLUÇÃO
    if config.res != resolucao_antiga or fullscreen_antigo != config.fullscreen_ativo:
        resolucao_antiga = config.res
        fullscreen_antigo = config.fullscreen_ativo
        if config.fullscreen_ativo:
            tela = pygame.display.set_mode(config.resulucao[config.res], pygame.FULLSCREEN)
        else:
            tela = pygame.display.set_mode(config.resulucao[config.res])
        config.imagem = ((config.resulucao[config.res][0] / 3) * 2, (config.resulucao[config.res][1] / 3) * 2)
        fundos = [carregar(c) for c in controller.salas]
        largura1, altura1 = config.resulucao[config.res]
        largura2, altura2 = config.imagem
        tamanho_slot = config.escalar2(50, 50, config.resulucao, config.res)
        caixa = pygame.Surface((config.escalar2(900, 80, config.resulucao, config.res)))
        caixa.fill((0, 0, 0))
        caixa.set_alpha(255)
        match config.res:
            case 0:
                fonte = pygame.font.SysFont(None,28)
            case 1:
                fonte = pygame.font.SysFont(None,35)
            case 2:
                fonte = pygame.font.SysFont(None,40)
            case 3:
                fonte = pygame.font.SysFont(None,45)
            case 3:
                fonte = pygame.font.SysFont(None,50)
            case 4:
                fonte = pygame.font.SysFont(None,55)
            case _:
                fonte = pygame.font.SysFont(None,28)

 #TROCA A MUSICA
    if config.menu != menu_anterior:
        if config.menu == True:
            tocar(tocarmenu)
            alpha = 255
            acende = True
        else:
            alpha = 255
            acende = True
            tocar(tocarjogo)
        menu_anterior = config.menu


#TROCA DE MODO MENU PARA NAO MODO MENU
    if progress.sala == 19 or progress.sala == 20:
        config.menu = True
    else:
        config.menu = False

#ACABOU FADE OUT
    if progress.state["acabou"]:
         alpha += 5
         if alpha >= 255:
              rodando = False

#TROCA DE SALAS
    if destino != progress.sala:
        apaga = True
        if destino != 20 and destino != 19 and destino != 21:
            progress.ultima_sala = destino
            
    if apaga == True:
        alpha += 15
        if alpha == 15:
            if som != "":
                 tocarsom.play()
        if alpha >= 255:
            progress.sala = destino
            apaga = False
            acende = True
    if acende == True:
        alpha -= 15
        if alpha <= 0:
            acende = False

    progress.mochiladef(progress.inventario)


## INICIO FOR DE EVENTOS
    for evento in pygame.event.get():


        if evento.type == pygame.QUIT:
            print("Fechando...")
            progress.state["acabou"] = True

        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
            destino = 19

        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1: 
            if not apaga and not acende:
                touch = controller.touch(config.menu,evento,progress)
                #print(evento.pos)

                #click som
                if touch[2] == '':
                    som = "./assets/sounds/click.mp3"
                #puxa sala nova
                destino = touch[0]
                #puxa o texto
                texto = touch[1]
                #puxa o som
                if touch[2] != '':
                    som = touch[2]

## FIM DO FOR DE EVENTOS

    if mochila_antiga != progress.mochila:
        mochila_antiga = progress.mochila.copy()
        for i in range(len(caminhoicone)):
            caminhoicone[i] = "./assets/icons/icon_vazio.png"
        for i, item in enumerate(progress.mochila):
            if i < len(caminhoicone):
                match item:
                    case "fuzivel":
                        caminhoicone[i] = "./assets/icons/icon_fuzivel.png"
                    case "chave":
                        caminhoicone[i] = "./assets/icons/icon_chave.png"
                    case "cartao":
                        caminhoicone[i] = "./assets/icons/icon_cartao.png"
                    case _:
                        caminhoicone[i] = "./assets/icons/icon_vazio.png"
        
        inv1 = carregaricon(caminhoicone[0],tamanho_slot)
        inv2 = carregaricon(caminhoicone[1],tamanho_slot)
        inv3 = carregaricon(caminhoicone[2],tamanho_slot)
        inv4 = carregaricon(caminhoicone[3],tamanho_slot)
        if progress.mochila == []:
            inv1 = carregaricon("./assets/icons/icon_vazio.png",tamanho_slot)
            inv2 = carregaricon("./assets/icons/icon_vazio.png",tamanho_slot)
            inv3 = carregaricon("./assets/icons/icon_vazio.png",tamanho_slot)
            inv4 = carregaricon("./assets/icons/icon_vazio.png",tamanho_slot)


    #print(som)

    #RENDERIZAÇÃO

    if config.menu:
        fundo = fundos[progress.sala]
        tela.blit(fundo, (0,0))
    else:
        fundo = fundos[progress.sala]
        tela.blit(fundo, ((largura1-largura2) /2,(altura1 - altura2) / 2 - 50))
    

    #if not menu:
    #  controller.colisoes(progress.sala, tela)
    if config.menu == False:
        tela.blit(inv1,(config.escalar2(673, 32,config.resulucao,config.res)))
        tela.blit(inv2,(config.escalar2(733, 32,config.resulucao,config.res)))
        tela.blit(inv3,(config.escalar2(673, 92,config.resulucao,config.res)))
        tela.blit(inv4,(config.escalar2(733, 92,config.resulucao,config.res)))

    if config.menu == False and texto != "":
        tela.blit(caixa, (config.escalar2(0, 380,config.resulucao,config.res)))
        tela.blit(fonte.render(texto,True, (255, 255, 255)), config.escalar2(140,380,config.resulucao,config.res))
    elif config.menu == True and texto == "Jogo carregado com sucesso!" or texto == "Jogo salvo com sucesso!" or texto == "Sem saves encontrados.":
        tela.blit(caixa, (config.escalar2(250, 380,config.resulucao,config.res)))
        tela.blit(fonte.render(texto,True, (255, 255, 255)), config.escalar2(460, 360,config.resulucao,config.res))

    if som != "":
        tocarsom = pygame.mixer.Sound(som)
        tocarsom.set_volume(config.vol)
    if som == "./assets/sounds/click.mp3":
        tocarsom.play()
        som = ""
    preta.set_alpha(alpha)
    tela.blit(preta,(0,0))
    pygame.display.flip()
    relogio.tick(config.fps)

pygame.quit()
