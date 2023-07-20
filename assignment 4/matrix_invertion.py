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

import numpy as np
# import math

def rref(B, tol=1e-8, debug=False):
    A = B.copy()
    rows, cols = A.shape
    r = 0
    pivots_pos = []
    row_exchanges = np.arange(rows)
    for c in range(cols):
        if debug: print
        "Now at row", r, "and col", c, "with matrix:";
        print
        A

        ## Find the pivot row:
        pivot = np.argmax(np.abs(A[r:rows, c])) + r
        m = np.abs(A[pivot, c])
        if debug: print
        "Found pivot", m, "in row", pivot
        if m <= tol:
            ## Skip column c, making sure the approximately zero terms are
            ## actually zero.
            A[r:rows, c] = np.zeros(rows - r)
            if debug: print
            "All elements at and below (", r, ",", c, ") are zero.. moving on.."
        else:
            ## keep track of bound variables
            pivots_pos.append((r, c))

            if pivot != r:
                ## Swap current row and pivot row
                A[[pivot, r], c:cols] = A[[r, pivot], c:cols]
                row_exchanges[[pivot, r]] = row_exchanges[[r, pivot]]

                if debug: print
                "Swap row", r, "with row", pivot, "Now:";
                print
                A

            ## Normalize pivot row
            A[r, c:cols] = A[r, c:cols] / A[r, c];

            ## Eliminate the current column
            v = A[r, c:cols]
            ## Above (before row r):
            if r > 0:
                ridx_above = np.arange(r)
                A[ridx_above, c:cols] = A[ridx_above, c:cols] - np.outer(v, A[ridx_above, c]).T
                if debug: print
                "Elimination above performed:";
                print
                A
            ## Below (after row r):
            if r < rows - 1:
                ridx_below = np.arange(r + 1, rows)
                A[ridx_below, c:cols] = A[ridx_below, c:cols] - np.outer(v, A[ridx_below, c]).T
                if debug: print
                "Elimination below performed:";
                print
                A
            r += 1
        ## Check if done
        if r == rows:
            break;
    return (A, pivots_pos, row_exchanges)
n = int(input())
matrix = []
for i in range(n):
    matrix.append(input().split())
# print(matrix)
matrix = np.append(matrix,np.identity(n),axis = 1)
#matrix = input().split()
# print(matrix)
matrix = np.array(matrix, dtype=np.float64)
# print(matrix)
a = rref(matrix)
a = a[0]
# print(a)
isIdentity = []
b = []
for i in range (n):
    isIdentity.append([l for l in a[i][:n]])
    b.append([k for k in a[i][n:]])
# print(isIdentity)
# print(b)
isIdentity = np.array(isIdentity)
# assert (isIdentity.shape[0] == isIdentity.shape[1]) and np.allclose(isIdentity, np.eye(isIdentity.shape[0]))
# print(bool)
bool = np.array_equal(isIdentity,np.eye(n))
if bool:
    for i in range(n):
        b[i] = [round(k) for k in b[i]]
    # b = np.ceil(b)
    b = np.array(b,dtype=np.int64)
    # print(str(b).replace(' [', '').replace('[', '').replace(']', ''))
    # print(*[str(row)[1:-1] for row in b], sep='\n')
    for row in b:
        print(*row)
# print(bool)