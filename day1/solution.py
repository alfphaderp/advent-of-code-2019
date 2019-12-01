def part1(lines):
    sum = 0
    for i in lines:
        sum += int(i) // 3 - 2
    return sum
    
def part2(lines):
    sum = 0
    while len(lines) > 0:
        i = int(lines.pop()) // 3 - 2
        if i > 0:
            sum += i
            lines.append(i)
    return sum

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    print(part1(lines))
    print(part2(lines))
