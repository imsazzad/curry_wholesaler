from constants import VEGETARIAN, MEAT
from curry.curry_info import CurryInfo


def get_next_curry_number(current_customer_info) -> CurryInfo:
    next_curry_info = CurryInfo()
    for current_curry_number in current_customer_info:
        current_curry_name = current_customer_info[current_curry_number]
        can_replace_next_curry = not next_curry_info.curry_name or (current_curry_name == VEGETARIAN
                                                                    and next_curry_info.curry_name == MEAT)
        if can_replace_next_curry:
            next_curry_info = CurryInfo(curry_number=current_curry_number, curry_name=current_curry_name)

    return next_curry_info
