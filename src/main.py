import argparse

def get_args():
    parse = argparse.ArgumentParse(
        description='ナンバープレイスを解きます。')

    parse.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    return parser.parse_args()

def main():
    args = get_args()
    print(args)


if __name__ == '__main__':
    main()
