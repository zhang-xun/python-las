#!/usr/bin/python3
# _*_ coding:utf-8  _*_
__author__ = 'zhangxun'

import ctypes

MAX_DATA_SET_SIZE = 256

class DataSetRegister:
    """
    数据集管理器在每一个具体的数据集类型中定义，用于管理数据集的ID
    由一个256数组构成，每种类型的数据最多支持255个，ID为0表示为分配id，1-255表示有效id
    数据集注册在IDataSet的析构函数和构造函数中实现，需要在IDataSet中定义类变量—_Register,
        并实现虚函数: Register()
    """
    def __init__(self):
        self._Size = 0
        self._DataSets = ctypes.py_object * MAX_DATA_SET_SIZE

    def Register(self, ds):
        if ds == None:
            return False
        if self._Size >= 255:
            return False

        for i in range(1, 256):
            if self._DataSets[i] == ds:
                return False
        for j in range(1, 256):
            if self._DataSets[j] == None:
                self._DataSets[j] = ds
                ds.Dsid(j)
                self._Size += 1
                return True

        return False

    def UnRegister(self, ds):
        if ds == None:
            return False
        if self._Size == 0:
            return False
        for i in range(1,256):
            if self._DataSets[i] == ds and ds.Dsid() == i:
                self._DataSets[i] == None
                self._Size -= 1
                ds.Dsid(0)
                return True
        return False

    @property
    def Size(self):
        return self._Size

    @property
    def GetDataSets(self):
        return self._DataSets



