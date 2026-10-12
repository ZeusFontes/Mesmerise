import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pygame
import telas
import config

pygame.init()

icone = pygame.image.load("icone.png")
pygame.display.set_icon(icone)
pygame.display.set_caption("mesmerize")
fonte = pygame.font.SysFont(None,28)


sala = 0
destino = 0
res = 0
fps = 0
alpha = 0

texto = "Teste de texto isso vai aparecer na tela"

rodando = True
menu = True
apaga = False
acende = False


def carregar(caminho):
    img = pygame.image.load(caminho).convert()
    return pygame.transform.scale(img, config.resulucao[res])

tela = pygame.display.set_mode(config.resulucao[res])
relogio = pygame.time.Clock()

fundo_menu = carregar("salas/menu.png")
fundos = [carregar(c) for c in telas.salas]

preta = pygame.Surface((1920,1080))
preta.fill((0,0,0))

caixa = pygame.Surface((720, 80))
caixa.fill((0, 0, 0))
caixa.set_alpha(177)

# LOOP DO PROGRAMA 
    
while rodando: 
    if destino != sala:
            apaga = True

    if apaga == True:
        
        alpha += 15
        if alpha >= 255:
            sala = destino
            apaga = False
            acende = True
    if acende == True:
        alpha -= 15
        if alpha <= 0:
            acende = False
        


    for evento in pygame.event.get():
        if menu:
            if evento.type == pygame.KEYDOWN:
                menu = False
             
        if evento.type == pygame.QUIT:
            print("Fechando...")
            rodando = False
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
            menu = True
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            destino = telas.touch(sala,menu,evento)

    if menu:
        fundo = fundo_menu
    else:
        fundo = fundos[sala]

    tela.blit(fundo, (0,0))
    if menu == False:
            tela.blit(caixa, (40, 400))
            tela.blit(fonte.render(texto,False, (255, 255, 255)), (55,430))
            preta.set_alpha(alpha)
            tela.blit(preta,(0,0))
    
    pygame.display.flip()
    relogio.tick(config.fps[fps])
    
pygame.quit()
