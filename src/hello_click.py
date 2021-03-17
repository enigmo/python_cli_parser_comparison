from typing import Tuple

import click


@click.group()
def cmd():
    pass


@cmd.command()
@click.option("--name", type=str, default="world", help="echo name", show_default=True)
def hello(name: str):
    print(f"hello {name}")


@cmd.command()
@click.argument("values", type=int, required=True, nargs=-1)
def add(values: Tuple[int]):
    print(f"result {sum(values)}")


def main():
    cmd()


if __name__ == "__main__":
    main()
