# *********************
# CONTANDO MILISEGUNDOS
# *********************


def run(hours: int, minutes: int, seconds: int) -> float:
    # TU CÓDIGO AQUÍ
    time_since_midnight = hours*3600*(10**3) + minutes*60*(10**3) + seconds*(10**3)

    return time_since_midnight


if __name__ == '__main__':
    run(0, 1, 1)