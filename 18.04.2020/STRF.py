##### Python String Opeartions ##############

# 1. Break 
for x in range(10):
 if (x==2):
  break
 print(x)
 
# 2. Continue
for x in range (10):
 if (x==4):
  continue
 print(x)

# 3. Pass
for x in range (100):
 if (x==88):
  pass
 print(x)


name="Python"
for n in name:
 if (n == 'h'):
    continue
 print(n);

name1="{} and {}".format("Rajesh","Kunal","Sumit")
print(name1);