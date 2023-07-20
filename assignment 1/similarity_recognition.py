# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
import numpy as np
# a = []
# a.append(4)
# a.append(3)
# a.append("i")
# a.append(4)
# print(a)
n = int(input())
allInputs = []
inputs = []
for i in range (n):
    para = input()
    # print(para)
    inputs.append(para.split())
    # print(inputs)
    # list = para.split()
    # d={}
    # for i in para.split(): d[i] = i in d
    # for i in range()
    # list = [k for k in d if not d[k]]  # unordered, loop over the dictionary
    # [k for k in l if not d[k]]
    # list =
    # print(list)
    # allInputs += [j for j in para.split() if j not in allInputs]
    # a = True
    for m in range(len(inputs)):
        for j in range(len(inputs[m])):
            if inputs[m][j] not in allInputs:
                allInputs.append(inputs[m][j])
    # for m in range(len(allInputs)):
    #     for j in range (len(para.split())):
    #         if(allInputs[m] == para.split()[j]):
    #             a= False

    # print(allInputs)
# allInputs = [i for i in allInputs if allInputs.count(i) < 20]
# print(inputs , allInputs)
vectors = [None] * len(inputs)
for i in range (len(inputs)):
    vectors[i] = []
    for j in range (len(allInputs)):

        # vectors.append()
        vectors[i].append(inputs[i].count(allInputs[j]))

# print(vectors)
# max = [None] * len(inputs)
# for r in range (len(max)):
#     max[r] = 0
for r in range(len(vectors)):
    vectors[r] = np.array(vectors[r] , dtype=np.int64)
    # vectors[r] /= np.linalg.norm(vectors[r])
vectors = [i/np.linalg.norm(i) for i in vectors]

# print(vectors , len(allInputs))
# vectors = [np.array(vectors[i]) for i in vectors]
# vectors[0] = np.dot(vectors[1],vectors[2])
# print(vectors)
for r in range(len(vectors)):
    maxIndex = 0
    max = -1
    for l in range(0,len(vectors)):
        if(l != r):
            d = np.dot(vectors[r], vectors[l])
            if (max < d):
                max = d
                maxIndex = l+1
            # if (max[l] < d):
            #     max[l] = r+1
        # print(max[r] , max[l])
    print(maxIndex)
# print(vectors , max)
# print(max)
# for i in range (len(max)):
#     print(max[i])