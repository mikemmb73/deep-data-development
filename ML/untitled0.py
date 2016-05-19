import csv
import random
import math
import operator
import statistics

answers = {}

def euclidian_distance(item1, item2, attributes):
    distance = 0
    for x in range(attributes):
        distance+=(float(item1[x]) - float(item2[x]))**2
    return math.sqrt(distance)

    
def loadDataset(filename, split, trainingSet, testSet):
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        newdata = []
        indicies = [4,5,7]
        for x in range(1,len(dataset)-1):
            #this needs to change in a different dataset  
            newdata.append([])
            for y in indicies:
                newdata[-1].append(float(dataset[x][y]))
            if random.random() < split:
                trainingSet.append(newdata[x - 1])
            else:
                testSet.append(newdata[x - 1])
                
def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response]+=1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key = operator.itemgetter(1), reverse = True)
    return sortedVotes[0][0]

def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct+=1
    return(correct/float(len(testSet)))*100.0
    
#def optimize(testSet, trainingSet):
    
# Replace getNeighbors with this
#David Micheleman created these two functions below
def getNeighbors(trainingSet, testpoint, k, answers=None):
    testpoint_hashable = str(testpoint)
    if answers is not None:
        if testpoint_hashable not in answers:
            answers[testpoint_hashable] = getAllNeighbors(trainingSet, testpoint, answers=answers)
        return answers[testpoint_hashable][0:k]
    else:
        return getAllNeighbors(trainingSet, testpoint, answers=answers)[0:k]


def getAllNeighbors(trainingSet, testpoint, answers=None):
    distances = []
    for i in trainingSet:
        distances.append((euclidian_distance(testpoint, i, len(i) - 1), i))
    distances.sort(key=lambda tup: tup[0])
    return distances
    

def kNN():
    trainingSet = []
    testSet = []
    split = 0.98
    loadDataset('datatraining.txt', split, trainingSet, testSet)
    bests = []
    for k in range (1, 15):
        avgresult = 0
        result_set = []
        print("!!!!!!!")
        print("Hey there! Now starting optimization for k = ",k)
        print("See you soon!")
        print("!!!!!!!")
        for times in range(10):
            predictions = []
            for x in range(len(testSet)):
        
                neighbors = getNeighbors(trainingSet, testSet[x], k)
                result = getResponse(neighbors)
                predictions.append(result)
                #print('predicted:' + str(result) + ', actual:' + str(testSet[x][-1]))
            accuracy = getAccuracy(testSet, predictions)
            result_set.append(accuracy)
        avgresult = statistics.mean(result_set)
        print("DONE! Average accuracy ", avgresult)
        print()
        print()
        bests.append([avgresult, k])
    print("Wow! That was a lot of work! Let's see which k value was the most efficent!")
    the_best_ones = sorted(bests, key = operator.itemgetter(0))
    print("Okay I got it! The most accurate k value is a value of ", the_best_ones[0][1], " with an accuracy level of ", bests[0][0])
    
    
kNN()