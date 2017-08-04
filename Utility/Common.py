#!/usr/bin/python3
# _*_ coding:utf-8  _*_
__author__ = 'zhangxun'

from enum import Enum

class GPSTmSpan:
    def __init__(self, start=0, end=0):
        self.s = start
        self.e = end

    def MsSpan(self):
        return self.e - self.s

    def SecSpan(self):
        return (self.e - self.s) / 1000.0


class ProjectEnum(Enum):
    NONE = 0
    GAUSS = 1
    UTM = 2


class BLH_t:
    """
    pos 中BLH
    """
    def __init__(self):
        self.B = 0.0
        self.L = 0.0
        self.H = 0.0


class Attitude_t:
    """
    pos 中的姿态
    """
    def __init__(self):
        self.heading = 0.0
        self.pitch = 0.0
        self.roll = 0.0


class Position_t:
    def __init__(self):
        self.X = 0.0
        self.Y = 0.0
        self.Z = 0.0


class Extent2D:
    def __init__(self, maxx=0, minx=0, maxy=0, miny=0):
        self.MaxX = maxx
        self.MaxY = maxy
        self.MinX = minx
        self.MinY = miny

    def Length(self):
        return self.MaxX - self.MinX

    def Width(self):
        return self.MaxY - self.MinY


class Extend3D(Extent2D):
    def __init__(self, maxx=0, minx=0, maxy=0, miny=0, maxz=0, minz=0):
        super.__init__(maxx, minx, maxy, miny)
        self.MaxZ = maxz
        self.MinZ = minz

    def Height(self):
        return self.MaxZ - self.MinZ




#Todo
#typedef std::pair<unsigned int, unsigned int> IndexInterval_t;