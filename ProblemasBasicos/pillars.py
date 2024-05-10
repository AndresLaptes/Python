# **********************
# POSTES EN LA CARRETERA
# **********************


def run(num_pillars: int, gap_pillars: float, pillar_width: float) -> float:
    # TU CÓDIGO AQUÍ
    distancia : float = (num_pillars - 2)*pillar_width + (num_pillars - 1)*gap_pillars*(10**2)
    inter_distance = round(distancia, 0)

    return inter_distance


if __name__ == '__main__':
    run(10, 5, 30)