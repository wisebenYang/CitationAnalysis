#coding=utf-8
'''
Created on 2018��3��13��

@author: Administrator
'''
from __future__ import division
import numpy as np

def getConfScore(c):
    c2m = [([0]* 36)for i in range(36)]
    for i in range( len(c) ):
        for j in range(len(c)):
            if c[i] <= c[j]:
                c2m[i][j] = 0
            else:
                c2m[i][j] = 1
    return c2m


def getConfRank(c):
    c2m = [([0]* 36)for i in range(36)]
    for i in range( len(c) ):
        for j in range(len(c)):
            if c[i] <= c[j]:
                c2m[i][j] = 1
            else:
                c2m[i][j] = 0
    return c2m

def getJourScore(c):
    c2m = [([0]* 42)for i in range(42)]
    for i in range( len(c) ):
        for j in range(len(c)):
            if c[i] <= c[j]:
                c2m[i][j] = 0
            else:
                c2m[i][j] = 1
    return c2m

def getJourRank(c):
    c2m = [([0]* 42)for i in range(42)]
    for i in range( len(c) ):
        for j in range(len(c)):
            if c[i] <= c[j]:
                c2m[i][j] = 1
            else:
                c2m[i][j] = 0
    return c2m

def getCompareMatrixConf():
    arrCOREConf = [ 22, 3, 43, 117, 5, 29, 27, 11, 64, 40, 510, 21, 145, 134, 133, 106, 4, 343, 97, 480, 492, 191, 203, 205, 516, 221, 265]
    arrGUIDEConf = [ 5, 26, 2, 1, 16, 50, 4, 99, 103, 158, 11, 157, 23, 3, 124, 92, 73, 35, 55, 117, 328, 153, 287, 95, 282, 116, 45]
    arrGIIConf = [ 24, 23, 35, 53, 21, 33, 29, 45, 47, 61, 116, 922, 49, 50, 177, 136, 44, 275, 92, 111, 919, 960, 427, 217, 446, 198, 70]
    arrThingHuaConf = [ 34, 32, 140, 33, 40, 30, 35, 139, 149, 148, 144, 145, 141, 143, 142, 147, 150, 280, 296, 282, 285, 287, 290, 291, 283, 293, 295]
    arrAminerConf = [ 6, 13, 8, 1, 10, 20, 7, 49, 59, 38, 5, 47, 12, 57, 48, 35, 93, 72, 30, 33, 89, 43, 90, 26, 69, 44, 70]
    arrCCFConf = [ 4, 1, 7, 3, 8, 6, 5, 9, 18, 17, 13, 14, 10, 12, 11, 16, 19, 21, 37, 23, 26, 28, 31, 32, 24, 34, 36]
    arrThisPaperConf = [ 3.27 , 2.04 , 2.97 , 3.32 , 2.63 , 2.17 , 3.22 , 2.94 , 2.46 , 2.48 , 2.47 , 2.57 , 2.75 , 2.90 , 1.77 , 1.98 , 1.23 , 1.67 , 2.36 , 1.85 , 1.46 , 2.23 , 1.06 , 1.67 , 1.52 , 1.49 , 2.24]
    arrCOREConf2 = getConfRank(arrCOREConf) 
    arrGUIDEConf2 = getConfRank(arrGUIDEConf) 
    arrGIIConf2 = getConfRank(arrGIIConf) 
    arrThingHuaConf2 = getConfRank(arrThingHuaConf) 
    arrAminerConf2 = getConfRank(arrAminerConf)
    arrCCFConf2 = getConfRank(arrCCFConf) 
    arrThisPaperConf2 = getConfScore(arrThisPaperConf)
    
    #求多个排名规则的集成矩阵:mixArr
    mixArr = np.array(arrCOREConf2) +np.array(arrGUIDEConf2) +np.array(arrGIIConf2) +np.array(arrThingHuaConf2) +np.array(arrAminerConf2) #矩阵对应位置的值相加
    mixArrCCF = np.array(arrCOREConf2) +np.array(arrGUIDEConf2) +np.array(arrGIIConf2) +np.array(arrThingHuaConf2) +np.array(arrAminerConf2) +np.array(arrCCFConf2)#矩阵对应位置的值相加
    mixArrThisPaper = np.array(arrCOREConf2) +np.array(arrGUIDEConf2) +np.array(arrGIIConf2) +np.array(arrThingHuaConf2) +np.array(arrAminerConf2) +np.array(arrThisPaperConf2)#矩阵对应位置的值相加
    mixArrAll = np.array(arrCOREConf2) +np.array(arrGUIDEConf2) +np.array(arrGIIConf2) +np.array(arrThingHuaConf2) +np.array(arrAminerConf2) +np.array(arrCCFConf2) +np.array(arrThisPaperConf2)#矩阵对应位置的值相加
    
    mixArr = mixArr/5#可以直接对举证的每个元素都除以2操作
    mixArrCCF = mixArrCCF/6#可以直接对举证的每个元素都除以2操作
    mixArrThisPaper = mixArrThisPaper/6#可以直接对举证的每个元素都除以2操作
    mixArrAll = mixArrAll/7#可以直接对举证的每个元素都除以2操作
    for i in range(len(mixArr)):
        for j in range(len(mixArr)):
            if mixArr[i][j] >= 0.5:
                mixArr[i][j] = 1
            else:
                mixArr[i][j] = 0
    
    for i in range(len(mixArrCCF)):
        for j in range(len(mixArrCCF)):
            if mixArrCCF[i][j] >= 0.5:
                mixArrCCF[i][j] = 1
            else:
                mixArrCCF[i][j] = 0
                
    for i in range(len(mixArrThisPaper)):
        for j in range(len(mixArrThisPaper)):
            if mixArrThisPaper[i][j] >= 0.5:
                mixArrThisPaper[i][j] = 1
            else:
                mixArrThisPaper[i][j] = 0
                
    for i in range(len(mixArrAll)):
        for j in range(len(mixArrAll)):
            if mixArrAll[i][j] >= 0.5:
                mixArrAll[i][j] = 1
            else:
                mixArrAll[i][j] = 0
    
    a = [[[0]*36]*36]*11#定义一个三维矩阵
    a[0] = arrCOREConf2     
    a[1] = arrGUIDEConf2     
    a[2] = arrGIIConf2     
    a[3] = arrThingHuaConf2     
    a[4] = arrAminerConf2     
    a[5] = arrCCFConf2     
    a[6] = arrThisPaperConf2 
    a[7] = mixArr   
    a[8] = mixArrCCF   
    a[9] = mixArrThisPaper  
    a[10] = mixArrAll   
    #下面三行代码是用来计算所有的排名矩阵相互之间的比较 
    for rank1 in a:
        s = ''
        for rank2 in a:
            s += ( str(compareMatrix(rank1, rank2)) + '\t' )
        print s


def getCompareMatrixJour():
    #去除缺失值的数据
    arrCOREJour = [ 14, 151, 23, 286, 65, 19, 106, 110, 46, 44, 131, 227, 77, 439, 209, 207, 75, 505, 95, 597, 280, 303, 618, 378, 305, 265, 355, 366, 377, 385, 386, 434, 376]
    arrGUIDEJour = [ 45, 39, 10, 148, 350, 13, 3, 32, 278, 297, 229, 316, 190, 259, 426, 601, 288, 456, 70, 160, 558, 24, 136, 101, 515, 166, 48, 261, 344, 421, 264, 197, 187]
    arrSJRJour = [ 2.039, 1.424, 6.298, 1.325, 0.586, 3.781, 3.544, 1.394, 0.831, 1.015, 1.453, 0.806, 1.524, 0.635, 0.305, 0.668, 0.536, 0.316, 1.433, 1.506, 0.375, 1.121, 1.277, 0.968, 0.346, 1.087, 1.877, 0.806, 0.404, 0.443, 0.82, 0.75, 0.637]
    arrZKYJour = [ 3.833666667, 3.307666667, 6.729, 2.664, 1.425666667, 7.706, 6.730333333, 3.737, 1.923666667, 1.818666667, 1.733333333, 1.436333333, 2.057333333, 2.056666667, 1.248, 1.039666667, 1.659, 0.962666667, 3.049666667, 2.267333333, 0.669666667, 6.308333333, 2.288333333, 2.597333333, 0.859333333, 2.008, 3.600333333, 1.542666667, 1.605, 1.034, 1.710666667, 1.791, 1.855333333]
    arrJCRJour = [ 4.797, 5, 8.329, 2.845, 1.606, 7.671, 10.629, 5.287, 1.938, 1.848, 2.284, 1.694, 2.498, 2.009, 1.316, 1.904, 1.9, 1.18, 3.928, 2.718, 0.772, 6.333, 2.929, 3.317, 0.994, 2.671, 4.529, 2.005, 1.62, 1.352, 1.995, 2.472, 2.505]
    arrCCFJour = [ 1, 4, 2, 17, 25, 15, 14, 23, 22, 21, 18, 9, 8, 28, 29, 27, 31, 35, 36, 37, 42, 46, 45, 57, 47, 41, 50, 52, 56, 58, 59, 60, 55]
    arrThisPaperJour = [ 3.567774037, 3.389878272, 4.082712508, 2.751301434, 2.855883721, 3.584368913, 3.640433687, 2.913039254, 2.675149861, 2.94688568, 3.146198863, 2.976819889, 2.742534813, 2.781217288, 2.339413915, 2.345191871, 2.635579964, 2.131266841, 3.157214966, 2.861689518, 1.710470981, 3.109917602, 2.383400342, 2.447849553, 1.63633107, 2.884644846, 2.805930531, 2.291916766, 2.108627775, 2.043742616, 2.772791227, 2.315026304, 2.214612481]
    
    arrCOREJour2 = getJourRank(arrCOREJour) 
    arrGUIDEJour2 = getJourRank(arrGUIDEJour) 
    arrSJRJour2 = getJourScore(arrSJRJour) 
    arrZKYJour2 = getJourScore(arrZKYJour) 
    arrJCRJour2 = getJourScore(arrJCRJour) 
    arrCCFJour2 = getJourRank(arrCCFJour) 
    arrThisPaperJour2 = getJourScore(arrThisPaperJour)
    #求多个排名规则的集成矩阵:mixArr
    mixArr = np.array(arrCOREJour2) +np.array(arrGUIDEJour2) +np.array(arrSJRJour2) +np.array(arrZKYJour2) +np.array(arrJCRJour2) #矩阵对应位置的值相加
    mixArrCCF = np.array(arrCOREJour2) +np.array(arrGUIDEJour2) +np.array(arrSJRJour2) +np.array(arrZKYJour2) +np.array(arrJCRJour2) +np.array(arrCCFJour2) #矩阵对应位置的值相加
    mixArrThisPaper = np.array(arrCOREJour2) +np.array(arrGUIDEJour2) +np.array(arrSJRJour2) +np.array(arrZKYJour2) +np.array(arrJCRJour2) +np.array(arrThisPaperJour2) #矩阵对应位置的值相加
    mixArrAll = np.array(arrCOREJour2) +np.array(arrGUIDEJour2) +np.array(arrSJRJour2) +np.array(arrZKYJour2) +np.array(arrJCRJour2)+np.array(arrCCFJour2) +np.array(arrThisPaperJour2) #矩阵对应位置的值相加
    mixArr = mixArr/5#可以直接对举证的每个元素都除以2操作
    mixArrCCF = mixArrCCF/6#可以直接对举证的每个元素都除以2操作
    mixArrThisPaper = mixArrThisPaper/6#可以直接对举证的每个元素都除以2操作
    mixArrAll = mixArrAll/7#可以直接对举证的每个元素都除以2操作
    for i in range(len(mixArr)):
        for j in range(len(mixArr)):
            if mixArr[i][j] >= 0.5:
                mixArr[i][j] = 1
            else:
                mixArr[i][j] = 0
    
    for i in range(len(mixArrCCF)):
        for j in range(len(mixArrCCF)):
            if mixArrCCF[i][j] >= 0.5:
                mixArrCCF[i][j] = 1
            else:
                mixArrCCF[i][j] = 0
                
    for i in range(len(mixArrThisPaper)):
        for j in range(len(mixArrThisPaper)):
            if mixArrThisPaper[i][j] >= 0.5:
                mixArrThisPaper[i][j] = 1
            else:
                mixArrThisPaper[i][j] = 0
    
    for i in range(len(mixArrAll)):
        for j in range(len(mixArrAll)):
            if mixArrAll[i][j] >= 0.5:
                mixArrAll[i][j] = 1
            else:
                mixArrAll[i][j] = 0
    
    a = [[[0]*42]*42]*11#定义一个三维矩阵
    a[0] = arrCOREJour2     
    a[1] = arrGUIDEJour2     
    a[2] = arrSJRJour2     
    a[3] = arrZKYJour2     
    a[4] = arrJCRJour2     
    a[5] = arrCCFJour2     
    a[6] = arrThisPaperJour2 
    a[7] = mixArr   
    a[8] = mixArrCCF   
    a[9] = mixArrThisPaper   
    a[10] = mixArrAll   
    #下面三行代码是用来计算所有的排名矩阵相互之间的比较 
    for rank1 in a:
        s = ''
        for rank2 in a:
            s += ( str(compareMatrix(rank1, rank2)) + '\t' )
        print s

def compareMatrix(a, b):
    m = n = len(a)
    t0 = 0
    t1 = 0
    t2 = 0
    for i in range(0,m):
        for j in range(i+1, m):
            t0 += (a[i][j] * b[i][j])/2
            t1 += (a[i][j])/2
            t2 += (b[i][j])/2
    t3 = 2*(t1*t2)/(m*(m-1))
    compareValue = (t0-t3)/((t1+t2)/2-t3)
    return compareValue

if __name__ == '__main__':
    getCompareMatrixJour()
#     getCompareMatrixConf()
    