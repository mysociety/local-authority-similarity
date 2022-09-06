import rich_click as click
from data_common.management.run_notebook import run_notebook
from pathlib import Path
import rich


def build_emissions():
    rich.print("[green]Building distance matrix for emissions[/green]")
    run_notebook(Path("notebooks", "emissions.ipynb"))


def build_imd():
    rich.print("[green]Building distance matrix for IMD[/green]")
    run_notebook(Path("notebooks", "imd.ipynb"))


def build_physical():
    rich.print("[green]Building distance matrix for physical distance[/green]")
    run_notebook(Path("notebooks", "physical.ipynb"))


def build_ruc():
    rich.print("[green]Building distance matrix for RUC[/green]")
    run_notebook(Path("notebooks", "ruc.ipynb"))


def build_composite():
    rich.print("[green]Building composite distance matrix[/green]")
    run_notebook(Path("notebooks", "composite.ipynb"))


@click.group()
def cli():
    pass


def main():
    cli()


@cli.command()
def build():
    build_emissions()
    build_imd()
    build_physical()
    build_ruc()
    build_composite()


if __name__ == "__main__":
    main()
