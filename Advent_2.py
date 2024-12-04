import pdb

RprtLst = [] #A list of list, indivual elements are levels from each report which is a list onto itself
SfeCnt = 0 # Int storing count of safe reports
Flg = [0,0] #Tracks if levels in report are ascending or descing
Safe = 0
Diff = []
with open('Advent_2_input.txt', 'r') as file:
    for line in file:
        Report = line
        LvlLst = [int(lvl) for lvl in Report.split()]
        RprtLst.append(LvlLst)

for Report in RprtLst:
    Diff.clear()

    for j in range(len(Report)-1):
        Diff.append(Report[j]-Report[j+1])

    for index, i in enumerate(Diff):
        if index == 0:
            Flg = [0,0] if i < 0 else [1,1]
        if index != 0:
            Flg[1] = 0 if i < 0 else 1
            print(i) 
            print(Flg)
            if Flg[1] != Flg[0]:
                break
        if abs(i) > 3 or i == 0:
            safe = 0
            break
        SfeCnt +=1

print(SfeCnt)
