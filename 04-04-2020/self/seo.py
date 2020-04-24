max=int(input("Please enter the maximum number value: "))
even_sum= 0
odd_sum= 0
num=1
while (num<=max):
 if num%2==0:
  even_sum= even_sum+num
  print("The sum of Even number 1 to entered number is ", even_sum)
 else:
  odd_sum= odd_sum+num
  print("The sum of Odd NUmber 1 to entered number is ", odd_sum)
 num+=1