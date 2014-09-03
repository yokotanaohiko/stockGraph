# -*- coding :utf-8 -*-
from meigara import Stock
import math
import numpy
class Analysis(object) :
    def __init__(self) :
        self.spanS = 25 
        self.spanM = 75
        self.spanL = 150
        pass

    def movingAv(self,stock,span=7) :
        ma = []
        try :
            tmp = map(float,stock.getClosingPriceList())
            for i in range(stock.span) :
                if i < span :
                    ma.append(0)
                else :
                    ma.append(round(numpy.average(tmp[i-span:i]),1))
        except ValueError :
            print(stock.getStockNum())
            print(stock.getClosingPriceList())

        return ma

    def highLowAv(self,stock,span=26) :
        hla = []
        try :
            high = map(float,stock.getHighPriceList())
            low = map(float,stock.getLowPriceList())
        except ValueError:
            pass



    def goldenX(self,stock):
        maS = self.movingAv(stock,self.spanS)
        maM = self.movingAv(stock,self.spanM)
        return self.upperX(maS[-len(maM):],maM)
       
    def deadX(self,stock):
        maS = self.movingAv(stock,self.spanS)
        maM = self.movingAv(stock,self.spanM)
        return self.lowerX(maS[-len(maM):],maM)

    @staticmethod
    def upperX(seq1,seq2) :
        if len(seq2)==0 :
            return -1
        if len(seq1) != len(seq2) :
            print("seq1="+str(len(seq1))+",seq2="+str(len(seq2)))
            raise Exception

        length = len(seq1)
        sq1 = seq1[::-1]
        sq2 = seq2[::-1]
        for i in range(length-1) :
            if sq1[i] > sq2[i] and sq1[i+1] <= sq2[i] :
                return i

        return -1

    @staticmethod
    def lowerX(seq1,seq2) :
        if len(seq1) != len(seq2) :
            raise Exception

        length = len(seq1)
        sq1 = seq1[::-1]
        sq2 = seq2[::-1]
        for i in range(length-1) :
            if sq1[i] < sq2[i] and sq1[i+1] >= sq2[i] :
                return i

        return -1

