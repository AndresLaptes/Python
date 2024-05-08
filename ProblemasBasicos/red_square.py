# ****************
# EL CUADRADO ROJO
# ****************


def run(arc_A: float) -> float:
    
    #arc_A = 2*pi*r -> 
    r: float = (4*arc_A)/(2*3.14) 
    area = round(r**2, 10)

    return area


if __name__ == '__main__':
    run(1)