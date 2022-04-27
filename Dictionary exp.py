from unicodedata import name
#
mydict = {'name': 'Max', 'age': 16, 'city': 'HK' }
print(mydict)

mydict2 = dict(name = 'Mary', age = 27, city = 'Boston')
print(mydict2)
#create dictionaries

#add items to dictionaries

mydict['email'] = 'hellomyass@gmail.com'
print(mydict)

mydict['email'] = 'helloass@gmail.com'
print(mydict)

#

del mydict['name']
print(mydict)

mydict.pop('age')
print(mydict) 
#delete assigned items

#delete last item from library
mydict.popitem()
print(mydict)
#

#check if item is in lib -- 1. if...in statement

if 'city' in mydict:
    print(mydict['city'])
#   
#check if item is in lib -- 1. 'Try' statement

try:
    print(mydict['city'])
except:
    print('Error')
# 
#looping through all the keys in a lib
for key in mydict2:
    print(key)
#or
for key in mydict2.keys():
    print(key)
#or
for value in mydict2.values():
    print(value)
#
#for both
for key, value in mydict2.items():
    print(key, value)
#
#copying dictionaries_simple assignment
mydict2Cpy = mydict2
print(mydict2Cpy)
#
#copying dictionaries_built-in operator
mydictCpy = mydict.copy()
mydictCpy['postcode'] = 'ME10 3LW'
print(mydict)
print(mydictCpy)
#
#copying dictionaries_'dict()' operator
mydictCpy2 = dict(mydict)
mydictCpy2['Fav. colour'] = 'Yellow'
print(mydict)
print(mydictCpy2)
#
#merging 2 dictionaries
myNewDict = dict(name='Hagum', age=16, city='HK')
myNewDict2 = dict(name='IDK', age=20, city='London')
myNewDict.update(myNewDict2)
print(myNewDict)
#
#assigning different types of KEYs_INT as keys
myNewDict = {0: 1, 1: 2, 2: 4}
print(myNewDict)
Val = myNewDict[0]
print(Val)
#
#assigning different types of KEYs_TUPLES as keys
myTuple = (8, 7)
myNewDict = {myTuple: 15}
print(myNewDict)
#


 






    

    





 











