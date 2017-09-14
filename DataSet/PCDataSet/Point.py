#!/usr/bin/python3
# _*_ coding:utf-8  _*_
__author__ = 'zhangxun'
import ctypes
import  laspy   # TODO
import  numpy as np # TODO

class Point_t:
    def __init__(self):
        self._xyz = ctypes.py_object * 3   # 偏移后的局部坐标
        self._rgbi = 0   # 颜色与强度值
        self._Time = 0   # 采集该点的GPS时间，ms
        self._Angle = 0  # 扫描角度
        self._PrePoint = 0  # 前一个点数据是否是由前一条激光产生的
        self._NextPoint = 0  # 后一个点数据是否是由后一条激光产生的
        self._Flag = 0  # 标记
        self._ReturnNum = 0  # 同一激光的回波总数，最大7
        self._ReturnSerial = 0  # 该点是第几次回波
        self._LineStartFlag = 0  # 该点是否为行开始点
        self._LineEndFlag = 0  # 该点是否为行结束点
        self._SrcID = 0   # 包含该点的源文件ID，0：该点不在任何文件中，1-255，文件编号
        self._Dist = 0  # 测距, 单位cm
        self._Class = 0  # 分类
        self._FID = 0  # 要素ID，0：未分类，非0：Feature ID
        self._ProfileDist = 0  # 侧方向距离，单位cm，abs(平台坐标系中的X值)
        self._GroundHeight = 0  # 地面高，单位cm，平台坐标系中的Z值+IMU的地面高 short
        self._LinePre = 0  # 行间前一个点的偏移，PrePtr  = PtPtr - LinePre,
        self._LineNext = 0  # 行间后一个点的偏移，NextPtr = PtPtr + LineNext
        self.X_Offset = 0.0  # 点云坐标全局偏移
        self.Y_Offset = 0.0  # 点云坐标全局偏移
        self.Z_Offset = 0.0  # 点云坐标全局偏移

    @property
    def X(self):
        return self.X_Offset + self._xyz[0]

    @X.setter
    def X(self, x:float)  -> float:
        self._xyz[0] = x - self.X_Offset

    @property
    def Y(self, y=None):
        return self.Y_Offset + self._xyz[1]

    @Y.setter
    def Y(self, y=None):
        self._xyz[1] = y - self.Y_Offset

    @property
    def Z(self, z=None):
        return self.Z_Offset + self._xyz[2]

    @Z.setter
    def Z(self, z=None):
        self._xyz[2] = z - self.Z_Offset

    def XYZ(self,x,y,z):
        self._xyz[0] = x - self.X_Offset
        self._xyz[1] = y - self.Y_Offset
        self._xyz[2] = z - self.Z_Offset

    def XYZ(self,xyzlist):
        if isinstance(xyzlist, list) and len(xyzlist) == 3:
            self._xyz[0] = xyzlist[0] - self.X_Offset
            self._xyz[1] = xyzlist[1] - self.Y_Offset
            self._xyz[2] = xyzlist[2] - self.Z_Offset
        else:
            raise ValueError("xyzlist must a list")

    def xyz(self):
        return self._xyz

    def x(self):
        return self._xyz[0]

    def y(self):
        return self._xyz[1]

    def z(self):
        return self._xyz[2]

    def R(self):
        pass

    def G(self):
        pass

    def B(self):
        pass

    def I(self):
        pass

    def RGBI(self):
        return self._rgbi

    def Time_ms(self):
        return self._Time

    def Time_s(self):
        return self._Time / 1000.0

    def SID(self):
        return self._SrcID

    def SID(self, sid):
        self._SrcID = sid

    def Angle(self):
        return self._Angle

    def Dist_cm(self):
        return self._Dist

    def Dist_m(self):
        return self._Dist / 100.0

    def ProfileDist_cm(self):
        return self._ProfileDist

    def ProfileDist_m(self):
        return self._ProfileDist / 100.0

    def GroundHeight_cm(self):
        return self._GroundHeight

    def GroundHeight_m(self):
        return self._GroundHeight / 100.0

    def Class(self,cls=None):
        if cls is None:
            return self._Class
        else:
            self._Class = cls

    def FID(self,fid=None):
        if fid is None:
            return self._FID
        else:
            self._FID = fid

    def PreLine(self):
        return self._LinePre

    def NextLine(self):
        return self._LineNext

    def PrePoint(self):
        return self._PrePoint

    def NextPoint(self):
        return self._NextPoint

    def ReturnNum(self):
        return self._ReturnNum

    def ReturnSerial(self):
        return self._ReturnSerial

    def isLineFirstPoint(self):
        return self._LineStartFlag

    def isLineLastPoint(self):
        return self._LineEndFlag

    def Flag(self,flag=None):
        if flag is None:
            return self._Flag
        else:
            self._Flag = flag << 5
            #_Flag = flag & 0X3FFFFF;


#Todo
#typedef std::vector<PointPtr_t> PointPtrArray_t; // 点云指针数组
#typedef std::vector<Point_t>	PointArray_t;


def CompPointbyZ(a, b):
    return a.z() < b.z()


#点属性过滤实验
# Todo
#raise NotImplementedError
class AttriHeightStrist:
    def __init__(self):
        self.ValType = 0.0



class AttriDistStrist:
    def __init__(self):
        pass



class OperLess:
    def __init__(self):
        pass


class OperGreater:
    def __init__(self):
        pass


class OperBetween:
    def __init__(self):
        pass

