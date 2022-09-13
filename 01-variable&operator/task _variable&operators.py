

#Create a Boolean variable named x
x = True

#Create an integer variable named y
y = 3

#Create a float variable named z
z = 2.5

#Create a string variable names s
s = 'abdullah'

#Convert the int variable to float
y = 3.0

#Can we convert the str to int ?
NO we can not

#Create a list of numbers from 1 to 5
d =[1 , 2 , 3, 5]
type(d)
<class 'list'>

#Create a tuple from 10 to 15
h = (10 , 11 , 12 ,13 ,14 ,15 )
type(h)
<class 'tuple'>

#Convert the list to tuple
d =(1 , 2 , 3, 5)
type(d)
<class 'tuple'>

#Create a dict of 3 values
C = {6 : 'abdullah' , 7 :'mohammed' , 8 :'ali'}
type(C)
<class 'dict'>
#Can we use semi colon ; with python
No we can not use it

#Python is interpreted or compiled ?
interpreted
#What is the differences between low level & high level
The low level programming languages are the language of the computer and it consist of 1,0
and it is easy to be excuted and hard to coding and we have to run only computer and to be rewritten to another languages such as C ,Assembley
The high level programming Languages are easy to coding and take less time to program and easy to be corrected and you can run it oenly one program on a diffrent pc such as java ,C# ,python
#What is the differences between = , ==
= it is meaning equal e.g x = 5
== you are asking python what is vlaue of x e.g x == The answer would be 5
#What do we mean by using !=?
we do mean by using is not equal e.g x = 3 x==3 annswer will be True but x != 9 not equal x
#What is the operator precedence?
Multiplication/Division/Addition/Subtraction and etc.
#Create a variable x with value of 10
x = 10
#Increase x value by 15 using assignment operators
x + 15
25
#Divide the x value by 5 using assignment operators
x / 5
2.0
#Multiply the x value by 10 using assignment operator
x *10
100
#Get module of x on 3 using assignment operators
x %3
1
#Using python print the module of 11 to 4
print (11, 10 , 9 , 8 , 7 , 6 , 5 , 4)
11 10 9 8 7 6 5 4
#Print the exponent of 2,3
2**3
8
3**2
9
#Divide 11 by 3 using python division
11/3
3.6666666666666665
#Can we divide 11 by 3 and get an integer number ?
NO we can not because 3.6666666666666665 and it is float not integer. The integer use integers number only.

#Check if 10 is bigger than 15 or not
10 > 15
False
#If 10 is not bigger than15 print x is smaller than 15
x = 10

if x != 15 :
    print('x<15')

x<15

#In which cases we will use all
True
#What is the differences between all , and
username = 'abdullah'
password = 12345

if username == 'abdullah' or password == 12345:
    print('Hello')




username = 'abdullah'
password = 12345

if username == 'abdullah' and password == 12345:
    print('Hello')


    

# all :one username or password are all   correct
# AND : username or password IS both correct .

#What is the differences between any , or
username = 'abdullah'
password = 12345

if username == 'abdullah' or password == 12345:
    print('Hello')




username = 'abdullah'
password = 12345

if username == 'abdullah' and password == 12345:
    print('Hello')


    

# RO :one username or password is  at least one of them correct
# any : username or password is  which one  correct .

#If we need all the conditions to be true we will use ....
elif
#What is the differences between if , elif
if different conditions
elif all in one condition


#Can we use more than one elif
yes we can use as many as you like

#Can we use more than one else
NO we can not

#write s simple ternary operator
print('x<50') if x < 50 else print(x)

#in elif , python will check all the conditions no matter what ?
check until foud the correct one

#in elif we use else for ... ?
check for multiple expressions

#if we have this list [2,4,6,8,10] :
○ check to see if 4 in this list or not

a = [2,4,6,8,10]
 
b = 2
c = 4
d = 6
e = 8
f = 10
if (b) in a:
    print('4  is in this list!')
else:
    print('4 is in this list')

   4  is in this list! 
---------------------------------------
○ check to see if 4 and 6 in this list on not

a = [2,4,6,8,10]
 
b = 2
c = 4
d = 6
e = 8
f = 10
if (c&d) in a:
    print('4 and 6  is in this list!')
else:
    print('4 and 6 is in this list')
4 and 6  is in this list!
---------------------------------------
○ check to see if 3 or 6 in this list

a = [2,4,6,8,10]
 
b = 2
c = 4
d = 6
e = 8
f = 10
g = 3
h = 5
if  g|d in a:
    print('3 or 6 is in this list!')
else:
    print('3 or 6 is not this list')
3 or 6 is not this list
-----------------------------------------------
○ check to see if 2 , 4 and 5 in this list
a = [2,4,6,8,10]
 
b = 2
c = 4
d = 6
e = 8
f = 10
g = 3
h = 5
if  b&c&h in a:
    print('2 , 4 and 5 is in this list!')
else:
    print('2 , 4 and 5 is not this list')
    2 , 4 and 5 is not this list
