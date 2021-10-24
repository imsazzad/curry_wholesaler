import logging
from typing import Optional

from app.constants import VEGETARIAN
from app.customer.customers import get_next_customer
from app.customer.happy_customers import get_happy_customers_id
from app.order.orders import Order
from app.customer.customers import get_next_customer_and_curry_number
from app.order.order_processor import update_order

logging.basicConfig(level=logging.DEBUG)


def prepare_curry(order: Order) -> Optional[list]:
    curries_list: list = [VEGETARIAN for _ in range(order.total_recipe)]
    num_of_happy_customer = 0
    log_updated_information(num_of_happy_customer, order)

    while num_of_happy_customer < order.total_customer and len(order.customers_info) > 0:
        next_customer = get_next_customer(order.customers_info)
        if next_customer.num_of_preference <= 0:
            break

        next_curry_info, next_customer_info = get_next_customer_and_curry_number(next_customer, order)
        curry_name = next_customer_info[next_curry_info.curry_number]
        curries_list[next_curry_info.curry_number - 1] = curry_name
        num_of_happy_customer, order = update_all_relevant_info(curry_name, next_curry_info,
                                                                num_of_happy_customer, order)
    return curries_list if order.total_customer == num_of_happy_customer else None


def update_all_relevant_info(curry_name, next_curry_info, num_of_happy_customer, order):
    happy_customer_ids = get_happy_customers_id(curry_name, next_curry_info, order)
    num_of_happy_customer += len(happy_customer_ids)
    order = update_order(order, happy_customer_ids, next_curry_info.curry_number)
    log_updated_information(num_of_happy_customer, order)
    return num_of_happy_customer, order


def log_updated_information(happy_customer: int, order: Order):
    logging.debug("customers info - {} - num of customer- {}".format(order.customers_info, len(order.customers_info)))
    logging.debug("meat pref- {} ".format(order.meat_preference))
    logging.debug("veg pref- {} ".format(order.veg_preference))
    logging.debug("happy customer- {} ".format(happy_customer))
