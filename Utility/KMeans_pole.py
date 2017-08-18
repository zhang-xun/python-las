#!/usr/bin/python3
# _*_ coding:utf-8  _*_
__author__ = 'zhangxun'
import numpy as np
import laspy
import math

K=2

def loadData(filename):
    las_file = laspy.file.File(filename,"r")
    coord = np.vstack((las_file.x, las_file.y, las_file.z)).transpose()
    return coord

def disEclud(vecA, vecB):
    return math.sqrt((vecA[0]-vecB[0])**2+(vecA[1]-vecB[1])**2 +(vecA[2]-vecB[2])**2)

def randCenter(dateset,k):
    """
    随机生成聚类的质心
    :param dateset:
    :param k:
    :return:
    """




def main():
    filename = "./electric_area16.las"
    coords = loadData(filename)



if __name__ == "__main__":
    main()