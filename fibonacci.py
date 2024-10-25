def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    return fib_sequence[:n]

# Example usage:
n = int(input("Enter number"))  # Get Fibonacci numbers
fib_numbers = fibonacci(n)
print(fib_numbers)