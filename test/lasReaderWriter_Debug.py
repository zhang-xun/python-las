#!/usr/bin/python3
# _*_ coding:utf-8  _*_
# @Time    : 9/12/17 1:39 AM
# @Author  : 'zhangxun'
# @Email   : 15025689012@163.com
# @File    : lasReaderWriter_Debug.py.py
# @Software: PyCharm

import datetime
import struct
from IO.PCIO.LasDefine import LasFormat0
from IO.PCIO.LasReader import LasReader
from IO.PCIO.LasWriter import LasWriter
import laspy

FILENAME = '/Users/zhangxun/code/tensorflow_code/tensorflow_for_pole/data/readertest.las'
FILENAME2 = '/Users/zhangxun/code/tensorflow_code/tensorflow_for_pole/data/pole_extraction/data1/electric_area1.las'


def main2():
    reader = LasReader()
    # LasWriter()
    reader.Open(FILENAME)
    ret = reader.Seek(1)
    print("ret:1", ret)
    pid = reader.getNextPointNum()
    print("pid:1", pid)
    pt = reader.getNextPoint()
    print("pt:1", pt)
    pid = reader.getNextPointNum()
    print("pid:2", pid)
    pt = reader.getNextPoint()
    print("pt:2", pt)

    x, y, z = reader.X(), reader.Y(), reader.Z()
    print("x:{}\ty:{}\tz:{}".format(x, y, z))

    ret = reader.Seek(100)
    print("ret3:", ret)
    pid = reader.getNextPointNum()
    print("pid3:", pid)
    pt = reader.getNextPoint()
    print("pt3:", pt)

    reader.Seek(1)
    pt = reader.getNextPoint()
    starttime = datetime.datetime.now()
    #count the calculate time
    s = []
    count = 0
    while pt is not None:
        x, y, z = reader.X(), reader.Y(), reader.Z()
        s.append(pt)
        print("x:{}\ty:{}\tz:{} count:{}".format(x, y, z, count))
        pt = reader.getNextPoint()
        count += 1
    pid = reader.getNextPointNum()
    print("pid:", pid)
    endtime = datetime.datetime.now()
    interval = (endtime - starttime).seconds
    print("interval time:{}".format(interval))
    reader.Close()


def test_struct():
    tmpref = open(FILENAME, "rb")
    tmpref.seek(104)
    fmt = int(struct.unpack("<B", tmpref.read(1))[0])
    compression_bit_7 = (fmt & 0x80) >> 7
    compression_bit_6 = (fmt & 0x40) >> 6

    if (not compression_bit_6 and compression_bit_7):
        compressed = True
    else:
        compressed = False
    tmpref.close()
    print(compression_bit_7, compression_bit_6, compressed)

def main():
    a = laspy.file.File(FILENAME2,mode="r")
    a.visualize()

if __name__ == "__main__":
    main()
    #test_struct()