#open the file 
file = open("addresses.txt.py", 'r')
varA = input("Enter MAC addresss")

#Look at each line
#If the Mac addresses is in it: We have foundthe vendor

file = open ('addresses.txt.py', 'rb')
for line in file:
	if varA in str(line):
		print (line)
