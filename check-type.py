"""
Armstrong number checker
checks if the number given is equal to the sum of power of each digit of the number to the number of digits
example- 153 = 1^3 + 5^3 + 3^3  (number of digits = 3)
         1634 = 1^4 + 6^4 + 3^4 + 4^4  (number of digits = 4)
"""
n=input("Enter number to check : ")
sum=0
#traversing the digits of input in string form
for i in n:
    #adding the digit to the power of number of digits in sum variable     
    sum += int(i)**len(n)
#ternary operator, checking if resultant sum is equal to the given number itself
print("Yes, its an Armstrong number") if (sum==int(n)) else print("No, its not an Armstrong number")
#=======================================================================================================================================================================================================================#

