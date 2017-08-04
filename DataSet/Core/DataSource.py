#!/usr/bin/python3
# _*_ coding:utf-8  _*_
__author__ = 'zhangxun'


class IDataSource:
    def __init__(self):
        self._url = ""
        self.opened_ = False
        # friend class IDataSet
        # friend class IDataSetFactory

    def Open(self):
        return True

    def Close(self):
        return True

    def isOpend(self):
        return True

    def setUrl(self, url):
        self._url = url

    def getUrl(self):
        return self._url

