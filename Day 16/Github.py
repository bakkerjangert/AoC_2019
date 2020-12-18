with open('input.txt') as f:
    lines = f.read().splitlines()

inputString = lines[0]
# inputString = "80871224585914546619083218645595"
inputList = []
basePattern = [0, 1, 0, -1]


def parseInput():
    global inputList
    inputList = []
    for c in inputString:
        inputList.append(int(c))


def calcNewSum(position):
    offset = position
    step = position + 1
    output = 0
    while offset < len(inputList):
        output += sum(inputList[offset:offset + step])
        offset += 2 * step

        output -= sum(inputList[offset:offset + step])
        offset += 2 * step
    return abs(output) % 10


def runPartialPhase(repeats, offset):
    global inputList
    length = len(inputList)
    for _ in range(repeats):
        newList = [0] * length
        # Last number is only relevant for the last line, others are times 0, last number will never change because of this.
        newList[length - 1] = inputList[length - 1]
        # we only need to calculate the last X numbers (in offset) because we ignore first X numbers. X - 1 because base 0
        for i in range(length - 2, offset-1, -1):
            # Number at position n-1 is the number found at position n in the new list plus the number at position n-1 in the old list.
            newList[i] = (inputList[i] + newList[i + 1]) % 10
        inputList = newList


def runPhases(repeats):
    global inputList
    for _ in range(repeats):
        newList = []
        for i in range(len(inputString)):
            newList.append(calcNewSum(i))
        inputList = newList


def partOne():
    parseInput()
    runPhases(100)
    print("".join(str(x) for x in inputList[:8]))


def partTwo():
    global inputList
    parseInput()
    offset = int(inputString[:7])
    inputList = inputList * 10000
    runPartialPhase(100, offset)
    print("".join(str(x) for x in inputList[offset:offset + 8]))


partOne()
partTwo()
