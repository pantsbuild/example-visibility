import click

from src.shared.casts import to_int
from src.apps.utils.cliutils import HELP_OPTS
from src.apps.geometry.implementation import calculate_rectangle_area


@click.group()
@click.pass_context
def cli(ctx: click.Context):
    """Main entrance point."""
    return


@cli.command(context_settings=HELP_OPTS)
@click.option(
    "--sides",
    "numbers",
    help="Height and width of a rectangle",
    nargs=2,
    required=True,
)
def area(numbers):
    """Calculate rectangle area."""
    result = calculate_rectangle_area(to_int(numbers[0]), to_int(numbers[1]))
    click.secho(str(result), fg="green")


if __name__ == "__main__":
    cli()
