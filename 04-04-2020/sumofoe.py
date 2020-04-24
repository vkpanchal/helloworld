#Python program to calculate sum of odd and even numbers using while loop
max=int(input("please enter the maximum value: "))
even_Sum=0
odd_Sum=0
num=1
while (num<=max):
    if (num%2==0):
        even_Sum=even_Sum+num
        print("The sum of Even numbers 1 to entered number", even_Sum)
    else:
        odd_Sum=odd_Sum+num
         #print("The sum of Even numbers 1 to entered number", odd_Sum)
        num+=1
  #print("The sum of Even numbers 1 to entered number", even_Sum)
 # print("The sum of Even numbers 1 to entered number", odd_Sum)