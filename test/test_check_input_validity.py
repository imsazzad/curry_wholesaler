from input_validity_checker import check_input_validity


def test_check_input_validity_when_input_is_none_is_invalid_input_is_true():
    lines = None
    assert check_input_validity(lines)[0] is True


def test_check_input_validity_when_num_of_curries_is_not_int_is_invalid_input_is_true():
    lines = ["a"]
    assert check_input_validity(lines)[0] is True


def test_check_input_validity_when_num_of_curries_is_zero_is_invalid_input_is_true():
    lines = ["0"]
    assert check_input_validity(lines)[0] is True


def test_check_input_validity_when_num_of_customer_is_zero_is_invalid_input_is_true():
    lines = ["5"]
    assert check_input_validity(lines)[0] is True


