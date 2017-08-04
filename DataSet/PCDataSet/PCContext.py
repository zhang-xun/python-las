#!/usr/bin/python3
# _*_ coding:utf-8  _*_
__author__ = 'zhangxun'


class PCContext:
    def __init__(self):
        self.GOffSetX = 0.0
        self.GOffsetY = 0.0
        self.GOffsetZ = 0.0
        self.isCreateBlockOctTree = True  # 顶层块下是否建立八叉树,默认建立
        self.isBlockSortbyHeight = True  # 块中是否按照高程值排序，默认排序
        self.isBlockUseGlobalXYZ = True  # Block中使用全局XYZ坐标进行计算Key值，否则使用偏移后的值

        self.nSegmentSize = 1  # 分段大小，单位M
        self._SptailIndex = None
        self._Inst = None

    def instances(self):
        if self._Inst is None:
            return PCContext()
        else:
            return self._Inst

    def Sptial(self):
        return self._SptailIndex