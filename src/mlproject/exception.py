import sys
from src.mlproject.logger import logging

class CustomException(Exception):
    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)
        self.error_message = self.error_detailed_message(error_message, error_details)

    def __str__(self):
        return self.error_message

    @staticmethod
    def error_detailed_message(error, error_detail: sys):
        exc_type, exc_obj, exc_tb = error_detail.exc_info()  # Extract traceback info
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        return f"Error occurred in script: [{file_name}] at line number: [{line_number}] with error message: [{str(error)}]"
