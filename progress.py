import json
import os

sala = 19
ultima_sala = 0

inventario = {
    "fuzivel": False,
    "horas": False,
    "chave": False,
    "cartao": False,
}

#ESTADO MUNDO
state = {
    "fuzivel_parede1": True,
    "cabeca_chave": False,
    "fuzivel_parede2": False,
    "elevador": False,
    "portilha": 0,
    "acabou": False
}


def salvar():
    caminho = "saves/save.json"
    dados = {
        "sala": sala,
        "inventario": inventario,
        "state": state,
        "ultima_sala": ultima_sala

    }
    
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4)
    print("Jogo salvo com sucesso!")

def carregar_save():
    global inventario, state, sala, ultima_sala
    if os.path.exists("saves/save.json"):
        with open("saves/save.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            inventario.update(dados['inventario'])
            state.update(dados['state'])
            sala = dados.get("sala",sala)
            ultima_sala = dados.get("ultima_sala",ultima_sala)
        return("Jogo carregado com sucesso!")

    else:
        return("Sem saves encontrados.")



mochila = []

def mochiladef(inventario):  

    if inventario["fuzivel"] and "fuzivel" not in mochila:
        mochila.append("fuzivel")
    if inventario["chave"] and "chave" not in mochila:
        mochila.append("chave")
    if inventario["cartao"] and "cartao" not in mochila:
        mochila.append("cartao")

    if inventario["fuzivel"] == False and "fuzivel"  in mochila:
            mochila.remove("fuzivel")
    if inventario["chave"] == False and "chave"  in mochila:
            mochila.remove("chave")
    if inventario["cartao"] == False and "cartao"  in mochila:
            mochila.remove("cartao")
    

    

