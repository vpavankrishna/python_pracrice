#arithmetical operations
"""a=float(input('a='))
b=float(input('b='))
print('sum = ',a+b)
print('difference = ',a-b)
print('multiplication = ',a*b)
print('division = ',a/b)"""

#area off triangle
"""base=float(input("enter the length of base of triangle: ")),
height=float(input("enter the height of triangle: ")),
area = 0.5*base*height
print("area of triangle is : ",area)"""

"""base=float(input("enter the length of base of triangle: ")),
height=float(input("enter the height of triangle: ")),
area = 0.5*base*height
print(f"area of triangle is : {area}",)"""

#swap variables
"""a=input("enter the value of first variable (a): ")
b=input("enter the value of second variable (b): ")
print(f"original values : a={a}, b={b}")
temp=a
a=b
b=temp
print(f"swap values : a={a}, b={b}")"""

#swap variables without using temporary variable
"""a=input("enter the value of first variable (a): ")
b=input("enter the value of second variable (b): ")
print(f"original values : a={a}, b={b}")
a,b=b,a
print(f"swap values : a={a}, b={b}")"""

#celsius to fahrenheit
"""celsius=input("enter temperature in celsius : ")
fahrenheit= (celsius*9/5)+32
print(f"{celsius} degrees in celsius is equal to {fahrenheit} degrees in fahrenheit")"""

#check the the number even or odd
"""number = int(input("enter the number you want to check :\n"))
reminder = number%2
if reminder == 0 :
    print("Number is even")
else :
    print("Number is odd")"""

"""number = int(input("enter the number you want to check :\n"))
if number%2 == 0 :
    print("Number is even")
else :
    print("Number is odd")"""

#check number is negative, positive or zero
"""number = int(input("enter the number you want to check :\n"))
if number<0 :
    print("Number is negative")
ifelse number ==0 :
    print("Number is zero")
else :
    print("number is positive")"""

#to check prime number
"""def is_prime(num):
    # Check if number is less than 2, as 0 and 1 are not prime numbers
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")"""

# python program to find prime numbers in given interval
"""def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_in_interval(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))

prime_numbers = find_primes_in_interval(start, end)

if prime_numbers:
    print(f"Prime numbers between {start} and {end}: {prime_numbers}")
else:
    print(f"No prime numbers found between {start} and {end}.")"""

# patterns using for loop
'''to print
1
22
333
4444
55555
666666'''
"""for i in range(1,7):
    for j in range(i):
         print(i, end='')
    print()"""


'''to print
*
**
***
****
*****'''
"""for i in range(1,6):
    for star in range(1,i+1):
        print('*', end='')
    print()"""

'''to print
1
2 2
1 1 1
2 2 2 2
1 1 1 1 1'''
"""n=5
for i in range(n):
    for j in range(i+1):
        if i%2==0:
            print("1" , end= ' ')
        else :
                print("2" , end= " ")
    print()        """

'''to print
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5'''
"""n=5
for i in range(n):
    p=1
    for j in range(i+1):
        print(p, end=' ')
        p+=1
    print()"""

'''to print
5
4 5
3 4 5
2 3 4 5
1 2 3 4 5'''
"""n=5
k=5
for i in range(n):
    p=k
    for j in range(i+1):
        print(p, end=' ')
        p=p+1
    k=k-1
    print()"""

'''to print
1 1 1 1 1
  1 1 1 1
    1 1 1
      1 1
        1'''
"""n=5
for i in range(n):
    p=1
    for j in range (i):
        print(' ', end=' ')
    for k in range(i,n):
        print(p, end=' ')
    print()"""

'''to print
1 2 3 4 5
  1 2 3 4
    1 2 3
      1 2
        1'''
"""n=5
for i in range(n):
    p=1
    for j in range (i):
        print(' ', end=' ')
    for k in range(i,n):
        print(p, end=' ')
        p=p+1
    print()"""

'''to print
  5 4 3 2 1
    4 3 2 1
      3 2 1
        2 1
          1'''
"""n=5
k=5
for i in range(n):
    p=k
    for j in range (i+1):
        print(' ', end=' ')
    for j in range(i,n):
        print(p, end=' ')
        p=p-1
    k=k-1
    print()"""



'''to print
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1'''
"""n=5
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()"""

'''to print
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1'''
"""n=5
for i in range(n):
    p=5
    for j in range(i+1):
        print(p, end=' ')
        p=p-1
    print()"""

'''to print
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5'''
"""n = 5
for i in range(1, n + 1):
    print(' ' * (n - i), end='')
    for j in range(1, i + 1):
        print(j, end=' ')
    print()"""

'''to print
 5 4 3 2 1
  4 3 2 1
   3 2 1
    2 1
     1'''
"""n=5
k=5
for i in range(n):
    p=k
    for j in range (i+1):
        print('', end =' ')
    for j in range (i,n):
        print(p, end =' ')
        p=p-1
    k=k-1
    print()"""




"""print("welcome to the split bill calculator calculator")
bill=float(input("what was the total bill \n"))
tip=float(input("how much percentage of tip will be given\n"))
members=int(input("how many members to split bill\n"))
print(f"total bill is \n{round(bill*(1+tip/100),2)}\nbill per person is\n {round((bill*(1+tip/100)/members),2)}")"""
#bill calculator code2
"""print("welcome to the split bill calculator calculator")
bill=float(input("what was the total bill \n"))
tip=float(input("how much percentage of tip will be given\n"))
bill_with_tip=round(bill*(1+(tip/100)),2)
print(f"total bill is\n{round(bill_with_tip,2)}")
members=int(input("how many members to split bill\n"))
print(f"Bill per person is\n{round((bill_with_tip/members),2)}\n")"""



"""print("welcome to the rollercoaster")
height=int(input("enter your height\n"))
if height >= 120 :
    print("you are eligible for ride")
    age=int(input("enter your age\n"))
    if age <= 18 :
        print("please pay $7")
    else :
        print("please pay $10")
else :
    print("you are not eligible for ride")"""

"""weight = 85
height = 1.85
bmi = weight / (height ** 2)
if bmi < 18.5 :
    print("underweight")
elif bmi < 25:
    print("normal weight")
else :
    print("overweight")"""

"""print("welcome to python pizza deliveries")
size=input("enter the size of pizza you want S,M or L : ")
bill = 0
if size=="s":
    bill+=15
elif size=="m":
    bill+=20
elif size=="l":
    bill+=25
else :
    print("you entered the wrong input")

pepperoni=input("Do you want pepperoni, y or n : ")
if pepperoni=="y":
    if size=="s":
        bill+=2
    else :
        bill+=3

cheese=input("Do you want extra cheese, y or n : ")
if cheese=="y":
    bill+=1

print("your bill is : $",bill)"""

"""print(''' _._     _,-'""`-._
(,-.`._,'(       |\`-/|
    `-.-' \ )-`( , o o)
          `-    \`_`"'-''')"""
