import sys
import traceback

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys): # type: ignore
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message

def error_message_detail(error, error_detail: sys): # type: ignore
    tb = traceback.extract_tb(error_detail.exc_info()[2])
    filename, lineno, _, _ = tb[-1]  # baris terakhir traceback
    error_message = (
        "Error occurred in python script name [{0}] line number [{1}] error message [{2}]"
        .format(filename, lineno, str(error))
    )
    return error_message
