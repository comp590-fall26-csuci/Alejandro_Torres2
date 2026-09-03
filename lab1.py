def fibonacci_recursive(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]

    sequence = fibonacci_recursive(n - 1)
    sequence.append(sequence[-1] + sequence[-2] if len(sequence) > 1 else 1)

    return sequence


with open("output/fibonacci.txt", "w") as file:
    for number in fibonacci_recursive(25):
        file.write(str(number) + "\n")

