import click

from src.apps.utils.cliutils import HELP_OPTS
from src.apps.algebra.implementation import calculate_sum
from src.shared.casts import to_int


@click.group()
@click.pass_context
def cli(ctx: click.Context):
    """Main entrance point."""
    return


@cli.command(context_settings=HELP_OPTS)
@click.option(
    "--numbers",
    "numbers",
    help="Two numbers to sum",
    nargs=2,
    required=True,
)
def add(numbers):
    """Add two numbers together."""
    result = calculate_sum(to_int(numbers[0]), to_int(numbers[1]))
    click.secho(str(result), fg="green")


if __name__ == "__main__":
    cli()
