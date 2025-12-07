
def solution2():
    input = readInput('input.txt')
    answer = 0
    for pair in input:
        start, end = map(int, pair.split('-'))
        pairs = checkRepeatingInRange(start, end)
        print(f"Pairs between {start} and {end}: {pairs}")
        answer += sum(pairs)
    print(f"Final answer: {answer}")

def checkRepeatingInRange(start: int, end: int) -> list:
    pairs = []
    for num in range(start, end+1):
        strNum = str(num)
        #print(f"Checking number {num}")
        if checkRepeatingNumbers(strNum):
            pairs.append(num)
        
    return pairs
    
def checkRepeatingNumbers(num: str) -> bool:
    for i in range(1, len(num)//2+1):
        #print(f"Checking window size {i} for number {num} | window is {num[:i]}")
        startWindow = num[:i]
        pairFlag = True
        for j in range(i, len(num), i):
            nextWindow = num[j:j+i]
            if startWindow != nextWindow:
                #print(f"Failed at {startWindow} and {nextWindow} for number {num}")
                pairFlag = False
        if pairFlag:
            #print(f"Found repeating pattern {startWindow} for number {num}")
            return True
    return False

def solution1():
    input = readInput('input.txt')
    answer = 0
    for pair in input:
        start, end = map(int, pair.split('-'))
        pairs = checkPairsInRange(start, end)
        print(f"Pairs between {start} and {end}: {pairs}")
        answer += sum(pairs)
    print(f"Final answer: {answer}")

def checkPairsInRange(start: int, end: int) -> list:
    pairs = []
    for num in range(start, end+1):
        strNum = str(num)
        if len(strNum)%2 != 0:
            continue
        if strNum[:len(strNum)//2] == strNum[len(strNum)//2:]:
            pairs.append(num)
    return pairs

def readInput(filename: str) -> list:
    with open(filename) as fp:
        lines = fp.read().splitlines()
    return lines[0].split(',')

if __name__ == "__main__":
    print("running")
    solution2()
    print(checkRepeatingNumbers("2121212121"))