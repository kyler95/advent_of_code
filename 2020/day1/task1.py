def sum_two(arr, target):
    res = dict()

    for i, elem in enumerate(arr):
        diff = target - elem

        if diff in res:
            return [diff, elem]

        res[elem] = i

    return []


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
print(multiply(sum_two(data, 2020)))
