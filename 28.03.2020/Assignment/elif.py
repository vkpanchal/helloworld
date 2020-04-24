
print("***********Check your Bonus for the financial year 2019-2020*************");



salary=int(input("Please enter your Salary per month"));
print("Your Salary per month is ", salary);
b1=salary*20/100;
b2=salary*30/100;
b3=salary*50/100;
if salary<=20000:
 print ("Your Bonus is 20% of your salary, which is", b1)
elif salary<50000:
 print ("Your Bonus is 30% of your salary, which is", b2)
elif salary<70000:
 print ("Your Bonus is 50% of your salary, which is", b3)
else