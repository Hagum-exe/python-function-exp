from itertools import combinations, combinations_with_replacement
a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb))
combwr = combinations_with_replacement(a,2)
print(list(combwr))