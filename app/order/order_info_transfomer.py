from app.order.orders import Order
from constants import MEAT


def prepare_choices(a_customer_choice: str, customer_id: int, meat_pref: dict, veg_pref: dict):
    choice_array = a_customer_choice.split()
    choice_dict = {}
    idx = 0

    while idx + 1 < len(choice_array):
        choice_dict[int(choice_array[idx])] = choice_array[idx + 1]

        if choice_array[idx + 1] == MEAT:
            meat_pref.setdefault(int(choice_array[idx]), set()).add(customer_id)
        else:
            veg_pref.setdefault(int(choice_array[idx]), set()).add(customer_id)
        idx += 2

    return choice_dict, meat_pref, veg_pref


def transform_order_info(lines, total_recipe, total_customer) -> Order:
    customers_info = {}
    meat_preference = {}
    veg_preference = {}

    for idx in range(1, len(lines)):
        customers_info[idx], meat_preference, veg_preference = prepare_choices(lines[idx], idx,
                                                                               meat_preference, veg_preference)

    return Order(customers_info, meat_preference, veg_preference, total_recipe, total_customer)
