
x = 1;
y = 4.8;
z = 1j;
print (type(x));
print (type(y));
print (type(z));

x = 3456789;
y = -8282828288888;
z = 4;
print (type(x));
print (type(y));
print (type(z));

x = 1.0
y = -45566.987
print (type(x))
print (type(y))

# Convert from one type to another
x = 1
y = 2.8
z = 1j

a = float(x) # convert from integer to float
print (a)

b = int(y) # convert float to interger
print (b)

c = complex (x) # convert interger to complex
print (c)

d = complex (y)  # float to complex
print (d)

import random
print (random.randrange(1,999999999999999999999999999999999))

# Specifiying a type on to a variable
# interger
x = int(1)
print (x)
y = int(2.6)
print(y)
z = int("3")
print(z)


# Float
x = float (2)
print (x)
y= float (2.5)
print (y)
z = float ("2.5")
print (z)
print (type(z))


# String

x = str("Hello Baby")
print (x)
y = str (2)
print (y)
z = str (3.0)
print (z)


# To get the posiotion at a particular place
a = "Hello World this is me"
print (a[1])
print (a[0])
print (a[2])
print (a[4])


#Slicing
b = ("Hello world i am coming to the first station")
print(b[5:10]) # here characters from position 5 to position 10(not inculded) in output

#  Negative Indexing
b = "Hello, World!"
print(b[-5:-2])
print(len(b))