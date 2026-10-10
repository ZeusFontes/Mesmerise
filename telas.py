salas = ("salas/sala0.png",
        "salas/sala1.png",
        "salas/sala2.png",
        "salas/sala3.png",
        "salas/sala4.png")

def validaSala(sala,move):
    match sala:
        case 0:
            if move == "up":
                    return 0
            if move == "down":
                    return 1
            if move == "left":
                    return 0
            if move == "right":
                    return 0
        case 1:
            if move == "up":
                    return 0
            if move == "down":
                    return 1
            if move == "left":
                    return 4
            if move == "right":
                    return 2
        case 2:
            if move == "up":
                    return 3
            if move == "down":
                    return 1
            if move == "left":
                    return 2
            if move == "right":
                    return 2
        case 3:
            if move == "up":
                    return 3
            if move == "down":
                    return 3
            if move == "left":
                    return 2
            if move == "right":
                    return 3
        case 4:
            if move == "up":
                    return 4
            if move == "down":
                    return 4
            if move == "left":
                    return 4
            if move == "right":
                    return 1