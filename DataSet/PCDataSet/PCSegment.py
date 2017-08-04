#!/usr/bin/python3
# _*_ coding:utf-8  _*_
__author__ = 'zhangxun'


from DataSet.PCDataSet.Block import BlockKey3D
from  Utility.Common import GPSTmSpan
from DataSet.PCDataSet import Block
from DataSet.PCDataSet.PCContext import PCContext

class PCSegment:
    def __init__(self, sig, pOwner):
        self._SegID = sig
        self._Owner = pOwner
        self._LineTopo = None
        self._Blks = []
        self._Points = None
        self._PtSize = 0
        self._TmSpan = GPSTmSpan(0,0)
        self._FirstPoint = None
        self._IdxInterval = None

    def __del__(self):
        pass

    def CreateOctTree(self):
        """
        after read point cloud data, call this function to create oct tree
        :return:
        """
        if not self.IsDataLoaded():
            return False
        x, y, z = 0, 0, 0
        Blks = dict()
        currKey = -1
        currtBlock = None

        pt = self._Points
        for i in len(pt):
            if PCContext.instances().isBlockUseGlobalXYZ:
                x, y, z = pt[i].X(), pt[i].Y(), pt[i].Z()
            else:
                x, y, z = pt[i].x(), pt[i].y(), pt[i].z()

        Key = BlockKey3D(x,y,z)
        if Key != currKey:
            itor = Blks.find(Key)
            if itor == Blks.end():
                currtBlock = Block(x, y, z, 1, self)
                currKey = Key

                Blks[currKey] = currtBlock
            else:
                currKey = Key
                currtBlock = itor.second

        assert(currtBlock != None,"currentBlock is Noe")
        currtBlock.PointArray().append(pt)

        # 对所有顶层的block建立八叉树
        # 判断是否建立八叉树
        isCreateOctTree = PCContext.instances().isCreateBlockOctTree

        for i in range(len(Blks)-1):
            currtBlock =Blks[i+1]  #Todo
            if isCreateOctTree:
                currtBlock.CreatOctTree()  #Todo

            self._Blks.append(currtBlock)
        return True


    def CreateLineTopo(self):
        """
        after read point cloud data, call this function to create line topo
        :return:
        """
        pass

    def PointArray(self):
        pass

    def NewPointArray(self, size):
        pass

    def PtSize(self):
        return self._PtSize

    def IsDataLoaded(self):
        return self._PtSize > 0 and self._Points != None

    def BlkSize(self):
        return self._Blks.size()

    def TimeSpan(self):
        return self._TmSpan

    def segmeng_id(self):
        return self._SegID

    def Owner(self):
        return self._Owner

    def LineTopoPtr(self):
        return self._LineTopo

    def IndexInterval(self):
        return self._IdxInterval



#Todo
#typedef PCSegment* PCSegmentPtr_t;
#typedef std::vector<PCSegment> PCSegmentArray_t;
#typedef std::vector<PCsegmentPtr_t> PCSegmentPtrArray_t;