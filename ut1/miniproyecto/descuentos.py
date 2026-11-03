"""PPS UT1 · Mini-proyecto para la práctica de pruebas y cobertura (PPS-E2).

INCIDENCIA #17 (reportada por soporte): un cliente aplicó un cupón del 150 %
y la tienda le devolvió un precio NEGATIVO (le "regalamos" dinero).
Tu trabajo: escribir primero el TEST DE REGRESIÓN que reproduce el fallo,
verlo en rojo, corregir el código y verlo en verde.
"""


import math


def aplicar_descuento(precio: float, pct: float) -> float:
    """Aplica un descuento porcentual a un precio.

    Reglas:
      - precio >= 0
      - 0 <= pct <= 100
    Un porcentaje fuera de rango debe RECHAZARSE (ValueError), no calcularse.
    """
    if not math.isfinite(precio) or not math.isfinite(pct):
        raise ValueError("valor no finito")
    if precio < 0:
        raise ValueError("precio negativo")
    if pct < 0 or pct > 100:
        raise ValueError("porcentaje fuera de rango")
    return round(precio * (1 - pct / 100), 2)


def es_precio_valido(precio: float) -> bool:
    return precio >= 0
