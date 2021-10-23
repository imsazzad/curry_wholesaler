from recipe_maker import prepare_curry
from curry_names import *


def test_prepare_curry_when_input_is_none_output_should_be_none():
    lines = None
    assert prepare_curry(lines) is None


def test_prepare_curry_when_num_of_curries_is_not_int_output_should_be_none():
    lines = ["a"]
    assert prepare_curry(lines) is None


def test_prepare_curry_when_num_of_curries_is_zero_output_should_be_none():
    lines = ["0"]
    assert prepare_curry(lines) is None


def test_prepare_curry_when_input_len_is_1_output_should_be_all_veg():
    lines = ["2"]
    assert prepare_curry(lines) == [VEGETARIAN, VEGETARIAN]


# def test_prepare_curry_when_empty_customer_info_output_should_be_all_veg():
#     lines = None
