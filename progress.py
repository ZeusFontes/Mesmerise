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
    

    

