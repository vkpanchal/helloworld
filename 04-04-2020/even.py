# Python program to print Even Numbers in given range 

start, end = 4, 100
ce=0;

# iterating each number in list 
for num in range(start, end + 1): 
	
	# checking condition 
	if num % 2 == 0: 
		ce=ce+1;
		print("Count of Even:",ce);
		print(num, end = " ") 
