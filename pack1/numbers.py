'''
Created on Jun 12, 2020

@author: AshitM

'''
for i in range(1,21):
    sentense='the value is :{:05f}'.format(i)
    print(sentense)
#format for decmal place
'''

pi=3.1424555554554
sentense='the value is :{:.02f}'.format(pi)
print(sentense)

sentense='1 MD id equal to {:,.3f}'.format(200**3)
                                      
print(sentense)

import datetime
mydate=datetime.datetime(2020,1,6,17,45,59)
sentence='{0:%B , %D, %Y} ell into {0:%A} and time {0:%j} day of the year'.format(mydate)
print(sentence)
'''
