def write_file():
	name=input("Enter name: ")
	reg=input("Enter reg no: ")
	f=open("file.txt","w")
	f.write(str(name))
	f.write("\n")
	f.write(str(reg))
	f.close()
def read_file():
	count=0
	var=str(input("Enter letter: "))
	f=open("file.txt","r")
	data=f.read()
	for i in data:
		if var==i:
			count=count+1
	print("no of ",var)
	print(count)
	f.close()
write_file()
read_file()