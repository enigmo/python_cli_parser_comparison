from typing import Tuple

import fire


class Test:
    def hello(self, name: str = "world"):
        """
        name: echo name
        """
        print(f"hello {name}")

    def add(self, values: Tuple[int]):
        """
        values: list sum values
        """
        print(f"result {sum(values)}")


if __name__ == "__main__":
    fire.Fire(Test)
