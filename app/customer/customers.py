import logging

from app.curry.curries import get_next_curry_number
from app.customer.customer_info import CustomerInfo
from app.order.orders import Order


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


def get_next_customer(customers_info: dict) -> CustomerInfo:
    next_customer = CustomerInfo()
    for key in customers_info:
        if len(customers_info[key]) < next_customer.num_of_preference:
            next_customer = CustomerInfo(idx=key, num_of_preference=len(customers_info[key]))

    return next_customer


def get_next_customer_and_curry_number(next_customer, order):
    next_customer_info = order.customers_info[next_customer.idx]
    next_curry_info = get_next_curry_number(next_customer_info)
    logging.debug("customer_to_be_picked_next - {} - {}".format(next_customer.idx, next_customer_info))
    logging.debug("curry to be picked for this customer -{} ".format((vars(next_curry_info))))
    return next_curry_info, next_customer_info
