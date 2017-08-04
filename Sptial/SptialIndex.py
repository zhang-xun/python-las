#!/usr/bin/python3
# _*_ coding:utf-8  _*_
__author__ = 'zhangxun'


class SptialIndex:
    def __init__(self):
        self._BlockMap3 = dict()
        self._BlockMap2 = dict()
        self._BlockKeyList3 = []
        self._BlockKeyList2 = []


    def InsertBlock(self, pBlock):
        if pBlock is None:
            return False
        if pBlock.Parent() != None or pBlock.Level() > 1:
            return False
        if pBlock.Owner() == None:
            return False
        if pBlock.Owner().Owner() == None:
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
        if pBlock is None:
            return False
        found = False
        num = self._BlockMap3.count(pBlock.Key3())
        if num > 0:
            while True:
                #Todo
                raise NotImplementedError

    def RemoveBlock(self, pBlock):
        if pBlock is None:
            return False
        if self.ExistBlock(pBlock):
            while True:
                #Todo
                raise NotImplementedError

            while True:
                raise NotImplementedError

    # 数据注册接口
    def RegisterSegmentBlocks(self, pSegment):
        if pSegment is None:
            return False
        for i in range(pSegment.BlkSize()):
            self.InsertBlock(pSegment[i])
        return True

    def UnRegisterSegmentBlocks(self, pSegment):
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