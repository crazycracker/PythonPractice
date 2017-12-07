def solution(array):
    array.sort()
    count = 0
    result = 0
    for x in range(len(array)-1):
        if array[x+1] == array[x]:
            count += 1
        else:
            if count > 1:
                count += 1
            result += count;
            count = 0

    return result


n = int(input("enter the number of elements"))
array = list()

for i in range(n):
    number = int(input())
    array.append(number)
print(solution(array))