from click.testing import CliRunner

from src.shared.constants import CUDA
from src.apps.algebra import main as algebra_main
from src.apps.geometry import main as geometry_main
from tests.integration.helpers import read_json


def test_add(gpu: str):
    assert gpu == CUDA
    runner = CliRunner()
    result = runner.invoke(algebra_main.add, ["--numbers", "5", "10"])
    assert result.exit_code == 0
    assert "15" in result.output


def test_rectangle_area():
    runner = CliRunner()
    rectangles = read_json("tests/integration/testdata/rectangles.json").get(
        "rectangles", []
    )
    for rectangle in rectangles:
        result = runner.invoke(
            geometry_main.area, ["--sides", rectangle["h"], rectangle["w"]]
        )
        assert result.exit_code == 0
        assert rectangle["area"] in result.output
