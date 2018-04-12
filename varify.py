#coding=utf-8
from __future__ import division 
import numpy as np
import os
from fileinput import filename

maxCC = 2000
diss = 1
Lenlist = 2000

wCA = [0.048576688850291046, 0.053810242751457217, 0.063040884399900077, 0.065752090412732167, 0.072735779197436762, 0.088510003952739266, 0.097816155747057196, 0.12909425115845949, 0.16696381888765385, 0.23793869599491221]
wCB = [0.024345972500258838, 0.027185791213886128, 0.030176045168646127, 0.033316961759677556, 0.035988049337448001, 0.042197078993682878, 0.049110105577163055, 0.058329161669709841, 0.076684744483119224, 0.11702345510098387]
wCC = [0.011339998478328677, 0.011679119084663531, 0.013863742651775734, 0.01521528289714268, 0.01787779960826328, 0.0194122892877879, 0.023535277148440125, 0.025266000904449554, 0.035261999262789445, 0.041673688129849742]
wJA = [0.10739181646483814, 0.11421623814400307, 0.11053297540053482, 0.1430716928111942, 0.1601230735400552, 0.19168010235407984, 0.21903009161351189, 0.27739422602780422, 0.34950284878368509, 0.58945381033286726]
wJB = [0.020358746489166094, 0.02145427887488649, 0.023453082862589611, 0.026136400328538988, 0.029433206141532553, 0.034156251365427368, 0.0404805580036873, 0.051093578108013696, 0.067266565007103665, 0.1076680054218957]
wJC = [0.0092166762615452074, 0.01009982813773814, 0.011662020284550226, 0.012621354038609449, 0.014252361338986877, 0.015906893517738524, 0.018787635380954685, 0.023457491721674599, 0.030817049739156156, 0.050333419522597164]

fnCA = ['ICCV', 'AAAI', 'NIPS', 'CVPR', 'ACL', 'IJCAI', 'ICML']
fnCB = ['COLT','UAI','PPSN','KR','ICRA','ICCBR','ICAPS','EMNLP','ECCV','ECAI','COLING','AAMAS']
fnCC = ['ACCV','AISTATS','BMVC','CoNLL','FGR','GECCO','ICANN','ICB','ICDAR','ICONIP','ICPR','ICTAI','IJCNN','IROS','KSEM','NAACL','PRICAI']
fnJA = ['AI','IJCV','JMLR','PAMI']
fnJB = ['IJAR','AAMAS','TNNLS','TFS','TEC','TCYB','TASLP','TAC','NN','NECO','ML','MIT','JAR','DKE','CVIU']
fnJC = ['AIM','Alife','APIN','CSL','DSS','EAAI','ES','ESWA','FSS','IDA','IJNS','IJIS','IJON','IJPRAI','IVC','KBS','MVA','NC','NPL','PAA','PRL','SOCO','tNCA']

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
            word.append( float(line) )
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
            line = line.split('\t')[1]
            word.append( float(line) )
        except:
            print line
    return word

def readAndWrite(filenameIn, filenameOut):
    file=open(filenameIn)
    while 1:
        line = file.readline().replace('\n','')
        if not line:
            break
        writeFile(filenameOut, line+'\n' )

def readFile16(filename, weight, pub, pub2):
    Infilename = r'data/counts/' +pub+ '/'+filename + '/2016'
    file=open(Infilename)
    while 1:
        line = file.readline().replace('\n','')
        if not line:
            break
        outFilename = r'varify/'+pub2+'//' + filename + '.txt'
        writeFile(outFilename, str( (int( (line.split('\t')[1]) )*weight[9] ))+'\n' )
    print filename,'2016','done...'

def readFile15(filename, weight, pub, pub2):
    Infilename = r'data/counts/' +pub+ '/'+filename + '/2015'
    file=open(Infilename)
    while 1:
        line = file.readline().replace('\n','')
        if not line:
            break
        outFilename = r'varify/'+pub2+'//' + filename + '.txt'
        writeFile(outFilename, str((int( (line.split('\t')[1]) )*weight[8] ))+'\n')
    print filename,'2015','done...'

def readFile14(filename, weight, pub, pub2):
    Infilename = r'data/counts/' +pub+ '/'+filename + '/2014'
    file=open(Infilename)
    while 1:
        line = file.readline().replace('\n','')
        if not line:
            break
        outFilename = r'varify/'+pub2+'//' + filename + '.txt'
        writeFile(outFilename, str((int( (line.split('\t')[1]) )*weight[7] ))+'\n')
    print filename,'2014','done...'

def readFile13(filename, weight, pub, pub2):
    Infilename = r'data/counts/' +pub+ '/'+filename + '/2013'
    file=open(Infilename)
    while 1:
        line = file.readline().replace('\n','')
        if not line:
            break
        outFilename = r'varify/'+pub2+'//' + filename + '.txt'
        writeFile(outFilename, str((int( (line.split('\t')[1]) )*weight[6] ))+'\n')
    print filename,'2013','done...'

def readFile12(filename, weight, pub, pub2):
    Infilename = r'data/counts/' +pub+ '/'+filename + '/2012'
    file=open(Infilename)
    while 1:
        line = file.readline().replace('\n','')
        if not line:
            break
        outFilename = r'varify/'+pub2+'//' + filename + '.txt'
        writeFile(outFilename, str((int( (line.split('\t')[1]) )*weight[5] ))+'\n')
    print filename,'2012','done...'

def readFile11(filename, weight, pub, pub2):
    Infilename = r'data/counts/' +pub+ '/'+filename + '/2011'
    file=open(Infilename)
    while 1:
        line = file.readline().replace('\n','')
        if not line:
            break
        outFilename = r'varify/'+pub2+'//' + filename + '.txt'
        writeFile(outFilename, str((int( (line.split('\t')[1]) )*weight[4] ))+'\n')
    print filename,'2011','done...'

def readFile10(filename, weight, pub, pub2):
    Infilename = r'data/counts/' +pub+ '/'+filename + '/2010'
    file=open(Infilename)
    while 1:
        line = file.readline().replace('\n','')
        if not line:
            break
        outFilename = r'varify/'+pub2+'//' + filename + '.txt'
        writeFile(outFilename, str((int( (line.split('\t')[1]) )*weight[3] ))+'\n')
    print filename,'2010','done...'

def readFile09(filename, weight, pub, pub2):
    Infilename = r'data/counts/' +pub+ '/'+filename + '/2009'
    file=open(Infilename)
    while 1:
        line = file.readline().replace('\n','')
        if not line:
            break
        outFilename = r'varify/'+pub2+'//' + filename + '.txt'
        writeFile(outFilename, str((int( (line.split('\t')[1]) )*weight[2] ))+'\n')
    print filename,'2009','done...'

def readFile08(filename, weight, pub, pub2):
    Infilename = r'data/counts/' +pub+ '/'+filename + '/2008'
    file=open(Infilename)
    while 1:
        line = file.readline().replace('\n','')
        if not line:
            break
        outFilename = r'varify/'+pub2+'//' + filename + '.txt'
        writeFile(outFilename, str((int( (line.split('\t')[1]) )*weight[1] ))+'\n')
    print filename,'2008','done...'

def readFile07(filename, weight, pub, pub2):
    Infilename = r'data/counts/' +pub+ '/'+filename + '/2007'
    file=open(Infilename)
    while 1:
        line = file.readline().replace('\n','')
        if not line:
            break
        outFilename = r'varify/'+pub2+'//' + filename+  + '.txt'
        writeFile(outFilename, str((int( (line.split('\t')[1]) )*weight[0] ))+'\n')
    print filename,'2007','done...'

def test_jiashudu():
    i = 0
    for fn in fnCA:
        for year in range(2007, 2017):
            filenameIn = 'data/counts/conferenceA/'+fn + '/' + str(year)
            filenameOut = 'data/counts/conferenceA/'+fn + '/' + str(year) + '.txt'
            try:
                file = open(filenameIn)
                while 1:
                    try:
                        line = file.readline()
                        if not line:
                            break
                        line = np.log( float( line.split('\t')[1] )*wCA[i] )
                        writeFile(filenameOut, str(line) +'\n')
                    except:
                        continue
            except Exception,e: 
                print e
                continue
            i += 1
        print year,'done...'

def jiashudu():
    for fn in fnCA:
        for year in range(2007, 2017):
            filenameIn = 'data/counts/conferenceA/'+fn + '/' + str(year) + '.txt'
            try:
                print readFile(filenameIn)
            except:
                continue

def test(filename, matrix, pub, pub2):
    try:
        readFile16(filename, matrix, pub, pub2)
    except Exception,e:
        print e
    try:
        readFile15(filename, matrix, pub, pub2)
    except Exception,e:
        print e
    try:
        readFile14(filename, matrix, pub, pub2)
    except Exception,e:
        print e
    try:
        readFile13(filename, matrix, pub, pub2)
    except Exception,e:
        print e
    try:
        readFile12(filename, matrix, pub, pub2)
    except Exception,e:
        print e
    try:
        readFile11(filename, matrix, pub, pub2)
    except Exception,e:
        print e
    try:
        readFile10(filename, matrix, pub, pub2)
    except Exception,e:
        print e
    try:
        readFile09(filename, matrix, pub, pub2)
    except Exception,e:
        print e
    try:
        readFile08(filename, matrix, pub, pub2)
    except Exception,e:
        print e
    try:
        readFile07(filename, matrix, pub, pub2)
    except Exception,e:
        print e

def getNewCitationJA(filename):
    fn = 'varify/JA/' + filename + '.txt'
    print filename,'\t', np.mean(readFile(fn))

def getNewCitationJB(filename):
    fn = 'varify/JB/' + filename + '.txt'
    print filename,'\t', np.mean(readFile(fn))

def getNewCitationJC(filename):
    fn = 'varify/JC/' + filename + '.txt'
    print filename,'\t', np.mean(readFile(fn))

def getNewCitationCA(filename):
    fn = 'varify/CA/' + filename + '.txt'
    print filename,'\t', np.mean(readFile(fn))

def getNewCitationCB(filename):
    fn = 'varify/CB/' + filename + '.txt'
    print filename,'\t', np.mean(readFile(fn))

def getNewCitationCC(filename):
    fn = 'varify/CC/' + filename + '.txt'
    print filename,'\t', np.mean(readFile(fn))

def combineFile():
    for fn in fnCA:
        for year in range(2007, 2017):
            fileIN = 'data/counts/conferenceA/'+fn+'/'+str(year)
            try:
                file=open(fileIN)
                fileOUT = 'f:/CA/' + fn + '.txt'
                while 1:
                    line = file.readline().replace('\n','')
                    if not line:
                        break
                    writeFile(fileOUT, line)
            except Exception,e:
                print e
                
def combine():
    for fn in fnJA:
        for year in range(2007, 2017):
            filenameIn = 'data/counts/journalA/'+fn+'/'+str(year)
            filenameOut = 'data/counts/date-year/'+str(year)+'/JA.txt'
            if ( os.path.isfile( filenameIn) ):
                readAndWrite(filenameIn, filenameOut)


def varify():
    for year in range(2007,2017):
        filename = 'data/counts/test/test'+str(year)+'.txt'
        arr = readFile2(filename)
        arr = [np.log(i+1)/(2017-year) for i in arr]
        print np.mean(arr)

def verifyJour():
#     for fn in fnJA:
#         test(fn, wJA, 'journalA', 'JA')
#     for fn in fnJB:
#         test(fn, wJB, 'journalB', 'JB')
#     for fn in fnJC:
#         test(fn, wJC, 'journalC', 'JC')
        
    for fn in fnJA:
        getNewCitationJA(fn)
    for fn in fnJB:
        getNewCitationJB(fn)
    for fn in fnJC:
        getNewCitationJC(fn)

def verifyConf():
#     for fn in fnCA:
#         test(fn, wCA, 'conferenceA', 'CA')
#     for fn in fnCB:
#         test(fn, wCB, 'conferenceB', 'CB')
#     for fn in fnCC:
#         test(fn, wCC, 'conferenceC', 'CC')
#     for fn in fnCA:
#         test(fn, wCA, 'conferenceA', 'CA')
        
    for fn in fnCA:
        getNewCitationCA(fn)
    for fn in fnCB:
        getNewCitationCB(fn)
    for fn in fnCC:
        getNewCitationCC(fn)

if __name__ == '__main__':
    verifyConf()
#     verifyJour()

