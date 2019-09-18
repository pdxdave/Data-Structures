import sys
sys.path.append('../queue_and_stack')
# from queue import Queue 
# from stack import Stack 

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    while True:
      if value < self.value and self.left is None:
        self.left = BinarySearchTree(value)
        break
      elif value < self.value and self.left is not None:
        self = self.left
      elif value >= self.value and self.right is None:
        self.right = BinarySearchTree(value)
        break
      else:
        self = self.right

  def contains(self, target):
    while True:
      if self.value == target:
        return True
      elif target < self.value and self.left is None: 
        return False
      elif target < self.value and self.left is not None:
        self = self.left
      elif target >= self.value and self.right is None:
        return False
      else:
        self = self.right 

  def get_max(self):
    if not self.right:
      return self.value 
    else:
      return self.right.get_max()


  def for_each(self, cb):
    cb(self.value)

    if self.left:
      self.left.for_each(cb)
    if self.right:
      self.right.for_each(cb)

  # only shows value.  maybe add a key?  value could be tuple?
  # or key is value

   # `insert` adds the input value to the binary search tree, adhering to the rules of the ordering of elements in a binary search tree.

  # `contains` searches the binary search tree for the input value, returning a boolean indicating whether the value exists in the tree or not.

  # `get_max` returns the maximum value in the binary search tree.

  # `for_each` performs a traversal of _every_ node in the tree, executing the passed-in callback function on each tree node value. There is a myriad of ways to perform tree traversal; in this case any of them should work. 