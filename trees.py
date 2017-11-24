from math import log

def clacShannonEnt(dataSet):
    numEntries = len(dataSet)
    labeCounts = {}
    for featVec in dataSet:
        correntLabel = featVec[-1]
        if correntLabel not in labeCounts.keys():
            labeCounts[correntLabel] = 0
        labeCounts[correntLabel] +=1
    shannonEnt = 0.0
    for key in labeCounts:
        prob = float(labeCounts[key]) / numEntries
        shannonEnt -=prob * log (prob,2)
    return shannonEnt

def creatDataSet():
    dataSet = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
    labels = ['no surfacing','flippers']
    return dataSet,labels
def splitDataSet(dataSet, axis, value):
    retdataset = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retdataset.append(reducedFeatVec)
    return retdataset
