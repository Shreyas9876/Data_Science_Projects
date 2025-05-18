import sys
from src.Logger import logging
from typing import Any

def error_message_detail(error: Any, error_detail: sys) -> str:
    _, _, exc_tb = error_detail.exc_info()
    
    if exc_tb is None:
        file_name = "Unknown"
        line_number = "Unknown"
    else:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno

    error_message = (
        f"Error occurred in Python script [{file_name}] "
        f"at line number [{line_number}] "
        f"with error message [{str(error)}]"
    )

    return error_message

class CustomException(Exception):
    def __init__(self, error_message: Any, error_detail: sys) -> None:
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self) -> str:
        return self.error_message
