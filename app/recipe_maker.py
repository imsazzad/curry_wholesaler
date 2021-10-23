import logging
from typing import Optional

from curry_names import VEGETARIAN, MEAT
from order import Order

logging.basicConfig(level=logging.DEBUG)


class CustomerInfo:
    def __init__(self, idx=None, num_of_preference=float("inf")):
        self.idx = idx
        self.num_of_preference = num_of_preference


class CurryInfo:
    def __init__(self, curry_number: int = -1, curry_name: str = None):
        self.curry_number = curry_number
        self.curry_name = curry_name


def pick_next_customer_to_be_made_happy(customers_info) -> CustomerInfo:
    next_customer = CustomerInfo()
    for key in customers_info:
        if len(customers_info[key]) < next_customer.num_of_preference:
            next_customer = CustomerInfo(idx=key, num_of_preference=len(customers_info[key]))

    return next_customer


def get_next_curry_number(current_customer_info) -> CurryInfo:
    next_curry_info = CurryInfo()
    for current_curry_number in current_customer_info:
        current_curry_name = current_customer_info[current_curry_number]
        can_replace_next_curry = not next_curry_info.curry_name or \
                                 (current_curry_name == VEGETARIAN and next_curry_info.curry_name == MEAT)
        if can_replace_next_curry:
            next_curry_info = CurryInfo(curry_number=current_curry_number, curry_name=current_curry_name)

    return next_curry_info


def prepare_curry(order: Order) -> Optional[list]:
    curries_list: list = [VEGETARIAN for _ in range(order.total_recipe + 1)]
    happy_customer = 0

    log_updated_information(happy_customer, order)

    while happy_customer < order.total_customer and len(order.customers_info) > 0:
        next_customer = pick_next_customer_to_be_made_happy(order.customers_info)
        if next_customer.num_of_preference <= 0:
            break

        current_customer_info = order.customers_info[next_customer.idx]
        logging.debug("customer_to_be_picked_next - {} - {}".format(next_customer.idx, current_customer_info))

        next_curry_info = get_next_curry_number(current_customer_info)
        logging.debug("curry to be picked for this customer -{} ".format((vars(next_curry_info))))
        if next_curry_info.curry_number == -1:  # customer curry_like_list is empty
            break


def log_updated_information(happy_customer, order):
    logging.debug("customers info - {} - num of customer- {}".format(order.customers_info, len(order.customers_info)))
    logging.debug("meat pref- {} ".format(order.meat_preference))
    logging.debug("veg pref- {} ".format(order.veg_preference))
    logging.debug("happy customer- {} ".format(happy_customer))
