import pygame
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

def points(sala,tela):
        if sala == 0:
               print("sala 0")
        elif sala == 1:
                print("sala 1")
                door1 = pygame.Rect(29, 171, 107, 126)
                door2 = pygame.Rect(311, 76, 189, 270)
                door3 = pygame.Rect(661, 82, 66, 404)
                pygame.draw.rect(tela, (255, 255, 0), door1, 2)
                pygame.draw.rect(tela, (255, 255, 0), door2, 2)
                pygame.draw.rect(tela, (255, 255, 0), door3, 2)
        elif sala == 2:
               print("sala 2")
        elif sala == 3:
               print("sala 3")
        elif sala == 4:
               print("sala 4")
