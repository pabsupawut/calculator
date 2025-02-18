from calculator import Calculator

# Create an instance of Calculator
calc = Calculator()

# Example cases
num1 = 10
num2 = 5

# Perform operations
addition_result = calc.add(num1, num2)
subtraction_result = calc.subtract(num1, num2)
multiplication_result = calc.multiply(num1, num2)
division_result = calc.divide(num1, num2)

# Print results
print(f"Addition of {num1} and {num2}: {addition_result}")
print(f"Subtraction of {num1} and {num2}: {subtraction_result}")
print(f"Multiplication of {num1} and {num2}: {multiplication_result}")
print(f"Division of {num1} and {num2}: {division_result}")