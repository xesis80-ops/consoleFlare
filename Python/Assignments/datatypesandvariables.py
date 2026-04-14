#Give a command that displays your introduction in 3 lines.
print("Hey ! My name is rohit chhabra. \nI am currently studying Data Science at ConsoleFlare. \nI live in Kanpur.")

#Write a program and create a variable, store an integer value in it, and print the value.
a=14
print(a)

''' Write a program and create three variables called name, age, and company then store your name, your age, and your company's name in it, and 
Print your name, age, and company.
Now display the message "After 5 Years".
Now you have switched to another company. Update the company variable and display your new company. '''
name,age,company = "Rohit","23","ConsoleFlare"
print("After 5 Year")
company = "ConFlare"
print(company)

# Declare a variable and store the value of pi in it. Display the value and check the type of it.
pi = 3.14
print(pi,type(pi))

'''Write a program to create two variables a and b which have 2 and 3 as data stored in them. Now create a program that swaps the data which means the data stored in a is 3 and data stored in b is 2.
(WITH THE HELP OF A THIRD VARIABLE).'''
a,b = 2,3
c = a
a = b
b = c
print(a,b)

'''Write a program to create two variables a and b which have 5 and 10 as data stored in them. Now create a program that swaps the data which means the data stored in a is 10 and data stored in b is 5.
(WITHOUT USING A THIRD VARIABLE).'''
a,b = 5,10
#Method-1
b,a = 5,10
print(a,b)
#Method-2
a = a+b
b = a-b
a = a-b
print(a,b)

#What is wrong in this code snippet?
a,b,c=1,2
print("Value of C is missing")

'''a,b,c=22,33,78
print(a,c)
What will be the output of this code?'''

print("22,78")


# You have to create three variables A, B, and C. Store 2000 in all of them. This task can be done by two methods:
print("A,B,C = 2000,2000,2000 or A=B=C=2000")

'''What will be the output of the following code?
x = 10 
y = 5.5 
z = "10" 
print(type(x), type(y), type(z))'''
print("class<int> , class <float> , class <string>")

'''Check the data type of the following:
a. 2+3
b. '56+78'
c. 'True + False * 0'
d. 32+0.0
e. 7834+57.23'''
print("int,str,str,float,float")