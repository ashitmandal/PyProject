tag='hi'
text='this is headline'

sentense='<{0}>{1}</{0}>'.format(tag,text)
print(sentense)
"""Access the value fro dictionary"""

person={'name':'ashit','age':28}
#from string

sentence2='my nme is {name}and my are is {age}'.format(**person)
sentence2='my name is {0[name]} and i am {1[age]} years old,'.format(person,person)
sentence2='my name is {0} and i am {1} years old,'.format(person['name'],person['age'])
sentence2='my name is {} and i am {} years old,'.format(person['name'],['age'])
print(sentence2)
#from list
"""

l=['ashit',23]

sen='me  name is :{0[0]} ans age is {0[1]}'.format(l)

print(sen)

#print(sentence2)                                                          
"""





