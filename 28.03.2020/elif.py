#this is a single line comment
'''
This is a m line 
'''
m=120;
tot=700;
p=m*100/tot;
print(p);
if p<30:
 print("Fail:",p);
elif  p>=30 and p<45:
 print("Pass",p);
elif p>=45 and p<60:
 print("Good",p);
elif p>=60 and p<75:
 print("Very Good",p);
elif p>=75 and p<=100:
 print("Excelent",p);
else:
 print("Not Found",p);

 
 
	