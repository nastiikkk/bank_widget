import pytest

from src.decorators import log


def test_log_success(capsys) -> None:
    @log()
    def my_function(x, y):
        return x + y

    my_function(1, 2)

    captured = capsys.readouterr()

    assert captured.out == "my_function ok\n"


def test_log_error(capsys) -> None:
    @log()
    def my_function(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        my_function(1, 0)

    captured = capsys.readouterr()

    assert "my_function error: division by zero. Inputs: (1, 0), {}" in captured.out


def test_log_file_success() -> None:
    filename = "mylog.txt"

    @log(filename=filename)
    def my_function(x, y):
        return x + y

    my_function(1, 2)

    with open(filename) as file:
        content = file.read()

    assert content == "my_function ok\n"


def test_log_file_error() -> None:
    filename = "mylog.txt"

    @log(filename=filename)
    def my_function(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        my_function(1, 0)

    with open(filename) as file:
        content = file.read()

    assert "my_function error: division by zero. Inputs: (1, 0), {}" in content
