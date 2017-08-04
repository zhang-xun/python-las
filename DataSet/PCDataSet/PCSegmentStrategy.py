#!/usr/bin/python3
# _*_ coding:utf-8  _*_
__author__ = 'zhangxun'


class PCSegmentStrategy:
    """
    点云的分段策略类: 等时模式，指定时间模式， 点云数量相同模式
    """
    def __init__(self,mode=2,modevalue=1000000):
        self._Mode = mode
        self._ModeValue = modevalue
        #Todo

    def __init__(self, obj):
        self._Mode = obj._Mode
        self._ModeValue = obj._ModeValue


    def IsEqualTimeMode(self):
        return self._Mode == 0

    def IsSpeficTimeSpanMode(self):
        return self._Mode == 1

    def IsEqualPointNumMode(self):
        return self._Mode == 2

    def setEqualTimeSpanValue(self, timeSpan):
        self._Mode = 0
        self._ModeValue = timeSpan

    def getEqualTimeSpanValue(self):
        pass

    def setEqualPointNumValue(self, PtNum):
        self._Mode = 2
        self._ModeValue = PtNum

    def getEqualPointNumValue(self):
        return self._ModeValue

    def setSpeficTimeSpanValue(self):
        pass

    def getSpeficTimeSpanValue(self):
        pass

    