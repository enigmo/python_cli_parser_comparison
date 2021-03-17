from argparse import ArgumentParser


def hello(args):
    print(f"hello {args.name}")


def add(args):
    print(f"result {sum(args.values)}")


def main():
    parser = ArgumentParser()
    subparsers = parser.add_subparsers()

    hello_parser = subparsers.add_parser("hello")
    hello_parser.add_argument("name", type=str, default="world", help="echo name")
    hello_parser.set_defaults(func=hello)

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("values", type=int, nargs="*")
    add_parser.set_defaults(func=add)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
