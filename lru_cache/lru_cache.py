"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next
  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next
  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev
  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev
"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0
  def __len__(self):
    return self.length
  def add_to_head(self, value):
    new_node = ListNode(value, prev=None, next=None)
    if not self.head and not self.tail:
      self.head = new_node
      self.tail = new_node
    else:
      self.head.prev = new_node
      new_node.next = self.head
      self.head = new_node
    self.length += 1
  def remove_from_head(self):
    if not self.head:
      return None
    self.length -= 1
    if self.head == self.tail:
      current_head = self.head
      self.head = None
      self.tail = None
      return current_head.value
    else:
      current_head = self.head
      self.head = self.head.next
      self.head.prev = current_head.prev
      return current_head.value
  def add_to_tail(self, value):
    new_node = ListNode(value, prev=None, next=None)
    if not self.head and not self.tail:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
    self.length += 1
  def remove_from_tail(self):
    if not self.tail:
      return None
    self.length -= 1
    if self.head == self.tail:
      current_tail = self.tail
      self.head = None
      self.tail = None
      return current_tail.value
    else:
      current_tail = self.tail
      self.tail = self.tail.prev
      self.tail.next = None
      return current_tail.value
  def move_to_front(self, node):
    if node == self.head:
      return
    if node == self.tail:
      self.remove_from_tail()
    else:
      node.delete()
      self.length -= 1
    self.add_to_head(node.value)
  def move_to_end(self, node):
    if node is self.tail:
      return
    if node is self.head:
      self.remove_from_head()
    else:
      node.delete()
      self.length -= 1
    self.add_to_tail(node.value)
  def delete(self, node):
    if self.head is self.tail:
      self.head = None
      self.tail = None
      self.length -= 1
    elif self.head == node:
      self.remove_from_head()
    elif self.tail == node:
      self.remove_from_tail()
    
  def get_max(self):
    if not self.head:
      return None
    max_value = self.head.value
    current = self.head
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.next
    return max_value
# What has already been provided for me?
# What do I need to use that's not already there?
# What do I need to return/what do I need to end up with?
"""
Our LRUCache class keeps track of the max number of nodes it
can hold,
 the current number of nodes it is holding,
 a doubly-
linked list that holds the key-value entries in the correct 
order,
as well as a storage dict that provides fast access
to every node stored in the cache.
""" 
class LRUCache:
  def __init__(self, limit=10):
    self.limit = limit
    self.current_size = 0
    self.order = DoublyLinkedList()
    self.fast_access = {}
  def search_and_if_exists_move_to_front(self, key):
    found = False
    current = self.order.head
    while current:
      if current.value == key:
        # If we're updating, then move that key to be the most recent key (move it to the head)
        self.order.move_to_front(current)
        found = True
      current = current.next
    if not found:
      # Add key and value to the ordered list, and we're going to keep the most recent value at the head, or the beginning of the list
      self.order.add_to_head(key)
      self.current_size += 1
  """
  Retrieves the value associated with the given key.
  
  Also needs to move the key-value pair to the top of the order such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """
  def get(self, key):
    # Check the cache to see if it exists
    if key in self.fast_access:
      # If it exists, move it to the front in the order and return the value
      self.search_and_if_exists_move_to_front(key)
      return self.fast_access[key]
    # If it doesn't exist
    else:
      return None
  """
  Adds the given key-value pair to the cache.
  
  The newly-
  added pair should be considered the most-recently used
  entry in the cache.
  
  If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room.
  
  Additionally, in the case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value. 
  """
  
  def set(self, key, value):
    # If it's not full
    if self.current_size < self.limit:
      # Add key and value to the fast_access dictionary or update if it already exists
      self.fast_access.update({key: value})
      # Loop through the ordered list, and if we find that the key is already there, update the value and move to the top of the list
      self.search_and_if_exists_move_to_front(key)
    # If it's full
    else:
      self.fast_access.update({key: value})
      # Look for the key to see whether or not it already exists
      found = False
      current = self.order.head
      while current:
        if current.value == key:
          # If we're updating, then move that key to be the most recent key (move it to the head)
          self.order.move_to_front(current)
          found = True
        current = current.next
      # If the key was not already in our cache
      if not found:
         key_to_remove = self.order.remove_from_tail()
         print("key_to_remove", key_to_remove)
         self.fast_access.pop(key_to_remove)
         # Set the new item in the ordered list (it already exists in the cache because we updated at the very beginning)
         self.order.add_to_head(key)
         self.current_size += 1
      # If the key doesn't already exists, put it at the front

# cache_test = LRUCache(5)
# cache_test.set(5, 10)
# cache_test.set(7, 11)
# cache_test.set(9, 5)
# cache_test.set(3, 11)
# cache_test.set(11, 5)
# cache_test.set(4, 11)
# cache_test.set(8, 5)
# print(cache_test.fast_access)
# print("head", cache_test.order.head.value)
# print("tail", cache_test.order.tail.value)





