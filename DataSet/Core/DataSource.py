#!/usr/bin/python3
# _*_ coding:utf-8  _*_
__author__ = 'zhangxun'


class IDataSource:
    def __init__(self):
        self._url = ""
        self.opened_ = False
        #Todo
        # friend class IDataSet
        # friend class IDataSetFactory

    def Open(self):
        return True

    def Close(self):
        return True

    def isOpend(self):
        return True

    @property
    def Url(self):
        return self._url

    @Url.setter
    def Url(self, url):
        self._url = url

