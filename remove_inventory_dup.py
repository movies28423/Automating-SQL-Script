__author__ = 'Stephanie'

uniqueOpen = open(r'C:\Users\Stephanie\rem_dup.txt', 'r')
uniqueText = uniqueOpen.readlines()
uniqueOpen.close()
uniqueInput = []
j = -1
for line in uniqueText:
    myLine = line.strip()
    myLine = myLine.replace('&', 'and')
    if j == -1 or myLine != uniqueInput[j]:
        print myLine
        uniqueInput.append(myLine)
        j += 1
