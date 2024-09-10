# hemanth=[] # empty list
# # hemanth=list()
# print(type(hemanth))


# usha=[1,2.2,"kiran",True]
# # print(usha[3])
# usha[0]="james"
# print(usha)

usha=[1,2.2,"kiran",True,False,3.4,57,5,75]
# print(usha[0:7:3])
# print(usha[:5])
# print(usha[::-2])



# variable.method()
# usha.append(314)
# usha.extend("python")
# print(usha)


# v=usha.copy()
# usha.append(12345)
# print(v)



# usha.clear()
# print(usha)
# print(usha.count(2))
# usha=[1,57,5,75,2,3,2,25,325,5,2]
# # print(len(usha))
# print(usha.index(2))


# usha=[1,57,5,75,2,3,2,25,325,5,2]
# usha.insert(0,112)
# usha[0]="vikas"
# usha.pop(0)
# usha.remove(5)
# usha.reverse()
# usha.sort(reverse=True)
# print(usha)






































# l=[1,1,24,3,435,53,435,1,2,321,131,1]

# for i in range(len(l)):
#     if l[i]==435:
#         print(i)









# l=[1,1,24,3,435,53,435,1,2,321,131,1]

# for i in range(len(l)):
#     if l[i]==435:
#         l[i]=2
# print(l)







## List Comprehension
# print(["EVEN" if i%2==0 else "ODD" for i in range(0,20)])













# print([num**2 for num in [1,2,3,4,5,6,7,8,9,10]])









# Create a list of only the first letters of words in a list
# print([word[0] for word in ['apple', 'banana', 'cherry', 'date']])











# Create a list of only the positive numbers from a given list
# print([num for num in [-2, -1, 0, 1, 2, 3, 4] if num > 0])

# for num in [-2, -1, 0, 1, 2, 3, 4] :
#     if num>0:
#         print(num)


# v=[-2, -1, 0, 1, 2, 3, 4]
# print(-10 not in v)











# #How to Remove Multiple Elements in List
# # using list comprehension
# num = [1, 2, 3, 4, 5, 6, 7, 8, 9,9,9,9,9 ,10]
# num_to_remove = [9]
# # create new list using list comprehension
# num = [i for i in num if i not in num_to_remove]
# print(num)







# l=[1,1,24,3,435,53,435,1,2,321,131,1]

# c=[]
# [c.append(i) if l[i]==1 else " " for i in range(len([1,1,24,3,435,53,435,1,2,321,131,1]))]
# print(c)





'''
Task 10
practice total today list topic
Task 11
write a program to build a table (1*1=1) using nested forloop
Task 12
write a program using list compherension cubic of list elements
'''



# d=['Ram','sunny']
# for i in range(len(d)):
#     v=d[i]
#     print(v[0])


l = [1,2.2,"Kiran",True,False,3.4,57,5,75]
print(l[-1:-4:-1])