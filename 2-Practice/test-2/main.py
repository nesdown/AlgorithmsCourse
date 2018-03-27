'''
The code provided here is a simple implementation of merge sort
combined with inversions counter. It is based on the task from
Algorithms Theory Course of Kyiv Polytechnical University
and same-named Prometheus Course.

Bohdan Glushko, 24.02.18
'''

import os

#toolslist functions
#this one is for splitting an array in two parts.
def splitList(arr):
    half = len(arr)/2
    return arr[:half], arr[half:]

#Function set to count inversions
def makeMerged(inputArray):
    #Is there a sense to check this array?
    if len(inputArray) > 1:
        leftPart, rightPart = splitList(inputArray)

        #and here we call functions to count desperate inversions
        leftPart, xInv = makeMerged(leftPart)
        rightPart, yInv = makeMerged(rightPart)

        resultPart, zInv = countMerged(leftPart, rightPart)
        return resultPart, (xInv + yInv + zInv)

    #there is nothing to do here, getting out!
    else:
        return inputArray, 0

def countMerged(leftPart, rightPart):
    #define an index of results
    i, j, invSum = 0, 0, 0 #left and righ indexes, sum of all inversions
    output = []

    #let's just count how many splitted inversions we have
    while (i < len(leftPart) and j < len(rightPart)):
        if leftPart[i] <= rightPart[j]:
            output.append(leftPart[i])
            i += 1
        else:
            output.append(rightPart[j])
            j += 1
            invSum += (len(leftPart) - i)

    for k in range(i, len(leftPart)):
        output.append(leftPart[k])

    for k in range(j, len(rightPart)):
        output.append(rightPart[k])

    return output, invSum

def generateRatings():
    userToCheck = int(raw_input("Enter the number of a user: "))
    fileOpen = open(raw_input("Enter filename: "), 'r')          # open file for reading

    arr = []                              # initialize empty array
    for line in fileOpen:
      arr.append(line.strip().split(' ')) # split each line on the <space>, and turn it into an array
                                          # this creating an array of arrays.
    fileOpen.close()

    usrNum = int(arr[0][0])
    filmNum = int(arr[0][1])

    arr.pop(0)
    for i in arr:
        i.pop(0)
    # print arr

    newArr = [[]]
    for i in range(len(arr)):
        tempoArr = [i+1, arr[i]]
        newArr.append(tempoArr)
    newArr.pop(0)
    return newArr, userToCheck, usrNum, filmNum

def getFinalResult():
    inputArray, userToCheck, userNumber, filmsNumber = generateRatings()
    #inputArray - default array here userToCheck - user's index userNumber - how many users are here filmsNumber - how many films
    userTop = inputArray[userToCheck-1][1]

    # #debug part
    # print(inputArray)
    # print()
    # print(userTop)

    outputArray = []

    #debug part
    # print(userTop)

    for i in range(0, userNumber):
        if i != userToCheck - 1:
            tempoArr = []
            # print(inputArray)
            for j in range(len(userTop)):
                tempoArr.append(inputArray[i][1][userTop.index(str(j+1))])
            out = makeMerged(tempoArr)
            outputArray.append([i + 1, out[1]])

    formFile(outputArray, userToCheck)

def formFile(inpArr, usrInd, ):
    fileOut = open('ip71_glushko_02_output.txt', 'w')
    fileOut.write(str(usrInd) + '\n')

    #This part of file output creation was taken from StackOverflow
    for subArray in sorted(inpArr, key = lambda i: int(i[1])):
        s = ' '.join([str(n) for n in subArray])
        print>>fileOut, ' '.join([str(n) for n in subArray])
    fileOut.write(str(usrInd))
    fileOut.close()

    with open('ip71_glushko_02_output.txt') as f:
        for line in f:
            print(line)

getFinalResult()
