import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Queue:
  def __init__(self):
    self.size = 0
    # Why is our DLL a good choice to store our elements?
    self.storage = []
    
  def enqueue(self, value):
    self.storage.insert(0, value)
    self.size += 1
  
  def dequeue(self):
    if len(self.storage) == 0:
      return None
    else:
      return self.storage.pop()

  def len(self):
    return len(self.storage)
