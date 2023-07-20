import numpy as np
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
def farLeftPoint(points):
    min = 0
    for i in range(1, len(points)):
        if points[i].x < points[min].x:
            min = i
        elif points[i].x == points[min].x:
            if points[i].y > points[min].y:
                min = i
    return min


def orientation(p, q, r):
    checker = (q.y - p.y) * (r.x - q.x) - \
          (q.x - p.x) * (r.y - q.y)

    if checker == 0:
        return 0
    elif checker > 0:
        return 1
    else:
        return 2


def convexHull(points, n):
    if n < 3:
        return
    left = farLeftPoint(points)

    hull = []
    p = left
    while True:
        hull.append(p)
        q = (p + 1) % n
        for i in range(n):
            if orientation(points[p], points[i], points[q]) == 2:
                q = i
        p = q
        if p == left:
            break
    return hull
# n,m = [int(i) for i in input().split()]
# print(n,m)
# doneCities = []
# for i in range(n):
#     # doneCities[i] = [float(j) for j in input().split()]
#     doneCities.append([float(j) for j in input().split()])
#     # print(doneCities[i])
# k = int(input())
# undoneCities = []
# for i in range(k):
#     undoneCities.append([float(j) for j in input().split()])
# xOfCenter , yOfCenter = 0,0
# points = []
# pointsOfCountries = {}
# for i in range(n):
#     xOfCenter += doneCities[i][1]
#     yOfCenter += doneCities[i][2]
#     # pointsOfCountries[int(doneCities[i][0])].append (Point(doneCities[i][1],doneCities[i][2]))
#     # points[i] = Point(doneCities[i][1],doneCities[i][2])
#     points.append(Point(doneCities[i][1],doneCities[i][2]))
# # doneCities[i][0] ~ points[i]
# for i in range(n):
#     if doneCities[i][0] not in pointsOfCountries:
#         pointsOfCountries[doneCities[i][0]] = [points[i]]
#     else:
#         pointsOfCountries[doneCities[i][0]].append(points[i])
# xOfCenter /= n
# yOfCenter /= n
#
# # for i in range (n)
# hullOfCountries = []
# print(pointsOfCountries)
# print(pointsOfCountries[0])
# for i in range(len(pointsOfCountries)):
#     hullOfCountries.append(convex_hull(pointsOfCountries[i],len(pointsOfCountries[i])))
#
# hull = convex_hull(points,n)
# xMax , yMax , xMin, yMin = 0,0,0,0
# # for i in range (len(hull)):
# #     if (hull[i].x > xMax):
# #         xMax= hull[i].x
# #     if (hull[i].x < xMin):
# #         xMin= hull[i].x
# #     if (hull[i].y > yMax):
# #         yMax= hull[i].y
# #     if (hull[i].y < yMax):
# #         yMax= hull[i].y
# # for city in undoneCities:
# countryToCity = []
# for i in range(n):
#     distMin = 100000000
#     vector = np.array(undoneCities[i])
#     index = -1
#     for j in range(m):
#         borderVector = np.array(hullOfCountries[j])
#         dist = np.linalg.norm(borderVector-vector)
#         if(dist<distMin):
#             index = j
#     countryToCity.append(j)
#     hullOfCountries[j] = convex_hull(pointsOfCountries[j].append(undoneCities[i]))
# print(countryToCity)
# cnt = 0
# for hullOfCountrie in hullOfCountries:
#     print(cnt , hullOfCountrie)
n, m = [int(i) for i in input().split()]
donePoints = [] #donePoint[i] = [country[i],x[i],y[i]]
for i in range(n):
    donePoints.append([float(j) for j in input().split()])
    donePoints[i][0] = int(donePoints[i][0])
    # print(donePoints[-1])
k = int(input())
undoneCities = []
for i in range(k):
    undoneCities.append([float(j) for j in input().split()])
    # print(undoneCities[-1])
hullOfCountries = []
for i in range(m):
    hullOfCountries.append([])
for i in range(m):
    for j in range(n):
        if donePoints[j][0] == i:
            hullOfCountries[i].append(Point(donePoints[j][1],donePoints[j][2]))
# print([i[1].x for i in hullOfCountries] )
# print([j[1].y for j in hullOfCountries])

borderPoints = []
for i in range(m):
    borderPoints.append([])
for i in range(m):
    borderPoints[i] = (convexHull(hullOfCountries[i],len(hullOfCountries[i])))
# print(borderPoints)
# print(hullOfCountries)
# holdHullOfCountries = hullOfCountries
# for i in range(m):
#
#     # hullOfCountries[i]=[]
#     for j in range(len(borderPoints[i])):
#         # if hullOfCountries[i]
#         size = len(hullOfCountries[i])
#         hullOfCountries[i].append(hullOfCountries[i][borderPoints[i][j]])
#         hullOfCountries[i] = hullOfCountries[i][size:]
#         print(hullOfCountries[i])
# print(hullOfCountries)
# print(hullOfCountries)
# print(borderPoints)
xCenter, yCenter = 0,0
for i in range(n):
    xCenter += donePoints[i][1]
    yCenter += donePoints[i][2]
xCenter /= n
yCenter /= n
countriesToAssign = []
country = -1
for i in range(k):
    minDist = 10000000000000
    city = np.array(undoneCities[i])
    for j in range(m):
        minDistForCountry = 10000000000
        for k in range(len(borderPoints[j])):
            border = np.array([hullOfCountries[j][borderPoints[j][k]].x ,hullOfCountries[j][borderPoints[j][k]].y ])
            dist = np.linalg.norm(border - city)
            if dist < minDistForCountry:
                minDistForCountry = dist
        if minDistForCountry < minDist :
            minDist = minDistForCountry
            country = j
    countriesToAssign.append(country)
    hullOfCountries[country].append(Point(undoneCities[i][0] , undoneCities[i][1]))
    borderPoints[country] = (convexHull(hullOfCountries[country], len(hullOfCountries[country])))
toPrint = []
print(*countriesToAssign)
for i in range(m):
    toPrint.append( [])
    for j in range(len(borderPoints[i])):

        toPrint[i].append([hullOfCountries[i][borderPoints[i][j]].x,hullOfCountries[i][borderPoints[i][j]].y])
# print(toPrint)
toPrintDict = []
dic = {}
for i in range(m):
    toPrint[i].sort()
# for i in range(m):
#     toPrintDict.append()
for i in range(m):
    toPrint[i] = [i] + [j for j in toPrint[i]]
    # print(*toPrint[i])
for i in range(m):
    hold = toPrint
    # toPrint[i] = [toPrint[i][0]] + ["{:.2f}".format(k) for k in toPrint[i][1:][j] for j in toPrint[i][1:]]
    # for j in range(len(toPrint[i])):
    for j in range(len(toPrint[i])):

        if j == 0:
            toPrint[i][j] = [i]
        else:
            toPrint[i][j]=([((format(a,'.2f'))) for a in hold[i][j]])
            # toPrint[i][j] = [format(float(b),'.2f') for b in toPrint[i][j]]
            # toPrint[i][j] = [format(a,'.2f') for a in toPrint[i][j]]

    #         print(toPrint[i][j] , ends = " ")
    #     else:
    #         toPrint[i]
    # print(*toPrint[i])
for i in range(m):
    print(toPrint[i][0][0] , end = " ")
    for j in range(1,len(toPrint[i])):
        print("[" ,end="")
        # for l in range(len(toPrint[i][j])):
        print(toPrint[i][j][0],end=", ")
        print(toPrint[i][j][1],end="")
        print("]" , end= " ")
    print()
# print(*toPrint)
