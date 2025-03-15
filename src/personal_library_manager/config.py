import json

class ValidationError(Exception):
    pass

def load_books():
    try:
        with open("./library.txt","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def add_data(books):
    with open("./library.txt","w") as file:
        json.dump(books,file)

def validate_string(value: str, errorMessage: str) -> str:
        if value.isdigit():
            print(errorMessage)
            raise ValidationError
        return value

def validate_integer(value: str, errorMessage: str) -> str:
    if not value.isdigit():
        print(errorMessage)
        raise ValidationError
    return value

def check_status(value: str) -> bool:
    if value.lower() == "yes" or value.lower() == "y":
        return True
    elif value.lower() == "no" or value.lower() == "n":
        return False
    else:
        print(f"Please enter valid value")
        raise ValidationError

