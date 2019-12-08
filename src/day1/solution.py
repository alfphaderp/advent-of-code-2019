def part1(lines):
    return sum([i // 3 - 2 for i in lines])

def part1Alt(lines):
    sum = 0
    for i in lines:
        sum += i // 3 - 2
    return sum

def part2(lines):
    sum = 0
    for i in lines:
        while i > 0:
            i = i // 3 - 2
            if i > 0:
                sum += i
    return sum

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = [int(i) for i in f.read().splitlines()]
    print(part1(lines))
    print(part1Alt(lines))
    print(part2(lines))
