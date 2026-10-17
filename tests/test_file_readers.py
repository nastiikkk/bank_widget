from unittest.mock import Mock, patch

from src.file_readers import read_csv_file, read_excel_file


@patch("src.file_readers.pd.read_csv")
def test_read_csv_file(mock_read_csv: Mock) -> None:
    """Проверяет чтение финансовых операций из CSV"""
    expected_data = [
        {"id": 1, "amount": 1000},
        {"id": 2, "amount": 2000},
    ]
    mock_read_csv.return_value.to_dict.return_value = expected_data
    result = read_csv_file("transactions.csv")
    assert result == expected_data
    mock_read_csv.assert_called_once_with("transactions.csv")


@patch("src.file_readers.pd.read_excel")
def test_read_excel_file(mock_read_excel: Mock) -> None:
    """Проверяет чтение финансовых операций из XLSX"""
    expected_data = [
        {"id": 1, "amount": 1000},
        {"id": 2, "amount": 2000},
    ]
    mock_read_excel.return_value.to_dict.return_value = expected_data
    result = read_excel_file("transactions_excel.xlsx")
    assert result == expected_data
    mock_read_excel.assert_called_once_with("transactions_excel.xlsx")
