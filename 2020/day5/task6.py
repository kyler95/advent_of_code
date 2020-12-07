# read data from file
file = open('input_5.txt', 'r')

lines = list(file)
ans = 0
ids = set()
for line in lines:
    rows = list(range(0, 128))
    cols = list(range(0, 8))
    line = line.strip()
    fw, lr = line[0:7], line[7:10]
    for ch in fw:
        if ch == 'F':
            rows = rows[:int(len(rows) / 2)]
        else:
            rows = rows[int(len(rows) / 2):]
    for ch in lr:
        if ch == 'L':
            cols = cols[:int(len(cols) / 2)]
        else:
            cols = cols[int(len(cols) / 2):]
    seat_id = rows[0] * 8 + cols[0]
    ids.add(seat_id)
    ans = max(ans, seat_id)

for id_ in sorted(ids):
    if id_ + 1 not in ids and id_ + 2 in ids:
        ans2 = id_ + 1

print(ans)
print(ans2)
