import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567812345678", "1234 56** **** 5678"),
        ("1111111111111111", "1111 11** **** 1111"),
    ],
)
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("card_number", ["1234567890", "", "ab1cd3"])
def test_get_mask_card_number_invalid(card_number: str) -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


@pytest.mark.parametrize(
    "card_number, expected", [("123456", "**3456"), ("12345678912345", "**2345")]
)
def test_get_mask_account(card_number: str, expected: str) -> None:
    assert get_mask_account(card_number) == expected


@pytest.mark.parametrize(
    "card_number",
    [
        "",
        "ab1cd3",
        "123",
    ],
)
def test_get_mask_account_invalid(card_number: str) -> None:
    with pytest.raises(ValueError):
        get_mask_account(card_number)
