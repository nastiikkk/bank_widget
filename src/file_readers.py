import pandas as pd


def read_csv_file(path_to_csv: str) -> list[dict]:
    """Считывает финансовые операции из CSV-файла"""
    df = pd.read_csv(path_to_csv)
    return df.to_dict(orient="records")


def read_excel_file(path_to_excel: str) -> list[dict]:
    """Считывает финансовые операции из Excel-файла"""
    df = pd.read_excel(path_to_excel)
    return df.to_dict(orient="records")
