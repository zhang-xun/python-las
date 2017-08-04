#!/usr/bin/python3
# _*_ coding:utf-8  _*_
__author__ = 'zhangxun'

MAX_DATA_SET_SIZE = 256

class DataSetRegister:
    def __init__(self):
        self._Size = 0
        #memset(self._DataSets,0,Max_DATA_SET_SIZE*sizeof(DataSetPtr_t)
        self._DataSets = []

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

