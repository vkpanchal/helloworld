name=["Raj","Rohan","Vinit","Sumit","Anil"];
name.append("Kunal");
print("After Append value",name);
name.insert(2,"Vikash");
print("After insert value",name);
name.remove("Sumit");
print("Remove Value",name);
name.pop();
name.pop();
name.pop();
name.pop();

print("using pop fun",name);

del name[0];
print("useing del fun",name);
name1=["abc","bbc","Raj","Rajesh"];
print("Value of name1",name1);
name1.clear();
print("Using clear fun",name1);
name3=["Raj","Rohan","Sumit","Amit"];
n=name3.copy();
print("Using copy fun of list",n);
add=["NCR","GGN","Noida"];
print("Using join",name3+add);

thislist = list(("apple", "banana", "cherry")) 
# note the double round-brackets
print("using double round brackets:",thislist)





