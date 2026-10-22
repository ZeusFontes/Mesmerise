import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pygame
import controller
import config
import progress
os.environ['SDL_VIDEO_CENTERED'] = '1'




pygame.init()

icone = pygame.image.load("icone.png")
pygame.display.set_icon(icone)
pygame.display.set_caption("Mesmerize")
fonte = pygame.font.SysFont(None,28)


sala = 0
destino = 0
fps = 0
alpha = 255
som = ""

texto = ""
mochila_antiga = progress.mochila.copy()

rodando = True
menu = True
apaga = False
acende = True

touch = (0,'','')


def carregar(caminho):
    img = pygame.image.load(caminho).convert()
    if caminho == "salas/menu.jpg":
          return pygame.transform.scale(img, config.resulucao[config.res])
    else:
        return pygame.transform.scale(img, config.imagem)

    
def tocar(caminho):
     pygame.mixer.music.fadeout(500)
     pygame.mixer.music.load(caminho)
     pygame.mixer.music.set_volume(0.2)
     pygame.mixer.music.play(-1, fade_ms=500) 




tocarmenu = "sounds/menu.mp3"
tocarjogo = "sounds/jogo.mp3"

tela = pygame.display.set_mode(config.resulucao[config.res])
relogio = pygame.time.Clock()

fundo_menu = carregar("salas/menu.jpg")
fundos = [carregar(c) for c in controller.salas]

preta = pygame.Surface((1920,1080))
preta.fill((0,0,0))


caixa = pygame.Surface((config.escalar2(900, 80,config.resulucao,config.res)))
caixa.fill((0, 0, 0))
caixa.set_alpha(255)


tamanho_slot = config.escalar2(50, 50, config.resulucao, config.res)
caminhoicone = [
    "./salas/icon_vazio.png",
    "./salas/icon_vazio.png",
    "./salas/icon_vazio.png",
    "./salas/icon_vazio.png"
]

imgicon = ['', '', '', '', '']

def carregaricon(caminhoicone,tamanho_slot):
    imgicon = pygame.image.load(caminhoicone).convert()
    return pygame.transform.scale(imgicon, tamanho_slot)

inicio_icon = pygame.image.load("./salas/icon_vazio.png").convert()
inv1 = pygame.transform.scale(inicio_icon, tamanho_slot)
inv2 = pygame.transform.scale(inicio_icon, tamanho_slot)
inv3 = pygame.transform.scale(inicio_icon, tamanho_slot)
inv4 = pygame.transform.scale(inicio_icon, tamanho_slot)


largura1, altura1 = config.resulucao[config.res]
largura2, altura2 = config.imagem

if menu:
    tocar(tocarmenu)
# LOOP DO PROGRAMA 
while rodando: 


    progress.mochiladef(progress.inventario)

    if not menu and not acende and not apaga:
      mouse_pos = pygame.mouse.get_pos()
      retangulos_atuais = controller.obter_retangulos(sala)

      if any(ret.collidepoint(mouse_pos) for ret in retangulos_atuais):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
      else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    else:
      pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    print(f"mochila = {progress.mochila} | mochila antiga = {mochila_antiga}")



    if progress.state["acabou"]:
         alpha += 5
         if alpha >= 255:
              rodando = False

    if destino != sala:
            apaga = True

    if apaga == True:
        alpha += 15
        if alpha == 15:
            if som != "":
                 tocarsom.play()
            
        if alpha >= 255:
            sala = destino
            apaga = False
            acende = True
    if acende == True:
        alpha -= 15
        if alpha <= 0:
            acende = False



 #FOR DE EVENTOS#
    for evento in pygame.event.get():
        if menu:
            if evento.type == pygame.KEYDOWN:
                tocar(tocarjogo)
                alpha = 255
                acende = True
                menu = False

        if evento.type == pygame.QUIT:
            print("Fechando...")
            progress.state["acabou"] = True
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
            menu = True
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1: 
            if not apaga and not acende:
                touch = controller.touch(sala,menu,evento,progress.inventario,progress.state)

                if touch[2] == '':
                    som = "./sounds/click.mp3"

            #print(evento.pos)
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_j:
             progress.cartao = True

    if mochila_antiga != progress.mochila:
        mochila_antiga = progress.mochila.copy()
        for i in range(len(caminhoicone)):
            caminhoicone[i] = "salas/icon_vazio.png"
        for i, item in enumerate(progress.mochila):
            if i < len(caminhoicone):
                match item:
                    case "fuzivel":
                        caminhoicone[i] = "salas/icon_fuzivel.png"
                    case "chave":
                        caminhoicone[i] = "salas/icon_chave.png"
                    case "cartao":
                        caminhoicone[i] = "salas/icon_cartao.png"
                    case _:
                        caminhoicone[i] = "salas/icon_vazio.png"
        
        inv1 = carregaricon(caminhoicone[0],tamanho_slot)
        inv2 = carregaricon(caminhoicone[1],tamanho_slot)
        inv3 = carregaricon(caminhoicone[2],tamanho_slot)
        inv4 = carregaricon(caminhoicone[3],tamanho_slot)
        if progress.mochila == []:
            inv1 = carregaricon("salas/icon_vazio.png",tamanho_slot)
            inv2 = carregaricon("salas/icon_vazio.png",tamanho_slot)
            inv3 = carregaricon("salas/icon_vazio.png",tamanho_slot)
            inv4 = carregaricon("salas/icon_vazio.png",tamanho_slot)

    #print(touch)
    if touch[2] != '':
        som = touch[2]

    destino = touch[0]
    texto = touch[1]
    #print(som)

    #RENDERIZAÇÃO

#iventario
    

    if menu:
        fundo = fundo_menu
    else:
        fundo = fundos[sala]
    if menu:
        tela.blit(fundo, (0,0))
    else:
        tela.blit(fundo, ((largura1-largura2) /2,(altura1 - altura2) / 2 - 50))
    

    #if not menu:
    #  controller.colisoes(sala, tela)
    if menu == False:
        tela.blit(inv1,(config.escalar2(673, 32,config.resulucao,config.res)))
        tela.blit(inv2,(config.escalar2(733, 32,config.resulucao,config.res)))
        tela.blit(inv3,(config.escalar2(673, 92,config.resulucao,config.res)))
        tela.blit(inv4,(config.escalar2(733, 92,config.resulucao,config.res)))

    if menu == False and texto != "":
            tela.blit(caixa, (config.escalar2(40, 400,config.resulucao,config.res)))
            tela.blit(fonte.render(texto,True, (255, 255, 255)), config.escalar2(140,420,config.resulucao,config.res))
    if som != "":
        tocarsom = pygame.mixer.Sound(som)
        tocarsom.set_volume(0.2)
    if som == "./sounds/click.mp3":
        tocarsom.play()
        som = ""
    preta.set_alpha(alpha)
    tela.blit(preta,(0,0))
    pygame.display.flip()
    relogio.tick(60)

pygame.quit()
