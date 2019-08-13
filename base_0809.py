# a = [1,2,3] #同一类型的列表
# print(a)    #----->[1, 2, 3]
#
# a = [1,'str',[45,89]]  #列表中可以有各种不同类型
# print(a)    #----->[1, 'str', [45, 89]]
#
# a.append(98.78)
# print(a)    #----->[1, 'str', [45, 89], 98.78]
#
# a.pop()
# print(a)    #----->[1, 'str', [45, 89]]
#
# del a[1]
# print(a)    #----->[1, [45, 89]]
#
# b=(1,2,3,4,56,789)
# print(b)    #----->(1, 2, 3, 4, 56, 789)
# print(b[1])  #----->2
#
# # b[1] = 555
# # print(b[1])  #----->报错
#
# s1 ='abcdd'
# s2 ='ttyyyy'
# s3 ='student'
# print(s1+s2)   #----->abcddttyyyy
# print(s1*2)     #----->abcddabcdd
# print("My name is %s and weight is %d kg!"% ('Zara', 21))
# print("we are %s"%(s1))

#dict
a = dict()
a['my']=123
a['b']=456
print(a)          #----->{'my': 123, 'b': 456}

if 'my' in a:
    print("exit!")     #----->exit!
else:
    print("None!")

ss={1,2,3,4}
tt={3,4,5,6}
print(ss&tt)         #----->{3, 4}
print(ss|tt)         #----->{1, 2, 3, 4, 5, 6}
print(ss-tt)         #----->{1, 2}

h='yes' if 5>1 else 'no'
print(h)              #----->yes

play=['yuh',456,'ty',8888]
for i in play:
    print(i)           #-----yuh
                           #-----456
                          #-----ty
                         #-----8888
