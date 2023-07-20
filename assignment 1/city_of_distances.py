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
# #
# import numpy
import numpy as np
n = int(input())
a = np.ones((n,) ,dtype=np.int64)
state = True
# print(a)
q =int(input())
for i in range(q):
    order = input()
    orderSplit = order.split()
    if(orderSplit[0] == "T"):
        # a = np.transpose(a)
        state = not state
    elif (orderSplit[0] == "dot"):
        # orderSplit = order.split()
        if (len(orderSplit) == a.size +1):
        # print(len(orderSplit) , orderSplit)
            if(not state):
                orderSplit.pop(0)
                for j in range(len(orderSplit)):
                    orderSplit[j] = int(orderSplit[j])
                b = np.array(orderSplit,dtype=np.int64)
                # b= b.reshape((n,1))
                # print(b)
                print(np.dot(a,b))
    elif(orderSplit[0] == "out"):
        # orderSplit = order.split()
        # if(len(orderSplit) == a.size+3):
            if(state):
                orderSplit.pop(0)
                k = int(orderSplit[-1])
                # print(k)
                orderSplit.pop(-1)
                orderSplit.pop(-1)
                for j in range(len(orderSplit)):
                    orderSplit[j] = int(orderSplit[j])
                b=np.array(orderSplit,dtype=np.int64)
                c = np.outer(a,b)
                # print(c , np.shape(c)[0])
                # if(k <= np.shape(c)[0]):
                a = c[k-1]
                    # print(a)
                state = False
                # print (a)

    elif(orderSplit[0] == "cross"):
        if(a.size == 3):
            # orderSplit = order.split()
            orderSplit.pop(0)
            for j in range(len(orderSplit)):
                orderSplit[j] = int(orderSplit[j])
            b = np.array(orderSplit,dtype=np.int64)
            b = np.cross(a,b)
            norm = np.linalg.norm(b)
            for j in range(len(b)):
                b[j] = float( b[j]/norm)

            for x in b :
                print("{0:.4f}".format(x) , end = " ")
            print()
    elif(orderSplit[0] == "had"):
        # orderSplit=order.split()
        if(len(orderSplit) == a.size+1):
            # orderSplit=order.split()
            orderSplit.pop(0)
            for j in range(len(orderSplit)):
                orderSplit[j] = int(orderSplit[j])
            b = np.array(orderSplit,dtype=np.int64)
            a = np.multiply(a,b)
    # elif(order)
    elif(orderSplit[0] == "print"):
        # print(a , a.shape , a.shape[0])
        if(state):
            # print(np.shape(a))
            for j in range(a.size):
                print(a[j])
        else:
            # print(' '.join((map(str, [int(i) for i in a[0]]))))
            for x in a:
                print(x , end=" ")
            print()
    elif(orderSplit[0] == "reset"):
        # orderSplit = order.split()
        orderSplit.pop(0)
        # state = True
        # for j in range(len(orderSplit)):
        #     orderSplit[j] = int(orderSplit[j])
        v = int(orderSplit[0])
        a= np.ones((v,),dtype=np.int64)



