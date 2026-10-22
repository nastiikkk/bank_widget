from functools import wraps
from typing import Any, Callable


def log(filename: str | None = None) -> Callable:
    """Логирует выполнение функции и возникающие ошибки"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
                if filename:
                    with open(filename, "a") as f:
                        f.write(f"{message}\n")
                else:
                    print(message)
                return result

            except Exception as e:
                message = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a") as f:
                        f.write(f"{message}\n")
                else:
                    print(message)
                raise

        return wrapper

    return decorator
