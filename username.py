passwordDictionary = {"raj" : "prav","bharath" : "1234"}

attempt=0
flag=0
while (attempt!=3):
	name = input(" enter a user name :")
	password = input("please enter a password :")
	if(name in passwordDictionary and passwordDictionary[name] == password):
		flag=1
		break
	else :
		attempt=attempt+1
		if(attempt==3):
			print("you have tried max no:of times")
if(flag==1):
	print("Thanks for entering the right username and passwors",name)
	


