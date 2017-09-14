#!/usr/bin/python3
# _*_ coding:utf-8  _*_
__author__ = 'zhangxun'
"""
    定义Block， 该类实现点云的八叉树索引， 对象在Segment中构建
    由owner管理生命周期
"""

def BlockKey3D(x,y,z):
    pass


def BlockKey3DX(key):
    pass


def BlockKey3DY(key):
    pass


def BlockKey3DZ(key):
    pass


def BlockKey3DXYZ(key, x, y, z):
    pass


def BlockKey2D(x, y):
    pass


def BlockKey2DX(key):
    pass


def BlockKey2DY (key):
    pass


def BlockKey2DXY(key, x, y):
    pass


class Block:
    def __init__(self, X, Y, Z, level, Owner):

        self._Key2d = None
        self._Owner = Owner
        self._Parent = None
        self._subBlks = []
        self._Array = []
        self._X = X
        self._Y = Y
        self._Z = Z
        self._Key3d = BlockKey3D(self._X, self._Y, self._Z)
        self._CellSize = 0
        self._Level = level

    def Key3(self):
        return self._Key3d

    def Key2(self):
        return self._Key2d

    def Owner(self):
        return self._Owner

    def Parent(self):
        return self._Parent

    def PointArray(self):
        return self._Array

    def CellSize(self):
        return self._CellSize

    def Level(self):
        return self._Level
