import queue

def test():
    pq = queue.PriorityQueue()

    pq.put(('b', 1))
    pq.put(('a', 1))
    pq.put(('c', 1))
    pq.put(('z', 0))
    pq.put(('d', 2))


    while not pq.empty():
        print(pq.get())
    
test() # prints z b a c d