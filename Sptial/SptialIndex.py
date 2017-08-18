#!/usr/bin/python3
# _*_ coding:utf-8  _*_
__author__ = 'zhangxun'
"""
定义顶层块的空间索引类，用于块以及点云的快速查找
"""


class SptialIndex:
    def __init__(self):
        self._BlockMap3 = dict()      # 3d key-> 顶层块多字典
        self._BlockMap2 = dict()       # 2dkey->顶层块多字典
        self._BlockKeyList3 = []       # 3d key列表
        self._BlockKeyList2 = []       # 2d key列表


    def InsertBlock(self, pBlock):
        """
        插入一个顶层块到map中
        :param pBlock:
        :return:
        """
        if pBlock is None:
            return False
        if pBlock.Parent() is not None or pBlock.Level() > 1:
            return False
        if pBlock.Owner() is None:
            return False
        if pBlock.Owner().Owner() is None:
            return False
        if not self.ExistBlock(pBlock):
            if self._BlockMap3.find(pBlock.Key3()) == self._BlockMap3.end():
                self._BlockKeyList3.append(pBlock.Key3())
            if self._BlockMap2.find(pBlock.Key2()) == self._BlockMap2.end():
                self._BlockKeyList2.append(pBlock.Key2())

            self._BlockMap3[pBlock.Key3()] = pBlock
            self._BlockMap2[pBlock.Key2()] = pBlock
            return True
        return False

    def ExistBlock(self, pBlock):
        """
        判断map中是否包含某个顶层块
        :param pBlock:
        :return:
        """
        if pBlock is None:
            return False
        found = False
        num = self._BlockMap3.count(pBlock.Key3())
        if num > 0:
            while True:
                #Todo
                raise NotImplementedError

    def RemoveBlock(self, pBlock):
        """
        从关联表中删除指定的块
        :param pBlock:
        :return:
        """
        if pBlock is None:
            return False
        if self.ExistBlock(pBlock):
            while True:
                #Todo
                raise NotImplementedError

            while True:
                raise NotImplementedError

    def RegisterSegmentBlocks(self, pSegment):
        """
        数据注册接口 registssser
        :param pSegment:
        :return:
        """
        if pSegment is None:
            return False
        for i in range(pSegment.BlkSize()):
            self.InsertBlock(pSegment[i])
        return True

    def UnRegisterSegmentBlocks(self, pSegment):
        """
        数据注册接口 unregister
        :param pSegment:
        :return:
        """
        if pSegment is None:
            return False
        for i in range(pSegment.BlkSize()):
            self.RemoveBlock(pSegment[i])
        return True

    # 空间查询接口
    def QueryBlockbyPoint(self, pt, bufSize=0.0):
        pass

    def QueryBlockbyRay(self):
        pass