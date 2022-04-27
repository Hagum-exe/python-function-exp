from itertools import accumulate
import operator
a = [1,2,5,3,4]
acc = accumulate(a, func=operator.mul)
print(a)
print(list(acc))
acc = accumulate(a, func=max)
print(list(acc))