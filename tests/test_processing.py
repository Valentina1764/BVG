import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(state_sort, result_state_default) -> str:
    assert filter_by_state(state_sort) == result_state_default


def test_filter_by_state_is(state_sort, result_state_canceled) -> str:

    assert filter_by_state(state_sort, state="CANCELED") == result_state_canceled


def test_state_error(state_sort_error):
    with pytest.raises(ValueError) as exc_info:
        filter_by_state(state_sort_error)
    assert str(exc_info.value) == "Значение ключа 'state' неопределено"


def test_sort_by_date(state_sort, result_sort_date_descending):
    assert sort_by_date(state_sort) == result_sort_date_descending


def test_sort_by_date_up(state_sort, result_sort_date_ascending) -> list:

    assert sort_by_date(state_sort, is_reversed=False) == result_sort_date_ascending


def test_date_error(state_date_error):
    with pytest.raises(ValueError) as exc_info:
        sort_by_date(state_date_error)
    assert str(exc_info.value) == "Значение ключа 'date' не может быть пустым"
