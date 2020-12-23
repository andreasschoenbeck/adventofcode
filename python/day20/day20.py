import re
import math

edges = dict()
matchingEdges = dict()
tiles = dict()

def readInput():
    
    content = ""
    with open("C:\\data\\dotnet_projects\\adventofcode\\python\\day20\\input_01.txt", 'r') as f:
        content = f.read()

    tilesList = content.split('\n\n')

    for tile in tilesList:
        readTile(tile)

def readTile(tile):
    lines = list(tile.split('\n'))
    match = re.match("Tile ([0-9]*):", lines.pop(0))
    id = match[1]

    matchingEdges[id] = [] 

    edges[(id,0)] = lines[0]
    edges[(id,1)] = ''.join(map(lambda s: s[-1], lines))
    edges[(id,2)] = lines[-1]
    edges[(id,3)] = ''.join(map(lambda s: s[0], lines))

    tiles[id] = tile[1:]

def findMatchingEdges():
    edgeKeys = list(edges.keys())
    for i in range(len(edgeKeys)):
        key = edgeKeys[i]
        value = edges[key]

        for j in range(i+1,len(edgeKeys)):
            compareKey = edgeKeys[j]
            compareValue = edges[compareKey]

            if compareKey[0] == key:
                # ignore the edges of the same tile
                continue
            else:
                if value == compareValue or ''.join(reversed(value)) == compareValue:
                    matchingEdges[key[0]].append((key, compareKey))
                    matchingEdges[compareKey[0]].append((key, compareKey))

def stitchImage(startingTile):
    global matchingEdges

    side = math.sqrt(len(matchingEdges))
    neighbors = matchingEdges[startingTile]

    


readInput()
findMatchingEdges()

corners = list(filter(lambda t: len(matchingEdges[t])==2, matchingEdges))

result = 1
for corner in corners:
    result *= int(corner)

print("corner ids multiplied: " + str(result))

# stitch tiles - start with first corner, then go left to right by following the tiles dict
# rotate and flip as needed e.g. #1,1 -> #2,3 and #2,2 has no partner -> flip top to bottom
# remove edge and add to picture
# (show picture)
# find seamonsters - hm.... probably manually see if there's a rotation/flip needed for the picture
# then create a mask with offset tuples and make a compare method, send it all possible coordinates and replace all pixels with O if found
# count remaining #...
# uff

stitchImage(startingTile=corners[0])