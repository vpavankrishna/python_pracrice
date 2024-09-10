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
