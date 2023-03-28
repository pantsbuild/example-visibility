import pytest

from src.shared.constants import CUDA


@pytest.fixture()
def gpu():
    return CUDA
