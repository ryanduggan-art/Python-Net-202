def fibonacci(n):
    a, b = 0, 1
    count = 0
    sequence = []

    while count < n:
        sequence.append(a)
        a, b = b, a + b
        count += 1

    return sequence

print(fibonacci(20))
