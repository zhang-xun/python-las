#!/usr/bin/python3
# _*_ coding:utf-8  _*_
__author__ = 'zhangxun'
from DataSet.Core.DataSet import IDataSet
from Utility.Common import GPSTmSpan
from DataSet.PCDataSet.PCContext import  PCContext
from DataSet.PCDataSet.PCMeta import  PCMeta
from DataSet.PCDataSet.PCDataSource import PCDataSource

class PCDataSet(IDataSet):
    _Register = None
    def __init__(self):
        super().__init__()

        self._pContext = PCContext()
        self._PMeta = None
        self._Segments = None
        self._SupportTopo = False
        self._IsSortByHeight = False
        self._TopUrl = ""
        self._SegmentStrategy = None
        self._tmSpan = GPSTmSpan(0,0)
        self._FirstPoint = None
        self._LastPoint = None

    def setDataSource(self, pSource):
        super().setDataSource(pSource)

    def getDataSource(self):
        return self._pSource

    def ReadData(self):
        pPCSource = PCDataSource(self._pSource)
        if pPCSource is None:return False
        if (not pPCSource.isOpened()):
            pPCSource.Open()
        if not pPCSource.isOpened():return False
        # Topo are the configure file of las file
        # same name but different suffix
        self._SupportTopo = pPCSource.openTop()
        if(self._PMeta is None):
            self._PMeta = PCMeta()
        pPCSource.ReadMetaInfo(self._PMeta)

        self._FirstPoint = pPCSource.FirstPoint()
        self._LastPoint = pPCSource.LastPoint()
        self._tmSpan = pPCSource.TimeSpan()

    def Destroy(self):
        super().Destroy()

    def Register(self):
        super().Register()

    def PCMetaPtr(self):
        return self._PMeta

    def Meta(self):
        pass

    def LoadSegmentData(self,segID):
        pass

    def UnLoadSegmentData(self,segID,updateClassify):
        pass

    def UnLoadSegmentArray(self):
        pass

    def Size(self):
        return self._Segments.size()

    def SupportTopo(self):
        return self._SupportTopo

    def IsSortbyHeight(self):
        return self._IsSortByHeight

    def setTopUrl(self, url):
        self._TopUrl = url

    def setSegmentStrategy(self, strategy):
        self._SegmentStrategy = strategy

    def getSegmentStrategy(self):
        return self._SegmentStrategy

    def DeleteSegmentArray(self):
        pass

    def CanReCreateSegment(self):
        pass

    def FirstPoint(self):
        return self._FirstPoint

    def LastPoint(self):
        return self._LastPoint

    def TimeSpan(self):
        return self._tmSpan





if __name__ == "__main__":
    t = PCDataSet()