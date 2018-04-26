# # while true:

# a=int(input("Enter a number:"))

# if(a % 2)== 0:
 
#   print("{} is even ".format(a))
# else:
#   print("{} is odd".format(a))
# a=int(input('enter a number:'))
# for i in range(1,10,1):
#   print(a,'x',i,'=',(a*i))

# a = [i*i for i in range(0,11)]
# print(a)

# a=int(input('enter a number:'))
# if(a>0):
# 	print("positive")
# elif(a==0):
# 	print("neutral")	
# else:
# 	print("negative")


# a = (int(input(enter a number))
# a=100
# for i in range (1,101):
# 	if(a%i==0):
# 		num=15
# 		for j in range (1,num):
# 			if(num%j)==0:
# 				print(j)
# a=int(input('enter a number:'))
# b=even
# d= odd
# while (i % 2)== 0:

# change the value for a different result
# num = 7

# uncomment to take input from the user
# num = int(input("Enter a number: "))

# factorial = 1

# # check if the number is negative, positive or zero
# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    for i in range(1,num + 1):
#        factorial = factorial*i
#    print("The factorial of",num,"is",factorial)

# key=int(input("Enter the key (int) to be added:"))
# value=int(input("Enter the value for the key to be added:"))
# d={}
# d.update({key:value})
# print("Updated dictionary is:")
# # print(d)
# d = {'Red': 1, 'Green': 2, 'Blue': 3} 
# for e, value in d.items():
#      print(e, 'corresponds to ', d[e]) 

import sqlite3

db = sqlite3.connect('database.db')