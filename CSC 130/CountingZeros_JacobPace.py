numList = []
counter = 0
for i in range(1,1000000,1):
    numList.append(i)
numStr = str(numList)
for n in numStr:
    countZeros = int(str(n.count("0")))
    counter += countZeros
print(counter)

# test
