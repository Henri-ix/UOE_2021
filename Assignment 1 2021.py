print("Exercise 1")
print("Palindrome numbers from 1-3000 are : ")
number=1
while number != 3000:
    digits=1
    Change_number=number//10
    while Change_number != 0:
        digits=digits+1
        Change_number=Change_number//10
    edited_number=number
    New_number=0
    for i in range (0,digits):
        single_digit= edited_number%10
        edited_number=edited_number//10
        New_number= New_number + (single_digit*(10** (digits-(i+1))))
    if New_number==number:
        print(number)
    number=number+1


print("#######################################################################")
print("Excercise 2")
print("Printing all prime numbers between 100 and 1000")
print("#######################################################################")
number=100
Total=0
count=0
counter=0
while number!=1000:
    count=2
    isPrime=True
    while count != number:
        if number%count == 0 :
            isPrime=False
            break
        if count**count > number:
            break
        count+=1
    if isPrime==True:
        if counter!=9 :
            print(number, end= " ")
            counter+=1
        else:
            print(number)
            counter=0
    number+=1

print("#######################################################################")
print("Excercise 3")
print("Common divisors of common integers")
print("#######################################################################")
num1= int(input("enter the first positive number" ))
while num1<=0:
    num1= int(input("enter the first positive number" ))
num2=int(input("enter the second positive number" ))
while num2<=0:
    num2=int(input("enter the second positive number" ))
count=1
total=0
print("the Common divisors are: " , end = " " )
if num2>num1:
    while count!=num2:
            if num2%count==0 and num1%count==0:
                total+=count
                print(count, end= " " )
            count+=1
else:
    while count!=num1:
            if num2%count==0 and num1%count==0:
                print(count, end= " ")
                total+=count
            count+=1
print(" ")
print("the Sum is: ", total)

def factorial(number):
    count=number-1
    while count >1:
        number=number*count
        count-=1
    if number==0:
        return 1
    else:
        return number


print("#######################################################################")
print("Exercise 4")
print("Calculating Polynomials")
print("#######################################################################")
Total_n1=0
Total_n=0
Total_n2=0
n=int(input("please enter the value for n:"))
while n<=1:
    n=int(input("please enter the value for n"))
n1= n-1
factorial_n1=n1
factorial_n1=factorial(factorial_n1)
print("binomial coefficients for ", n-1, ":", end = " " )
for k in range (0,n1+1):
    print(factorial_n1/((factorial(n1-k))*factorial(k)), end= " " )
print(" ")
factorial_n=n
factorial_n=factorial(factorial_n)
print("binomial coefficients for ", n, ":", end = " ")
for k in range (0,n+1):
    print(factorial_n/((factorial(n-k))*factorial(k)), end= " " )
print(" ")
n2= n+1
factorial_n2=n2
factorial_n2=factorial(factorial_n2)
print("binomial coefficients for ", n+1, ":", end = " ")
for k in range (0,n2+1):
    print(factorial_n2/((factorial(n2-k))*factorial(k)), end= " " )
print(" ")
x=int(input("enter your value for x"))
y= int(input("enter your value for y"))
for k in range (0,n1+1):
    Total_n1+=(factorial_n1/((factorial(n1-k))*factorial(k)))*(x**(n1-k))*(y**k)
for k in range (0,n+1):
    Total_n+=((factorial_n/((factorial(n-k))*factorial(k)))*(x**(n-k))*(y**k))
for k in range (0,n2+1):
    Total_n2+=((factorial_n2/((factorial(n2-k))*factorial(k)))*(x**(n2-k))*(y**k))
print("Calculated value for (", x, "+", y, ")**", n1,"=", Total_n1)
print("Calculated value for (", x, "+", y, ")**", n,"=" ,Total_n)
print("Calculated value for (", x, "+", y, ")**", n2,"=" ,Total_n2)
        
    
        
    
    
        
        
        
        
    
    
    
    
    
    
        
                
                
            
            
            
        
        
        
        
        
        
        

    
    
