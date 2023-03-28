import pytest
import platform


@pytest.fixture()
def runtime():
    return platform.platform()
