import pygame


salas = ("salas/sala0.jpg",
        "salas/sala1.jpg",
        "salas/sala2.jpg",
        "salas/sala3.jpg",
        "salas/sala4.jpg")

def interacao(sala,move):
        
        match sala:
               case 0:
                   if move == "porta":
                           print("Está trancada.")
                           return sala
                   if move == "voltar":
                           return 1
               case 1:
                   if move == "meio":
                           return 0
                   if move == "esquerda":
                           return 4
                   if move == "direita":
                           return 2
               case 2:
                   if move == "porta":
                           return 3
                   if move == "painel":
                           print("Painel quebrado.")
                           return sala
                   if move == "voltar":
                           return 1
               case 3:
                   if move == "relogio":
                           print("Relógio quebrado")
                           return sala
                   if move == "painel":
                           print("Painel de energia")
                           return sala
                   if move == "voltar":
                           return 2
               case 4:
                   if move == "painel":
                           print("Painel quebrado.")
                           return sala
                   if move == "homem":
                           print("Olá!")
                           return sala
                   if move == "voltar":
                           return 1

        


def touch(sala,menu,evento):
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and menu == False:
                if sala == 0:
                        if pygame.Rect(307, 116, 178, 214).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                sala = interacao(sala, "porta")
                        elif pygame.Rect(1, 412, 797, 82).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                sala = interacao(sala, "voltar")
                elif sala == 1:
                        if pygame.Rect(29, 171, 107, 126).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                sala = interacao(sala, "esquerda")
                        elif pygame.Rect(311, 76, 189, 270).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                sala = interacao(sala, "meio")
                        elif pygame.Rect(646, 81, 131, 411).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                sala = interacao(sala, "direita")
                elif sala == 2:
                        if pygame.Rect(340, 25, 107, 193).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                sala = interacao(sala, "porta")
                        elif pygame.Rect(465, 94, 64, 86).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                sala = interacao(sala, "painel")
                        elif pygame.Rect(1, 412, 797, 82).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                sala = interacao(sala, "voltar")
                elif sala == 3:
                        if pygame.Rect(160, 97, 120, 276).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                sala = interacao(sala, "relogio")
                        elif pygame.Rect(723, 214, 73, 137).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                sala = interacao(sala, "painel")
                        elif pygame.Rect(1, 412, 797, 82).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                sala = interacao(sala, "voltar")
                elif sala == 4:
                        if pygame.Rect(457, 129, 69, 62).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                sala = interacao(sala, "painel")
                        elif pygame.Rect(36, 81, 182, 417).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                sala = interacao(sala, "homem")
                        elif pygame.Rect(1, 412, 797, 82).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                sala = interacao(sala, "voltar")
        
        return sala