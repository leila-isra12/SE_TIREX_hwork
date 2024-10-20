class CustomError(Exception):
    """Custom exception for special cases."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Example usage
def divide_numbers(a, b):
    if b == 0:
        raise CustomError("Cannot divide by zero")
    return a / b
