import itertools

# read data from file
file = open('input_9.txt', 'r')

ans = None
ans2 = None
lines = list([int(x) for x in file])

len_preamble = 25

for i in range(len_preamble, len(lines)):
    prev = lines[i-len_preamble:i]
    if ans is None and (not any([x+y == lines[i] for x, y in itertools.combinations(prev, 2)])):
        ans = lines[i]

for i in range(len(lines)):
    for j in range(i+2, len(lines)):
        xs = lines[i:j]
        if sum(xs) == ans and ans2 is None:
            ans2 = min(xs) + max(xs)

print(ans)
print(ans2)
