def part1(ints, m, n):
    ints[1], ints[2] = m, n
    for i in range(0, len(ints), 4):
        if ints[i] == 1:
            ints[ints[i + 3]] = ints[ints[i + 1]] + ints[ints[i + 2]]
        elif ints[i] == 2:
            ints[ints[i + 3]] = ints[ints[i + 1]] * ints[ints[i + 2]]
        else:
            break
    return ints[0]
    
def part2(lines):
    for i in range(0, 100):
        for j in range(0, 100):
            if part1(lines.copy(), i, j) == 19690720:
                return str(i * 100 + j)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = [int(i) for i in f.read().splitlines()[0].split(",")]
    print(part1(lines.copy(), 12, 2))
    print(part2(lines.copy()))
