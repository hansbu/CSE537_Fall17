from queue import PriorityQueue

a = PriorityQueue()

a.put((10, 'a'))
a.put((4, 'b'))
a.put((3, 'c'))

(y, x) = a.get()
print(y)

print (a.get())
print (a.get())