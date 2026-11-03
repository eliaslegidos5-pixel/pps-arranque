"""Suite de PPS-E2. Todo en verde... ¿significa que el código está bien?"""
import pytest
from descuentos import aplicar_descuento, es_precio_valido


# --- ¿Qué comprueba realmente este test?
def test_ejecuta_sin_reventar():
    aplicar_descuento(100, 10)
    assert True


def test_descuento_correcto():
    assert aplicar_descuento(100, 10) == 90.0
    assert aplicar_descuento(50, 0) == 50.0
    assert aplicar_descuento(80, 100) == 0.0


def test_precio_negativo_se_rechaza():
    with pytest.raises(ValueError):
        aplicar_descuento(-10, 10)


# --- TU TEST DE REGRESIÓN (incidencia #17) va aquí debajo.


def test_regresion_incidencia_17():
    import pytest
    from descuentos import aplicar_descuento
    with pytest.raises(ValueError):
        aplicar_descuento(100, 150)
    with pytest.raises(ValueError):
        aplicar_descuento(100, -5)


def test_regresion_fuzzing_nan_inf():
    for precio, pct in [(float("nan"), 10), (100, float("nan")),
                        (float("inf"), 10), (100, float("inf"))]:
        with pytest.raises(ValueError):
            aplicar_descuento(precio, pct)
