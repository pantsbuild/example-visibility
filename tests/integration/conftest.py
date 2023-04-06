import pytest

from src.shared.constants import CUDA
from tests.unit.conftest import hardware


@pytest.fixture()
def gpu():
    return CUDA
