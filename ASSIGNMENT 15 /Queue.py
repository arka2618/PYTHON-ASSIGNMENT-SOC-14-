from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque([34, 67, 89, 10, 78])
    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} has been added to the queue")
        print(f"New Queue: {self.queue}")
    def safe_dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty, cannot dequeue.")
        else:
            removed = self.queue.popleft()
            print(f"{removed} has been removed from the queue")
            print(f"{self.queue}")

q = Queue()
q.enqueue(99)
q.safe_dequeue()
