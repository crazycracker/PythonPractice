
"""
If 0 ≤ C[a] < 1, then (a, b) is multiplicative only if C[a] = 0
If 1 < C[a] < 2, then C[a] / (C[a] - 1) > 2, therefore C[b] > 2. So, C[b] > C[a], but this is impossible because C[a] ≥ C[b] (because the array is sorted).
If C[a] > 2 then the pair is multiplicative for any C[b] where C[b] ≥ C[a] / (C[a] - 1)

"""


def solution(A, B):
    c = list()
    for x in range(len(A)):
        c.append(A[x] + B[x])
    c.sort()
    result = 0
    length = len(c)

    if length > 1:
        l_index = 0
        r_index = length - 1

        while r_index > l_index:
            value = float(c[r_index]/(c[r_index]-1))

            while l_index < r_index and c[l_index] < value:
                l_index += 1

            if l_index == r_index:
                break

            result += (r_index - l_index)
            r_index -= 1

    if result > pow(10, 9):
        result = pow(10, 9)

    return result


n = int(input("Enter the number of elements"))
print("Enter the elements of the first Array")
count = 0
A = list()
B = list()

while count < n:
    number = input()
    A.append(int(number))
    count += 1
count = 0

print("Enter the elements of the second Array")

while count < n:
    number = int(input())
    B.append(float(number/pow(10, 6)))
    count += 1

print(solution(A, B))
