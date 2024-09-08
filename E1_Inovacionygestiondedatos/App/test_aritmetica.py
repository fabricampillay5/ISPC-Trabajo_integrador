# Archivo de pruebas para el módulo aritmética

from aritmetica import sumar, restar, dividir, multiplicar, sumar_n, promedio_n

def test_sumar():
    assert sumar(1.5, 2.5) == 4.0
    assert sumar(-1, 1) == 0.0
    assert sumar(0, 0) == 0.0


def test_restar():
    assert restar(5.5, 2.5) == 3.0
    assert restar(0, 0) == 0.0
    assert restar(1, -1) == 2.0


def test_dividir():
    assert dividir(10, 2) == 5.0
    assert dividir(0, 1) == 0.0
    assert dividir(5, 0) is None


def test_multiplicar():
    assert multiplicar(3, 2) == 6.0
    assert multiplicar(0, 5) == 0.0
    assert multiplicar(-1, -1) == 1.0


def test_sumar_n():
    assert sumar_n(1, 2, 3) == 6.0
    assert sumar_n(0) == 0.0
    assert sumar_n() == 0.0


def test_promedio_n():
    assert promedio_n(1, 2, 3) == 2.0
    assert promedio_n(0) == 0.0
    assert promedio_n() == 0.0


if __name__ == "__main__":
    test_sumar()
    test_restar()
    test_dividir()
    test_multiplicar()
    test_sumar_n()
    test_promedio_n()
    print("Todas las pruebas pasaron correctamente.")




