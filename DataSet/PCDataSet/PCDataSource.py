#!/usr/bin/python3
# _*_ coding:utf-8  _*_
__author__ = 'zhangxun'

from DataSet.Core.DataSource import IDataSource
from DataSet.PCDataSet.PCMeta import PCMeta
from IO.PCIO.LasReader import LasReader
from IO.PCIO.TopReader import TopReader

class PCDataSource(IDataSource):
    def __init__(self):
        self._LasReader = LasReader()
        self._TopReader = TopReader()
        self._url = ""
        self._PCClass = None
        self._TmSpan = None
        self._FirstPoint = None
        self._LasPoint = None


    def __del__(self):
        pass

    def Open(self):
        pass

    def Close(self):
        pass

    def isOpend(self):
        pass

    def OpenTop(self, url):
        pass

    def OpenClass(self, url):
        pass

    def updataClass(self, buffer, idxs):
        pass

    def closeClass(self):
        pass

    @property
    def TopUrl(self):
        pass

    @property.setter
    def TopUrl(self):
        pass

    def ReadMetaInfo(self, pMeta):
        pass

    def FillPointBuffer(self, buffer, idxs, srcID, withTopo, withClass):
        pass

    def FirstPoint(self):
        pass

    def LastPoint(self):
        pass

    def TimeSpan(self):
        pass

    def GetPointbyIndex(self, idx, out):
        pass

    def GetPointbyTime(self, tm, out):
        t = PCMeta(out)

