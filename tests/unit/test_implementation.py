from src.apps.algebra.implementation import calculate_sum
from src.apps.geometry.implementation import calculate_rectangle_area

from tests.integration.test_apps import test_add


def test_calculate_sum(hardware: tuple[str, str], runtime: str) -> None:
    print(hardware, runtime)
    assert calculate_sum(5, 10) == 15


def test_calculate_rectangle_area(hardware: tuple[str, str]) -> None:
    print(hardware)
    assert calculate_rectangle_area(4, 3) == 12
