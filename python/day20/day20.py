import re

edges = dict()
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

    tiles[id] = 0 # matching edgecount

    edges[(id,0)] = lines[0]
    edges[(id,1)] = ''.join(map(lambda s: s[-1], lines))
    edges[(id,2)] = lines[-1]
    edges[(id,3)] = ''.join(map(lambda s: s[0], lines))
    
    



readInput()