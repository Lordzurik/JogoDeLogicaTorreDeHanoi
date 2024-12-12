from os import system, name
import time
import keyboard

# Variáveis globais
estacas = {
    1: [3, 2, 1], 
    2: [], 
    3: []
}
posicao_seta = 1  
disco_selecionado = None
movimentos = 0



def exibir_estado():
    system("cls")
    
    if posicao_seta == 1:
        seta = "         |                                                        \n         V                                                        "
    elif posicao_seta == 2:
        seta = "                                  |                                    \n                                  V                                    "
    elif posicao_seta == 3:
        seta = "                                                           |                 \n                                                           V                 "

   
    def criar_estaca(discos, altura_total=3):
        representacoes = {
            1: [
                "     ____|____    ",
                "    [____|____]   "
            ],
            2: [
                "   ______|______  ",
                "  [______|______] "
            ],
            3: [
                "  _______|_______ ",
                " [_______|_______]"
            ]
        }

        estaca_visual = []
        for _ in range(altura_total - len(discos)):
            estaca_visual.extend([
                "         |        ",
                "         |        "
            ])
        for disco in reversed(discos):
            estaca_visual.extend(representacoes[disco])

        return estaca_visual

    estaca1 = criar_estaca(estacas[1])
    estaca2 = criar_estaca(estacas[2])
    estaca3 = criar_estaca(estacas[3])

    print(f"""
{seta}

{''.join(line + "       " + estaca2[i] + "       " + estaca3[i] + "\n" for i, line in enumerate(estaca1))}

Movimentos: {movimentos}
    """)

    if disco_selecionado == 3:
        print(f"Disco Grande selecionado.")
    elif disco_selecionado == 2:
        print(f"Disco Médio selecionado.")
    elif disco_selecionado == 1:
        print(f"Disco Pequeno selecionado.")
    else:
        print("Nenhum disco selecionado.")

def mudar_posicao():
    global posicao_seta
    nova_posicao = posicao_seta
    if keyboard.is_pressed("right"):
        nova_posicao = 1 if posicao_seta == 3 else posicao_seta + 1
        time.sleep(0.2)
    elif keyboard.is_pressed("left"):
        nova_posicao = 3 if posicao_seta == 1 else posicao_seta - 1
        time.sleep(0.2)
    return nova_posicao

def manipular_disco():
    global disco_selecionado, posicao_seta, movimentos
    if keyboard.is_pressed("down"):
        if disco_selecionado is None:  
            if estacas[posicao_seta]: 
                disco_selecionado = estacas[posicao_seta].pop()
        else:  
            if not estacas[posicao_seta] or estacas[posicao_seta][-1] > disco_selecionado:
                estacas[posicao_seta].append(disco_selecionado)
                disco_selecionado = None
        movimentos += 1  
        time.sleep(0.2)
        return True  
    return False 

def verificar_vitoria():
    return len(estacas[2]) == 3 or len(estacas[3]) == 3

def jogo():
    global estacas, posicao_seta, disco_selecionado, movimentos


    estacas = {
        1: [3, 2, 1], 
        2: [], 
        3: []
    }
    posicao_seta = 1
    disco_selecionado = None
    movimentos = 0

    exibir_estado()
    while True:
        if manipular_disco(): 
            exibir_estado()

        nova_posicao = mudar_posicao()
        if nova_posicao != posicao_seta:
            posicao_seta = nova_posicao
            exibir_estado()

        if verificar_vitoria():
            print(f"Parabéns! Você GANHOU em {movimentos} movimentos!")          
            break

jogo()
