import logging
from typing import Optional

logging.basicConfig(level=logging.DEBUG)


def check_input_validity(lines: list) -> tuple:
    is_invalid_input = False
    total_recipe = -1
    total_customer = 0

    if not lines or len(lines) < 1:
        logging.error("Not a valid input")
        is_invalid_input = True
    else:
        total_customer = len(lines) - 1

        try:
            total_recipe = int(lines[0])
            if total_recipe <= 0:
                logging.info("No recipes to be made")
                is_invalid_input = True

        except ValueError:
            logging.error("Number of curries should be an integer")
            is_invalid_input = True

    return is_invalid_input, total_recipe, total_customer


def prepare_curry(lines: list) -> Optional[list]:
    is_invalid_input, total_recipe, total_customer = check_input_validity(lines)
    if is_invalid_input:
        return None

    curries_list: list = ["V" for _ in range(total_recipe + 1)]

    if total_customer == 0:
        # no customer preference , prepare all veg
        return curries_list[1:]

