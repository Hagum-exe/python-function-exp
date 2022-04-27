#using counter form collections
#counter: a container that stores the element as dictionary keys and their counts as diectionary values
from collections import Counter
a = 'aaaaaaaaaaaaabbbbbxxxxxxxx'
myCounter = Counter(a)
print(myCounter.items())
print(myCounter.keys())
print(myCounter.values())
