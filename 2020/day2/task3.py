from collections import defaultdict

# read data from file
file = open('input_2.txt', 'r')
data = list(file)

ans = 0
ans2 = 0
for line in data:
    words = line.strip().split()
    low, high = [int(x) for x in words[0].split('-')]
    char = words[1][0]
    password = words[2]
    counter = defaultdict(int)
    for ch in password:
        counter[ch] += 1
    if low <= counter[char] <= high:
        ans += 1
    if (password[low - 1] == char) ^ (password[high - 1] == char):
        ans2 += 1
print(ans, ans2)

