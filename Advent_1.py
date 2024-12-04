# Create two list to store each column of the numbers

Left = []
Right = []
Diff = []
Similarity = []
# Open file where input is stored

with open('Advent1.txt', 'r') as file:
    for line in file:
        values = line.split()
        Left.append(int(values[0]))
        Right.append(int(values[1]))

Left.sort()
Right.sort()

x = 0


for i in range(len(Left)):
    #Diff.append(abs(Left[i] - Right[i]))
    for j in range(len(Right)):
        if Left[i] == Right[j]: x=x+1
    print(x)
    Similarity.append(Left[i]*x)
    x = 0

print(sum(Diff))
print(sum(Similarity))
