import numpy as np
# import math
k,m,n = input().split()

listOfM = []
for i in range(int(m)):
    listOfM.append(input().split())


votedCondidates = input().split()
votedCondidates = np.array(votedCondidates)
listOfM = np.array(listOfM,dtype=np.float64)
# print(votedCondidates)
result = []
# distList = []

for i in range(int(n)):
    vector = np.array(input().split(), dtype=np.float64)
    mHold = listOfM
    mHold = mHold - vector
    distList = np.sum(mHold ** 2, axis=1)
    args = distList.argpartition(int(k))[:int(k)]
    cntList = votedCondidates[args]
    cntList = np.array(cntList, dtype=np.int64)
    maxArg = np.bincount(cntList).argmax()
    result.append(maxArg)
print(*result)