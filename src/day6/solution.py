def part1(lines):
    parents = {}
    for i in lines:
        parents[i[1]] = i[0]
    count = 0
    for k, v in parents.items():
        count += 1
        while v in parents:
            count += 1
            v = parents[v]
    return count
    
def part2(lines):
    parents = {}
    for i in lines:
        parents[i[1]] = i[0]
    myParentsDists = {}
    current = "YOU"
    dist = 0
    while current in parents:
        myParentsDists[current] = dist
        dist += 1
        current = parents[current]
        
    current = "SAN"
    dist = 0
    while current not in myParentsDists:
        dist += 1
        current = parents[current]
    
    print(dist + myParentsDists[current] - 2)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = [i.split(")") for i in f.read().splitlines()]
    print(part1(lines))
    print(part2(lines))
