from gendiff.cli import make_parser
from gendiff.gendiff import generate_diff


def main():
    args = make_parser().parse_args()

    print(generate_diff(args.path_file1, args.path_file2, args.format))

    return


if __name__ == '__main__':
    main()
