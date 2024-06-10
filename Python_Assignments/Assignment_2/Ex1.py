#Excerise 1
#Part A

def Occurence(Array,Num): #Defining the function with the name "Occurence", with 2 paramaters, "Array" will be the list and "Num" will be the integer
    Count=0 #initialise count, this value will increment by one every time there is an occurence of Num in Array
    for i in range (0,len(Array)): # Loop is repeated from 0 to the length of Array
        if Array[i]==Num: 
            Count+=1                # if the index for the the value of I in the array is the same as the number we are checking, increase count  by 1
    print(Num, "is in this list ", Count, "times.") # outputs the number that is being checked and how many times its in the list

print("Finding the occurence of a number in a list")
Array=[] #creates an empty Array/List
Indexes= input("enter the amount of values your list has: ") #recieves an input from the user
while Indexes.isdigit()== False: 
    Indexes= input("That is not a number ,enter the amount of values your list has: ") #makes sure the input is a number and allows the user to reinput if it isnt
Indexes= int(Indexes)
for i in range (0,Indexes): #Loop is repeated by the value input by the user for the Indexes Variable, this is so all values can be added
    entry=input("enter the next number in the list: ") 
    while entry.isdigit() == False:
        entry=input("That is not a number, enter the next number in the list: ")
    entry=int(entry)
    Array.append(entry) #asks for an input and adds it to the list "Array"
    
Number = input("enter the number you are looking for: ") #the number that the user wants to check the occurences of
while Number.isdigit() == False:
    Number = input("that is not a number, enter the number you are looking for: ")
Number = int(Number)
Occurence(Array,Number)# calling the function "Occurence" with the variables Array and Number as the parameter
    
#Part B
print("#######################################################################")
print("circular shifting an array")
def circular_shift(Array2,Shift): #defines the function circular_shift  requiring arguments Array2 and shift which are  a list and an int respectively
    for i in range (0,Shift): #runs this loop "shift" amount of times
        Carry=Array2.pop(0) #removes the first value in the the list and saves it to the Carry variable
        Array2.append(Carry) #adds the value saved to "Carry" to the back of the list
    print("Shifted list = ", Array2) # Outputs the changes list
    

Array2=[] #creates and empty Array/List
Indexes=input("enter the amount of values your list has: ") #recieves an input from the user
while Indexes.isdigit() == False:
    Indexes= input("That is not a number ,enter the amount of values your list has: ")
Indexes=int(Indexes)
for i in range (0,Indexes): #Loop is repeated by the value input by the user for the Indexes Variable, this is so all values can be added
    Value=input("enter the next number in the list: ")
    while Value.isdigit() ==False:
        Value=input("That is not a number, enter the next number in the list: ")
    Value = int(Value)
    Array2.append(Value) #asks for an input and adds it to the list "Array2"
Shift = input("Enter the amount of shifts you want to do, please know that this must be less than the values in your list :")#the user enters how many times they want to shift the list
while Shift.isdigit() == False:
    Shift = input("that is not a number, enter the amount of shifts you want to do, please know that this must be less than the values in your list :")
Shift=int(Shift)
while Shift>=Indexes: 
    Shift = input("Enter the amount of shifts you want to do, please know that this must be less than the values in your list :")#makes sure the user doesnt enter a number bigger than the length of the list, or the shift will be bigger than the actual Array
    while Shift.isdigit() == False:
        Shift = input("that is not a number, enter the amount of shifts you want to do, please know that this must be less than the values in your list :")
    Shift=int(Shift)
circular_shift(Array2,Shift) #Calls the function circular_shift with Array2 and shift as the parameters

