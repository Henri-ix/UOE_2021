#Exercise2
print("PART A")
print("combines two sentences and prints all words alphabetically")
Sent1 = input("Enter your first sentence: ") #First Sentence is input by the user
Sent1=Sent1 + " "  #makes sure theres a space at the end of the sentence so that the first word of the next sentence is seperate
Sent2 = input("Enter you second sentence: ") #Second Sentence is input by the user
SentComb= Sent1+Sent2 # joins both sentences
SentComb = SentComb.lower() #makes all characters lowercase
Array=[] #creates and empty list
Word= " " #creates an empty string
for i in range (0,len(SentComb)): # runs a loop that repeats the code below as many times as the length of the String "SentComb"
    if ord(SentComb[i])>=97 and ord(SentComb[i])<=122: #only runs the code below if the character referenced is in the ascii 97-122, which is a-z
        Word += SentComb[i] # adds the referenced character into the  empty string
    elif len(Word) > 1: #checks if the length of the string is bigger than one to verify that a character is in fact in the string
        Array.append(Word) #adds the Word to the Array
        Word=" " #resets the String
    if i==len(SentComb)-1: #checks to see if the current iteration is the last one
        Array.append(Word) #adds the word to the array
Array.sort() #Sorts the List  alphabetically
Final_word=' '
for i in range(0,len(Array)):
    Final_word += Array[i]
print(Final_word) #Outputs the sorted List

print("#######################################################################")
print("Part B")
print("reverses a string and adds in -* in between, and adds * to the beginning and end")
def Switch(User_str): #defines  the function with a string as the argument
    Reverse=" " #empty string to add in the reversed and edited values
    for i in range (0,len(User_str)): #loop repeats itself, the amount of repeats depends on the length of the string 
        Reverse+= "*" + User_str[len(User_str)-(i+1)] #adds in the * to the  string followed by the refernced character in the User entered string, from last to first character
        if i==len(User_str)-1: #checks to see if it is at the end of the loop 
            Reverse+= "*" #adds the "*" to the end of the string as we have reached the end
        else:
            Reverse+="-" #adds the "-" to the next string
    print(Reverse) #outputs the new string

Str = input("enter your sentence") #asks the user to enter the string
Switch(Str) #carries out the function and takes in "Str" as the Argument
    
    
    
    
    
    


