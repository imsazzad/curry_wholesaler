import logging
from typing import Optional
from copy import deepcopy
from constants import VEGETARIAN, MEAT
from curry_info import CurryInfo
from customer_info import CustomerInfo
from order import Order
logging.basicConfig(level=logging.DEBUG)


def get_next_customer(customers_info:dict) -> CustomerInfo:
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


def update_customer_preferences(order: Order, curry_number):
    updated_customers_preferences = order.customers_info.copy()
    if curry_number in order.meat_preference:
        for customer_id in order.meat_preference[curry_number]:
            if customer_id in updated_customers_preferences:
                updated_customers_preferences[customer_id].pop(curry_number, None)

    if curry_number in order.veg_preference:
        for customer_id in order.veg_preference[curry_number]:
            if customer_id in updated_customers_preferences:
                updated_customers_preferences[customer_id].pop(curry_number, None)

    return updated_customers_preferences


def update_order(order: Order, happy_customer_ids: list, next_curry_number):
    updated_order = deepcopy(order)
    remove_happy_customer_info(happy_customer_ids, updated_order)
    updated_order.customers_info = update_customer_preferences(updated_order, next_curry_number)
    updated_order.meat_preference.pop(next_curry_number, None)
    updated_order.veg_preference.pop(next_curry_number, None)
    return updated_order


def remove_happy_customer_info(happy_customer_ids, order):
    for customer_id in happy_customer_ids:
        order.customers_info.pop(customer_id, None)
        for curry_num in order.meat_preference:
            order.meat_preference[curry_num].discard(customer_id)
        for curry_num in order.veg_preference:
            order.veg_preference[curry_num].discard(customer_id)


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


def get_next_customer_and_curry_number(next_customer, order):
    next_customer_info = order.customers_info[next_customer.idx]
    next_curry_info = get_next_curry_number(next_customer_info)
    logging.debug("customer_to_be_picked_next - {} - {}".format(next_customer.idx, next_customer_info))
    logging.debug("curry to be picked for this customer -{} ".format((vars(next_curry_info))))
    return next_curry_info, next_customer_info


def get_happy_customers_id(curry_name, next_curry_info, order):
    if curry_name == MEAT:
        happy_customer_ids = order.meat_preference[next_curry_info.curry_number]
    else:
        happy_customer_ids = order.veg_preference[next_curry_info.curry_number]
    return happy_customer_ids


def log_updated_information(happy_customer:int, order:Order):
    logging.debug("customers info - {} - num of customer- {}".format(order.customers_info, len(order.customers_info)))
    logging.debug("meat pref- {} ".format(order.meat_preference))
    logging.debug("veg pref- {} ".format(order.veg_preference))
    logging.debug("happy customer- {} ".format(happy_customer))
