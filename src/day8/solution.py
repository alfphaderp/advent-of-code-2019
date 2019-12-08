def part1(image):
    layers = []
    for i in range(0, len(image), 25 * 6):
        layers.append(image[i:i + 25 * 6])
    minZ, minZLayer = 1e99, []
    for l in layers:
        if l.count("0") < minZ:
            minZLayer = l
            minZ = l.count("0")
    return minZLayer.count("1") * minZLayer.count("2")
    
def part2(image, r, c):
    layers = []
    for i in range(0, len(image), r * c):
        rows = []
        for j in range(0, r * c, r):
            rows.append(image[i + j:i + j + r])
        layers.append(rows)
    
    print(layers)
    final = []
    for i in range(c):
        row = []
        for j in range(r):
            for k in range(len(layers)):
                print(k, i, j)
                if layers[k][i][j] != "2":
                    row.append(layers[k][i][j])
                    break
        final.append("".join(row))
        
    return "\n".join(final)
    

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        image = f.read().splitlines()[0]
    print(part1(image))
    print(part2(image, 25, 6))
