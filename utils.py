"""kalkulator"""


def add(a: int, b: int) -> int:
    """dodawanie"""
    return a + b


def subtract(a: int, b: int) -> int:
    """odejmowanie"""
    return a - b


def multiply(a: int, b: int) -> int:
    """mnozenie"""
    return a * b


def divide(a: int, b: int) -> float:
    """dzielenie"""
    return a / b


def to_binary(n: int) -> str:
    """konwertowanie liczby naturalnej do binarnej"""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("Argument musi byc liczba naturalna")
    if n < 0 or n > 100:
        raise ValueError("Argument ma być w zakresie od [0 do 100]")
    return bin(n)
