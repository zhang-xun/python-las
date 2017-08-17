#!/usr/bin/python3
# _*_ coding:utf-8  _*_
__author__ = 'zhangxun'
from abc import abstractmethod

class IDataSourceFactory:
    def __init__(self):
        self._URI = ""

    def __del__(self):
        pass

    @property
    def URI(self, uri=None):
        return self._URI

    @URI.setter
    def URI(self, uri):
        self._URI = uri

    @abstractmethod       #TODO test
    def CreateDataSource(self):
        """
        virtual TODO
        :return:  IDataSource *
        """
        return None