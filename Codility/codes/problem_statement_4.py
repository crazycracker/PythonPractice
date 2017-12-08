def solution(array):
    element = 0
    count = 0

    for i in range(len(array)):
        if i == 0:
            element = array[i]
            count = 1
        else:
            if element == array[i]:
                count += 1
            else:
                count -= 1

    return count


print("Enter the size of the array \n")
counter = int(input())
print("Enter the elements\n")
array = list()
for i in range(counter):
    element = int(input())
    array.append(element)
print("If the value is negative then there is no majority element\n")
print("The majority element is %d" % solution(array))
