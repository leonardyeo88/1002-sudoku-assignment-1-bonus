import functions

inputArray = ["P1", "P2", "P3", "Q1", "Q2", "Q3", "R1", "R2", "R3"]                                 #init list "inputArray" with temporary coordinate labels
coordArray = []                                                                                     #init coordArray
listAcceptedChar = ["A", "B", "C"]                                                                  #init list "listAcceptedChar" which contains A, B and C

functions.populateListWithCoordinates(coordArray)                                                   #populate the "coordArray" list with coordinates

''' --- start main application--- '''
functions.displayBoard(inputArray)                                                                  #display empty board

for x in range(len(inputArray)):                                                                    #loops based the length of inputArray
    if(functions.checkInput(coordArray[x], x, inputArray, listAcceptedChar, coordArray) == True):   #checks if input is valid, updates into the board
        functions.displayBoard(inputArray)                                                          #displays the updated board
        
print "This is a valid sudoku board"
''' --- end main application--- '''
