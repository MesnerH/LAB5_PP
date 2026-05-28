import pytest
import utils


@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (2, 3, 5), (3, 4, 7), (4, 5, 9)])
def test_add(a, b, expected):
    result = utils.add(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected", [(1, 2, -1), (2, 3, -1), (3, 4, -1), (4, 5, -1)]
)
def test_subtract(a, b, expected):
    result = utils.subtract(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected", [(1, 2, 2), (2, 3, 6), (3, 4, 12), (4, 5, 20)]
)
def test_multiply(a, b, expected):
    result = utils.multiply(a, b)
    assert result == expected


@pytest.mark.parametrize("a, b, expected", [(1, 2, 0.5), (3, 4, 0.75), (4, 5, 0.8)])
def test_divide(a, b, expected):
    result = utils.divide(a, b)
    assert result == expected


def test_to_binary_valid():
    """poprawnosc konwersji liczb"""
    assert utils.to_binary(0) == "0b0"
    assert utils.to_binary(5) == "0b101"
    assert utils.to_binary(100) == "0b1100100"


def test_to_binary_out_of_range():
    """sprawdzanie zakresu od 0 do 100"""
    with pytest.raises(ValueError):
        utils.to_binary(-1)
    with pytest.raises(ValueError):
        utils.to_binary(101)


def test_to_binary_not_integer():
    """czy liczba jest naturalna"""
    with pytest.raises(TypeError):
        utils.to_binary(10.5)
    with pytest.raises(TypeError):
        utils.to_binary("5")
