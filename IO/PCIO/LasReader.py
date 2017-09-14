#!/usr/bin/python3
# _*_ coding:utf-8  _*_
import os

__author__ = 'zhangxun'
"""
    定义Las文件格式的读取类
"""

from IO.PCIO.LasDefine import LasHeader_t, LasVLR_t, EnumLasFmt, LasFormat0, LasFormat1, LasFormat3, LasFormat2


class LasReader:
    def __init__(self, inBuffSize=1):
        """
        构造函数，默认文件缓存1M
        :param inBuffSize:
        :return:
        """
        self.GeoKeys = None  # GEoKeyDirectory
        self.Opened_ = False  # bool
        self.Header_ = None  # LasHeader_t
        self.hFile = None  # File
        self.Buff_Size_ = 0  # int
        self.Point_ = None  # LasFormat0   读取的当前点对象
        self.Point1_ = None  # LasFormat1
        self.Point2_ = None  # LasFormat2
        self.Point3_ = None  # LasFormat3
        self.VLRPtrArray = None # LasVLRPtrArray
        self.isGPSTimeAvailable_ = False
        self.isRGBAvailable_ = False

        self.BufferSize(inBuffSize)

    def __del__(self):
        if True == self.Opened_ and self.hFile is not None:
            self.Close()

    def Close(self):
        """
        关闭打开的文件
        :return:
        """
        if self.hFile is not None:
            self.hFile.close()
            self.hFile = None

        if self.Header_ is not None:
            del self.Header_
            self.Header_ = None

        if self.Point_ is not None:
            del self.Point_
            self.Point_ = None
        # Release VLR
        del self.VLRPtrArray
        self.VLRPtrArray = None
        self.GeoKeys.EntryMap.clear()

        self.isGPSTimeAvailable_ = False
        self.isRGBAvailable_ = False
        self.Opened_ = False



    def Open(self, lasFilename):
        """
        打开文件，如果该实例已经绑定了一个打开的las文件，则会自动关闭
        :param lasFilename: string
        :return:
        """
        ret = False
        if self.Opened_:
            self.Close()

        self.hFile = open(lasFilename, mode="rb", buffering=self.Buff_Size_*1024)
        if self.hFile is None:
            return False
        self.Header_ = LasHeader_t()

        #FREAD stuff Todo



        ret &= self.ReadVLS()
        self.isGPSTimeAvailable_ = False
        self.isRGBAvailable_ = False
        self.Point_ = None
        self.Point1_ = None
        self.Point2_ = None
        self.Point3_ = None

        switch_dict= {EnumLasFmt.LAS_FORMAT0:LasFormat0,
                     EnumLasFmt.LAS_FORMAT1:LasFormat1,
                     EnumLasFmt.LAS_FORMAT2:LasFormat2,
                     EnumLasFmt.LAS_FORMAT3:LasFormat3}

        switch_GPS = {EnumLasFmt.LAS_FORMAT0:False,
                     EnumLasFmt.LAS_FORMAT1:True,
                     EnumLasFmt.LAS_FORMAT2:False,
                     EnumLasFmt.LAS_FORMAT3:True}
        switch_RGB = {EnumLasFmt.LAS_FORMAT0:False,
                     EnumLasFmt.LAS_FORMAT1:False,
                     EnumLasFmt.LAS_FORMAT2:True,
                     EnumLasFmt.LAS_FORMAT3:True}

        if ret:
            self.Opened_ = True
            self.Point_ = switch_dict.get(self.LasFmt(),None)()

            self.isGPSTimeAvailable_ = switch_GPS.get(self.LasFmt())
            self.isRGBAvailable_ = switch_RGB.get(self.LasFmt())

            self.Seek(0)
        else:
            self.Close()

        return ret

    def getNextPoint(self):
        """
            获取点，返回点记录的基类
        :return: LastPoint
        """
        if self.hFile is None or self.Point_ is None:
            return None
        nSize = self.Header_.Point_Data_Record_Length
        # Todo
        # nRead = fread(Point_t, 1,nSize, hFile)
        nRead = os.read(self.hFile, nSize)

        if nSize == nRead:
            return self.Point_
        else:
            return None

    def Seek(self, nptNum):
        """
            定位到文件中的nptNum个点，点从 1 开始编号
        :param nptNum:
        :return:
        """
        if self.Opened_:
            return False
        # 越界检查
        if nptNum > self.Header_.Number_of_Point_Records:
            return False
        if nptNum == 0:
            nptNum = 1
        offset = self.Header_.Offset_to_Point_Data
        offset += self.Header_.Point_Data_Record_Length * (nptNum - 1)
        self.hFile.seek(offset, os.SEEK_SET)



    def getNextPointNum(self):
        """
            返回下一个读取点的点好，从1开始，0表示还没有读取点
        :return:
        """
        if self.Opened_:
            return 0
        offset = self.hFile.tell()
        if offset == -1:
            return 0
        ret = offset - self.Header_.Offset_to_Point_Data
        try:
            ret = ret / self.Header_.Point_Data_Record_Length
        except ZeroDivisionError:
            print("division by zero")
        return int(ret+1)

    def isOpened(self):
        """
            返回文件是否正常打开
        :return:
        """
        return self.Opened_

    def LasFmt(self):
        """
            返回打开的Las文件中点的记录个数
        :return:
        """
        if self.Header_:
            return EnumLasFmt(self.Header_.Point_Data_Format + 1)
        else:
            return "UNKNOWN"

    def RecSize(self):
        """
            返回点记录大小
        :return:
        """
        if self.Header_:
            return self.Header_.Point_Data_Record_Length
        else:
            return 0

    def Header(self):
        """
            返回las文件的header
        :return:
        """
        return self.Header_

    def BufferSize(self, buff_size):
        if buff_size < 1:
            self.Buff_Size_ = 1
        elif buff_size > 4:
            self.Buff_Size_ = 4
        else:
            self.Buff_Size_ = buff_size

    def PointNumber(self):
        """
            获得打开的Las文件中的点数，文件未打开，返回0
        :return:
        """
        if self.Header_:
            return self.Header_.Number_of_Point_Records
        else:
            return 0

    def X(self):
        """
        计算真实X坐标
        :return: double
        """
        if self.Point_ is not None:
            return self.Point_.X * self.Header_.X_Scale_Factor + self.Header_.X_Offset
        else:
            return 0.0

    def x(self, x0):
        return x0*self.Header_.X_Scale_Factor + self.Header_.X_Offset

    def Y(self):
        """
        计算真实Y坐标
        :return: double
        """
        if self.Point_ is not None:
            return self.Point_.Y * self.Header_.Y_Scale_Factor + self.Header_.Y_Offset
        else:
            return 0.0

    def y(self, y0):
        return y0*self.Header_.Y_Scale_Factor + self.Header_.Y_Offset

    def Z(self):
        """
        计算真实Z坐标
        :return: double
        """
        if self.Point_ is not None:
            return self.Point_.Z * self.Header_.Z_Scale_Factor + self.Header_.Z_Offset
        else:
            return 0.0

    def z(self, z0):
        return z0*self.Header_.Z_Scale_Factor + self.Header_.Z_Offset


    def GPSTime(self, x0):
        if self.Point1_:
            return self.Point1_.GPS_Time
        if self.Point3_:
            return self.Point3_.GPS_Time
        return 0.0

    def getRGB(self):
        if self.Point3_:
            # Todo Red << 16 | Grren << 8 | Blue
            return [self.Point3_.Red, self.Point3_.Green, self.Point3_.Blue]
        if self.Point2_:
            return [self.Point2_.Red, self.Point2_.Green, self.Point2_.Blue]
        return 0

    def getRGBI(self):
        """
         same with getGRB but with Intensity
        :return:
        """
        if self.Point3_:
            # Todo Red << 16 | Grren << 8 | Blue
            return [self.Point3_.Red, self.Point3_.Green, self.Point3_.Blue, self.Point3_.Intensity]
        if self.Point2_:
            return [self.Point2_.Red, self.Point2_.Green, self.Point2_.Blue, self.Point2_.Intensity]
        return 0


    def GPSTimeAvailable(self):
        return self.isGPSTimeAvailable_

    def RGBAvailable(self):
        return self.isRGBAvailable_

    def Intensity(self):
        if self.Point3_:
            return self.Point3_.Intensity
        elif self.Point2_:
            return self.Point2_.Intensity
        elif self.Point1_:
            return self.Point1_.Intensity
        elif self.Point_:
            return self.Point_.Intensity
        else:
            return 0

    def ReadVLS(self):
        if self.hFile is None:
            return False
        if self.Header_.Number_of_Variable_Length_Records  < 1:
            return True
        ret = os.lseek(self.hFile,self.Header_.Header_Size, os.SEEK_SET)
        if ret != 0: return False

        # 读取所有的可变长记录
        for i in range(self.Header_.Header_Size):
            vlr = LasVLR_t()
            nReadSize = 54
            nRead = fread(vlr, 1, nReadSize, self.hFile)
            if nRead != 54:
                del vlr
                return False
            nReadSize = vlr.Record_Length_After_Header
            vlr.pData = [0]*nRead
            nRead = fread(vlr.pData, 1, nReadSize, self.hFile)
            if nRead != nReadSize:
                del vlr
                return False
            self.VLRPtrArray

        # 解析投影信息

        # 关联GeoKey的值



