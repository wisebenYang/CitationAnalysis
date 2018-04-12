#coding=utf-8
from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.optimize import curve_fit  

diss = 1
maxCC = 1000
Lenlist = 1000

def writeFile(filename,Txtstr):
    fr = open(filename,'a+')
    fr.write(Txtstr)
    fr.close()

def readFile(fileneme):
    word = []
    file=open(fileneme)
    while 1:
        line = file.readline().replace('\n','')
        if not line:
            break
        try:
            word.append(line.split('\t')[1])
        except:
            print line
    return word

def readFile2(fileneme):
    word = []
    file=open(fileneme)
    while 1:
        line = file.readline().replace('\n','')
        if not line:
            break
        try:
            word.append(line)
        except:
            print line
    return word

def getRepeatCountlOG(mylist, maxCC, diss, lenY=1):
    myset = set(mylist) 
    indexNum = []
    for i in range(0, maxCC, diss):
        indexNum.append(i)
    indexNum.append(diss)
    listX = indexNum[0:Lenlist]
    listY = [0]*Lenlist
    for item in myset:
        try:
            if ( int(item) < maxCC):
                for m in range(0,len(indexNum)-1):
                    if (int(item) >= indexNum[m] and int(item) < (indexNum[m]+diss) ):
                        listX[m] = (indexNum[m+1]+indexNum[m])/2
                        listY[m] +=math.log((mylist.count(item)+1))
            continue
        except:
            print '..'
    listY = [i/lenY for i in listY]
    listX = [math.log(x) for x in listX]
    return listX, listY 

def getRepeatCountlOG2(mylist, maxCC, diss, lenY=1):
    myset = set(mylist) 
    indexNum = []
    for i in range(0, maxCC, diss):
        indexNum.append(i)
    indexNum.append(diss)
    listX = indexNum[0:Lenlist]
    listY = [0]*Lenlist
    for item in myset:
        try:
            if ( int(item) < maxCC):
                for m in range(0,len(indexNum)-1):
                    if (int(item) >= indexNum[m] and int(item) < (indexNum[m]+diss) ):
                        listX[m] = (indexNum[m+1]+indexNum[m])/2
                        listY[m] +=math.log((mylist.count(item)+1))
            continue
        except:
            print '..'
    listY = [i/lenY for i in listY]
    return listX, listY 

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

def conferenceA(journal):
    filename = 'data/counts/conferenceA/' + journal
    mylist = readFile(filename)
    return mylist, filename

def conferenceB(journal):
    filename = 'data/counts/conferenceB/' + journal
    mylist = readFile(filename)
    return mylist, filename

def conferenceC(journal):
    filename = 'data/counts/conferenceC/' + journal
    mylist = readFile(filename)
    return mylist, filename

def journalA(journal):
    filename = 'data/counts/journalA/' + journal
    mylist = readFile(filename)
    return mylist, filename

def journalB(journal):
    filename = 'data/counts/journalB/' + journal
    mylist = readFile(filename)
    return mylist, filename

def journalC(journal):
    filename = 'data/counts/journalC/' + journal
    mylist = readFile(filename)
    return mylist, filename


def journalAll(journal):
    filename = r'data/counts/' + journal
    mylist = readFile(filename)
    return mylist, filename

def conferenceAll(journal):
    filename = r'data/counts/' + journal
    mylist = readFile(filename)
    return mylist, filename

def setFigure(plts, typeC,x,y, la, labelX='The logarithm of the cited count ', labelY='The logarithm of the frequency of cited count'):
    plts.plot(x, y, typeC, label=la)
    plts.xlabel(labelX)
    plts.ylabel(labelY)
    


def classConferenceABC():
    mylist = conferenceA('testA.txt')[0]
    conference = conferenceA('testA.txt')[1]
    conference = conference.split('/')[2]
    mylist2 = conferenceB('testB.txt')[0]
    conference2 = conferenceB('testB.txt')[1]
    conference2 = conference2.split('/')[2]
    mylist3 = conferenceC('testC.txt')[0]
    conference3 = conferenceC('testC.txt')[1]
    conference3 = conference3.split('/')[2]
    x = getRepeatCountlOG(mylist, maxCC, diss)[0] 
    y = getRepeatCountlOG(mylist, maxCC, diss, 8)[1]
    typeC = '.'
    setFigure(plt, typeC, x, y, 'Conference A')
    x = getRepeatCountlOG(mylist2, maxCC, diss)[0]
    y = getRepeatCountlOG(mylist2, maxCC, diss, 13)[1]
    typeC = 'r*'
    setFigure(plt, typeC, x, y, 'conference B')
    x = getRepeatCountlOG(mylist3, maxCC, diss)[0] 
    y = getRepeatCountlOG(mylist3, maxCC, diss, 21)[1]
    typeC = 'k+'
    setFigure(plt, typeC, x, y, 'conference C')
    plt.legend(loc='upper right')
#     plt.savefig('images/conferenceABC.eps')
    plt.show()

def classJournalABC():
    mylist = journalA('testA.txt')[0]
    journal = journalA('testA.txt')[1]
    journal = journal.split('/')[2]
    mylist2 = journalB('testB.txt')[0]
    journal2 = journalB('testB.txt')[1]
    journal2 = journal2.split('/')[2]
    mylist3 = journalC('testC.txt')[0]
    journal3 = journalC('testC.txt')[1]
    journal3 = journal3.split('/')[2]
    x = getRepeatCountlOG(mylist, maxCC, diss)[0] 
    y = getRepeatCountlOG(mylist, maxCC, diss, 5)[1]
    typeC = '.'
    setFigure(plt, typeC, x, y, 'journal A')
    x = getRepeatCountlOG(mylist2, maxCC, diss)[0] 
    y = getRepeatCountlOG(mylist2, maxCC, diss, 19)[1]
    typeC = 'r*'
    setFigure(plt, typeC, x, y, 'journal B')
    x = getRepeatCountlOG(mylist3, maxCC, diss)[0] 
    y = getRepeatCountlOG(mylist3, maxCC, diss, 36)[1]
    typeC = 'k+'
    setFigure(plt, typeC, x, y, 'journal C')
    plt.legend(loc='upper right')
    plt.savefig('images/journalABC.eps')
    plt.show()

def CJA():
    mylist = journalA('testA.txt')[0]
    journal = journalA('testA.txt')[1]
    journal = journal.split('/')[2]
    x = getRepeatCountlOG(mylist, maxCC, diss)[0] 
    y = getRepeatCountlOG(mylist, maxCC, diss, 5)[1]
    typeC = '.'
    setFigure(plt,  typeC, x, y,'journal')
    mylist2 = conferenceA('testA.txt')[0]
    conference = conferenceA('testA.txt')[1]
    conference = conference.split('/')[2]
    x = getRepeatCountlOG(mylist2, maxCC, diss)[0] 
    y = getRepeatCountlOG(mylist2, maxCC, diss, 8)[1]
    typeC = 'r+'
    setFigure(plt, typeC, x, y, 'conference')
    plt.legend(loc='upper right')
    plt.savefig('images/A.eps')
    plt.show()

def CJB():
    mylist = journalB('testB.txt')[0]
    journal = journalB('testB.txt')[1]
    journal = journal.split('/')[2]
    x = getRepeatCountlOG(mylist, maxCC, diss)[0] 
    y = getRepeatCountlOG(mylist, maxCC, diss, 19)[1]
    typeC = '.'
    setFigure(plt, typeC, x, y, 'journal')
    mylist2 = conferenceB('testB.txt')[0]
    conference = conferenceB('testB.txt')[1]
    conference = conference.split('/')[2]
    x = getRepeatCountlOG(mylist2, maxCC, diss)[0] 
    y = getRepeatCountlOG(mylist2, maxCC, diss, 13)[1]
    typeC = 'r+'
    setFigure(plt, typeC, x, y, 'conference')
    plt.legend(loc='upper right')
    plt.savefig('images/B.eps')
    plt.show()

def CJC():
    mylist = journalC('testC.txt')[0]
    journal = journalC('testC.txt')[1]
    journal = journal.split('/')[2]
    x = getRepeatCountlOG(mylist, maxCC, diss)[0] 
    y = getRepeatCountlOG(mylist, maxCC, diss, 36)[1]
    typeC = '.'
    setFigure(plt, typeC, x, y,'journal')
    mylist2 = conferenceC('testC.txt')[0]
    conference = conferenceC('testC.txt')[1]
    conference = conference.split('/')[2]
    x = getRepeatCountlOG(mylist2, maxCC, diss)[0] 
    y = getRepeatCountlOG(mylist2, maxCC, diss, 21)[1]
    typeC = 'r+'
    setFigure(plt, typeC, x, y,'conference')
    plt.legend(loc='upper right')
    plt.savefig('images/C.eps')
    plt.show()
    
    
if __name__ == '__main__':
#     classConferenceABC()
#     classJournalABC()
    CJA()
    CJB()
    CJC()