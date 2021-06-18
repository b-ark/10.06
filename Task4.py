# Create your custom exception named `CustomException`, you can inherit from base Exception class,
# but extend its functionality to log every error message to a file named `logs.txt`.
# Tips: Use __init__ method to extend functionality for saving messages to file
from datetime import datetime


class CustomException(Exception):
    def __init__(self, msg):
        with open('logs.txt', 'a') as file_object:
            file_object.write(f'{datetime.ctime(datetime.now())}: {msg}')


try:
    raise CustomException('Something went wrong!')
except PermissionError:
    print('File is read-only!')
except CustomException as massage:
    print(massage)
