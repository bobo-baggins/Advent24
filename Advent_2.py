
RprtLst = [] #A list of list, indivual elements are levels from each report which is a list onto itself
SfeCnt = 0 # Int storing count of safe reports
DngrLvl = 0
Diff = []
ShftLst = []
with open('Advent_2_input.txt', 'r') as file:
    for line in file:
        Report = line
        LvlLst = [int(lvl) for lvl in Report.split()]
        RprtLst.append(LvlLst)

for Report in RprtLst:
    Diff.clear()
    ShftLst.clear()
    DngrLvl = 0

    for j in range(len(Report)-1):
        Diff.append(Report[j+1]-Report[j])

    for index, i in enumerate(Diff):
        if i == 0:
             ShftLst.append(0)
        else:
            ShftLst.append( 1 ) if i > 0 else ShftLst.append(-1)

        if abs(i) > 3 or i == 0:
                DngrLvl += 1
                continue
    if abs(sum(ShftLst)) < len(Diff)-1 and DngrLvl > 1:
         DngrLvl += 1

    if DngrLvl == 2 or DngrLvl == 3:
        print(Report)
        print(Diff)
        print(ShftLst)
        print(DngrLvl)
    if DngrLvl < 2:
        SfeCnt +=1

print(SfeCnt)
