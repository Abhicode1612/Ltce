import math

x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]



m1 = [x[3], y[3]]
m2 = [x[6], y[6]]
k1 = []
k2 = []

for i in range(10):
    p1 = [x[i], y[i]]
    d1 = math.dist(m1, p1)
    d2 = math.dist(m2, p1)
    if d1 > d2:
        k1.append('p' + str(i))
    else:
        k2.append('p'+ str(i))

print(k1, k2)



import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
data = list(zip(x, y))
plt.scatter(x, y)
plt.show()

kmeans = KMeans(n_clusters=2)
kmeans.fit(data)

plt.scatter(x, y, c=kmeans.labels_)
plt.show()