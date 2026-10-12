import pygame


salas = ("salas/sala0.jpg",
        "salas/sala1.jpg",
        "salas/sala2.jpg",
        "salas/sala3.jpg",
        "salas/sala4.jpg")  

def touch(sala,menu,evento):
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and menu == False:
                if sala == 0:
                        #PORTA PRINCIPAL
                        if pygame.Rect(307, 116, 178, 214).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return sala, "Está trancada"
                        #VOLTAR
                        elif pygame.Rect(1, 412, 797, 82).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 1, ""
                elif sala == 1:
                        #PORTA DIREITA
                        if pygame.Rect(29, 171, 107, 126).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 4, ""
                        #PORTA MEIO
                        elif pygame.Rect(311, 76, 189, 270).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 0, ""
                        #PORTA ESQUERDA
                        elif pygame.Rect(646, 81, 131, 411).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 2, ""
                elif sala == 2:
                        #PORTA FRENTE
                        if pygame.Rect(340, 25, 107, 193).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 3, ""
                        #PAINEL
                        elif pygame.Rect(465, 94, 64, 86).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return sala, "Painel quebrado."
                        #PORTA VOLTAR
                        elif pygame.Rect(1, 412, 797, 82).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 1, ""
                elif sala == 3:
                        #RELOGIO
                        if pygame.Rect(160, 97, 120, 276).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return sala, "Relógio quebrado"
                        #PAINEL
                        elif pygame.Rect(723, 214, 73, 137).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return sala, "Painel de energia"
                        #VOLTAR
                        elif pygame.Rect(1, 412, 797, 82).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 2, ""
                elif sala == 4:
                        #PAINEL
                        if pygame.Rect(457, 129, 69, 62).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return sala, "Painel quebrado."
                        #MANEQUIM
                        elif pygame.Rect(36, 81, 182, 417).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return sala, "Olá!"
                        #VOLTAR
                        elif pygame.Rect(1, 412, 797, 82).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 1, ""
        
        return sala, ""