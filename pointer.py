import re

def calcular_rect(texto):
    numeros = list(map(int, re.findall(r"-?\d+", texto)))

    if len(numeros) != 4:
        return "Erro: digite dois pontos, como (612, 203) (350, 410)"

    x1, y1, x2, y2 = numeros

    x = min(x1, x2)
    y = min(y1, y2)
    largura = abs(x2 - x1)
    altura = abs(y2 - y1)

    return f"pygame.Rect(config.escalar_cheio({x}, {y}, {largura}, {altura},config.resulucao,config.res).collidepoint(evento.pos) and evento.type == pygame.MOUSEBUTTONDOWN:"


while True:
    texto = input("Cole os dois cantos (Enter para sair): ")
    if texto.strip() == "":
        break
    print(calcular_rect(texto))
    print()