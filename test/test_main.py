import pytest
from app.main import main


@pytest.fixture
def example_valid_input_data():
    return [
        ['5', '1 M 3 V 5 V', '2 V 3 M 4 V', '5 M'],
        ['5', '2 M', '5 V', '1 V', '5 V 1 V 4 M', '3 V', '5 V', '3 V 5 V 1 V', '3 V', '2 M', '5 V 1 V', '2 M', '5 V',
         '4 M', '5 V 4 M'],
        ['2', '1 V 2 M', '1 M']
    ]


@pytest.fixture
def example_invalid_input_data():
    return [
        ['1', '1 V', '1 M'],
        ["a"],
        ["0"],
        None
    ]


def test_main_with_valid_input_it_should_return_correct_output(example_valid_input_data):
    assert main(example_valid_input_data[0]) == ['V', 'V', 'V', 'V', 'M']
    assert main(example_valid_input_data[1]) == ['V', 'M', 'V', 'M', 'V']
    assert main(example_valid_input_data[2]) == ['M', 'M']


def test_main_with_invalid_input_it_should_return_no_solution(example_invalid_input_data):
    assert main(example_invalid_input_data[0]) is None
    assert main(example_invalid_input_data[1]) is None
    assert main(example_invalid_input_data[2]) is None
    assert main(example_invalid_input_data[3]) is None


