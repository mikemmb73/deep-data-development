# -*- coding: utf-8 -*-
"""
Naive Bayes Outline and Testing
Emma Anderson
Adapted from Jason Brownlee
"""


import csv
import random
import math

#function to load the file into a list of floats
def loadCSV(filename):
    lines = csv.reader(open(filename, 'r'))
    dataset = list(lines)
    for i in range(len(dataset)):
        dataset[i] = [float(x) for x in dataset[i]]
    return dataset

#function to split the list 
def splitDataset(dataset, splitRatio):
    trainSize = int(len(dataset)*splitRatio)
    trainSet = []
    copy = list(dataset)
    while len(trainSet) < trainSize:
        index = random.randrange(len(copy))
        trainSet.append(copy.pop(index))
    return[trainSet, copy]
    

#function to split the data into a dictionary of separate classes

#make functions for mean and standard deviation

#function to summarize the data - mean and stdev for each attribute

#function to make a summary by class label

#functions for Gaussian probability density (equation then returning by class)

#functions to get predictions

#function to determine accuracy


        
#TEST 1
#filename = 'pima-indians-diabetes.data.txt'
#dataset = loadCSV(filename)
#print('Loaded data file', filename, 'with', len(dataset), 'rows')

#TEST 2
dataset = [[1], [2], [3], [4], [5]]
splitRatio = 0.67
train, test = splitDataset(dataset, splitRatio)
print('Split', len(dataset), 'rows into train with', train, 'and test with', test)

#TEST 3
#dataset = [[1, 20, 1], [2, 21, 0], [3, 22, 1]]
#separated = separateByClass(dataset)
#print('Separated instances:', separated)

#TEST 4
#numbers = [1, 2, 3, 4, 5]
#print('Summary of', numbers, ': mean=', mean(numbers), 'stdev=', stdev(numbers))

#TEST 5
#dataset = [[1, 20, 1], [2, 21, 0], [3, 22, 1]]
#summary = summarize(dataset)
#print('Attribute summaries', summary)

#TEST 6
#dataset = [[1, 20, 1], [2, 21, 0], [3, 22, 1], [4, 22, 0]]
#summary = summarizeByClass(dataset)
#print('Summary by class value', summary)

#TEST 7
#x = 71.5
#thismean = 73
#thisstdev = 6.2
#probability = gaussianProbability(x, thismean, thisstdev)
#print('Probability of belonging to this class', probability)

#TEST 8
#summaries = {0:[(1, 0.5)], 1:[(20, 5.0)]}
#inputVector = [1.1, '?']
#probabilities = gaussianByClass(summaries, inputVector)
#print('Probabilities for each class', probabilities)

#TEST 9
#summaries = {'A':[(1, 0.5)], 'B':[(20, 5.0)]}
#inputVector = [1.1, '?']
#result = predict(summaries, inputVector)
#print('Prediction:', result)

#TEST 10
#summaries = {'A':[(1, 0.5)], 'B':[(20, 5.0)]}
#testSet = [[1.1, '?'], [19.1, '?']]
#predictions = getPredictions(summaries, testSet)
#print('Predictions:', predictions)

#TEST 11
#testSet = [[1, 1, 1, 'a'], [2, 2, 2, 'b'], [3, 3, 3, 'b']]
#predictions = ['a', 'a', 'a']
#accuracy = getAccuracy(testSet, predictions)
#print('accuracy:', accuracy)
