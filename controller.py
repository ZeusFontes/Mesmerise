import pygame


salas = ("salas/sala0.jpg",#elevador                             0
        "salas/sala1.jpg",#hall                                  1
        "salas/sala2.jpg",#corredor                              2
        "salas/sala3.jpg",#relogio sala                          3
        "salas/sala4.jpg",#manequim sala                         4
        "salas/sala01.jpg",#elevador aberto                      5
        "salas/sala0001.jpg",#painel elevador                    6
        "salas/sala2001.jpg",#painel corredor fuzivel            7
        "salas/sala2002.jpg",#painel corredor                    8
        "salas/sala3001.jpg",#close relogio                      9
        "salas/sala3002.jpg",#portilha relogio cartao            10
        "salas/sala3003.jpg",#portilha relogio aberto            11
        "salas/sala3004.jpg",#portilha relogio fechado           12
        "salas/sala4001.jpg",# close manequim                    13
        "salas/sala4002.jpg",#close manequim chave               14
        "salas/sala4003.jpg",#portilha manequim fuzivel          15
        "salas/sala4004.jpg",#portilha manequim                  16
        "salas/sala4005.jpg"#manquim sem cabeça e chave          17
        )  

def touch(sala,menu,evento,inventario,state):
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and menu == False:
                if sala == 0: #elevador 
                        #PORTA PRINCIPAL
                        if pygame.Rect(327, 120, 148, 209).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return sala, "Está trancada"
                        #PAINEL ELEVADOR
                        elif pygame.Rect(282, 181, 43, 67).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 6, ""
                        #VOLTAR
                        elif pygame.Rect(1, 412, 797, 82).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 1, ""
                elif sala == 1:#hall 
                        #PORTA DIREITA
                        if pygame.Rect(29, 171, 107, 126).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 4, ""
                        #PORTA MEIO
                        elif pygame.Rect(311, 76, 189, 270).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if state["elevador"]:
                                        return 5, ""
                                else:
                                        return 0, ""
                        #PORTA ESQUERDA
                        elif pygame.Rect(646, 81, 131, 411).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 2, ""
                elif sala == 2:#corredor
                        #PORTA FRENTE
                        if pygame.Rect(340, 25, 107, 193).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if state["fuzivel_parede2"]:
                                        return 3, ""
                                else:
                                        return sala, "Está sem energia"
                                
                        #PAINEL
                        elif pygame.Rect(465, 94, 64, 86).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if state["fuzivel_parede2"]:
                                        return 7, ""
                                else:
                                        return 8, ""
                        #MANEQUIM
                        #PORTA VOLTAR
                        elif pygame.Rect(1, 412, 797, 82).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 1, ""
                elif sala == 3:#relogio sala 
                        #RELOGIO
                        if pygame.Rect(160, 97, 120, 276).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 9, ""
                        #PAINEL
                        elif pygame.Rect(723, 214, 73, 137).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if state["portilha"] == 0: #trancado
                                        return 12, ""
                                elif state["portilha"] == 1: #sem cartao
                                        return 11, ""
                                elif state["portilha"] == 2: #com cartao
                                        return 10, ""
                        #VOLTAR
                        elif pygame.Rect(1, 412, 797, 82).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 2, ""
                elif sala == 4:#manequim sala 
                        #PAINEL
                        if pygame.Rect(457, 129, 69, 62).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if state["fuzivel_parede1"]:
                                        return 15, ""
                                else:
                                        return 16, ""
                        #MANEQUIM
                        elif pygame.Rect(36, 81, 182, 417).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if state["cabeca_chave"] and inventario["chave"]:
                                        return 17, ""
                                elif state["cabeca_chave"] and inventario["chave"] == False:
                                        return 14, ""
                                elif state["cabeca_chave"] == False and inventario["chave"] == False:
                                        return 13, ""
                        #VOLTAR
                        elif pygame.Rect(1, 412, 797, 82).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 1, ""
                elif sala == 5:#elevador aberto
                        print("teste")
                        #VOLTAR
                        if pygame.Rect(1, 412, 797, 82).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 1, ""
                        #PORTA PRINCIPAL
                        elif pygame.Rect(327, 120, 148, 209).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return sala, "Está trancada"
                        #PAINEL ELEVADOR
                        elif pygame.Rect(282, 181, 43, 67).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 6, ""
                elif sala == 6:#painel elevador
                        #VOLTAR
                        if pygame.Rect(1, 412, 797, 82).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if state["elevador"]:
                                        return 5, ""
                                else:
                                        return 0, ""
                        #CLICAR PAINEL
                        elif pygame.Rect(318, 63, 162, 325).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                print("oi")
                elif sala == 7 or sala == 8 :#FUZIVEL corredor
                        #VOLTAR
                        if pygame.Rect(1, 412, 797, 82).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 2, ""
                        #CLICAR FUZIVEL
                        elif pygame.Rect(256, 37, 370, 341).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if inventario["fuzivel"] == False:
                                        return sala,"É necessario um fuzivel"
                                elif inventario["fuzivel"] and state["fuzivel_parede2"] == False:
                                        state["fuzivel_parede2"] = True
                                        return 7, ""
                                elif state["fuzivel_parede2"]:
                                        return sala, "Você já pôs o fuzivel."

                elif sala == 9:#close relogio 
                        #VOLTAR
                        if pygame.Rect(1, 412, 797, 82).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 3, ""
                        #CLICAR RELOGIO
                        elif pygame.Rect(116, 44, 600, 450).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return sala, "São 7:45"
                elif sala == 10 or sala == 11 or sala == 12:#portilha relogio
                        #VOLTAR
                        if pygame.Rect(1, 412, 797, 82).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 3, ""
                        #CLICAR PORTINHOLA
                        elif pygame.Rect(253, 82, 318, 305).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                print("oi")
                elif sala == 13 or sala == 14 or sala == 17:#close manequim
                        #VOLTAR
                        if pygame.Rect(1, 412, 797, 82).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 4, ""
                        #CLICAR MANEQUIM
                        elif pygame.Rect(169, 3, 525, 493).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                print("oi")
                elif sala == 15 or sala == 16:#portilha manequim fuzivel
                        #VOLTAR
                        if pygame.Rect(1, 412, 797, 82).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 4, ""
                        #CLICAR FUZIVEL
                        elif pygame.Rect(252, 71, 326, 356).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if state["fuzivel_parede1"]:
                                        inventario["fuzivel"] = True; 
                                        state["fuzivel_parede1"] = False
                                        return 16, ""
                                else:
                                        return sala, "Você ja pegou o fuzivel."
        
        return sala, ""