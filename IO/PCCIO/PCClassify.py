#!/usr/bin/python3
# _*_ coding:utf-8  _*_
__author__ = 'zhangxun'

class PCClassify:
    def __init__(self):
        self.m_hFile = None
        self.m_hMapping = None
        self.m_AccessPOS = None
        self.m_pRecords = None
        self.m_pHead = None
        self.m_Opened = None
        self.m_PCCHead = None

    def Open(self, Filename):
        pass

    def Create(self, fileName, PCNum):
        pass

    def Close(self):
        pass

    def Seek(self, PCNum):
        pass

    def WriteData(self, record, num=1):
        pass

    def ReadData(self, record, num=1):
        pass

    def GetHead(self):
        pass

    def IsOpend(self):
        pass

def main():
    pass


if __name__ == "__main__":
    main()