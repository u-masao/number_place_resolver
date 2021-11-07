import argparse


def get_args():
    parser = argparse.ArgumentParser(description="ナンバープレイスを解きます。")

    parser.add_argument(
        "infile",
        nargs=1,
        type=argparse.FileType("r"),
    )
    return parser.parse_args()


def main():
    args = get_args()
    print(vars(args))


if __name__ == "__main__":
    main()
