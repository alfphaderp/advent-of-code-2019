def adjSame(num):
    s = str(num)
    for i in range(0, len(s) - 1):
        if s[i] == s[i + 1]:
            return True
    return False

def increasing(num):
    s = str(num)
    for i in range(0, len(s) - 1):
        if s[i + 1]  < s[i]:
            return False
    return True

def part1(nums):
    count = 0
    for i in range(nums[0], nums[1]):
        if adjSame(i) and increasing(i):
            count += 1
    return count
    
def hasDouble(num):
    for i in range(0, 10):
        count = 0
        for j in str(num):
            if int(j) == i:
                count += 1
        if count == 2:
            return True
    return False
    
def part2(nums):
    count = 0
    for i in range(nums[0], nums[1]):
        if adjSame(i) and increasing(i) and hasDouble(i):
            count += 1
    return count

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        nums = [int(i) for i in f.read().splitlines()[0].split("-")]
    print(part1(nums))
    print(part2(nums))
