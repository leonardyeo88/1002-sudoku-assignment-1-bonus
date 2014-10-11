'''
This functions takes in 3 inputs:
1) var (user's input)
2) varCoord (input coordinate, e.g. P1 = 11, Q1 = 21, R1 = 31 and etc)

Outputs:
Either True or False. Depends on the processing in the function
'''
def checkTop(var, varCoord):
    xCoord = varCoord[0]                                                        #gets x coordinate
    yCoord = varCoord[1]                                                        #gets y coordinate

    topArrayVar = []                                                            #array to store coordinates
    topInputVarArray = []                                                       #array to store values from locations above the current input
    topReturnArray = []                                                         #array to store "false" and "true" values
 
    if xCoord == "1":                                                           #if x coordinate is 1
        topCoord = "%s%s" % (xCoord, yCoord)                                    #combines x coordinate and y coordinate
        topArrayVar.append(topCoord)                                            #adds to list array
    elif xCoord == "2":                                                         #if x coordinate is 2
        for x in range(1):                                                      #runs 1 loop
            newXCoord = int(xCoord)-1                                           #takes current x coordinate and minus 1, saves into new variable "newXcoord"
            topCoord = "%s%s" % (newXCoord, yCoord)                             #combines "newXCoord" and y coordinate
            topArrayVar.append(topCoord)                                        #addes to list array
    elif xCoord == "3":                                                         #if x coordinate is 3
        for x in range(2):                                                      #runs 2 loops
            newXCoord = int(xCoord)-1                                           #takes current x coordinate and minus 1, saves into new variable "newXcoord"
            topCoord = "%s%s" % (newXCoord, yCoord)                             #combines "newXCoord" and y coordinate
            topArrayVar.append(topCoord)                                        #addes to list array
            xCoord = newXCoord                                                  #x coordinate stores "newXCoord" value

    '''
    gets the values of input locations which could be above the current input from the user
        example.
        r1 is the current user input. above r1 is q1 and p1.
        the function retrieve the values from q1 and p1 and stores them into the "topInputVarArray" list
    '''
    for x in range(len(coordArray)): 
        for y in range(len(topArrayVar)):
            if(coordArray[x] == topArrayVar[y]):
                topInputVarArray.append(inputArray[x])

    '''
    checks if the user input matches the values in "topInputVarArray" list
        example.
        r1 is the current input and has the value A
        q1 has the value A
        p1 has the value B

        r1 checks with q1, decides that they match, "topReturnArray" list stores "false"
        r1 checks with p1, decides that they do not match, "topReturnArray" list stores "true"
    '''
    for x in range(len(topInputVarArray)):
        if(var == topInputVarArray[x]):
            topReturnArray.append("false")                                      #false = has the input "var" in inputVarArray
        else:
            topReturnArray.append("true")                                       #true = doesnt have the input "var" in inputVarArray

    '''
    checks if "topReturnArray" list contains "false",
    if any values in "topReturnArray" list contains "false", checkTop function will return "False"

        example.
        "topReturnArray" list contains ["false", "true"],
        "false" is found in "topReturnArray" list,
        returns False
    '''
    if any("false" in s for s in topReturnArray):
         return False
    else:
         return True

def checkBottom(var, varCoord):
    xCoord = varCoord[0]
    yCoord = varCoord[1]

    bottomArrayVar = []
    bottomInputVarArray = []
    bottomConfirmationArray = []
    bottomReturnArray = []

    if xCoord == "1":
        for x in range(2):
            newXCoord = int(xCoord)+1
            bottomCoord = "%s%s" % (newXCoord, yCoord)
            bottomArrayVar.append(bottomCoord)
            xCoord = newXCoord
    elif xCoord == "2":
        for x in range(1):
            newXCoord = int(xCoord)+1
            bottomCoord = "%s%s" % (newXCoord, yCoord)
            bottomArrayVar.append(bottomCoord)
    elif xCoord == "3":
        bottomCoord = "%s%s" % (xCoord, yCoord)
        bottomArrayVar.append(bottomCoord)
            
    for x in range(len(coordArray)):
        for y in range(len(bottomArrayVar)):
            if(coordArray[x] == bottomArrayVar[y]):
                bottomInputVarArray.append(inputArray[x])

    #print inputVarArray

    for x in range(len(bottomInputVarArray)):
        if(var == bottomInputVarArray[x]):
            bottomReturnArray.append("false") #true = has the input "var" in inputVarArray
        else:
            bottomReturnArray.append("true") #true = doesnt have the input "var" in inputVarArray

    #print bottomReturnArray

    if any("false" in s for s in bottomReturnArray):
         return False
    else:
         return True

def checkLeft(var, varCoord):
    xCoord = varCoord[0]
    yCoord = varCoord[1]

    leftArrayVar = []
    leftInputVarArray = []
    leftConfirmationArray = []
    leftReturnArray = []

    if yCoord == "1":
        leftCoord = "%s%s" % (xCoord, yCoord)
        leftArrayVar.append(leftCoord)
        
    elif yCoord == "2":
        for x in range(1):
            newYCoord = int(yCoord)-1
            leftCoord = "%s%s" % (xCoord, newYCoord)
            leftArrayVar.append(leftCoord)
    elif yCoord == "3":
        for x in range(2):
            newYCoord = int(yCoord)-1
            leftCoord = "%s%s" % (xCoord, newYCoord)
            leftArrayVar.append(leftCoord)
            yCoord = newYCoord
            
    for x in range(len(coordArray)):
        for y in range(len(leftArrayVar)):
            if(coordArray[x] == leftArrayVar[y]):
                leftInputVarArray.append(inputArray[x])

    #print inputVarArray

    for x in range(len(leftInputVarArray)):
        if(var == leftInputVarArray[x]):
            leftReturnArray.append("false") #true = has the input "var" in inputVarArray
        else:
            leftReturnArray.append("true") #true = doesnt have the input "var" in inputVarArray

    #print leftReturnArray

    if any("false" in s for s in leftReturnArray):
         return False
    else:
         return True

def checkRight(var, varCoord):
    xCoord = varCoord[0]
    yCoord = varCoord[1]

    rightArrayVar = []
    rightInputVarArray = []
    rightConfirmationArray = []
    rightReturnArray = []

    if yCoord == "1":
        for x in range(2):
            newYCoord = int(yCoord)+1
            rightCoord = "%s%s" % (xCoord, newYCoord)
            rightArrayVar.append(rightCoord)
            yCoord = newYCoord
        
    elif yCoord == "2":
        for x in range(1):
            newYCoord = int(yCoord)+1
            rightCoord = "%s%s" % (xCoord, newYCoord)
            rightArrayVar.append(rightCoord)
    elif yCoord == "3":
        rightCoord = "%s%s" % (xCoord, yCoord)
        rightArrayVar.append(rightCoord)
            
    for x in range(len(coordArray)):
        for y in range(len(rightArrayVar)):
            if(coordArray[x] == rightArrayVar[y]):
                rightInputVarArray.append(inputArray[x])

    #print inputVarArray

    for x in range(len(rightInputVarArray)):
        if(var == rightInputVarArray[x]):
            rightReturnArray.append("false") #false = has the input "var" in inputVarArray
        else:
            rightReturnArray.append("true") #true = doesnt have the input "var" in inputVarArray

    #print rightReturnArray

    if any("false" in s for s in rightReturnArray):
         return False
    else:
         return True

def validateMiddleOfTheBoard(var, varCoord):

    if varCoord == "21":
        if var == inputArray[1]:
            return False
        else:
            return True
    else:
        return True

def validate(var, varCoord):
    if(not validateMiddleOfTheBoard(var, varCoord)):
        return "invalid"
    if(not checkTop(var, varCoord)
       or not checkBottom(var, varCoord)
       or not checkLeft(var, varCoord)
       or not checkRight(var, varCoord)):
        return "invalid"
    else:
        return "valid"
        
    
def updateBoard(var, varCoord):
    for x in range(len(coordArray)):
            if(coordArray[x] == varCoord):
                inputArray[x] = var
    
def checkInput(coord, num):
    counter = "invalid"
    while(counter == "invalid"):
        var = raw_input("Enter "+inputArray[num]+": ")
        varUpper = var.upper()
        if(validate(varUpper, coord) == "valid"
           and any(varUpper in s for s in listAcceptedChar)
           and varUpper != ""):
            updateBoard(varUpper, coordArray[num])
            counter = "valid"
            return True
        else:
            print "invalid"
            counter = "invalid"

def displayBoard():
    print "Board"
    print "-----------------"
    i=1
    for x in range(len(inputArray)):
        print inputArray[x]+"\t",
        if(i % 3 == 0):
            print "\n"
        i+=1
            

inputArray = ["P1", "P2", "P3", "Q1", "Q2", "Q3", "R1", "R2", "R3"]
coordArray = []
listAcceptedChar = ["A", "B", "C"]

''' populate the "coordArray" list with coordinates '''
for x in range(1, 4):
    for y in range(1, 4):
        var = str(x)+""+str(y)
        coordArray.append(var)


''' --- start main --- '''
displayBoard() #display empty board

for x in range(len(inputArray)):
    if(checkInput(coordArray[x], x) == True):
        displayBoard()
        
print "This is a valid sudoku board"
''' --- end main --- '''
