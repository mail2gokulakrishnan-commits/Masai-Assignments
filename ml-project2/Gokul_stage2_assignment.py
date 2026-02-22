num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform subtraction
result = num1 - num2

# Show result
print("Result =", result)

# Check if result is positive, negative, or zero
if result > 0:
    print("Positive")
elif result < 0:
    print("Negative")
else:
    print("Zero")
