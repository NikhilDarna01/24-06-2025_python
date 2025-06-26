name=input("Enter Your Name:")
print("Your Name is :- " + name)

''' Operators '''
print("   -: Operators :-   ")

a=int(input("Enter A value :- "))
b=int(input("Enter B value :- "))

# Arithmetic operators:-
print("   -: ArithMetic Operators :-   ")
print("a and b sum is :- " + str(a+b))
print("a and b sub is :- " + str(a-b))
print("a and b Multiply is :- " + str(a*b))
print("a and b dividedby is :- " + str(a/b))
print("a and b persentage is :- " + str(a%b))
print("a and b root is :- " + str(a**b))


print("   -: Assignment Operators :-   ")
#Assignment operators
# syntax = "variable = value"

name = "Ram"
print(name)

x=int(input("Enter Assignment operator x value :- "))
y=int(input("Enter Assignment operator y value :- "))


y+=x
print("x = ", x, "and y = ", y)

y -= x        # y = y - x
print("x =", x, "and y =", y)

y *= x        # y = y * x
print("x =", x, "and y =", y)

x /= y        # x = x / y
print("x =", x, "and y =", y)

x //= y        # x = x // y
print("x =", x, "and y =", y)

x %= y    # x = x % y
print("x =", x, "and y =", y)

x **= y       # x = x ** y
print("x =", x, "and y =", y)


# Comparsion Operators
print("   -: Comparsion Operators :-   ")



c=int(input("Enter Comparsion operator c value :- "))
d=int(input("Enter Comparsion operator D  value :- "))

print("c =", c, "d =", d)
print("c < d  is", c < d)
print("c <= d is", c <= d)
print("c > d  is", c > d)
print("c >= d is", c >= d)
print("c == d is", c == d)
print("c != d is", c != d)


print("   -: Logical Operators :-   ")
#Logical :
e=10
f=20
print(e>1 and f<100)
print(e>1 or f<0)
print(not(e>1 and f<0))

print("   -: Membership Operators :-   ")
#membership

print("z" in "zebra")  # True

email = "ravi@yahoo.com"
print(("@" in email) and (".com" in email))  # True

print("x" not in email)  # True
print("x" in email)      # False

emails = ["nik@gmail.com", "nik@yahoo.com", "ravi@outlook.com"]
email = "nikhil@gmail.com"
print(email in emails)     # True
print(email not in emails) # False



#Identity
print("   -: Identity Operators :-   ")
f = 20
g = f
print(f is g)
print(f is not g)

z = 20
print(f is z)

print("   -: Data Types :-   ")
#Datatypes
print("   -: Numbers and Numeric :-   ")
#Numbers/numeric
print("   -: int :-   ")
#int
num = 100
print(type(num))
print(25 * 4)

print("   -: float :-   ")
# float
rate = 3.75
print(type(rate))
print(rate + 1.25)

print("   -: complex :-   ")
# complex
c1 = 2 + 3j
c2 = 1 - 1j
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)

a=1
print(type(a))
print(10+3)

print("   -: float :-   ")
#float
print(1.3+0.2)
a=2.8
print(type(a))

print("   -: Strings :-   ")
#srting
print("   -: Char/str :-   ")
#char/str
city = "Hyderabad"
print(city)
print(type(city))

print("   -: Non String :-   ")
#Non-nothing
data = None
print(data)
print(type(data))



