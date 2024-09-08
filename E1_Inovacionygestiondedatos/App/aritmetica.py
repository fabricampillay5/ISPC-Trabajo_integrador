#  Módulo de operaciones básicas

def sumar(a: float, b: float) -> float:
    return round(a + b, 2)


def restar(a: float, b: float) -> float:
    return round(a - b, 2)


def dividir(a: float, b: float) -> float:
    try:
        return round(a / b, 2)
    except ZeroDivisionError:
        print("Error: Division por cero.")
    return None


def multiplicar(a: float, b: float) -> float:
    return round(a * b, 2)


def sumar_n(*args: float) -> float:
    return round(sum(args), 2)


def promedio_n(*args:float) -> float:
    if len(args) == 0:
        return 0
    return round(sum(args) / len(args), 2)

