from copy import deepcopy
# read data from file
file = open('input_8.txt', 'r')


def run(p, pc, acc):
    words = p[pc]
    if words[0] == 'acc':
        pc += 1
        acc += int(words[1])
    elif words[0] == 'nop':
        pc += 1
    elif words[0] == 'jmp':
        pc += int(words[1])

    return pc, acc


program = list([line.split() for line in file])
pc = 0
acc = 0
seen = set()

while True:
    if pc in seen:
        print(acc)
        break
    seen.add(pc)
    pc, acc = run(program, pc, acc)

for change in range(len(program)):
    new_program = deepcopy(program)
    if new_program[change][0] == 'nop':
        new_program[change][0] = 'jmp'
    elif new_program[change][0] == 'jmp':
        new_program[change][0] = 'nop'
    else:
        continue
    pc = 0
    acc = 0
    temp = 0
    while 0 <= pc < len(new_program) and temp < 1000:
        temp += 1
        pc, acc = run(new_program, pc, acc)
    if pc == len(new_program):
        print(acc)
