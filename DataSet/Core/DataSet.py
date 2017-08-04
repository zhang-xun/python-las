#!/usr/bin/python3
# _*_ coding:utf-8  _*_
__author__ = 'zhangxun'

from enum import Enum

class DataSetType_t(Enum):
    DATASET_TYPE_UNKNOWN = 0
    DATASET_TYPE_PANOIMAGE = 1
    DATASET_TYPE_POINTCLOUD = 2
    DATASET_TYPE_POS = 3
    DATASET_TYPE_DMI = 4
    DATASET_TYPE_MARKER = 5

class IDataSet:
    def __init__(self):
        self._pSource = None
        self._Name = ""
        self._Alias = ""
        self._DataSetType = DataSetType_t.DATASET_TYPE_UNKNOWN
        self._DSID = 0

    def __del__(self):
        self.Destroy()


    def Name(self, name=None):
        if name is None:
            return self._Name
        else:
            self._Name = name

    def Alias(self, alias=None):
        if alias is None:
            return self._Alias
        else:
            self._Alias = alias

    def Dsid(self, m_dsid=None):
        if m_dsid is None:
            return self._DSID
        else:
            self._DSID = dsid

    def DataSetType(self):
        return self._DSID

    def setDataSource(self, pSource):
        if self._pSource != None:
            del self._pSource           #may be wrong
            self._pSource = None
        self._pSource = pSource

    def getDataSource(self):
        return self._pSource

    def ReadData(self):
        if self._pSource == None:return False
        if not self._pSource.isOpened():
            self._pSource.Open()
        if not self._pSource.isOpened():
            return False
        #Todo in subclass
        return True

    def Destroy(self):
        if self._pSource != None:
            del self._pSource           #may be wrong
            self._pSource = None

    def Register(self):
        return None


#Todo
#typedef IDataSet *DataSetPtr_t;