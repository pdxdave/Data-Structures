import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Queue:
  def __init__(self):
    self.size = 0
    # Why is our DLL a good choice to store our elements?
    '''
    Because the length is constantly changing
    '''
    self.storage = []
    # self.storage = DoublyLinkedList()
    
  def enqueue(self, value):
    self.storage.insert(0, value)
    self.size += 1
    # self.storage.add_to_tail(value)
    # self.size += 1
  
  def dequeue(self):
    if len(self.storage) == 0:
      return None
    else:
      return self.storage.pop()
      # if self.size > 0:
      # self.size -= 1
      # return self.storage.remove_from_head()
      # else:
      # return None
  

  def len(self):
    return len(self.storage)
    # return self.size
