##1. Even or Odd
a = 0
if a==0:
  print("Number is Zero")
elif  (a % 2) ==0:
   print ("number is divisibal by 2")
else:
   print("number if odd") 
  
## 2. Largest of Three Numbers
### Input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
   largest = a
elif b>= a and b>=c:
   largest = b
else:
   largest = c
print("The LArgest Number is:", largest)

###Simple Calculator
#Ask the user for:
#	•	two numbers
#	•	an operation (+, -, *, /)
#Perform the operation and print the result.
a = int(input("first number:"))
b = int(input("second number:"))
op = input("tell me the operation:") ##python takes this operand directly
match op:
case "+": result= a + b 
case "-": result= a + b
case "*": result= a + b
case "/": result= a + b
  
print("the result is:", result)
