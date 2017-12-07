import csv

with open('iris.data', 'r') as csvfile:
    lines = csv.reader(csvfile)
    dataset = list(lines)
    iterator = iter(dataset)

    while True:
        try:
            print(next(iterator))
        except StopIteration:
            print("completed printing")
            break


