from docopt import docopt


def hello():
    """OverView:
    Usage:
        hello.py [-h]
        hello.py --name=NAME

    Options:
        -h, --help  show this help message and exit
        --name=NAME  name echo name  [default: world].

    """
    args = docopt(hello.__doc__)
    print(f"hello {args['--name']}")


if __name__ == "__main__":
    hello()
