



# The handshake used by the card and the door involves an operation that transforms a subject number. To transform a subject number, start with the value 1. Then, a number of times called the loop size, perform the following steps:

#     Set the value to itself multiplied by the subject number.
#     Set the value to the remainder after dividing the value by 20201227.

def getLoopSize(subjectNumber, publicKey):
    loopSize = 0
    value = 1

    while value != publicKey:
        value = transform(value, subjectNumber)
        loopSize += 1

    return loopSize

def transform(value, subjectNumber):
    newValue = value*subjectNumber
    newValue %= 20201227
    return newValue

def calculate(subjectNumber, loopSize):
    value = 1
    for i in range(loopSize):
        value = transform(value, subjectNumber)

    return value


# publicCardKey = 5764801
publicCardKey = 6929599
loopSizeCardKey = getLoopSize(7, publicCardKey)
# publicDoorKey = 17807724
publicDoorKey = 2448427
loopSizeDoorKey = getLoopSize(7, publicDoorKey)

print("loop size for public key '" + str(publicCardKey) + "' (card): " + str(loopSizeCardKey))
print("loop size for public key '" + str(publicDoorKey) + "' (door): " + str(loopSizeDoorKey))

encryptionKey = calculate(publicDoorKey, loopSizeCardKey)

print("encryption key for the public key of the door and the card's loop size: " + str(encryptionKey))