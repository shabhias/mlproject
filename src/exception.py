import sys
import traceback
import logging

import traceback
import logging

class CustomException(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)
    
    def __str__(self):
        return self.error_message

def error_message_detail(error, error_detail):
    _, _, exc_tb = error_detail.exc_info()
    tb = traceback.extract_tb(exc_tb)
    filename, lineno, _, _ = tb[-1]
    
    error_message = (
        "Error occurred in python script name [{0}] line number [{1}] error message [{2}]"
        .format(filename, lineno, str(error))
    )
    return error_message



# if __name__ == "__main__":
    # try:
    #     a = 1 / 0
    # except Exception as e:
    #     logging.info("Exception occurred", exc_info=True)
    #     raise CustomException(e, sys) from e


