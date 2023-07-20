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

def eig_vals(A: np.matrix , iter : int) -> np.array:
    for i in range(iter):
        q,r = np.linalg.qr(A)
        A = np.dot(r,q)
    return A.diagonal()

a = np.matrix(input())
a =np.array(a,dtype=np.float64)
a = eig_vals(a,1000)
a =np.array(a,dtype=np.float64)
a = np.sort(a)[::-1]


# print(a)
# diagonals = a.diagonal()
# diagonals = np.array(*diagonals[0][0])
# print(diagonals)
# diagonals = diagonals.tolist()
# print(diagonals)
# diagonals.sort(reverse = True)
np.set_printoptions(formatter={'float':lambda x:"{0:0.2f}".format(x)})
a = ["{:.2f}".format(x) for x in a]
# format_float = "{:.2f}".format(x)
print(*a)
# print(*diagonals[0])
# print(b)
# print(*b[0])