# Queue using collections module

from collections import deque

queue = deque()

# Enqueue
queue.append("A")
queue.append("B")
queue.append("C")

print("Queue:", queue)

# Dequeue
print("Removed:", queue.popleft())

print("Queue after removal:", queue)
