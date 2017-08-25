#!/usr/bin/python3
# _*_ coding:utf-8  _*_
__author__ = 'zhangxun'
import numpy as np
import laspy
import math


K=2

def loadData(filename):
    las_file = laspy.file.File(filename, mode='r')
    coord = np.vstack((las_file.x, las_file.y, las_file.z)).transpose()
    return coord,las_file.header


def disEclud(vecA, vecB):
    return math.sqrt((vecA[0]-vecB[0])**2+(vecA[1]-vecB[1])**2 +(vecA[2]-vecB[2])**2)
    #return math.sqrt(np.power(vecA[0],vecB[0]) + np.power(vecA[1],vecB[1]) + np.power(vecA[2],vecB[2]))
def randCenter(dateset,k):
    """
    随机生成初始的质心，这里是虽具选取数据范围内的点
    :param dateset:
    :param k:
    :return:
    """
    n = np.shape(dateset)[1]
    #centroids = np.mat(np.zeros((k,n)))
    centroids = (np.zeros((k,n)))
    for j in range(n):
        minJ = min(dateset[:,j])
        #maxJ = max(dateset[:,j])
        rangeJ = float(max(dateset[:, j]) - minJ)
        print(centroids[:,j].shape)
        centroids[:, j] = minJ + rangeJ * np.random.rand(k, )
    return centroids

def KMeans(dataset, k, distMean=disEclud, createCent=randCenter):
    m = np.shape(dataset)[0]
    clusterAssment = np.mat(np.zeros((m, 2)))


    centroids = createCent(dataset, 2)

    print(dataset.shape,type(dataset))
    print(centroids.shape,type(centroids))
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            minDist = np.inf
            minIndex = -1
            for j in range(k):
                distJI = distMean(centroids[j,:],dataset[i,:])
                if distJI < minDist:
                    minDist = distJI
                    minIndex = j
            if clusterAssment[i, 0] != minIndex:
                clusterChanged = True
            clusterAssment[i, :] = minIndex, minDist**2
            print(int(clusterAssment[i, 1]))
        print(centroids)
        for cent in range(k):
            ptsInClust = dataset[np.nonzero(clusterAssment[:,0].A == cent)[0]]
            centroids[cent, :] = np.mean(ptsInClust, axis=0)
    return centroids, clusterAssment


def main():
    filename = "../data_/electric_area16.las"

    coords, las_header = loadData(filename)

    myCentroids, clustAssing = KMeans(coords, 2)
    print("debug1")
    show3d(coords, 2, myCentroids, clustAssing)

def show2d(dataset, k, cetroids, clusterAssment):
    import matplotlib.pyplot as plt
    numSamples, dim = dataset.shape
    mark = ["or", "ob", "og", "ok", "^r", "+r", "sr", "dr", "<r", "pr"]
    for i in range(numSamples):
        markIndex = int(clusterAssment[i, 1])
        print(markIndex)
        plt.plot(dataset[i,0], dataset[i, 1], mark[markIndex])

    mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']
    for i in range(k):
        plt.plot(cetroids[i, 0], cetroids[i, 1], mark[i], markersize=12)
    plt.show()
    print("finished")

def show3d(dataset, k, cetroids, clusterAssment):
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d  import Axes3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(dataset[:, 0], dataset[:, 1], dataset[:, 2], marker="o")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.scatter(cetroids[:, 0], cetroids[:, 1],cetroids[:, 2], marker="^")
    plt.show()



if __name__ == "__main__":
    main()