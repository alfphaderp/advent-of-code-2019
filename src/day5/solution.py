def configParams(mem, params, mode):
    for i in range(0, len(params)):
        if mode[i] == 0:
            params[i] = mem[i]
    return params

def add(mem, params, mode):
    params = configParams(mem, params, mode)
    mem[params[2]] = mem[params[0]] + mem[params[1]]
    
def mult(mem, params, mode):
    params = configParams(mem, params, mode)
    mem[params[2]] = mem[params[0]] * mem[params[1]]
    
def input(mem, params, mode):
    mem[params[0]] = 1

def output(mem, params, mode):
    print("OUTPUT" + str(mem[params[0]]))

paramLengths = {
    1: 3,
    2: 3,
    3: 1,
    4: 1
}

opcodes = {
    1: add,
    2: mult,
    3: input,
    4: output
}

def compute(ints):
    programCounter = 0
    while(True):
        params = []
        codeWithMode = str(ints[programCounter])
        code = int(codeWithMode[-2::])
        if code == 99:
            break
        mode = str(codeWithMode[:-2]).zfill(paramLengths[code])
        for i in range(1, paramLengths[code] + 1):
            params.append(ints[programCounter + i])
        opcodes[code](ints, params, mode)
        programCounter += 1 + paramLengths[code]

def part1(ints):
    compute(ints)
    
def part2(lines):
    return 0

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = [int(i) for i in f.read().splitlines()[0].split(",")]
    part1(lines.copy())
    print(part2(lines.copy()))
