import argparse

import numpy as np


def get_args():
    parser = argparse.ArgumentParser(description="ナンバープレイスを解きます。")

    parser.add_argument(
        "infile",
    )
    return parser.parse_args()


class Board:
    """
    self.data
      0: blank cell
      1-9: number cell
    """

    def __init__(self, infile=None, size=9):
        self.data = np.zeros((size, size)).astype(int)

        if infile is not None:
            self.load(infile)

    def load(self, filename):
        question = np.loadtxt(filename, delimiter=",", dtype=str)
        question[question == " "] = 0
        question = question.astype(int)
        self.data = question

    def __str__(self):
        return "board: \n" + str(self.data).replace("0", ".")


def main():
    args = get_args()
    print("args:\n", vars(args))
    board = Board()
    print(board)
    board = Board(infile=args.infile)
    print(board)


if __name__ == "__main__":
    main()
