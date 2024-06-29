#python prog

print("hello, world")

#print
x=20
print(x)

#function
def my_fun():
    print("Hello from fun")
my_fun()
def new_fun(name):
    print(name + "Reshma")
new_fun("Sharon ")

#if else
y=10
if x>y:
    print("x is greater")

#import math
import math
print(math.factorial(4))

#sum
print(x + y)

#sqr root
import math
print(math.sqrt(x))

#area of triangle
x = 10
y = 20
area = 0.5*x*y
print(area)

# Solve the quadratic equation
import cmath
a=1
b=5
c=4
d= (b**2)-(c*a*2)
ans1=( -b-(cmath.sqrt(d)))/(2*a)
ans2=( -b-(cmath.sqrt(d)))/(2*a)
print(ans1)
print(ans2)


#swap no
print("before swap")
print(a, b)
print("after swap")
print(b, a)

#random num
import random
print(random.randrange(0,10))

#celcius to far
cel=35
far=(cel*1.8)/32
print("%0.2f celcius is converted into %0.2f farenheit " %(cel,far))

#km to miles
km=1200
mil=km*0.621371
print(mil)

#pos or neg num
n=int(input("Enter num: "))
if n > 0:
    print("postive")
elif n==0:
    print("zero")
else:
    print("negative")

#odd or even
m=int(input("Enter num: "))
if (n%2 == 0):
    print("even")
else:
    print("odd")

#leap year
s=int(input("Enter year: "))
if(s%4==0 and s%100!=0) or (s%400==0) :
    print("leap year")
else:
    print("not leap year")

#min max
num1=10
num2=5
num3=23
if (num1>=num2 or num1>=num3):
    print("num1 is grt")
elif (num2>=num1 or num2>=num3):
    print("num2 is greater")
else:
    print("num3 is greater")

#prime num
w=int(input("enter num: "))
f=False
if w==1:
    print("not prime")
elif w>1:
    for i in range(2, w):
        if(w%i==0):
            f=True
            break
if (f==True):
    print("not prime")
else:
    print("prime")

lower=900
upper=1000
for num in range(lower, upper+1):
    if num>1:
        for i in range(2, num):
            if(num%i==0):
                break
        else:
            print(num)

#multiplication table
p=12
for i in range(0,10):
    print(p,"*",i," = ",p*i)

#fibonacci
def fib(n):
    if(n==0):
        return 0
    if(n==1 or n==2):
        return 1
    else:
        return fib(n-1)*fib(n-2)
print(fib(10))