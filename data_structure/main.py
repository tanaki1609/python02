from collections import deque


class Queue(deque):
    def pop(self):
        return self.popleft()


q = Queue()
q.append('a')
q.append('b')
q.append('c')
print("Initial queue")
print(q)
print("\nElements dequeued from the queue")
print(q.pop())
print(q.pop())
print(q.pop())
print("\nQueue after removing elements")
print(q)
