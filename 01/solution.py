directionModifier = {
    'L': -1,
    'R': 1
}

def solution1():
    input = readInput('input.txt')
    zeroCounter = 0
    startPosition = 50
    for l in input:
        direction, distance = parseCommand(l)
        startPosition += directionModifier[direction]*(distance%100)
        
        if startPosition < 0:
            startPosition = 100-abs(startPosition)
        elif startPosition >= 100:
            startPosition = startPosition - 100
        print(startPosition)
        if startPosition == 0:
            zeroCounter += 1
    print(f"Zero was hit {zeroCounter} times")
def solution2():
    input = readInput('input.txt')
    zeroCounter = 0
    extraZeros = 0
    startPosition = 50
    for l in input:
        direction, distance = parseCommand(l)
        originalPosition = startPosition
        startPosition += directionModifier[direction]*(distance%100)
        extraZeros += distance//100
        
        if startPosition < 0:
            startPosition = 100-abs(startPosition)
            if startPosition != 0 and originalPosition != 0:
                extraZeros += 1
        elif startPosition >= 100:
            startPosition = startPosition - 100
            if startPosition != 0 and originalPosition != 0:
                extraZeros += 1
        if startPosition == 0:
            zeroCounter += 1
        print(f"Ran command {l}, now at position {startPosition} with {extraZeros} extra zeros")
    print(f"Zero was hit {zeroCounter+extraZeros} times")


def parseCommand(command: str) -> tuple:
    direction = command[0]
    distance = int(command[1:])
    return direction, distance

def readInput(filename: str) -> list:
    with open(filename) as fp:
        lines = fp.read().splitlines()
    return lines

if __name__ == "__main__":
    print("running")
    solution2()