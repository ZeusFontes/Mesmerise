import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pygame
import telas
import config
res = 0

pygame.init()

icone = pygame.image.load("icone.png")
pygame.display.set_icon(icone)
pygame.display.set_caption("mesmerize")

tela = pygame.display.set_mode(config.resulucao[res])

sala = 0

rodando = True
menu = True
            

    
while rodando:
    if menu:
        fundo = pygame.image.load("salas/menu.png").convert()
        fundo = pygame.transform.scale(fundo, config.resulucao[res])
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN:
                menu = False
    else:
        fundo = pygame.image.load(telas.salas[sala]).convert()
        fundo = pygame.transform.scale(fundo, config.resulucao[res])

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            print("Fechando...")
            pygame.quit()
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
            menu = True
        else:
            sala = telas.touch(sala,menu,evento)
        

    tela.blit(fundo, (0,0))
    pygame.display.flip()
    
pygame.quit()
