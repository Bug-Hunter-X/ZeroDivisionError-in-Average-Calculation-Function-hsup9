def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage (will not cause an error):
my_list = []
result = calculate_average(my_list)
print(result) # Output: 0

my_list = [1,2,3,4,5]
result = calculate_average(my_list)
print(result) # Output: 3.0