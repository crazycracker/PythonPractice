def fibonacci():
    a, b, counter = 0, 1, 0
    while True:
        if counter > 19:
            return
        print(a)
        a, b = b, a + b
        counter += 1


fibonacci()