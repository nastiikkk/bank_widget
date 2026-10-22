import pytest

from src.processing import filter_by_state, sort_by_date

"""Тесты для filter_by_state"""


@pytest.fixture
def operations_for_filter_by_state() -> list[dict]:
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
        },
        {
            "id": 2,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
        },
    ]


@pytest.mark.parametrize(
    "state, expected",
    [
        (
            "EXECUTED",
            [
                {
                    "id": 1,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                },
                {
                    "id": 3,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
            ],
        ),
        (
            "CANCELED",
            [
                {
                    "id": 2,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                },
            ],
        ),
    ],
)
def test_filter_by_state(
    operations_for_filter_by_state: list[dict],
    state: str,
    expected: list[dict],
) -> None:
    assert filter_by_state(operations_for_filter_by_state, state) == expected


def test_filter_by_state_no_matches(
    operations_for_filter_by_state: list[dict],
) -> None:
    assert filter_by_state(operations_for_filter_by_state, "IN PROCESS") == []


"""Тесты для sort_by_date"""


@pytest.fixture
def operations_for_sort_by_date() -> list[dict]:
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
        },
        {
            "id": 2,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
        },
    ]


@pytest.fixture
def operations_same_date() -> list[dict]:
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
        },
        {
            "id": 2,
            "state": "CANCELED",
            "date": "2019-07-03T18:35:29.512364",
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
        },
    ]


@pytest.fixture
def operations_invalid_date() -> list[dict]:
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2019/07/03",
        },
        {
            "id": 2,
            "state": "CANCELED",
            "date": "03.07.2019",
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": "not a date",
        },
    ]


@pytest.mark.parametrize(
    "reverse, expected",
    [
        (
            True,
            [
                {
                    "id": 1,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                },
                {
                    "id": 2,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                },
                {
                    "id": 3,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
            ],
        ),
        (
            False,
            [
                {
                    "id": 3,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
                {
                    "id": 2,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                },
                {
                    "id": 1,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                },
            ],
        ),
    ],
)
def test_sort_by_date(
    operations_for_sort_by_date: list[dict],
    reverse: bool,
    expected: list[dict],
) -> None:
    assert sort_by_date(operations_for_sort_by_date, reverse) == expected


def test_sort_by_date_same_dates(
    operations_same_date: list[dict],
) -> None:
    expected = [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
        },
        {
            "id": 2,
            "state": "CANCELED",
            "date": "2019-07-03T18:35:29.512364",
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
        },
    ]

    assert sort_by_date(operations_same_date) == expected


def test_sort_by_date_invalid_format(
    operations_invalid_date: list[dict],
) -> None:
    with pytest.raises(ValueError):
        sort_by_date(operations_invalid_date)
