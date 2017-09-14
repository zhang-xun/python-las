#!/usr/bin/python3
# _*_ coding:utf-8  _*_
__author__ = 'zhangxun'

from enum import Enum
from abc import ABCMeta, abstractmethod


class DataSetType_t(Enum):
    DATASET_TYPE_UNKNOWN = 0
    DATASET_TYPE_PANOIMAGE = 1
    DATASET_TYPE_POINTCLOUD = 2
    DATASET_TYPE_POS = 3
    DATASET_TYPE_DMI = 4
    DATASET_TYPE_MARKER = 5


class IDataSet:
    def __init__(self):
        """
        _pSource : IDataSource * 数据源
        _Name : 数据源的名称
        _Alis : 数据集的别人
        _DSID : DataSetID_t  数据源运行时的ID
        _DataSetType : 数据源类型
        :return:
        """
        self._pSource = None
        self._Name = ""
        self._Alias = ""
        self._DataSetType = DataSetType_t.DATASET_TYPE_UNKNOWN
        self._DSID = 0

    def __del__(self):
        self.Destroy()

    @property
    def Name(self):
        """
        获取数据集的名称
        """
        return self._Name

    @Name.setter
    def Name(self, name):
        self._Name = name

    @property
    def Alias(self):
        """
        获取数据集的别名
        """
        return self._Alias

    @Alias.setter
    def Alias(self, alias):
        self._Alias = alias

    @property
    def Dsid(self):
        """
        获取数据集的内部id, 0-255,该id是该数据集在内部数组中的索引
        0:表示还未分配的无效索引，还没有加入到数据集管理器中
        """
        return self._DSID

    @Dsid.setter
    def Dsid(self, m_dsid=None):
        self._DSID = m_dsid

    def DataSetType(self):
        """
        数据集类型，在子类中初始化
        :return:
        """
        return self._DSID

    @abstractmethod
    def setDataSource(self, pSource):
        if self._pSource != None:
            del self._pSource  # TODO may be wrong
            self._pSource = None
        self._pSource = pSource

    @property
    def DataSetType(self):
        return self._DataSetType



    @abstractmethod
    def getDataSource(self):
        return self._pSource

    @abstractmethod
    def ReadData(self):
        if self._pSource == None: return False
        if not self._pSource.isOpened():
            self._pSource.Open()
        if not self._pSource.isOpened():
            return False
        # Todo in subclass
        return True

    @abstractmethod
    def Destroy(self):
        if self._pSource is not None:
            del self._pSource  # TODO may be wrong
            self._pSource = None

    @abstractmethod
    def Register(self):
        return None


        # Todo
        #typedef IDataSet *DataSetPtr_t;


