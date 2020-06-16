"""fibonacci sequence

a=0
b=1

for i in range(1,10):
    print(a)
    a,b=b,a+b
"""
#list comprehensin

num=[1,2,3,4,5,6,7,8,9,10]

""" hoe to copy the list from other

mylist=[]
for i in num:
    mylist.append(i)
print(mylist)

#list comprensios:

mylist=[i*i for i in num]
print(mylist)


myList=map(lambda n: n*n, num)

for i in myList:
    print(i)
"""
#enen list
"""one way
my_list=[]

for n in num:
    if n%2==0:
        my_list.append(n)
print(my_list)    

#another way
my_list=[n for n in num if n%2 ==0]
print(my_list)

my_list=filter(lambda n: n%2 ==0,num)
for i in my_list:
    print(i)  
"""
#dictonary comprehension

name=['ashit','binod','deepak','bakeshwar','bimal']
title=['mandal','mandal','mandal','mandal','kumar']

my_list={name: title for name,title in zip(name,title) if title == 'mandal'}



print(my_list)
"""
hi=zip(name,title)
for i,j in hi:
    print(i,j)
"""
#a=zip(name,title)
"""i want a dich for 

my_list={}

for name,title in zip(name,title):
    my_list[name]=title
print (my_list)
"""