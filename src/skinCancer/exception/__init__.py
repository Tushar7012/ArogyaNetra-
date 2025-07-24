import sys
from skinCancer.logger import logger

def error_message_detail(error, error_detail: sys):
    """
    Formats a detailed error message including the script name, line number, and error message.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in python script name [{file_name}] line number [{line_number}] error message [{str(error)}]"
    return error_message

class CustomException(Exception):
    """
    Custom exception class that formats error messages for better logging.
    """
    def __init__(self, error_message, error_detail: sys):
        """
        Initializes the CustomException.

        Args:
            error_message (str): The error message from the exception.
            error_detail (sys): The sys object, used to get exception details.
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        """
        Returns the formatted error message when the exception is printed.
        """
        return self.error_message

