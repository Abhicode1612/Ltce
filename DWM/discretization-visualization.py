#Data Discretization
#  1)  Binning

# import numpy as np
# from sklearn.datasets import load_iris

# dataset = load_iris()
# a = dataset.data
# b = np.zeros (150)

# for i in range (150):
#     b[i] = a[i, 1]
#     b = np.sort(b)


# bin1 = np.zeros((30, 5))
# bin2 = np.zeros((30, 5))
# bin3 = np.zeros((30, 5))


# #Bin Mean
# for i in range(0, 150, 5):
#     k = int(1/5)
# print ("Bin Mean: \n", bin1)


# #Bin boundaries
# for i in range(0, 150, 5):
#     k = int(i/5)
#     for j in range (5):
#         if(b[i+j]-b[i]) < (b[i+4] - b[i+j]):
#             bin2[k, j] = b[i]
#         else:
#             bin2[k, j] = b[i + 4]
# print ("Bin Boundaries: \n", bin2)


# #Bin Median
# for i in range(0, 150, 5):
#     k = int(1/5)
#     for j in range (5) :
#         bin3[k, j] = b[i+2]
# print ("Bin Median: \n", bin3)


# Data Visiualization


# Scatter


# import matplotlib.pyplot as plt

# girls_attendance = [25, 28,18, 19, 21, 26, 27, 11, 25, 16]
# boys_attendance = [24, 23,12, 14, 28, 29,25, 13, 16, 19]
# days_range = [1, 2, 3, 4,5, 6, 7, 8, 9, 10]
# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
# ax.scatter (days_range, girls_attendance, color='r')
# ax.scatter (days_range, boys_attendance, color='b')
# ax.set_xlabel ("Days Range")
# ax.set_ylabel ("Comparison")
# ax.set_title("Scatterplot")
# plt.show()


# Bargraph


# import matplotlib.pyplot as plt
# studet_attendance = [25, 14, 18, 16, 21, 23, 27, 11, 25, 16]
# days_range = [1, 2, 3, 4,5, 6, 7, 8, 9, 10]
# fig= plt.figure()
# ax = fig.add_axes([0, 0,1, 1])
# ax.bar (days_range, studet_attendance, color='b' )
# ax.set_title ("Bar Graph")
# plt.show()




