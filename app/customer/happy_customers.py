from constants import MEAT


def remove_happy_customer_info(happy_customer_ids, order):
    for customer_id in happy_customer_ids:
        order.customers_info.pop(customer_id, None)
        for curry_num in order.meat_preference:
            order.meat_preference[curry_num].discard(customer_id)
        for curry_num in order.veg_preference:
            order.veg_preference[curry_num].discard(customer_id)


def get_happy_customers_id(curry_name, next_curry_info, order):
    if curry_name == MEAT:
        happy_customer_ids = order.meat_preference[next_curry_info.curry_number]
    else:
        happy_customer_ids = order.veg_preference[next_curry_info.curry_number]
    return happy_customer_ids
