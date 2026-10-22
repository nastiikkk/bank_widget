import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "card, expected",
    [
        ("Visa 1234567812345678", "Visa 1234 56** **** 5678"),
        ("MasterCard 9876543210987654", "MasterCard 9876 54** **** 7654"),
        ("Счет 40817810099910004312", "Счет **4312"),
    ],
)
def test_mask_account_card(card: str, expected: str) -> None:
    assert mask_account_card(card) == expected


@pytest.mark.parametrize(
    "card",
    [
        (""),
        ("Visa"),
        ("1234567812345678"),
        ("Visa abcdefgh"),
        ("Счет abcdefgh"),
        ("Счет 123"),
        ("Visa 123"),
    ],
)
def test_mask_account_card_invalid(card: str) -> None:
    with pytest.raises(ValueError):
        mask_account_card(card)


@pytest.mark.parametrize(
    "date, expected",
    [("2026-01-15T12:30:00", "15.01.2026"), ("2023-12-31T23:59:59", "31.12.2023")],
)
def test_get_date(date: str, expected: str) -> None:
    assert get_date(date) == expected


@pytest.mark.parametrize(
    "date",
    [
        (""),
        ("sadsd"),
        ("2024-13-01"),
        ("01.01.2024"),
    ],
)
def test_get_date_invalid(date: str) -> None:
    with pytest.raises(ValueError):
        get_date(date)
