from copy import deepcopy

from app.customer.customers import update_customer_preferences
from app.customer.happy_customers import remove_happy_customer_info
from app.order.orders import Order


def update_order(order: Order, happy_customer_ids: list, next_curry_number):
    updated_order = deepcopy(order)
    remove_happy_customer_info(happy_customer_ids, updated_order)
    updated_order.customers_info = update_customer_preferences(updated_order, next_curry_number)
    updated_order.meat_preference.pop(next_curry_number, None)
    updated_order.veg_preference.pop(next_curry_number, None)
    return updated_order
