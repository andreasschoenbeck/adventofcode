
# coordinates like this:
#    ---
#    32101234
# -1 X X X
#  0  X O X X
#  1 X X X
#  2

directions = { 'ne': (-1,1), 'e': (0,2), 'se': (1,1), 'sw': (1,-1), 'w': (0,-2), 'nw': (-1,-1) }

def readInput():
    lines = []
    paths = []

    #with open("F:\\programming\\github\\adventofcode\\python\\day24\\input_01.txt", 'r') as f:
    with open("C:\\data\\dotnet_projects\\adventofcode\\python\\day24\\input_02.txt", 'r') as f:
        lines = f.readlines()

    for line in lines:
        currentLine = line.strip()

        instructions = []
        i = 0
        while i < len(currentLine):
            instruction = currentLine[i]
            if instruction == 's' or instruction == 'n':
                i+=1
                instruction += currentLine[i]
            
            instructions.append(instruction)
            i += 1
        
        paths.append(instructions)

    return paths

def flipTiles(paths):
    tiles = dict()

    for path in paths:
        row = 0
        col = 0

        for instruction in path:
            direction = directions[instruction]
            row += direction[0]
            col += direction[1]
        
        # flip
        tile = (row, col)
        if tile in tiles:
            tiles[tile] = not tiles[tile]
        else:
            tiles[tile] = False # flipped to black up

    return tiles
        
def countBlackTiles(tiles):
    onlyBlack = list(filter(lambda x: not x, tiles.values()))
    return len(onlyBlack)


def printTiles(tiles):
    minRow, maxRow, minCol, maxCol = getDimensions(tiles)
    
    for row in range(minRow, maxRow+1):
        line = ""
        for col in range(minCol, maxCol+1):
            if (row,col) in tiles:
                line += "W" if tiles[(row,col)] else "B"
            else:
                line += " "
        print(line)

def getDimensions(tiles):
    minRow = None
    maxRow = None
    minCol = None
    maxCol = None

    for row, col in tiles:
        if minRow == None or minRow > row:
            minRow = row
        if maxRow == None or maxRow < row:
            maxRow = row
        if minCol == None or minCol > col:
            minCol = col
        if maxCol == None or maxCol < col:
            maxCol = col
    return minRow, maxRow, minCol, maxCol

def flipTilesIteration(tiles):
    minRow, maxRow, minCol, maxCol = getDimensions(tiles)

    evenMinCol = minCol-2 if minCol%2 == 0 else minCol-1
    oddMinCol = minCol-1 if minCol%2 == 0 else minCol-2

    evenRange = range(evenMinCol, maxCol+3,2)
    oddRange = range(oddMinCol, maxCol+3, 2)

    newTiles = dict()

    for row in range(minRow-1, maxRow+2): 
        lineRange = None
        if row%2 == 0:
            # even row gets even cols
            lineRange = evenRange
        else:
            lineRange = oddRange

        for col in lineRange:
            if not (row, col) in tiles:
                newTiles[(row,col)] = True
            if needsFlippin(row, col, tiles):
                if not (row,col) in tiles:
                    newTiles[(row,col)] = False # flipped from white
                else: 
                    newTiles[(row,col)] = not tiles[(row, col)]

    return newTiles


def needsFlippin(row, col, tiles):

    blackCount = 0
    for rowOffset, colOffset in directions.values():
        neighbourCoord = (row+rowOffset, col+colOffset)
        if neighbourCoord in tiles and not tiles[neighbourCoord]:
            blackCount += 1

    if (row,col) in tiles and not tiles[(row,col)]:
        # black
        return blackCount == 0 or blackCount > 2
    else:
        # white
        return blackCount == 2


paths = readInput()
tiles = flipTiles(paths)
count = countBlackTiles(tiles)
#tiles = flipTilesIteration(tiles)
printTiles(tiles)
print("Number of black tiles: " + str(count))