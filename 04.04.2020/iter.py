mytuple = ("Banana", "Orange", "Grapes")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))



###################################
#String also iterable

mystr = "RamKishan"
myit= iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


#######################################
# Looping Through an Iterator

mytuple = ("sam", "tam", "non")
for x in mytuple:
 print(x)

########################################

str = "samister"
for x in str:
 print(x)


##########################################

# The while Loop
# With the while loop we can execute a set of statements as long as a condition is true.

# Example
# Print i as long as i is less than 6:

i = 1
while i < 6:
  print(i)
  i += 1

# Print i as long as i is less than 99:
i = 65
while i < 99:
 print(i)
 i += 1
 

#The break Statement
#With the break statement we can stop the loop even if the while condition is true:

#Example
#Exit the loop when i is 3:

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#The continue Statement
#With the continue statement we can stop the current iteration, and continue with the next:

#Example
#Continue to the next iteration if i is 3:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#The else Statement
#With the else statement we can run a block of code once when the condition no longer is true:

#Example
#Print a message once the condition is false:

i = 1
while i < 6:
 print(i)
 i += 1
else:
 print("i is no longer less than 6")


##################

#Python program to calculate sum of odd and even numbers using while loop
max=int(input("please enter the maximum value: "))
even_Sum=0
odd_Sum=0
num=1
while (num<=max):
    if (num%2==0):
        even_Sum=even_Sum+num
    else:
        odd_Sum=odd_Sum+num
    num+=1
print("The sum of Even numbers 1 to entered number", even_Sum)
print("The sum of Odd numbers 1 to entered number", odd_Sum)