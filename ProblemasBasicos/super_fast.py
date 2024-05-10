# **********************
# ANIMALES SUPER RÁPIDOS
# **********************

#km->cm de 10³ -> 10⁻2 ==> 10⁻5
#h->s 1h -> 3600s
def run(speed_km_h: float) -> float:
    # TU CÓDIGO AQUÍ
    speed_cm_s = round((speed_km_h*((10**5)/3600)), 0)

    return speed_cm_s


if __name__ == '__main__':
    run(1.08)