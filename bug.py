def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage (will cause ZeroDivisionError):
my_list = []
result = calculate_average(my_list)