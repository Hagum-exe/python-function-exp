from collections import deque

D = deque()

D.append(1)
D.append(2)
print(D)
D.appendleft(10)
print(D)
D.append(0)
print(D)

D.pop()
print(D)

D.clear()
print(D)

D.extend([3,4,5])
D.extendleft([11,12,13])
print(D)

D.rotate(-1)  #rotate left
print(D)


D.rotate(1)  #rotate right
print(D)
