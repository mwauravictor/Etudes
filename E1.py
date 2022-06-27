bareLand = '.'
cell = '@'
neighbor = '#'
fieldSize = 90
#function to find neighbours
def cellNeighbor(x, j):
    n1 = [x-1, j-1]
    n2 = [x-1, j]
    n3 = [x-1, j+1]
    n4 = [x, j-1]
    n5 = [x, j+1]
    n6 = [x+1, j-1]
    n7 = [x+1, j]
    n8 = [x+1, j+1]

    nList = [n1, n2, n3, n4, n5, n6, n7, n8]
    return nList
# initial list of cell positions
initList = []
initList.append([9, 9])
initList.append([10, 10])
initList.append([10, 11])
initList.append([9, 11])
initList.append([8, 11])
# initList.append([12, 10])
# initList.append([12, 11])
# initList.append([12, 12])
# initList.append([12, 13])
# initList.append([12, 14])



def generationRules(cellList):
    theDead = []
    survivers = []
    theRevived = []
    nextList = []

    # Find the cells that survive and those that die
    for cell in cellList:
        neibacount = 0
        nList = cellNeighbor(cell[0], cell[1])
        for i in nList:
            if i in cellList:
                neibacount += 1
        # print(f'Cell {cell} has {neibacount} live neighbor(s)')
        if neibacount < 2:
            # print(f'Cell {cell} dies of loneliness')
            theDead.append(cell)
        elif neibacount > 3:
            # print(f'Cell {cell} dies of overcrowding')
            theDead.append(cell)
        else:
            # print(f'Cell {cell} survives')
            survivers.append(cell)
    # Find the cells that are born again
    for i, row in enumerate(range(1, fieldSize + 1)):
        for j, column in enumerate(range(1, fieldSize + 1)):
            if [i, j] not in cellList:
                #print(f'{[i, j]} not in cellList')
                nList2 = cellNeighbor(i, j)
                neibacount2 = 0
                for nn in nList2:
                    if nn in cellList:
                        neibacount2 += 1
                if neibacount2 == 3:
                    # print(f"Cell {[i, j]} will be revived")
                    theRevived.append([i, j])
                # else:
                #     print("I'm not a happy man")

	#the end List to be used as input for next generation
    nextList.extend(survivers)
    nextList.extend(theRevived)

    return nextList

    # print(theDead)
    # print(survivers)
    # print(theRevived)


# generationRules(initList)
#Loop that prints the grid.
quit = False
while not quit:
    print("\x1b[2J\x1b[H", end="")
    for i, row in enumerate(range(1, fieldSize + 1)):
        for j, column in enumerate(range(1, fieldSize + 1)):
            for position in initList:
                if i == position[0] and j == position[1]:
                    print(f'{cell:2}', end="")
                # else:
            if [i, j] not in initList:
                print(f'{bareLand:2}', end="")
        print()
    initList = generationRules(initList)
    # quit += 1




#born again cells
# if [i, j] not in cellList:
#     # print(f'{[i, j]} not in cellList')
#     nList2 = cellNeighbor(i, j)
#     neibacount2 = 0
#     for nn in nList2:
#         if nn in cellList:
#             neibacount2 += 1
#     if neibacount2 == 3:
#         print("I'm a happy man")
#         theRevived.append([i, j])
#     else:
#         print("I'm not a happy man")

#Thinking of building a Graphical interface for display
