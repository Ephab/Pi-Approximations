#This is an unoptimized implementation of the Chudnovsky algorithm
#This implementation does not use Binary Splitting

from mpmath import mp
import time

mp.dps = 2000 # set precision of floating point numbers


def chudnovsky(n):
    sum = 0
    for k in range(0, n):
        numerator = mp.power(-1, k) * mp.factorial(6*k) * ((545140134*k) + 13591409)
        denominator = mp.factorial(3*k) * mp.factorial(k)**3 * mp.power(640320,(3*k + 3/2))
        sum += numerator / denominator

    oneOverPi = 12 * sum
    return mp.power(oneOverPi,-1)


calc1TimeStart = time.time()
calculatedPi = str(chudnovsky(4000))
calc1TimeEnd = time.time()
print(f"\nUnoptimized Chudnovsky algorithm took {calc1TimeEnd - calc1TimeStart:.2f} seconds")

existingTimeStart =time.time()
actualPi = str(mp.pi)
existingTimeEnd =time.time()
print(f"Pre-existing algorithm took {existingTimeEnd - existingTimeStart:.5f} seconds")


print(f"\ncalculated digits: {len(calculatedPi)}", end="")
print(f"\nactual digits: {len(actualPi)}")

sharedLength = min(len(calculatedPi), len(actualPi))

calculatedPiDigits = calculatedPi[:sharedLength]
actualPiDigits = actualPi[:sharedLength]

counter = 0

for actual, calculated in zip(actualPiDigits, calculatedPiDigits):
    counter += 1
    if actual != calculated:
        break

print(f"\n\n--calculated pi is accurate to the {counter}th number--\n")