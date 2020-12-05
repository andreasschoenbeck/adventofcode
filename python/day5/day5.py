import re


def getBinarySeat (seat, lowerRange, upperRange):
    lower = lowerRange
    upper = upperRange

    for i in range(len(seat)):
        half = ((upper - lower + 1) / 2)
        upperHalf = lower + half
        if seat[i] == 'F' or seat[i] == 'L':
            upper = upperHalf-1
        else:
            lower = upperHalf
    
    return upper

def getSeatId(seat):
    row = getBinarySeat(seat[0:7], 0, 127)
    col = getBinarySeat(seat[7:10], 0, 7)

    seatId = (row * 8) + col
    return seatId

def part1():
    highestSeatId = 0
    for seat in seats:
        seatId = getSeatId(seat)

        if seatId > highestSeatId:
            highestSeatId = seatId
            print("new highest: " + str(highestSeatId))

def part2():
    list = []
    for seat in seats:
        seatId = getSeatId(seat)
        list.append(seatId)
    
    list.sort()
    
    for i in range(75,865):
        if(i != list[i-75]):
            print("my seat: ", i)
            break


seats = []
with open("F:\\programming\\github\\adventofcode\\python\\day5\\input_01.txt", 'r') as f:
    seats = f.readlines()




#part1()
part2()