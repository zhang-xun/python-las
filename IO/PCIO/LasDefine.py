#!/usr/bin/python3
# _*_ coding:utf-8  _*_
# __author__ = 'zhangxun'


"""
    定义Las文件格式的基本数据结构
"""

from collections import namedtuple
from enum import Enum


# 点数据格式0， 20字节
class LasPoint0_tag:
    def __init__(self):
        self.X = 0
        self.Y = 0
        self.Z = 0    # 点内坐标， 实际坐标=x*scale+offset
        self.Intensity = 0  # 反射强度
        # Todo  with    (unit8 return :3???)
        self.Return_Number = 0      # 反射数
        self.Number_of_Returns_of_Given_Pulse = 0 # 该点属于第几波回波
        self.Scan_Direction_Flag = 0    # 扫描方向：以前进方向为准， 1代表从左向右扫描， 0 代表从右向左扫描
        self.Edge_of_Flight_Line = 0    # 扫描边沿旗标，1：它是飞机改变航向前的扫描的最后一个点
        self.Classfication = 0          # 分类
        self.Scan_Angle_Rank = 0        # 扫描角度  -90-90
        self.User_Data = 0              # 用户数据
        self.Point_Source_ID  = 0       #点源id


class LasPoint1_tag(LasPoint0_tag):
    def __init__(self):
        super().__init__()
        self.GPS_Time = 0.0


class LasPoint2_tag(LasPoint0_tag):
    def __init__(self):
        super().__init__()
        #Todo with 255bit
        self.Red = 0  # Todo
        self.Green = 0 # Todo
        self.Blue = 0 # Todo


class LasPoint3_tag(LasPoint0_tag):
    def __init__(self):
        super().__init__()
        self.GPS_Time = 0.0
        self.Red = 0  # Todo
        self.Green = 0 # Todo
        self.Blue = 0 # Todo

LasPoint0_t = LasPoint0_tag
LasPoint1_t = LasPoint1_tag
LasPoint2_t = LasPoint2_tag
LasPoint3_t = LasPoint3_tag

LasFormat0 = LasPoint0_t
LasFormat1 = LasPoint1_t
LasFormat2 = LasPoint2_t
LasFormat3 = LasPoint3_t


class EnumLasFmt(Enum):
    UNKNOWN = 0
    LAS_FORMAT0 = 1
    LAS_FORMAT1 = 2
    LAS_FORMAT2 = 3
    LAS_FORMAT3 = 4


# 变长记录格式
class LasVLR_Tag:
    def __init__(self):
        self.Reserved = 0
        self.User_id = []
        self.Record_ID = 0
        self.Record_Length_After_Header = 0
        self.Description = []
        self.pData = None
        # Todo
        # memo pData

    def __del__(self):
        if self.pData is not None:
            del self.pData
            self.pData = None

LasVLRPtrArray = []

LasVLR_t = LasVLR_Tag
LasVLRPtrArray = []


class LasVLR_Geo_Keys_tag:
    def __init__(self):
        self.key_directiory_version = 0
        self.key_revision = 0
        self.minor_revision = 0
        self.number_of_keys = 0

LasVLR_Geo_Keys_t = LasVLR_Geo_Keys_tag

class LasVLR_Key_Entry_tag:
    def __init__(self):
        self.key_id = 0
        self.tiff_tag_location = 0
        self.count = 0
        self.value_offset = 0


LasVLR_Key_Entry_t = LasVLR_Key_Entry_tag

# Todo
# LasVLRPtrArray  * pointer



class KeyEntry_t:
    def __init__(self):
        self.KeyID = 0
        self.ValueType = 0
        self.usValue = 0
        self.dValue = 0.0
        self.strValue = ""
        self.TIFFTagLocation = 0
        self.Count = 0
        self.Value_offset = 0




class GeoKeyDirectory:
    def __init__(self):
        self.KeyEntrys = {}

    def add(self, ent):
        """

        :param ent:  KeyEntry_t
        :return: bool
        """
        self.KeyEntrys[ent.KeyID] = ent
        return True

    def Size(self):
        return len(self.KeyEntrys)

    def Exist(self, KeyID):
        if KeyID in self.KeyEntrys:
            return True
        else:
            return False

    def Remove(self, KeyID):
        return self.KeyEntrys.pop(KeyID, False)

    def Item(self, KeyID):
        """

        :param KeyID:
        :return: KeyEntry_t
        """
        return self.KeyEntrys.get(KeyID,None)


    def EntryMap(self):
        return self.KeyEntrys


class LasHeader_tag:
    """
    Las 文件头数据结构

    """

    def __init__(self, inBufferSize=1):
        # 文件标签 “LASF”
        self.File_Signature = "LASF"
        self.File_Source_Id = 0  # 文件源ID，如果该文件有一个原始航线获取，文件ID为航线号
        self.Global_Encoding = 0  # 全局编码，http://wenku.baidu.com/link?url=hhUSaaBdPZeK00uyKIvhB6zxQ-hXxtSDygKuBxqhxiXBLLKotaSlW94w2oMTWYVgL_wFXKwrJWYDSlWrAfgQpxcdGiOt6YLwVZLMl6fIaJi
        self.Project_ID_GUID_Data_1 = 0  # 项目全球编码
        self.Project_ID_GUID_Data_2 = 0
        self.Project_ID_GUID_Data_3 = 0
        self.Project_ID_GUID_data_4 = [0]*8
        self.Version_Major = 1  # 主版本号：1
        self.Version_Minor = 2  # 次版本号：2
        self.System_Identifier = "MODIFICATION"  # "DCQMMS" "MERGE" "MODIFICATION" "EXTRACTION" "TRANSFORMATION" "OTHER"
        self.Generating_Software = "DCQ MMS X1"  # "DCQMMS X1"
        self.File_Creation_Day_of_Year = 0  # 生产日期：年内天
        self.File_Creation_Year = 0  # 生成年
        self.Header_Size = 0  # Todo 公共文件头区大小，单位字节
        self.Offset_to_Point_Data = 512  # 第一个点相对于文件起始的偏移
        self.Number_of_Variable_Length_Records = 0  # 点数据之前的变成记录数
        self.Point_Data_Format = 0  # 目前支持0-4
        self.Point_Data_Record_Length = 0  # Todo 每个点记录的长度，单位字节
        self.Number_of_Point_Records = 0  # 点记录的个数
        self.Number_of_Points_by_Return = [0]*5  # 各回波点数统计，最大5回波
        self.X_Scale_Factor = 0.01  # 点的X坐标的比例因子,坐标=记录值*X_Scale_Factor+X_Offset
        self.Y_Scale_Factor = 0.01
        self.Z_Scale_Factor = 0.01
        self.X_Offset = 0.0
        self.Y_Offset = 0.0
        self.Z_Offset = 0.0
        self.Max_X = 0.0
        self.Min_X = 0.0
        self.Max_Y = 0.0
        self.Min_Y = 0.0
        self.Max_Z = 0.0
        self.Min_Z = 0.0

    def __del__(self):
        pass

    def setVersion(self, major, minor):
        assert major == 1 and (minor == 1 or minor == 2 or minor == 3), "Version Error in LasHeader_tag"
        self.Version_Major = major
        self.Version_Minor = minor

    def setScale_Factory(self, scale):
        self.X_Scale_Factor = self.Y_Scale_Factor = self.Z_Scale_Factor = scale

LasHeader_t = LasHeader_tag
LasHeader = LasHeader_t

