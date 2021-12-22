str = input("Enter any String\n")
str1 = ""
L=str
str = [i[0].upper()+i[1:] for i in L.split()]
str1= ' '.join(str)
print(str1)

str = "String Slicing in Python"
print("Given string is :\n",str)
print()
print("Reverse string is :\n",str[::-1])

str = "String Slicing in Python"
print("Given string is:\n",str)
word = str.split(" ")
print("First two character of each string:")
for i in word:
     print(i[0:2], end = " ")

x,y=10,20
print("x =",x)
print("y =",y)
print("Multiplication of x and y=",x*y)

n=int(input("Please provide the number to calculate it\'s factorial\n"))
print("you entered the number =",n)
fact=1
for i in range(1,n+1):
    fact=fact*i
print("Factorial of given number is = ",fact)