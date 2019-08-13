class student():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show(self):
        print("Name:",self.name,"Age:",self.age,"Gender:",self.gender)

a = student("Li",18,"boy")
a.show()

import re

res = re.match('......', 'li123kunhong123')
print(res.group())  # 结果——li123k


res = re.match('.+', 'li123kunhong123')
print(res.group())  # 结果——li123kunhong123


res = re.match('^li\d+', 'li123kunhong123')
print(res.group())


