import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
  def __init__(self):
    self.size = 0
    # Why is our DLL a good choice to store our elements?
    '''
     constantly changing the length of the data
     why ddl instead of array?  b/c doyle thinks it's slightly better
    '''

    self.storage = []
    # self.storage = DoublyLinkedList()

  def push(self, value):
    return self.storage.append(value)
    # self.storage.add_to_head(value)
  
  def pop(self):
    if len(self.storage) == 0:
      return None 
    else:
      return self.storage.pop()
    # return self.storage.remove_from_head()
    # 

  def len(self):
    return len(self.storage)
    # return self.storage.__len__()
