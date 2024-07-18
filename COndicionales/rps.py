# **********************
# PIEDRA, PAPEL O TIJERA
# **********************


def run(choice1: str, choice2: str) -> int:
    
    jugador1 = choice1.lower()
    jugador2 = choice2.lower()
    ganaJ1: bool = (jugador1 == 'piedra' and jugador2 == 'tijera') or (jugador1 == 'tijera' and jugador2 == 'papel') or (jugador1 == 'papel' and jugador2 == 'piedra')
    if ganaJ1:
        winner = 1
    elif jugador1 == jugador2:
        winner = 0
    else: 
        winner = 2

    return winner


if __name__ == '__main__':
    run('piedra', 'PAPEL')