def getPath(moves):
    path = {}
    x, y = 0, 0
    count = 0;
    for i in moves:
        for j in range(0, int(i[1::])):
            count += 1
            if i[0] == 'L':
                x -= 1;
            elif i[0] == 'R':
                x += 1;
            elif i[0] == 'U':
                y += 1;
            elif i[0] == 'D':
                y -= 1;
            path[(x, y)] = count
    return path

def part1(line1, line2):
    inter = getPathSet(line1).intersection(getPathSet(line2))
    return min(abs(x) + abs(y) for x, y in inter.keys())
    
def part2(lines):
    d1, d2 = getPath(line1), getPathSet(line2)
    minimum = 1e99
    for k, v in d1.items():
        if k in d2:
            if v + d2[k] < minimum:
                minimum = v + d2[k]
    return minimum

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    line1 = lines[0].split(",")
    line2 = lines[1].split(",")
    # print(part1(line1, line2))
    print(part2(lines))
