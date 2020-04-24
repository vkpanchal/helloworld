
numbers = range(1,11)
'''
the range(a,b) function creates a list of number 1 to (b-1)
So, in this case it would generate
numbers from 1 to 10
'''
for number in numbers:
        #check the skipping condition
        if number == 7:
                #this statement will be executed
                print("7 is skipped")
                continue
                #this statement won't be executed
                print ("This won't be printed")
 
        #print the values
        #for example:
        #2 is double of 1
        print (number*2),
        print ("is double of"),
        print (number)
