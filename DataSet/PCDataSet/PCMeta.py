#!/usr/bin/python3
# _*_ coding:utf-8  _*_
__author__ = 'zhangxun'


class PCMeta:
    def __init__(self):
        self._FileSourceID = 0
        self._GlobalEncoding = 0
        self._VerMajor = 0
        self._VerMinor = 0
        self._SystemIdentifier = ""
        self._GeneratingSoftware = ""
        self._CreateDay = 0
        self._CreateYear = 0
        self._PointRecNum = 0
        self._PlatformHeight = 0
        self._DevX_Offset = 0
        self._DevY_Offset = 0
        self._DevZ_Offset = 0
        self._Dev_Alph = 0
        self._Dev_Beta = 0
        self._Dev_Gama = 0
        self._LineFrequency = 0
        self._AngleResolution = 0
        self._LiDARPosition = ""
        self._AngleError = 0
        self._Max_X = 0
        self._Min_X = 0
        self._Max_Y = 0
        self._Min_Y = 0
        self._Max_Z = 0
        self._Min_Z = 0

    def FileSourceID(self):
        return self._FileSourceID

    def GlobalEncoding(self):
        return self._GlobalEncoding

    def VerMajor(self):
        return self._VerMajor

    def VerMinor(self):
        return self._VerMinor

    def SystemIdentifier(self):
        return self._SystemIdentifier

    def GeneratingSoftware(self):
        return self._GeneratingSoftware

    def CreateDay(self):
        return self._CreateDay

    def CreateYear(self):
        return self._CreateYear

    def PointRecNumber(self):
        return self._PointRecNum

    def PlatformHeight(self):
        return self._PlatformHeight

    def DevX_Offset(self):
        return self._DevX_Offset

    def DevY_Offset(self):
        return self._DevY_Offset

    def DevZ_Offset(self):
        return self._DevZ_Offset

    def Dev_Alph(self):
        return self._Dev_Alph

    def Dev_Beta(self):
        return self._Dev_Beta

    def Dev_Gama(self):
        return self._Dev_Gama

    def LineFrequency(self):
        return self._LineFrequency

    def AngleResolution(self):
        return self._AngleResolution

    def LiDARPosition(self):
        return self._LiDARPosition

    def AngleError(self):
        return self._AngleError


















#typedef PCMeta* PCMetaPtr_t;