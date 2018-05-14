import sys
# Copyright 2018 Arshitha Basavaraj <arshitha@bu.edu>
# Copyright 2018 Swarnim Sinha <swarnims@bu.edu>
# msg = "Given board " + str(sys.argv[1]) + "\n";
msg = ''
values = sys.argv[1].replace('[','').split(']')
size = len(values) - 2
# reversed because the height starts from the bottom
boardValues = values[:-1][::-1]
print(boardValues)
lastMadeMove = values[-1].replace('LastPlay:','').replace('(','').replace(')','').split(',')

# sys.stderr.write('LastMove:'+str(lastMadeMove)+'Stage'+str(boardValues));

def findNeighbors(boardStatus, lastMove):
    try:
        height = int(lastMove[1])
        leftIndex = int(lastMove[2])
        rightIndex = int(lastMove[3])
        # left, right, topleft, topright, bottomleft, bottomright
        neighbors = [(height, leftIndex-1), (height, rightIndex-1), (height+1, leftIndex), (height+1, rightIndex), (height-1, leftIndex), (height-1, rightIndex)]
        return neighbors
        # sys.stderr.write(str(neighbors))
    except:
        return []

def printAvailable(boardStatus, neighbors, lm):
    available = []
    unavailable = []
    for i,j in neighbors:
        try:
            if boardStatus[i][j] == '0':
                available.append((i,j))
            else:
                unavailable.append((i,j))
            # sys.stderr.write(boardStatus[i][j] + '\n')
        except IndexError:
            continue
    return available, unavailable
    # pass

neighbors = findNeighbors(boardValues, lastMadeMove)
# if lastMadeMove[0] != 'null':
availableMoves, unavailableMoves =  printAvailable(boardValues, neighbors, lastMadeMove)
print(unavailableMoves)
if len(availableMoves) > 0:
    sys.stderr.write(str(availableMoves[0]))
    # if not availableMoves[0]:
    i,j = availableMoves[0]
    k = (size + 2) - (int(i) + int(j))
    sys.stdout.write("(3,"+str(i) + "," + str(j) + "," + str(k)+")")
#else
sys.stdout.write("(3,2,2,2)")
#perform intelligent search to determine the next move

#print to stdout for AtroposGame
