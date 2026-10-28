import pygame
res = 0
vol = 0.2
volmusica = 0.2
fullscreen_ativo = False
resulucao = [(800,500),(1280,800),(1440,900),(1680,1050),(1920,1200)]
imagem = ((resulucao[res][0] / 3) *2,(resulucao[res][1] / 3) *2 )
fps = 60

menu = True


def escalar(esquerda,topo,largura,altura,resulucao,res):
    largura1 = resulucao[res][0]
    altura1 = resulucao[res][1]
    largura2 = (resulucao[res] [0] / 3 ) *2
    altura2 = (resulucao[res] [1] /3) *2
    x = (largura1-largura2) /2
    y = (altura1 - altura2) / 2

    esquerda2 = (esquerda/800) * largura2 + x
    topo2 = (topo/500) * altura2 + y - 50
    largura2 = (largura/800) * largura2
    altura2 = (altura/500) * altura2
    return (esquerda2,topo2,largura2,altura2)

def escalar2(x,y,resolucao,res):
    x2 = (x / 800) * resolucao[res][0]
    y2 = (y / 500) * resolucao[res][1]
    return x2,y2

def escalar_cheio(esquerda, topo, largura, altura, resulucao, res):
    w, h = resulucao[res]
    return ((esquerda/800) * w, (topo/500) * h,
            (largura/800) * w, (altura/500) * h)
