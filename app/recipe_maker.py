import logging
from typing import Optional

from curry_names import VEGETARIAN
from order import Order

logging.basicConfig(level=logging.DEBUG)


def prepare_curry(order: Order) -> Optional[list]:
    curries_list: list = [VEGETARIAN for _ in range(order.total_recipe + 1)]
    happy_customer = 0

    logging.debug("customers info - {} - num of customer- {}".format(order.customers_info, len(order.customers_info)))
    logging.debug("meat pref- {} ".format(order.meat_preference))
    logging.debug("veg pref- {} ".format(order.veg_preference))
    logging.debug("happy customer- {} ".format(happy_customer))