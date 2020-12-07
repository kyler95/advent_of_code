import string

# read data from file
file = open('input_6.txt', 'r')

ans = 0
ans2 = 0

lines = list(file)
lines.append('')

any_yes = set()
all_yes = set(string.ascii_lowercase)

for line in lines:
    line = line.strip()
    if not line:
        ans += len(any_yes)
        ans2 += len(all_yes)
        any_yes = set()
        all_yes = set(string.ascii_lowercase)
    else:
        for ch in line:
            any_yes.add(ch)

        for ch in string.ascii_lowercase:
            if ch not in line and ch in all_yes:
                all_yes.remove(ch)

print(ans)
print(ans2)
