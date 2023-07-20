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
from scipy import linalg
import numpy as np
vec1 = [float(x) for x in input().split()]
vec2 = [float(x) for x in input().split()]
# toepForm = linalg.toeplitz(vec1)
# toepForm = np.array(toepForm)
# print(toepForm)
# vec2 = np.array(vec1)
# padding = np.zeros(vec2.shape[0] - 1, vec2.dtype)
# first_col = np.r_[vec2, padding]
# first_row = np.r_[vec2[0], padding]
#
# H = linalg.toeplitz(first_col, first_row)
# print(H)
# H = np.transpose(H)
# result = np.dot(H,vec2)
# print(H)
# print(result)
# result = np.dot(toepForm,vec2)
#
# print(result)
if len(vec2) > len(vec1):
    hold = np.array(vec1)
    vec1 = np.array(vec2)
    vec2 = hold

m = len(vec1)
n = len(vec2)
tpForm = []



# for i in range(m+n-1):
#     tpForm.append([])
#     # for j in range(n):
#     #     tpForm[i].append(0)
#
#     if i<m-1:
#         cnt = i
#         while(cnt>=0 and len(tpForm[i]) < n):
#             tpForm[i].append(vec1[cnt])
#             cnt -= 1
#         for ll in range(n-(i+1)):
#             tpForm[i].append(0)
#     if (i == m-1):
#         for j in range(i+1):
#             if len(tpForm[i])<n:
#                 tpForm[i].append(vec1[i-j])
#     if(i>m-1):
#         for r in range(i-(m-1)):
#             tpForm[i].append(0)
#         for k in range(m+n-i-1):
#             tpForm[i].append(vec1[m-1-k])
# print(tpForm)
# tpForm = np.array(tpForm ,dtype=np.int64)
# # print(tpForm)
# result = np.array([int(x) for x in np.dot(tpForm,vec2)])
#
# # np.set_printoptions(formatter={'float': lambda x: "{0:0.1f}".format(x)})
# print("[" ,*result,"]")




mat=[]
zeroList = []
for i in range(n):
    zeroList.append(0)
for i in range(m+n-1):
    mat.append(zeroList)
# print(mat)
mat2 = []
for i in range(m+n-1):
    if(i<=m-1):
        # if i>0:
        #     mat[i] = mat[i-1]
        #     test1 = 0
        # test2 = 0
        mat[i] =[vec1[i]] + mat[i]
        mat[i+1] = mat[i]
    else :
        mat[i] = [0]+ mat[i]
        if i != m+n-2:
            mat[i+1] = mat[i]
    mat2.append(mat[0])
    # print(mat)
for i in range(m+n-1):
    mat[i] = mat[i][:n]
# mat = mat[:][:n]
# print(mat)
mat = np.array(mat)
result = [int(x) for x in np.dot(mat,vec2)]
print('[',*result,']')
# print(mat2)