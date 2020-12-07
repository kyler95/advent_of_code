# read data from file
file = open('input_4.txt', 'r')


def in_range(s, low, high):
    return low <= int(s) <= high


ans1 = 0
ans2 = 0
passport = {}

lines = list(file)
lines.append('')

for line in lines:
    line = line.strip()
    if not line:
        valid1 = all([field in passport for field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']])
        if valid1:
            ans1 += 1
            valid2 = True
            if not in_range(passport['byr'], 1920, 2002):
                valid2 = False
            if not in_range(passport['iyr'], 2010, 2020):
                valid2 = False
            if not in_range(passport['eyr'], 2020, 2030):
                valid2 = False

            hgt = passport['hgt']
            if hgt.endswith('in'):
                if not in_range(hgt[:-2], 59, 76):
                    valid2 = False
            elif hgt.endswith('cm'):
                if not in_range((hgt[:-2]), 150, 193):
                    valid2 = False
            else:
                valid2 = False

            hcl = passport['hcl']
            if hcl[0] != '#' or any([c not in '0123456789abcdef' for c in hcl[1:]]):
                valid2 = False

            ecl = passport['ecl']
            if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                valid2 = False

            pid = passport['pid']
            if len(pid) != 9 or any([c not in '0123456789' for c in pid]):
                valid2 = False

            if valid2:
                ans2 += 1
        passport = {}
    else:
        words = line.split()
        for word in words:
            key, value = word.split(':')
            passport[key] = value
print(ans1)
print(ans2)
