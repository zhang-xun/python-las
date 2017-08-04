#!/usr/bin/python3
# _*_ coding:utf-8  _*_
__author__ = 'zhangxun'


class IDataSourceFactory:
    def __init__(self):
        self._URI = ""

    def URI(self, uri=None):
        if uri is None:
            return self._URI
        else:
            self._URI = uri

    def CreateDataSource(self):
        """
        virtual TODO
        :return:  IDataSource *
        """
        return None