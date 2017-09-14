#!/usr/bin/python3
# _*_ coding:utf-8  _*_
from DataSet.PCDataSet.Point import Point_t

__author__ = 'zhangxun'

from DataSet.Core.DataSource import IDataSource
from DataSet.PCDataSet.PCMeta import PCMeta
from IO.PCIO.LasReader import LasReader
from IO.PCIO.TopReader import TopReader
from Utility.Common import GPSTmSpan
from DataSet.PCDataSet.PCContext import PCContext, PCCXTOBJ
from IO.PCCIO.PCClassify import PCClassify


class PCDataSource(IDataSource):
    def __init__(self):
        super().__init__()
        self._LasReader = LasReader()
        self._TopReader = TopReader()
        self._TopUrl = ""
        self._PCClass = PCClassify()
        self._TmSpan = None
        self._FirstPoint = None
        self._LasPoint = None


    def __del__(self):
        pass

    def Open(self):
        if self._LasReader is None:
            self._LasReader.Close()
            # Todo
            # python delete object and assign to None
            del self._LasReader
            self._LasReader = None
        self._LasReader = LasReader()
        if self._LasReader.isOpened():
            self.opened_ = True
            X1,Y1,Z1,X2,Y2,Z2,X,Y,Z = 0,0,0,0,0,0,0,0,0
            Tm1, Tm2 = None, None
            if self._LasReader.Seek(1):
                X1 = self._LasReader.X()
                Y1 = self._LasReader.Y()
                Z1 = self._LasReader.Z()
                Tm1 = int(self._LasReader.GPSTime()*1000.0 + 0.5)
            else:
                #Todo del and None
                del self._LasReader
                self._LasReader = None
                self.opened_ = False
                return False

            if self._LasReader.Seek(self._LasReader.PointNumber()):
                self._LasReader.getNextPoint()
                X2 = self._LasReader.X()
                Y2 = self._LasReader.Y()
                Z2 = self._LasReader.Z()
                Tm2 = int(self._LasReader.GPSTime()*1000.0 + 0.5)
            else:
                #Todo del None
                del self._LasReader
                self._LasReader = None
                self.opened_ = False
                return False

            X, Y, Z= (X1+X2)/2.0, (Y1+Y2)/2.0, (Z1+Z2)/2.0

            if PCCXTOBJ.GOffsetX == 0.0 and PCCXTOBJ.GOffsetY == 0.0:
                PCCXTOBJ.GOffSetX = (int(X/1000))*1000
                PCCXTOBJ.GOffsetY = (int(X/1000))*1000
                PCCXTOBJ.GOffsetZ = 0.0

                #Todo
                Point_t.X_Offset = PCCXTOBJ.GOffsetX
                Point_t.Y_Offset = PCCXTOBJ.GOffsetY
                Point_t.Z_Offset = PCCXTOBJ.GOffsetZ

            self._FirstPoint.XYZ(X1,Y1,Z1)
            self._FirstPoint._Time = Tm1
            self._LastPoint.XYZ(X2,Y2,Z2)
            self._LastPoint._Time = Tm2

            self._TmSpan = GPSTmSpan(Tm1, Tm2)

            self._LasReader.Seek(1)
            return True


    def Close(self):
        if self._LasReader is not None:
            self._LasReader.Close()
            #Todo del None
            del self._LasReader
            self._LasReader = None
        if self._TopReader is not None:
            self._TopReader.Close()
            #Todo del None
            del self._TopReader
            self._TopReader = None
        self.opened_ = False
        return True


    def isOpend(self):
        return self.opened_

    def OpenTop(self, url):
        if self._LasReader is None or not self._LasReader.isOpened():
            return False
        if self._TopReader is not None:
            self._TopReader.Close()
            #Todo
            del self._TopReader
            self._TopReader = None

        if url != "":
            self._TopUrl = url
        if self._TopUrl == "" and self._url != "":
            #Todo
            pass

        self._TopReader = TopReader()
        if (self._TopReader.Open(self._TopUrl)):
            if self._TopReader.Header() is not None:
                if self._TopReader.Header().DataRecCnt == self._LasReader.Header().Number_of_Point_Records:
                    return True

        del self._TopReader
        self._TopReader = None
        return False


    def OpenClass(self, url=""):
        """
        open .cls file
        :param url:
        :return:
        """
        if self._PCClass.IsOpened():
            return True
        classFile = url
        if classFile == "":
            classFile = self._url
            #Todo
            # replace _url (.las) to (.cls)
        else:
            # replace _url (.las) to (.cls)
            pass

        bOK = self._PCClass.Open(classFile)
        if not bOK:
            if self._LasReader is None:
                bOK = self._PCClass.Create(classFile,self._LasReader.PointNumber())
        return bOK


    def updataClass(self, buffer, idxs):
        if idxs.first > idxs.second:
            return False
        if not self.OpenClass():
            return False
        if idxs.first > 0 :
            idxs.first -= 1
        if idxs.second > 0:
            idxs.second -= 1

        self._PCClass.Seek(idxs.first)
        uSize = idxs.second - idxs.first + 1
        p = buffer  # PointPtr_t
        pccr = None # PointCloudClassify_R
        while uSize > 0:
            pccr.Class = p.Class()
            pccr.FID = p.FID()
            if self._PCClass.WriteData(pccr) != 1:
                return False
            uSize -= 1
            p += 1
        self.closeClass()
        return True
    
    def closeClass(self):
        self._PCClass.Close()

    @property
    def TopUrl(self):
        return self._TopUrl

    @property.setter
    def TopUrl(self, value):
        self._TopUrl = value

    def ReadMetaInfo(self, pMeta:PCMeta):
        # Todo
        # 把源数据填入参数中
        pass

    def FillPointBuffer(self, buffer, idxs, srcID, withTopo, withClass):
        # 填充点缓存， buffer缓存base地址， 读入的数量为idxs.second - idxs.first
        # idxs文件索引起止， withtopo是否读入拓扑信息
        # withClass 是否读入分类信息，
        ret = 0
        # Todo

        # 参数检查

        # 文件检查是否打开

        # 数据定义

        # 数据转换比例


        # 读取每一个点记录


        # 读取拓扑信息

        # 待补充Class相关代码




        return ret

    def FirstPoint(self):
        return self._FirstPoint

    def LastPoint(self):
        return self._LasPoint

    def TimeSpan(self):
        # Todo
        # OSG
        return self._TmSpan

    def GetPointbyIndex(self, idx, out):
        # 读取指定索引的点，只填入了XYZ和时间信息
        if self._LasReader is None and not self._LasReader.isOpened():
            return False
        if not self._LasReader.Seek(idx):
            return False

        # Todo
        # memset out
        # LasFormat0
        return False

    def GetPointbyTime(self, tm, out):
        t = PCMeta(out)

        # 文件是否打开


        # 二分查找

        pass


if __name__ == '__main__':
    PCDataSource()