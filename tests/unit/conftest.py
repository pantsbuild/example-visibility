import pytest
import platform


@pytest.fixture()
def hardware():
    return platform.architecture()
