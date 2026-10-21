import pygame
import config

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
        "salas/sala4005.jpg",#manquim sem cabeça e chave          17
        "salas/sala0002.jpg"#painel elevador aberto              18
        )  

def touch(sala,menu,evento,inventario,state):

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and menu == False:
                if sala == 0 or sala == 5: #elevador 
                        #PORTA PRINCIPAL
                        if pygame.Rect(config.escalar(327, 120, 148, 209,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if state["elevador"] == False:
                                        return sala, "Está trancada", ""
                                else:
                                        state["acabou"] = True
                                        return sala, "", ""
                                        
                        #PAINEL ELEVADOR
                        elif pygame.Rect(config.escalar(282, 181, 43, 67,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if state["elevador"] == False:
                                        return 6, "", "./sounds/walk.mp3"
                                else:
                                        return 18, "", "./sounds/walk.mp3"
                        #VOLTAR
                        elif pygame.Rect(config.escalar(1, 412, 797, 82,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 1, "", "./sounds/walk.mp3"
                elif sala == 1:#hall 
                        #PORTA DIREITA
                        if pygame.Rect(config.escalar(29, 171, 107, 126,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 4, "", "./sounds/walk.mp3"
                        #PORTA MEIO
                        elif pygame.Rect(config.escalar(311, 76, 189, 270,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if state["elevador"]:
                                        return 5, "", "./sounds/walk.mp3"
                                else:
                                        return 0, "", "./sounds/walk.mp3"
                        #PORTA ESQUERDA
                        elif pygame.Rect(config.escalar(646, 81, 131, 411,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 2, "", "./sounds/walk.mp3"
                elif sala == 2:#corredor
                        #PORTA FRENTE
                        if pygame.Rect(config.escalar(309, 26, 149, 290,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if state["fuzivel_parede2"]:
                                        return 3, "", "./sounds/gate.mp3"
                                else:
                                        return sala, "Está sem energia", ""
                                
                        #PAINEL
                        elif pygame.Rect(config.escalar(465, 94, 64, 86,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if state["fuzivel_parede2"]:
                                        return 7, "", "./sounds/walk.mp3"
                                else:
                                        return 8, "", "./sounds/walk.mp3"
                        #PORTA VOLTAR
                        elif pygame.Rect(config.escalar(1, 412, 797, 82,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 1, "", "./sounds/walk.mp3"
                elif sala == 3:#relogio sala 
                        #RELOGIO
                        if pygame.Rect(config.escalar(160, 97, 120, 276,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 9, "", "./sounds/walk.mp3"
                        #PAINEL
                        elif pygame.Rect(config.escalar(723, 214, 73, 137,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if state["portilha"] == 0: #trancado
                                        return 12, "", "./sounds/walk.mp3"
                                elif state["portilha"] == 1: #sem cartao dentro
                                        return 11, "", "./sounds/walk.mp3"
                                elif state["portilha"] == 2: #com cartao dentro
                                        return 10, "", "./sounds/walk.mp3"
                        #VOLTAR
                        elif pygame.Rect(config.escalar(1, 412, 797, 82,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 2, "", "./sounds/gate.mp3"
                elif sala == 4:#manequim sala 
                        #PAINEL
                        if pygame.Rect(config.escalar(457, 129, 69, 62,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if state["fuzivel_parede1"]:
                                        return 15, "", "./sounds/walk.mp3"
                                else:
                                        return 16, "", "./sounds/walk.mp3"
                        #MANEQUIM
                        elif pygame.Rect(config.escalar(36, 81, 182, 417,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if state["cabeca_chave"] and inventario["chave"]:
                                        return 17, "", "./sounds/walk.mp3"
                                elif state["cabeca_chave"] and inventario["chave"] == False:
                                        return 14, "", "./sounds/walk.mp3"
                                elif state["cabeca_chave"] == False and inventario["chave"] == False:
                                        return 13, "", "./sounds/walk.mp3"
                        #VOLTAR
                        elif pygame.Rect(config.escalar(1, 412, 797, 82,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 1, "", "./sounds/walk.mp3"
                elif sala == 6 or sala == 18:#painel elevador
                        #VOLTAR
                        if pygame.Rect(config.escalar(1, 412, 797, 82,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if state["elevador"]:
                                        return 5, "", "./sounds/walk.mp3"
                                else:
                                        return 0, "", "./sounds/walk.mp3"
                        #CLICAR PAINEL
                        elif pygame.Rect(config.escalar(318, 63, 162, 325,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if inventario["cartao"] and state["elevador"] == False:
                                        state["elevador"] = True
                                        inventario["cartao"] = False
                                        return 18,"Você abriu a porta.", "./sounds/elevator.mp3"
                                elif inventario["cartao"] and state["elevador"] == True:
                                        return sala,"A porta está aberta", ""
                                elif inventario["cartao"] == False:
                                        return sala,"Aparenta precisar de um cartão de acesso...", ""
                                
                                
                elif sala == 7 or sala == 8 :#FUZIVEL corredor
                        #VOLTAR
                        if pygame.Rect(config.escalar(1, 412, 797, 82,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 2, "", "./sounds/walk.mp3"
                        #CLICAR FUZIVEL
                        elif pygame.Rect(config.escalar(256, 37, 370, 341,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if inventario["fuzivel"] == False and state["fuzivel_parede2"] == False:
                                        return sala,"É necessario um fuzivel", ""
                                elif inventario["fuzivel"] and state["fuzivel_parede2"] == False:
                                        inventario["fuzivel"] = False
                                        state["fuzivel_parede2"] = True
                                        return 7, "", "./sounds/metal.mp3"
                                elif state["fuzivel_parede2"]:
                                        return sala, "Você já pôs o fuzivel.", ""

                elif sala == 9:#close relogio 
                        #VOLTAR
                        if pygame.Rect(config.escalar(1, 412, 797, 82,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 3, "", "./sounds/walk.mp3"
                        #CLICAR RELOGIO
                        elif pygame.Rect(config.escalar(116, 44, 600, 450,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                inventario["horas"] = True;
                                return sala, "São 7:45", ""
                elif sala == 10 or sala == 11 or sala == 12:#portilha relogio
                        #VOLTAR
                        if pygame.Rect(config.escalar(1, 412, 797, 82,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 3, "", "./sounds/walk.mp3"
                        #CLICAR PORTINHOLA
                        elif pygame.Rect(config.escalar(253, 82, 318, 305,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if inventario["chave"] == False and state["portilha"] == 0:
                                        return sala, "Está trancado, precisa de chave...", ""
                                elif inventario["chave"] and state["portilha"] == 0:
                                        state["portilha"] = 2
                                        inventario["chave"] = False
                                        return 10, "", "./sounds/metal.mp3"
                                elif state["portilha"] == 2:
                                        inventario["cartao"] = True
                                        state["portilha"] = 1
                                        return 11, "", "./sounds/item.mp3"
                                elif state["portilha"] == 2:
                                        return sala, "Você já pegou o cartão", ""

                elif sala == 13 or sala == 14 or sala == 17:#close manequim
                        #VOLTAR
                        if pygame.Rect(config.escalar(1, 412, 797, 82,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 4, "", "./sounds/walk.mp3"
                        #CLICAR MANEQUIM
                        elif pygame.Rect(config.escalar(169, 3, 525, 493,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if inventario["horas"] == False and state["cabeca_chave"] == False:
                                        return sala, "??: Que horas são meu caro cavalheiro?", ""
                                elif inventario["horas"] == True and state["cabeca_chave"] == False:
                                        state["cabeca_chave"] = True
                                        inventario["horas"] = False
                                        return 14, "", "./sounds/break.mp3"
                                elif state["cabeca_chave"] == True:
                                        inventario["chave"] = True
                                        return 17, "", "./sounds/item.mp3"

                        
                elif sala == 15 or sala == 16:#portilha manequim fuzivel
                        #VOLTAR
                        if pygame.Rect(config.escalar(1, 412, 797, 82,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 4, "", "./sounds/walk.mp3"
                        #CLICAR FUZIVEL
                        elif pygame.Rect(config.escalar(252, 71, 326, 356,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if state["fuzivel_parede1"]:
                                        inventario["fuzivel"] = True; 
                                        state["fuzivel_parede1"] = False
                                        return 16, "", "./sounds/metal.mp3"
                                else:
                                        return sala, "Você ja pegou o fuzivel.", ""
        
        return sala, "", "", ""



def obter_retangulos(sala):
  retangulos = []

  if sala == 0 or sala == 5:  # elevador
    retangulos = [
        pygame.Rect(config.escalar(327, 120, 148, 209, config.resulucao, config.res)),
        pygame.Rect(config.escalar(282, 181, 43, 67, config.resulucao, config.res)),
        pygame.Rect(config.escalar(1, 412, 797, 82, config.resulucao, config.res)),
    ]
  elif sala == 1:  # hall
    retangulos = [
        pygame.Rect(config.escalar(29, 171, 107, 126, config.resulucao, config.res)),
        pygame.Rect(config.escalar(311, 76, 189, 270, config.resulucao, config.res)),
        pygame.Rect(config.escalar(646, 81, 131, 411, config.resulucao, config.res)),
    ]
  elif sala == 2:  # corredor
    retangulos = [
        pygame.Rect(config.escalar(340, 25, 107, 193, config.resulucao, config.res)),
        pygame.Rect(config.escalar(465, 94, 64, 86, config.resulucao, config.res)),
        pygame.Rect(config.escalar(1, 412, 797, 82, config.resulucao, config.res)),
    ]
  elif sala == 3:  # relogio sala
    retangulos = [
        pygame.Rect(config.escalar(160, 97, 120, 276, config.resulucao, config.res)),
        pygame.Rect(config.escalar(723, 214, 73, 137, config.resulucao, config.res)),
        pygame.Rect(config.escalar(1, 412, 797, 82, config.resulucao, config.res)),
    ]
  elif sala == 4:  # manequim sala
    retangulos = [
        pygame.Rect(config.escalar(457, 129, 69, 62, config.resulucao, config.res)),
        pygame.Rect(config.escalar(36, 81, 182, 417, config.resulucao, config.res)),
        pygame.Rect(config.escalar(1, 412, 797, 82, config.resulucao, config.res)),
    ]
  elif sala == 6 or sala == 18:  # painel elevador
    retangulos = [
        pygame.Rect(config.escalar(1, 412, 797, 82, config.resulucao, config.res)),
        pygame.Rect(config.escalar(318, 63, 162, 325, config.resulucao, config.res)),
    ]
  elif sala == 7 or sala == 8:  # fuzivel corredor
    retangulos = [
        pygame.Rect(config.escalar(1, 412, 797, 82, config.resulucao, config.res)),
        pygame.Rect(config.escalar(256, 37, 370, 341, config.resulucao, config.res)),
    ]
  elif sala == 9:  # close relogio
    retangulos = [
        pygame.Rect(config.escalar(1, 412, 797, 82, config.resulucao, config.res)),
        pygame.Rect(config.escalar(116, 44, 600, 450, config.resulucao, config.res)),
    ]
  elif sala == 10 or sala == 11 or sala == 12:  # portilha relogio
    retangulos = [
        pygame.Rect(config.escalar(1, 412, 797, 82, config.resulucao, config.res)),
        pygame.Rect(config.escalar(253, 82, 318, 305, config.resulucao, config.res)),
    ]
  elif sala == 13 or sala == 14 or sala == 17:  # close manequim
    retangulos = [
        pygame.Rect(config.escalar(1, 412, 797, 82, config.resulucao, config.res)),
        pygame.Rect(config.escalar(169, 3, 525, 493, config.resulucao, config.res)),
    ]
  elif sala == 15 or sala == 16:  # portilha manequim fuzivel
    retangulos = [
        pygame.Rect(config.escalar(1, 412, 797, 82, config.resulucao, config.res)),
        pygame.Rect(config.escalar(252, 71, 326, 356, config.resulucao, config.res)),
    ]

  return retangulos


