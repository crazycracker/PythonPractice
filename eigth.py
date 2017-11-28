def fibonacci(n):
    if n <= 0:
        return
    a, b, counter = 0, 1, 0
    values = list()
    while True:
        if counter > n-1:
            return values
        values.append(a)
        a, b = b, a + b
        counter += 1


number = input("Enter the number\n")
print(fibonacci(int(number)))
