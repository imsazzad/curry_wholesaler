from typing import Optional
from order import Order
from order_info_transfomer import transform_order_info
from recipe_maker import prepare_curry
from input_validity_checker import check_input_validity
from utils.argument_parser import parse_args_and_load_vars
from utils.reader.text_file_reader import TextFileReader
from constants import NO_SOLUTION_MSG

import logging
logging.basicConfig(level=logging.DEBUG)


def main(lines: list) -> Optional[list]:
    is_invalid_input, total_recipe, total_customer = check_input_validity(lines)
    curries = None

    if not is_invalid_input:
        order: Order = transform_order_info(lines, total_recipe, total_customer)
        curries = prepare_curry(order)

    return curries


if __name__ == '__main__':
    args = parse_args_and_load_vars()
    line_arr: list = TextFileReader().read(args.input_file)
    result = main(line_arr)

    if not result:
        logging.info(NO_SOLUTION_MSG)
    else:
        logging.info("Final Curry list is :-")
        logging.info(" ".join(result))

