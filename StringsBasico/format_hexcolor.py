# ************************************
# FORMATEANDO A COLORES EN HEXADECIMAL
# ************************************


def run(intcolor: int) -> str:
    # TU CÓDIGO AQUÍ
    hexcolor = f'{intcolor:06x}'
    hexcolor = hexcolor.upper()

    return hexcolor


if __name__ == '__main__':
    run(45782)