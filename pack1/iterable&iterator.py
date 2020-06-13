
""" we are making the iterator function """
"""
class MY_RANGE:
    def __init__(self,start,end):
        self.value=start
        self.end=end
    def __iter__(self):
        return self
    def __next__(self):
        if self.value >=self.end:
            raise StopIteration
        current=self.value
        self.value +=1
        return current

nums=MY_RANGE(1,10)"""


"""by gererator function
"""
#def my_range(start,end):
def my_range(start):
    current=start
#    while current <=end
    while True:
#
        yield current
        current += 1
        
nums=my_range(1)

for i in nums:
    print(i)


for num in test:
   print(num)
"""

print(next(nums))
print(next(nums))        
print(next(nums))
"""
