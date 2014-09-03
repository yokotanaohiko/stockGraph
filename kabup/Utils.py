# -*- coding: utf-8 -*-

import numpy

class Utils(object):

    def __init__(self):
        pass
    
    # 二つのリストの相関係数を返す。
    # 長さが異なる場合は、短い方に合わせる。
    @staticmethod
    def correlation_coefficient(data1,data2):
        if not isinstance(data1,list) or not isinstance(data2,list) :
            return "some argument are not lists"
        if len(data1) > len(data2) :
            return numpy.corrcoef(data1[-len(data2):],data2)[0][1] 
        if len(data2) < len(data1) :
            return numpy.corrcoef(data1,data2[-len(data1):])[0][1]
        return numpy.corrcoef(data1,data2)[0][1]

