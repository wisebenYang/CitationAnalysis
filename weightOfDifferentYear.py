#coding=utf-8
from __future__ import division 
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit  
from sympy import *
from fileinput import filename

maxCC = 2000
diss = 1
Lenlist = 2000


def writeFile(filename,Txtstr):
    fr = open(filename,'a+')
    fr.write(Txtstr)
    fr.close()

def readFile(fileneme):
    '''
    get the citaion counting of each papers and saved them in a list.
    '''
    word = []
    file=open(fileneme)
    while 1:
        line = file.readline().replace('\n','')
        if not line:
            break
        try:
            word.append(line.split('\t')[1])
        except:
            pass
    return word

def readFile16(filename, weight):
    filename = r'data/counts/conferenceA/'+filename + '/2016.txt'
    file=open(filename)
    while 1:
        line = file.readline().replace('\n','')
        if not line:
            break
        try:
            outFilename = r'varify/' + filename + '.txt'
            writeFile(outFilename, (line.split('\t')[1])*weight[9])
        except:
            print line
    print filename,'2016','done...'

def calculateMean_07(filename):
    meanLog = np.mean( [np.log( (int(n)+1) )/10 for n in readFile(filename)] )
    return meanLog
def calculateMean_08(filename):
    meanLog = np.mean( [np.log( (int(n)+1) )/9 for n in readFile(filename)] )
    return meanLog
def calculateMean_09(filename):
    meanLog = np.mean( [np.log( (int(n)+1) )/8 for n in readFile(filename)] )
    return meanLog
def calculateMean_10(filename):
    meanLog = np.mean( [np.log( (int(n)+1) )/7 for n in readFile(filename)] )
    return meanLog
def calculateMean_11(filename):
    meanLog = np.mean( [np.log( (int(n)+1) )/6 for n in readFile(filename)] )
    return meanLog
def calculateMean_12(filename):
    meanLog = np.mean( [np.log( (int(n)+1) )/5 for n in readFile(filename)] )
    return meanLog
def calculateMean_13(filename):
    meanLog = np.mean( [np.log( (int(n)+1) )/4 for n in readFile(filename)] )
    return meanLog
def calculateMean_14(filename):
    meanLog = np.mean( [np.log( (int(n)+1) )/3 for n in readFile(filename)] )
    return meanLog
def calculateMean_15(filename):
    meanLog = np.mean( [np.log( (int(n)+1) )/2 for n in readFile(filename)] )
    return meanLog
def calculateMean_16(filename):
    meanLog = np.mean( [np.log( (int(n)+1) )/1 for n in readFile(filename)] )
    return meanLog
def calculateMean(filename):
    meanLog = np.mean( [ (int(n)) for n in readFile(filename)] )
    return meanLog
        
def getRepeatCount(mylist, maxCC, diss,lenY=1):
    myset = set(mylist)  
    indexNum = []
    for i in range(0, maxCC, diss):
        indexNum.append(i)
    indexNum.append(diss)
    listX = indexNum[0:Lenlist]
    listY = [0]*Lenlist
    for item in myset:
        try:
            if ( int(item) < maxCC ):
                for m in range(0,len(indexNum)-1):
                    if (int(item) >= indexNum[m] and int(item) < (indexNum[m]+diss) ):
                        listX[m] = (indexNum[m+1]+indexNum[m])/2 
                        listY[m] += mylist.count(item)
            continue
        except:
            print '..'
    listY = [y/lenY for y in listY ]
    return listX, listY 

def calculateWeights(name):
    orignalMatrix = []
    filename_16 = 'data/2016/'+name+'.txt'
    filename_15 = 'data/2015/'+name+'.txt'
    filename_14 = 'data/2014/'+name+'.txt'
    filename_13 = 'data/2013/'+name+'.txt'
    filename_12 = 'data/2012/'+name+'.txt'
    filename_11 = 'data/2011/'+name+'.txt'
    filename_10 = 'data/2010/'+name+'.txt'
    filename_09 = 'data/2009/'+name+'.txt'
    filename_08 = 'data/2008/'+name+'.txt'
    filename_07 = 'data/2007/'+name+'.txt'
    orignalMatrix.append( calculateMean_07(filename_07) )
    orignalMatrix.append( calculateMean_08(filename_08) )
    orignalMatrix.append( calculateMean_09(filename_09) )
    orignalMatrix.append( calculateMean_10(filename_10) )
    orignalMatrix.append( calculateMean_11(filename_11) )
    orignalMatrix.append( calculateMean_12(filename_12) )
    orignalMatrix.append( calculateMean_13(filename_13) )
    orignalMatrix.append( calculateMean_14(filename_14) )
    orignalMatrix.append( calculateMean_15(filename_15) )
    orignalMatrix.append( calculateMean_16(filename_16) )
    return orignalMatrix

if __name__ == '__main__':
    CA = [t/7 for t in calculateWeights('CA')]
    CB = [t/12 for t in calculateWeights('CB')]
    CC = [t/20 for t in calculateWeights('CC')]
    JA = [t/4 for t in calculateWeights('JA')]
    JB = [t/18 for t in calculateWeights('JB')]
    JC = [t/34 for t in calculateWeights('JC')]
    print CA
    print CB
    print CC
    print JA
    print JB
    print JC
