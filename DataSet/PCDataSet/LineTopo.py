#!/usr/bin/python3
# _*_ coding:utf-8  _*_
__author__ = 'zhangxun'

class LineTopoItem:
    """
    _PData: PointPtr_t
    _Time: GPSMSec_t
    _Size: unsigned int
    """
    def __init__(self, pdata=0, size=0):
        """
        construction for LineTopItem
        :param pdata:  PointPtr_t
        :param size:  unsigned int
        :return:
        """
        self._PData = pdata
        if self._PData != 0 and self._Size > 0:
            self._Time = self._PData.Time_ms()
        else:
            self._Time = 0

        self._Size = size

    def pData(self):
        return self._PData

    def Time(self):
        return self._Time

    def LastTime(self):
        lastPoint = LastPointPtr()
        if lastPoint != None:
            return lastPoint.Time_ms()
        else:
            return 0

    def Size(self):
        return self._Size

    def FirstPointPtr(self):
        """
        return the Gps time of the first point
        :return: GPSMSec_t
        """
        return self._PData  #Todo  [0]

    def LastPointPtr(self):
        """
        return the GPS time of the last point
        :return: GPSMSec_t
        """
        if self._PData != None:
            return self._PData[self._Size-1] #Todo
        else:
            return None








class LineTopo:
    def __init__(self, owner):
        self._Owner = owner
        self._Items = None

    def CreateLineTopo(self):
        pass

    def Owner(self):
        return self._Owner

    def Size(self):
        return self._Items.size()

    def FindbyTime(self, tm):
        """

        :param tm :GPTime
        :return:
        """
        pass

    def FindbyTime(self, tm):
        """

        :param tm:  GPSMSec_t
        :return:
        """

    def FindbyPoint(self, point):
        pass
