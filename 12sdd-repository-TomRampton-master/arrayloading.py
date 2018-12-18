##The load array routine should:
##
##prompt the user to enter a number
##check that the entered value is valid
##add the number to the array
##return the program to the main routine when user enters a sentinal
##value such as "xxx"
def loadArray(mainarray):
    n = 0
    Arrayinput = input("enter a number into the array, or quit to stop the session: ")    
    
    while Arrayinput != 'quit':
        while Arrayinput.isdigit() == False and Arrayinput != 'quit':
           Arrayinput = input("invalid input, enter only numbers. Try again ")

        if Arrayinput != 'quit':
            mainarray.append(Arrayinput)
            n = n+1
            print("there is now " + str(n) + " in the array")
            Arrayinput = input("please enter a number, or quit to stop the session ")
    
    return(mainarray)






