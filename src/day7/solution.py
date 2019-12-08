def part1(image):
    return image
    
def part2(lines):
    return 0

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        image = f.read().splitlines()
    print(part1(image))
    print(part2(image))
