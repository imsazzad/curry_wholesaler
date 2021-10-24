import logging


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

    if total_customer <= 0:
        is_invalid_input = True  # each customer must have some preference

    return is_invalid_input, total_recipe, total_customer
