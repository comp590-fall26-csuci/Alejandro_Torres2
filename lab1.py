def fibonacci_iterative(n):
    sequence = []
    a, b = 0, 1

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    return sequence


with open("output/fibonacci.txt", "w") as file:
    for number in fibonacci_iterative(25):
        file.write(str(number) + "\n")
