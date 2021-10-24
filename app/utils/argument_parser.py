from argparse import ArgumentParser


def parse_args_and_load_vars():
    parser = ArgumentParser()
    parser.add_argument("-f", "--file", dest="input_file",
                        help="FILE to read input data from")

    args = parser.parse_args()
    if not args.input_file:
        args.input_file = "../data/input3.txt"

    return args
