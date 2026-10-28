import pygame
import config




salas = ("./assets/salas/sala0.jpg",#elevador                             0
        "./assets/salas/sala1.jpg",#hall                                  1
        "./assets/salas/sala2.jpg",#corredor                              2
        "./assets/salas/sala3.jpg",#relogio sala                          3
        "./assets/salas/sala4.jpg",#manequim sala                         4
        "./assets/salas/sala01.jpg",#elevador aberto                      5
        "./assets/salas/sala0001.jpg",#painel elevador                    6
        "./assets/salas/sala2001.jpg",#painel corredor fuzivel            7
        "./assets/salas/sala2002.jpg",#painel corredor                    8
        "./assets/salas/sala3001.jpg",#close relogio                      9
        "./assets/salas/sala3002.jpg",#portilha relogio cartao            10
        "./assets/salas/sala3003.jpg",#portilha relogio aberto            11
        "./assets/salas/sala3004.jpg",#portilha relogio fechado           12
        "./assets/salas/sala4001.jpg",# close manequim                    13
        "./assets/salas/sala4002.jpg",#close manequim chave               14
        "./assets/salas/sala4003.jpg",#portilha manequim fuzivel          15
        "./assets/salas/sala4004.jpg",#portilha manequim                  16
        "./assets/salas/sala4005.jpg",#manquim sem cabeça e chave         17
        "./assets/salas/sala0002.jpg",#painel elevador aberto             18
        "./assets/menu.png",#MENU 1                                 19
        "./assets/menu1.png",#MENU 2                                20
        )  


def touch(menu,evento,progress):

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                #MENUUUUUUUU
                if progress.sala == 19:
                        #JOGAR
                        if pygame.Rect(config.escalar_cheio(168, 267, 59, 24,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return progress.ultima_sala, "", ""
                        #SALVAR
                        elif pygame.Rect(config.escalar_cheio(168, 295, 68, 28,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                progress.salvar()
                                return progress.sala, "Jogo salvo com sucesso!", ""
                        #CARREGAR
                        elif pygame.Rect(config.escalar_cheio(165, 323, 91, 29,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                resposta = progress.carregar_save()
                                if resposta == "Jogo carregado com sucesso!":
                                        return progress.ultima_sala, resposta, ""
                                elif resposta == "Sem saves encontrados.":
                                        return progress.sala, resposta, ""
                                else:
                                        return progress.sala, "", ""
                                        
                        #CONFIG
                        elif pygame.Rect(config.escalar_cheio(165, 352, 147, 35,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 20, "", ""
                        #SAIR
                        elif pygame.Rect(config.escalar_cheio(167, 382, 53, 31,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                progress.state["acabou"] = True
                                return progress.sala, "", ""
                if progress.sala == 20:
                        #VOLTAR
                        if pygame.Rect(config.escalar_cheio(46, 34, 84, 34,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                print("Fechando...")
                                return 19, "", ""
                        #VOLUME MENOS
                        elif pygame.Rect(config.escalar_cheio(218, 93, 36, 31,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if config.vol > 0:
                                        config.vol = config.vol - 0.1
                                        config.vol = round(config.vol,1)
                                        print(config.vol)
                                return progress.sala, "", ""
                        #VOLUME MAIS
                        elif pygame.Rect(config.escalar_cheio(295, 90, 37, 37,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if config.vol < 1:
                                        config.vol = config.vol + 0.1
                                        config.vol = round(config.vol,1)
                                        print(config.vol)
                                return progress.sala, "", ""
                        #VOLUME MUSICA MENOS
                        elif pygame.Rect(config.escalar_cheio(216, 177, 37, 32,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if config.volmusica > 0:
                                        config.volmusica = config.volmusica - 0.1
                                        config.volmusica = round(config.volmusica,1)
                                        pygame.mixer.music.set_volume(config.volmusica)
                                        print(config.volmusica)
                                return progress.sala, "", ""
                        #VOLUME MUSICA MAIS
                        elif pygame.Rect(config.escalar_cheio(296, 179, 37, 31,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if config.volmusica < 1:
                                        config.volmusica = config.volmusica + 0.1
                                        config.volmusica = round(config.volmusica,1)
                                        pygame.mixer.music.set_volume(config.volmusica)
                                        print(config.volmusica)
                                return progress.sala, "", ""
                        #RES MENOS
                        elif pygame.Rect(config.escalar_cheio(369, 92, 49, 36,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if config.res > 0:
                                        config.res -= 1
                                        print(config.res)
                                return progress.sala, "", ""
                        #RES MAIS
                        elif pygame.Rect(config.escalar_cheio(485, 91, 49, 40,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if config.res <= 3:
                                        config.res += 1
                                        print(config.res)
                                return progress.sala, "", ""
                        #TELA CHEIA
                        elif pygame.Rect(config.escalar_cheio(556, 53, 140, 46,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                config.fullscreen_ativo = not config.fullscreen_ativo
                                print(config.fullscreen_ativo)
                                return progress.sala, "", ""            
                if progress.sala == 0 or progress.sala == 5: #elevador 
                        #PORTA PRINCIPAL
                        if pygame.Rect(config.escalar(327, 120, 148, 209,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if progress.state["elevador"] == False:
                                        return progress.sala, "Está trancada", ""
                                else:
                                        progress.state["acabou"] = True
                                        return progress.sala, "", ""
                                        
                        #PAINEL ELEVADOR
                        elif pygame.Rect(config.escalar(282, 181, 43, 67,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if progress.state["elevador"] == False:
                                        return 6, "", "./assets/sounds/walk.mp3"
                                else:
                                        return 18, "", "./assets/sounds/walk.mp3"
                        #VOLTAR
                        elif pygame.Rect(config.escalar(1, 412, 797, 82,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 1, "", "./assets/sounds/walk.mp3"
                elif progress.sala == 1:#hall 
                        #PORTA DIREITA
                        if pygame.Rect(config.escalar(29, 171, 107, 126,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 4, "", "./assets/sounds/walk.mp3"
                        #PORTA MEIO
                        elif pygame.Rect(config.escalar(311, 76, 189, 270,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if progress.state["elevador"]:
                                        return 5, "", "./assets/sounds/walk.mp3"
                                else:
                                        return 0, "", "./assets/sounds/walk.mp3"
                        #PORTA ESQUERDA
                        elif pygame.Rect(config.escalar(646, 81, 131, 411,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 2, "", "./assets/sounds/walk.mp3"
                elif progress.sala == 2:#corredor
                        #PORTA FRENTE
                        if pygame.Rect(config.escalar(309, 26, 149, 290,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if progress.state["fuzivel_parede2"]:
                                        return 3, "", "./assets/sounds/gate.mp3"
                                else:
                                        return progress.sala, "Está sem energia", ""
                                
                        #PAINEL
                        elif pygame.Rect(config.escalar(465, 94, 64, 86,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if progress.state["fuzivel_parede2"]:
                                        return 7, "", "./assets/sounds/walk.mp3"
                                else:
                                        return 8, "", "./assets/sounds/walk.mp3"
                        #PORTA VOLTAR
                        elif pygame.Rect(config.escalar(1, 412, 797, 82,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 1, "", "./assets/sounds/walk.mp3"
                elif progress.sala == 3:#relogio progress.sala 
                        #RELOGIO
                        if pygame.Rect(config.escalar(160, 97, 120, 276,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 9, "", "./assets/sounds/walk.mp3"
                        #PAINEL
                        elif pygame.Rect(config.escalar(723, 214, 73, 137,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if progress.state["portilha"] == 0: #trancado
                                        return 12, "", "./assets/sounds/walk.mp3"
                                elif progress.state["portilha"] == 1: #sem cartao dentro
                                        return 11, "", "./assets/sounds/walk.mp3"
                                elif progress.state["portilha"] == 2: #com cartao dentro
                                        return 10, "", "./assets/sounds/walk.mp3"
                        #VOLTAR
                        elif pygame.Rect(config.escalar(1, 412, 797, 82,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 2, "", "./assets/sounds/gate.mp3"
                elif progress.sala == 4:#manequim progress.sala 
                        #PAINEL
                        if pygame.Rect(config.escalar(457, 129, 69, 62,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if progress.state["fuzivel_parede1"]:
                                        return 15, "", "./assets/sounds/walk.mp3"
                                else:
                                        return 16, "", "./assets/sounds/walk.mp3"
                        #MANEQUIM
                        elif pygame.Rect(config.escalar(36, 81, 182, 417,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if progress.state["cabeca_chave"] and progress.inventario["chave"]:
                                        return 17, "", "./assets/sounds/walk.mp3"
                                elif progress.state["cabeca_chave"] and progress.inventario["chave"] == False:
                                        return 14, "", "./assets/sounds/walk.mp3"
                                elif progress.state["cabeca_chave"] == False and progress.inventario["chave"] == False:
                                        return 13, "", "./assets/sounds/walk.mp3"
                        #VOLTAR
                        elif pygame.Rect(config.escalar(1, 412, 797, 82,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 1, "", "./assets/sounds/walk.mp3"
                elif progress.sala == 6 or progress.sala == 18:#painel elevador
                        #VOLTAR
                        if pygame.Rect(config.escalar(1, 412, 797, 82,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if progress.state["elevador"]:
                                        return 5, "", "./assets/sounds/walk.mp3"
                                else:
                                        return 0, "", "./assets/sounds/walk.mp3"
                        #CLICAR PAINEL
                        elif pygame.Rect(config.escalar(318, 63, 162, 325,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if progress.inventario["cartao"] and progress.state["elevador"] == False:
                                        progress.state["elevador"] = True
                                        progress.inventario["cartao"] = False
                                        return 18,"Você abriu a porta.", "./assets/sounds/elevator.mp3"
                                elif progress.state["elevador"] == True:
                                        return progress.sala,"A porta está aberta", ""
                                elif progress.inventario["cartao"] == False:
                                        return progress.sala,"Aparenta precisar de um cartão de acesso...", ""
                                
                                
                elif progress.sala == 7 or progress.sala == 8 :#FUZIVEL corredor
                        #VOLTAR
                        if pygame.Rect(config.escalar(1, 412, 797, 82,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 2, "", "./assets/sounds/walk.mp3"
                        #CLICAR FUZIVEL
                        elif pygame.Rect(config.escalar(256, 37, 370, 341,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if progress.inventario["fuzivel"] == False and progress.state["fuzivel_parede2"] == False:
                                        return progress.sala,"É necessario um fuzivel", ""
                                elif progress.inventario["fuzivel"] and progress.state["fuzivel_parede2"] == False:
                                        progress.inventario["fuzivel"] = False
                                        progress.state["fuzivel_parede2"] = True
                                        return 7, "", "./assets/sounds/metal.mp3"
                                elif progress.state["fuzivel_parede2"]:
                                        return progress.sala, "Você já pôs o fuzivel.", ""

                elif progress.sala == 9:#close relogio 
                        #VOLTAR
                        if pygame.Rect(config.escalar(1, 412, 797, 82,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 3, "", "./assets/sounds/walk.mp3"
                        #CLICAR RELOGIO
                        elif pygame.Rect(config.escalar(116, 44, 600, 450,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                progress.inventario["horas"] = True;
                                return progress.sala, "São 7:45", ""
                elif progress.sala == 10 or progress.sala == 11 or progress.sala == 12:#portilha relogio
                        #VOLTAR
                        if pygame.Rect(config.escalar(1, 412, 797, 82,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 3, "", "./assets/sounds/walk.mp3"
                        #CLICAR PORTINHOLA
                        elif pygame.Rect(config.escalar(253, 82, 318, 305,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if progress.inventario["chave"] == False and progress.state["portilha"] == 0:
                                        return progress.sala, "Está trancado, precisa de chave...", ""
                                elif progress.inventario["chave"] and progress.state["portilha"] == 0:
                                        progress.state["portilha"] = 2
                                        progress.inventario["chave"] = False
                                        return 10, "", "./assets/sounds/metal.mp3"
                                elif progress.state["portilha"] == 2:
                                        progress.inventario["cartao"] = True
                                        progress.state["portilha"] = 1
                                        return 11, "", "./assets/sounds/item.mp3"
                                elif progress.state["portilha"] == 2:
                                        return progress.sala, "Você já pegou o cartão", ""

                elif progress.sala == 13 or progress.sala == 14 or progress.sala == 17:#close manequim
                        #VOLTAR
                        if pygame.Rect(config.escalar(1, 412, 797, 82,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 4, "", "./assets/sounds/walk.mp3"
                        #CLICAR MANEQUIM
                        elif pygame.Rect(config.escalar(169, 3, 525, 493,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if progress.inventario["horas"] == False and progress.state["cabeca_chave"] == False:
                                        return progress.sala, "??: Que horas são meu caro cavalheiro?", ""
                                elif progress.inventario["horas"] == True and progress.state["cabeca_chave"] == False:
                                        progress.state["cabeca_chave"] = True
                                        progress.inventario["horas"] = False
                                        return 14, "", "./assets/sounds/break.mp3"
                                elif progress.state["cabeca_chave"] == True:
                                        progress.inventario["chave"] = True
                                        return 17, "", "./assets/sounds/item.mp3"

                        
                elif progress.sala == 15 or progress.sala == 16:#portilha manequim fuzivel
                        #VOLTAR
                        if pygame.Rect(config.escalar(1, 412, 797, 82,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                return 4, "", "./assets/sounds/walk.mp3"
                        #CLICAR FUZIVEL
                        elif pygame.Rect(config.escalar(252, 71, 326, 356,config.resulucao,config.res)).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:
                                if progress.state["fuzivel_parede1"]:
                                        progress.inventario["fuzivel"] = True; 
                                        progress.state["fuzivel_parede1"] = False
                                        return 16, "", "./assets/sounds/metal.mp3"
                                else:
                                        return progress.sala, "Você ja pegou o fuzivel.", ""

        return progress.sala, "", "", ""





