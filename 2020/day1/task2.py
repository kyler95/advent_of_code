def sum_three(arr, target):
    res = []

    arr.sort()
    for i in range(0, len(arr) - 2):
        l = i + 1
        r = len(arr) - 1

        while l < r:
            if arr[i] + arr[l] + arr[r] == target:
                res.append(arr[i])
                res.append(arr[l])
                res.append(arr[r])
                return res
            elif arr[i] + arr[l] + arr[r] < target:
                l += 1
            else:
                r -= 1
    return res


def multiply(iterable):
    prod = 1
    for x in iterable:
        prod *= x

    return prod


# read data from file
file = open('input.txt', 'r')
data = []
for line in file:
    data.append(int(line))
file.close()
print(multiply(sum_three(data, 2020)))
