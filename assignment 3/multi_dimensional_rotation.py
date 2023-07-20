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
from math import sin , cos
n = int(input())
listOfInput = []
for i in range(int(n)):
    listOfInput.append(input().split())
angles = np.array(input().split(),dtype=np.float64)
listOfInput = np.array(listOfInput,dtype=np.float64)
# print(listOfInput)
# print(angles)
# rotationMatrix = []
rot = np.array([[cos(angles[2])*cos(angles[1]), cos(angles[2])*sin(angles[1])*sin(angles[0])-sin(angles[2])*cos(angles[0]) , cos(angles[2])*sin(angles[1])*cos(angles[0]) + sin(angles[2])*sin(angles[0])]
                   , [sin(angles[2])*cos(angles[1]), sin(angles[2])*sin(angles[1])*sin(angles[0])+cos(angles[2])*cos(angles[0]) , sin(angles[2])*sin(angles[1])*cos(angles[0]) - cos(angles[2])*sin(angles[0])]
                   ,[-sin(angles[1]),cos(angles[1])*sin(angles[0]),cos(angles[1])*cos(angles[0])]])

result = []
for i in range(n):
    result.append(np.dot(rot, listOfInput[i]).tolist())
# print(result)
for i in range(n):
    result[i] = [(round(e, 1)) for e in result[i]]
    # result[i] = np.array(result[i])
# print(result)
result = np.array(result , dtype=float)
# result = result.astype(.2%f float)
# print(result)
np.set_printoptions(formatter={'float': lambda x: "{0:0.1f}".format(x)})
print(result)
# print(np.around(result,3))