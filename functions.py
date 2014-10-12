"""
Function validates with TOP coodinates 
This function takes in 2 inputs:
1) var (user's input)
2) varCoord (input coordinate, e.g. P1 = 11, Q1 = 21, R1 = 31 and etc)

Outputs:
Either True or False. Depends on the processing in the function
"""
def checkTop(var, varCoord, coordArray, inputArray):
    xCoord = varCoord[0]                                                        #gets x coordinate
    yCoord = varCoord[1]                                                        #gets y coordinate

    topArrayVar = []                                                            #array to store coordinates
    topInputVarArray = []                                                       #array to store values from coordinates above the current input coordinate
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
            if(coordArray[x] == topArrayVar[y]):                                #if indexed value of coordArray is equal to the indexed value of topArrayVar
                topInputVarArray.append(inputArray[x])                          #adds the indexed value of inputArray into topInputVarArray

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
            topReturnArray.append("false")                                      #adds "false" into topReturnArray
        else:
            topReturnArray.append("true")                                       #adds "true" into topReturnArray

    '''
    checks if "topReturnArray" list contains "false",
    if any values in "topReturnArray" list contains "false", checkTop function will return "False"

        example.
        "topReturnArray" list contains ["false", "true"],
        "false" is found in "topReturnArray" list,
        returns False
    '''
    if any("false" in s for s in topReturnArray):                               #checks if there is any "false" in topReturnArray
         return False                                                           #return False if topReturnArray contains "false"
    else:
         return True                                                            #return True if topReturnArray contains "true"

"""
Function validates with BOTTOM coodinates 
This function takes in 2 inputs:
1) var (user's input)
2) varCoord (input coordinate, e.g. P1 = 11, Q1 = 21, R1 = 31 and etc)

Outputs:
Either True or False. Depends on the processing in the function
"""
def checkBottom(var, varCoord, coordArray, inputArray):
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
            bottomReturnArray.append("false") 
        else:
            bottomReturnArray.append("true") 

    #print bottomReturnArray

    if any("false" in s for s in bottomReturnArray):
         return False
    else:
         return True

"""
Function validates with LEFT coodinates 
This function takes in 2 inputs:
1) var (user's input)
2) varCoord (input coordinate, e.g. P1 = 11, Q1 = 21, R1 = 31 and etc)

Outputs:
Either True or False. Depends on the processing in the function
"""
def checkLeft(var, varCoord, coordArray, inputArray):
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
            leftReturnArray.append("false") 
        else:
            leftReturnArray.append("true") 

    #print leftReturnArray

    if any("false" in s for s in leftReturnArray):
         return False
    else:
         return True

"""
Function validates with RIGHT coodinates 
This function takes in 2 inputs:
1) var (user's input)
2) varCoord (input coordinate, e.g. P1 = 11, Q1 = 21, R1 = 31 and etc)

Outputs:
Either True or False. Depends on the processing in the function
"""
def checkRight(var, varCoord, coordArray, inputArray):
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
            rightReturnArray.append("false") 
        else:
            rightReturnArray.append("true") 

    #print rightReturnArray

    if any("false" in s for s in rightReturnArray):
         return False
    else:
         return True

"""
Function 
This function takes in 2 inputs:
1) var (user's input)
2) varCoord (input coordinate, e.g. P1 = 11, Q1 = 21, R1 = 31 and etc)

Outputs:
Returns True if the value of var is not the same as the value of P1
Returns False if the value of var is the same as the value of P1
"""

def validateMiddleOfTheBoard(var, varCoord, inputArray):

    if varCoord == "21":
        if var == inputArray[1]:
            return False
        else:
            return True
    else:
        return True

"""
Function that validates user input on the board by accessing validateMiddleOfTheBoard(), checkTop(), checkBottom(), checkLeft() and checkRight()
This function takes in 2 inputs:
1) var (user's input)
2) varCoord (input coordinate, e.g. P1 = 11, Q1 = 21, R1 = 31 and etc)

Outputs:
1) Returns "invalid" if validateMiddleOfTheBoard function is False
2) Returns "invalid" if any of the function(checkTop, checkBottom, checkLeft, checkRight) returns False
Example:
checkTop checkBottom checkLeft checkRight Result
------------------------------------------------
false    true         true      true       "invalid"
true     false        true      true       "invalid"
true     true         false     true       "invalid"

3) Returns "valid" if any of the function(checkTop, checkBottom, checkLeft, checkRight) returns True
Example:
checkTop checkBottom checkLeft checkRight Result
------------------------------------------------
true    true        true      true       "valid"
"""
def validate(var, varCoord, inputArray, coordArray):

    if(not validateMiddleOfTheBoard(var, varCoord, inputArray)):
        return "invalid"
    
    if(not checkTop(var, varCoord, coordArray, inputArray)
       or not checkBottom(var, varCoord, coordArray, inputArray)
       or not checkLeft(var, varCoord, coordArray, inputArray)
       or not checkRight(var, varCoord, coordArray, inputArray)):
        return "invalid"
    else:
        return "valid"
        
"""
Function that updates the board based on the input value and coordinates
This function takes in 2 inputs:
1) var (user's input)
2) varCoord (input coordinate, e.g. P1 = 11, Q1 = 21, R1 = 31 and etc)
3) coordArray
4) inputArray
"""    
def updateBoard(var, varCoord, coordArray, inputArray):
    for x in range(len(coordArray)):
            if(coordArray[x] == varCoord):
                inputArray[x] = var

"""
Function that updates the board based on the input value and coordinates
This function takes in 2 inputs:
1) num (used for getting the indexed value from inputArray)
2) coord (input coordinate, e.g. P1 = 11, Q1 = 21, R1 = 31 and etc)
3) inputArray
4) listAcceptedChar
5) coordArray

Output:
Returns True if the input is valid by the following conditions:
1) not empty,
2) not duplicated input when
checked with checkTop function, checkBottom function,
checkLeft function, checkRight function)
3) equals to A or B or C
"""
def checkInput(coord, num, inputArray, listAcceptedChar, coordArray):
    counter = "invalid"
    while(counter == "invalid"):
        var = raw_input("Enter "+inputArray[num]+": ")
        var = var.upper()
        if(validate(var, coord, inputArray, coordArray) == "valid"
           and any(var in s for s in listAcceptedChar)
           and var != ""):
            updateBoard(var, coordArray[num], coordArray, inputArray)
            counter = "valid"
            return True
        else:
            print "invalid"
            counter = "invalid"

"""
Function that prints out a board
This function takes in 1 inputs:
1) inputArray

Output:
prints out a 3 x 3 board with coordinates
"""
def displayBoard(inputArray):
    print "\n"
    print "Board"
    print "-----------------"
    i=1
    for x in range(len(inputArray)):
        print inputArray[x]+"\t",
        if(i % 3 == 0):
            print "\n"
        i+=1

"""
Function to populate the "coordArray" list with coordinates
This function takes in 1 inputs:
1) coordArray (coordinate list array)

Output:
populated coordArray
"""
def populateListWithCoordinates(coordArray):
    for x in range(1, 4):
        for y in range(1, 4):
            var = str(x)+""+str(y)  #creates coordinate
            coordArray.append(var)  #add coordinate to coordArray
