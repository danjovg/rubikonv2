def calcular_volumen(ancho, largo, altura_promedio):
    try:
        return round(ancho * largo * altura_promedio, 2)
    except:
        return 0

def calcular_quimicos(volumen_m3):
    litros = volumen_m3 * 1000
    shock_alguicida = round((4 / 50000) * litros, 2)
    mantenimiento_alguicida = round((0.25 / 50000) * litros, 2)
    tricloro_dosis = round((28 / 3785) * (litros / 1000), 2)
    return {
        "shock_alguicida_L": shock_alguicida,
        "mantenimiento_alguicida_L": mantenimiento_alguicida,
        "tricloro_g": tricloro_dosis
    }