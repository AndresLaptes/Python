# *******************
# MÍNIMO DE 3 VALORES
# *******************

def min(value1: int, value2: int) ->  int:
    if value1 != value2:
        if value1 > value2: return value2
        else: return value1
    return value1


def run(value1: int, value2: int, value3: int) -> int:
    # TU CÓDIGO AQUÍ
    min_value = 'output'

    return min_value


if __name__ == '__main__':
    run(7, 4, 9)