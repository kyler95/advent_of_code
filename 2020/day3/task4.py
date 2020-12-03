# read data from file
file = open('input_3.txt', 'r')
data = []
for line in file:
    data.append(list(line.strip()))

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

ans = 1
for (dc, dr) in slopes:
    r = 0
    c = 0
    score = 0
    while r + 1 < len(data):
        c += dc
        r += dr
        if data[r][c % len(data[r])] == '#':
            score += 1
    ans *= score

print(ans)
