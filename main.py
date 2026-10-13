import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pygame
import controller
import config
import progress

pygame.init()

icone = pygame.image.load("icone.png")
pygame.display.set_icon(icone)
pygame.display.set_caption("Mesmerize")
fonte = pygame.font.SysFont(None,28)


sala = 0
destino = 0
res = 0
fps = 0
alpha = 255

texto = ""


rodando = True
menu = True
apaga = False
acende = True
touch = (0,'')


def carregar(caminho):
    img = pygame.image.load(caminho).convert()
    return pygame.transform.scale(img, config.resulucao[res])

def tocar(caminho):
     pygame.mixer.music.fadeout(500)
     pygame.mixer.music.load(caminho)
     pygame.mixer.music.set_volume(0.2)
     pygame.mixer.music.play(-1, fade_ms=500) 

som_andar = pygame.mixer.Sound("sounds/walk.mp3")
tocarmenu = "sounds/menu.mp3"
tocarjogo = "sounds/jogo.mp3"

tela = pygame.display.set_mode(config.resulucao[res])
relogio = pygame.time.Clock()

fundo_menu = carregar("salas/menu.jpg")
fundos = [carregar(c) for c in controller.salas]

preta = pygame.Surface((1920,1080))
preta.fill((0,0,0))

caixa = pygame.Surface((720, 80))
caixa.fill((0, 0, 0))
caixa.set_alpha(177)

if menu:
    tocar(tocarmenu)
# LOOP DO PROGRAMA 
    
while rodando: 
    if progress.state["acabou"]:
         alpha += 5
         if alpha >= 255:
              rodando = False

    if destino != sala:
            apaga = True

    if apaga == True:
        alpha += 15
        if alpha == 15:
            som_andar.play()
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
            touch = controller.touch(sala,menu,evento,progress.inventario,progress.state)
           #print(evento.pos)
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_j:
             progress.cartao = True


    destino = touch[0]
    texto = touch[1]

    #RENDERIZAÇÃO
    if menu:
        fundo = fundo_menu
    else:
        fundo = fundos[sala]

    tela.blit(fundo, (0,0))

    if menu == False and texto != "":
            tela.blit(caixa, (40, 400))
            tela.blit(fonte.render(texto,True, (255, 255, 255)), (55,430))
            
    preta.set_alpha(alpha)
    tela.blit(preta,(0,0))
    pygame.display.flip()
    relogio.tick(config.fps)

pygame.quit()
