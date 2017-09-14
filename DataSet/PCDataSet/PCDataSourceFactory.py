#!/usr/bin/python3
# _*_ coding:utf-8  _*_
from DataSet.PCDataSet.PCDataSource import PCDataSource

__author__ = 'zhangxun'

from DataSet.Core.DataSourceFactory import IDataSourceFactory

class DataSetCore(IDataSourceFactory):
    def __init__(self):
        super().__init__()
        self._SegmentStrategy = None

    def __del__(self):
        pass

    def CreateDataSource(self):
        """

        :return: IDataSource
        """
        pSource = PCDataSource()
        pSource.Url = self._URI
        return pSource

    def SegmentStrategy(self):
        """
        设置点云数据的分段策略
        :return:
        """
        return self._SegmentStrategy


if __name__ == "__main__":
    DataSetCore()