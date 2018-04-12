#coding=utf-8
'''
Created on 2018��1��16��

@author: Administrator
'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

diss = 1
maxCC = 1000
Lenlist = 1000

n1 = 3
m1 = 3
n2 = 3
m2 = 7

fnCA = ['ICCV', 'AAAI', 'NIPS', 'CVPR', 'ACL', 'IJCAI', 'ICML','COLT','UAI']
fnCA2 = ['PPSN','KR','ICRA','ICCBR','ICAPS','EMNLP','ECCV','ECAI','COLING']
fnCA3 = ['AAMAS','ACCV','AISTATS','BMVC','CoNLL','FGR','GECCO','ICANN','ICB']
fnCA4 = ['ICDAR','ICONIP','ICPR','ICTAI','IJCNN','IROS','KSEM','NAACL','PRICAI']
fnJA = ['AI','IJCV','JMLR','PAMI','IJAR','AAMAS','TNNLS','TFS','TEC','TCYB','TASLP','TAC','NN','NECO','ML','MIT','JAIR','DKE','CVIU','AIM','Alife']
fnJA2 = ['APIN','CSL','DSS','EAAI','ES','ESWA','FSS','IDA','IJNS','IJIS','IJON','IJPRAI','IVC','KBS','MVA','NC','NPL','PAA','PRL','SOCO','tNCA']

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
            if ( float(item) < maxCC ):
                for m in range(0,len(indexNum)-1):
                    if (float(item) >= indexNum[m] and float(item) < (indexNum[m]+diss) ):
                        listX[m] = (indexNum[m+1]+indexNum[m])/2 
                        listY[m] += mylist.count(item)
            continue
        except:
            continue
    listY = [y/lenY for y in listY ]
    return listX, listY

def readFile(fileneme):
    word = []
    file=open(fileneme)
    while 1:
        line = file.readline().replace('\n','')
        if not line:
            break
        try:
            line = line.split('\t')[1]
            word.append( int(line) )
        except:
            continue
    return word

def drawAllJA(filename):
    filename = 'data/counts/test/journals/' + filename + '.txt'
    titleSize = 6
    pointSize = 0.1
    x = getRepeatCount(readFile(filename), maxCC, diss)[0]
    y = getRepeatCount(readFile(filename), maxCC, diss)[1]
    plt.scatter(x,y,c='b',s=pointSize)
    plt.title(filename.split('/')[3].replace('.txt',''), fontsize = titleSize)

def drawAllCA(filename):
    filename = 'data/counts/test/conferences/' + filename + '.txt'
    titleSize = 6
    pointSize = 0.1
    x = getRepeatCount(readFile(filename), maxCC, diss)[0]
    y = getRepeatCount(readFile(filename), maxCC, diss)[1]
    plt.scatter(x,y,c='b',s=pointSize)
    plt.title(filename.split('/')[3].replace('.txt',''), fontsize = titleSize)
    
def showConferences1():
    matplotlib.rc('xtick', labelsize=5) 
    matplotlib.rc('ytick', labelsize=5)
    count = 1
    for f in fnCA:
        plt.subplot(n1,m1,count)
        drawAllCA(f)
        count += 1
    plt.show()
    
def showConferences2():
    matplotlib.rc('xtick', labelsize=5) 
    matplotlib.rc('ytick', labelsize=5)
    count = 1
    for f in fnCA2:
        plt.subplot(n1,m1,count)
        drawAllCA(f)
        count += 1
    plt.show()
    
def showConferences3():
    matplotlib.rc('xtick', labelsize=5) 
    matplotlib.rc('ytick', labelsize=5)
    count = 1
    for f in fnCA3:
        plt.subplot(n1,m1,count)
        drawAllCA(f)
        count += 1
    plt.show()
    
def showConferences4():
    matplotlib.rc('xtick', labelsize=5) 
    matplotlib.rc('ytick', labelsize=5)
    count = 1
    for f in fnCA4:
        plt.subplot(n1,m1,count)
        drawAllCA(f)
        count += 1
    plt.show()

def showJournals1():
    matplotlib.rc('xtick', labelsize=5) 
    matplotlib.rc('ytick', labelsize=5)
    count = 1
    for f in fnJA:
        plt.subplot(n2,m2,count)
        drawAllJA(f)
        count += 1
    plt.show()

def showJournals2():
    matplotlib.rc('xtick', labelsize=5) 
    matplotlib.rc('ytick', labelsize=5)
    count = 1
    for f in fnJA2:
        plt.subplot(n2,m2,count)
        drawAllJA(f)
        count += 1
    plt.show()


if __name__ == '__main__':
    showConferences1()
    showConferences2()
    showConferences3()
    showConferences4()
    showJournals1()
    showJournals2()