import time
import math
import sys

sys.setrecursionlimit(2000000)

fraction = 0.14159265358979323846264338327950288419716939937510582097 # 50 digits of π after decimal point

firstNumerator = 0
firstDenominator = 1

secondNumerator = 1
secondDenominator = 1

counter = 0

def getFraction(firstNumerator, firstDenominator, secondNumerator, secondDenominator, counter=0):

    midpointNumerator = firstNumerator + secondNumerator
    midpointDenominator = firstDenominator + secondDenominator
    midpoint = float(midpointNumerator/midpointDenominator)

    if fraction < midpoint:
        secondNumerator = midpointNumerator
        secondDenominator = midpointDenominator
    elif fraction > midpoint:
        firstNumerator = midpointNumerator
        firstDenominator = midpointDenominator

    counter += 1

    if counter == 200000:
        return [midpointNumerator, midpointDenominator]

    return getFraction(firstNumerator, firstDenominator, secondNumerator, secondDenominator, counter)


def getPi():
   fractionPart = getFraction(firstNumerator, firstDenominator, secondNumerator, secondDenominator)
   pi = [3*fractionPart[1] + fractionPart[0], fractionPart[1]]
   piFraction = f"π is approximately equal to = {pi[0]}/{pi[1]}"
   return piFraction

print(getPi())