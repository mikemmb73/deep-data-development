# -*- coding: utf-8 -*-
"""
Created on Mon May  9 13:30:08 2016

@author: mikebaldwin
"""

import tokenizing_and_misspelling as token
import bayes_classifier as bayes
import time

filename = "training_neatfile.csv"
positive = []
negative = []
neutral = []

print("Fixing lists give me a second!")
positive, negative, neutral = token.loadDataset(filename)
positive = token.fixList(positive)
negative = token.fixList(negative)
neutral = token.fixList(neutral)

print("\n" * 30)

count = 0
print("HERE I GO! See you soon!")
print()
print()
print()
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("GO!")
time.sleep(1)
for i in range(len(positive)):
    print("\n" * 25) 
    print("I have checked " + str(i) + " words!")
    count += bayes.get_message_probability(positive[i], positive, [negative, neutral])
    
accuracy = count/len(positive)
print("our program is " + str(accuracy * 100) + " times awesome")
