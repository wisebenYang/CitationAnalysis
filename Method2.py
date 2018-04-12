#coding=utf-8
from __future__ import division
import numpy as np
import random

def weight_choice(list, weight):
    new_list = []
    for i, val in enumerate(list):
        new_list.extend(val * weight[i])
    return random.choice(new_list)

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
    
def getConfScore(c):
    c2m = [([0]* 36)for i in range(36)]
    for i in range( len(c) ):
        for j in range(len(c)):
            if c[i] == None:
                c2m[i][j] = None
            elif c[i] <= c[j]:
                c2m[i][j] = 0
            else:
                c2m[i][j] = 1
    return c2m

def getConfRank(c):
    c2m = [([0]* 36)for i in range(36)]
    for i in range( len(c) ):
        for j in range(len(c)):
            if c[i] == None:
                c2m[i][j] = None
            elif c[i] <= c[j]:
                c2m[i][j] = 1
            else:
                c2m[i][j] = 0
    return c2m

def getJourScore(c):
    c2m = [([0]* 42)for i in range(42)]
    for i in range( len(c) ):
        for j in range(len(c)):
            if c[i] == None:
                c2m[i][j] = None
            elif c[i] <= c[j]:
                c2m[i][j] = 0
            else:
                c2m[i][j] = 1
    return c2m

def getJourRank(c):
    c2m = [([0]* 42)for i in range(42)]
    for i in range( len(c) ):
        for j in range(len(c)):
            if c[i] == None:
                c2m[i][j] = None
            elif c[i] <= c[j]:
                c2m[i][j] = 0
            else:
                c2m[i][j] = 1
    return c2m

def getCompareMatrixJour():
    arrCOREJour = [ 23, 286, 65, None, 19, 106, None, 200, None, 110, 46, 44, 364, 131, 227, 77, 439, 209, 207, 75, 15, None, 505, 95, 597, 280, 303, 618, 378, 305, 265, 355, 366, None, 377, 385, 386, 434, 376]
    arrGUIDEJour = [ 10, 148, 350, 26, 13, 3, 14, 193, 116, 32, 278, 297, None, 229, 316, 190, 259, 426, 601, 288, None, 141, 456, 70, 160, 558, 24, 136, 101, 515, 166, 48, 261, 555, 344, 421, 264, 197, 187]
    arrSJRJour = [ 6.298, 1.325, 0.586, 2.49, 3.781, 3.544, 2.906, 0.887, 1.072, 1.394, 0.831, 1.015, 0.158, 1.453, 0.806, 1.524, 0.635, 0.305, 0.668, 0.536, 1.806, 1.047, 0.316, 1.433, 1.506, 0.375, 1.121, 1.277, 0.968, 0.346, 1.087, 1.877, 0.806, 0.318, 0.404, 0.443, 0.82, 0.75, 0.637]
    arrZKYJour = [ 6.729, 2.664, 1.425666667, 5.084333333, 7.706, 6.730333333, 5.265333333, 2.185, 2.565666667, 3.737, 1.923666667, 1.818666667, None, 1.733333333, 1.436333333, 2.057333333, 2.056666667, 1.248, 1.039666667, 1.659, 2.713, 2.489666667, 0.962666667, 3.049666667, 2.267333333, 0.669666667, 6.308333333, 2.288333333, 2.597333333, 0.859333333, 2.008, 3.600333333, 1.542666667, 0.948333333, 1.605, 1.034, 1.710666667, 1.791, 1.855333333]
    arrJCRJour = [ 8.329, 2.845, 1.606, 6.108, 7.671, 10.629, 7.384, None, 3.149, 5.287, 1.938, 1.848, None, 2.284, 1.694, 2.498, 2.009, 1.316, 1.904, 1.9, 3.222, 2.894, 1.18, 3.928, 2.718, 0.772, 6.333, 2.929, 3.317, 0.994, 2.671, 4.529, 2.005, 0.778, 1.62, 1.352, 1.995, 2.472, 2.505]
    arrCCFJour = [ 2, 17, 25, 16, 15, 14, 13, 12, 11, 23, 22, 21, 51, 18, 9, 8, 28, 29, 27, 31, 33, 34, 35, 36, 37, 42, 46, 45, 57, 47, 41, 50, 52, 53, 56, 58, 59, 60, 55]
    arrThisPaperJour = [ 4.082712508, 2.751301434, 2.855883721, 3.272171121, 3.584368913, 3.640433687, 2.956270052, 2.977392586, 3.136010311, 2.913039254, 2.675149861, 2.94688568, 3.218654441, 3.146198863, 2.976819889, 2.742534813, 2.781217288, 2.339413915, 2.345191871, 2.635579964, 3.322660273, 2.747680062, 2.131266841, 3.157214966, 2.861689518, 1.710470981, 3.109917602, 2.383400342, 2.447849553, 1.63633107, 2.884644846, 2.805930531, 2.291916766, 2.115829248, 2.108627775, 2.043742616, 2.772791227, 2.315026304, 2.214612481]
    arrCOREJour2 = getJourRank(arrCOREJour) 
    arrGUIDEJour2 = getJourRank(arrGUIDEJour) 
    arrSJRJour2 = getJourScore(arrSJRJour) 
    arrZKYJour2 = getJourScore(arrZKYJour) 
    arrJCRJour2 = getJourScore(arrJCRJour) 
    arrCCFJour2 = getJourRank(arrCCFJour) 
    arrThisPaperJour2 = getJourScore(arrThisPaperJour)
    for i in range(42):
        for j in range(42):
            s0 = 0
            s1 = 0
            if ( arrCOREJour2[i][j] == None or arrGUIDEJour2[i][j] == None or arrSJRJour2[i][j] == None or arrZKYJour2[i][j] == None or arrJCRJour2[i][j] == None):
                if arrCOREJour2[i][j] != None :
                    if arrCOREJour2[i][j] == 0:
                        s0 += 1
                    else:
                        s1 += 1  
                if arrGUIDEJour2[i][j] != None :
                    if arrGUIDEJour2[i][j] == 0:
                        s0 += 1
                    else:
                        s1 += 1
                if arrSJRJour2[i][j] != None :
                    if arrSJRJour2[i][j] == 0:
                        s0 += 1
                    else:
                        s1 += 1
                if arrZKYJour2[i][j] != None :
                    if arrZKYJour2[i][j] == 0:
                        s0 += 1
                    else:
                        s1 += 1
                if arrJCRJour2[i][j] != None :
                    if arrGUIDEJour2[i][j] == 0:
                        s0 += 1
                    else:
                        s1 += 1
                if arrCCFJour2[i][j] == 0:
                    s0 += 1
                else:
                    s1 += 1
                if arrThisPaperJour2[i][j] == 0:
                    s0 += 1
                else:
                    s1 += 1
                if s0 > s1:
                    if arrCOREJour2[i][j] == None :
                        arrCOREJour2[i][j] = 0
                    if arrGUIDEJour2[i][j] == None :
                        arrGUIDEJour2[i][j] = 0
                    if arrSJRJour2[i][j] == None :
                        arrSJRJour2[i][j] = 0
                    if arrZKYJour2[i][j] == None :
                        arrZKYJour2[i][j] = 0
                    if arrJCRJour2[i][j] == None :
                        arrJCRJour2[i][j] = 0
                else:
                    if arrCOREJour2[i][j] == None :
                        arrCOREJour2[i][j] = 1
                    if arrGUIDEJour2[i][j] == None :
                        arrGUIDEJour2[i][j] = 1
                    if arrSJRJour2[i][j] == None :
                        arrSJRJour2[i][j] = 1
                    if arrZKYJour2[i][j] == None :
                        arrZKYJour2[i][j] = 1
                    if arrJCRJour2[i][j] == None :
                        arrJCRJour2[i][j] = 1
    
    mixArr = np.array(arrCOREJour2) +np.array(arrGUIDEJour2) +np.array(arrSJRJour2) +np.array(arrZKYJour2) +np.array(arrJCRJour2) 
    mixArrCCF = np.array(arrCOREJour2) +np.array(arrGUIDEJour2) +np.array(arrSJRJour2) +np.array(arrZKYJour2) +np.array(arrJCRJour2) +np.array(arrCCFJour2) 
    mixArrThisPaper = np.array(arrCOREJour2) +np.array(arrGUIDEJour2) +np.array(arrSJRJour2) +np.array(arrZKYJour2) +np.array(arrJCRJour2) +np.array(arrThisPaperJour2)
    mixArrAll = np.array(arrCOREJour2) +np.array(arrGUIDEJour2) +np.array(arrSJRJour2) +np.array(arrZKYJour2) +np.array(arrJCRJour2)+np.array(arrCCFJour2) +np.array(arrThisPaperJour2) 
    mixArr = mixArr/5
    mixArrCCF = mixArrCCF/6
    mixArrThisPaper = mixArrThisPaper/6
    mixArrAll = mixArrAll/7
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
    
    
    a= [[[0]*42]*42]*11
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
    for rank1 in a:
        s = ''
        for rank2 in a:
            s += ( str(compareMatrix(rank1, rank2)) + '\t' )
        print s


def getCompareMatrixConf():
    arrCOREConf = [ 22, 3, 43, 117, 5, 29, 27, 11, 64, 284, 40, 510, None, 21, 145, 134, 133, 106, 4, 343, 641, 97, 108, None, 480, 492, None, 191, 203, 205, 516, 221, 535, None, 265, 590]
    arrGUIDEConf = [ 5, 26, 2, 1, 16, 50, 4, 99, 103, 316, 158, 11, None, 157, 23, 3, 124, 92, 73, 35, 112, 55, 222, 137, 117, 328, 121, 153, 287, 95, 282, 116, 36, None, 45, None]
    arrGIIConf = [ 24, 23, 35, 53, 21, 33, 29, 45, 47, 232, 61, 116, 596, 922, 49, 50, 177, 136, 44, 275, 595, 92, 173, 193, 111, 919, 392, 960, 427, 217, 446, 198, 128, 1512, 70, 1944]
    arrThingHuaConf = [ 34, 32, 140, 33, 40, 30, 35, 139, 149, None, 148, 144, 146, 145, 141, 143, 142, 147, 150, 280, None, 296, 281, 286, 282, 285, 292, 287, 290, 291, 283, 293, None, 289, 295, 294]
    arrAminerConf = [ 6, 13, 8, 1, 10, 20, 7, 49, 59, None, 38, 5, 74, 47, 12, 57, 48, 35, 93, 72, None, 30, None, 94, 33, 89, 64, 43, 90, 26, 69, 44, None, 86, 70, 81]
    arrCCFConf = [ 4, 1, 7, 3, 8, 6, 5, 9, 18, 20, 17, 13, 15, 14, 10, 12, 11, 16, 19, 21, 39, 37, 22, 27, 23, 26, 33, 28, 31, 32, 24, 34, 38, 30, 36, 35]
    arrThisPaperConf = [ 3.27 , 2.04 , 2.97 , 3.32 , 2.63 , 2.17 , 3.22 , 2.94 , 2.46 , 2.04 , 2.48 , 2.47 , 1.74 , 2.57 , 2.75 , 2.90 , 1.77 , 1.98 , 1.23 , 1.67 , 2.73 , 2.36 , 2.86 , 2.48 , 1.85 , 1.46 , 2.42 , 2.23 , 1.06 , 1.67 , 1.52 , 1.49 , 2.14 , 1.16 , 2.24 , 1.26 ]
    arrCOREConf2 = getConfRank(arrCOREConf) 
    arrGUIDEConf2 = getConfRank(arrGUIDEConf) 
    arrGIIConf2 = getConfScore(arrGIIConf) 
    arrThingHuaConf2 = getConfScore(arrThingHuaConf) 
    arrAminerConf2 = getConfScore(arrAminerConf) 
    arrCCFConf2 = getConfRank(arrCCFConf) 
    arrThisPaperConf2 = getConfScore(arrThisPaperConf)
    for i in range(36):
        for j in range(36):
            s0 = 0
            s1 = 0
            if ( arrCOREConf2[i][j] == None or arrGUIDEConf2[i][j] == None or arrGIIConf2[i][j] == None or arrThingHuaConf2[i][j] == None or arrAminerConf2[i][j] == None):
                if arrCOREConf2[i][j] != None :
                    if arrCOREConf2[i][j] == 0:
                        s0 += 1
                    else:
                        s1 += 1  
                if arrGUIDEConf2[i][j] != None :
                    if arrGUIDEConf2[i][j] == 0:
                        s0 += 1
                    else:
                        s1 += 1
                if arrGIIConf2[i][j] != None :
                    if arrGIIConf2[i][j] == 0:
                        s0 += 1
                    else:
                        s1 += 1
                if arrThingHuaConf2[i][j] != None :
                    if arrThingHuaConf2[i][j] == 0:
                        s0 += 1
                    else:
                        s1 += 1
                if arrAminerConf2[i][j] != None :
                    if arrAminerConf2[i][j] == 0:
                        s0 += 1
                    else:
                        s1 += 1
                if arrCCFConf2[i][j] == 0:
                    s0 += 1
                else:
                    s1 += 1
                if arrThisPaperConf2[i][j] == 0:
                    s0 += 1
                else:
                    s1 += 1
                    
                if s0 > s1:
                    if arrCOREConf2[i][j] == None :
                        arrCOREConf2[i][j] = 0
                    if arrGUIDEConf2[i][j] == None :
                        arrGUIDEConf2[i][j] = 0
                    if arrGIIConf2[i][j] == None :
                        arrGIIConf2[i][j] = 0
                    if arrThingHuaConf2[i][j] == None :
                        arrThingHuaConf2[i][j] = 0
                    if arrAminerConf2[i][j] == None :
                        arrAminerConf2[i][j] = 0
                else:
                    if arrCOREConf2[i][j] == None :
                        arrCOREConf2[i][j] = 1
                    if arrGUIDEConf2[i][j] == None :
                        arrGUIDEConf2[i][j] = 1
                    if arrGIIConf2[i][j] == None :
                        arrGIIConf2[i][j] = 1
                    if arrThingHuaConf2[i][j] == None :
                        arrThingHuaConf2[i][j] = 1
                    if arrAminerConf2[i][j] == None :
                        arrAminerConf2[i][j] = 1
    mixArr = np.array(arrCOREConf2) +np.array(arrGUIDEConf2) +np.array(arrGIIConf2) +np.array(arrThingHuaConf2) +np.array(arrAminerConf2) 
    mixArrCCF = np.array(arrCOREConf2) +np.array(arrGUIDEConf2) +np.array(arrGIIConf2) +np.array(arrThingHuaConf2) +np.array(arrAminerConf2) +np.array(arrCCFConf2)
    mixArrThisPaper = np.array(arrCOREConf2) +np.array(arrGUIDEConf2) +np.array(arrGIIConf2) +np.array(arrThingHuaConf2) +np.array(arrAminerConf2) +np.array(arrThisPaperConf2) 
    mixArrAll = np.array(arrCOREConf2) +np.array(arrGUIDEConf2) +np.array(arrGIIConf2) +np.array(arrThingHuaConf2) +np.array(arrAminerConf2)+np.array(arrCCFConf2) +np.array(arrThisPaperConf2)
    mixArr = mixArr/5
    mixArrCCF = mixArrCCF/6
    mixArrThisPaper = mixArrThisPaper/6
    mixArrAll = mixArrAll/7
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
    
    
    a= [[[0]*36]*36]*11
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
    for rank1 in a:
        s = ''
        for rank2 in a:
            s += ( str(compareMatrix(rank1, rank2)) + '\t' )
        print s
if __name__ == '__main__':
#     getCompareMatrixConf()
    getCompareMatrixJour()