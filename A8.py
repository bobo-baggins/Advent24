def ProcessGrid(FileName, FreqId):
    with open(FileName, 'r') as file:
        for i, line in enumerate(file):
            line = line.strip()  # Remove whitespace/newlines
            for j, char in enumerate(line):
                if char == ".":
                    continue
                if char not in FreqId:
                    FreqId[char] = []
                FreqId[char].append((i, j))
#    print(FreqId)
    return FreqId

def CalcAntinode(FreqId):
    for key in FreqId.keys():
        print(key)

def Main():
    FileName = "A8_Test.txt"
    FreqId = {}

    FreqId = ProcessGrid(FileName, FreqId)

    CalcAntinode(FreqId)
 

if __name__ == "__main__":
    Main()


