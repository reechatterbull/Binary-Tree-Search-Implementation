""" THIS IS A CODE TO IMPLEMENT A BINARY TREE AND PERFORM DIFFERENT OPERATIONS ON IT"""

class BinaryTreeSearch: #A binary tree class would always have value, left and right attributes
  def __init__(self,value): #This is basically defining the reference (root) node
    self.data = value
    self.left = None
    self.right = None

  """ ADDING CHILD NODES TO ROOT """
  """-------------------------------------------------------------------------------------------"""
  def add_child(self, add_data):  #Defining a method to add a child node

    #Steps: 1. Check if data point already exists in the tree. Return if that is the case
    #       2. Recursively, add to left if data is < self (i.e., reference node value)
    #       3. Recursively, add to the right if data > self

      if add_data == self.data: #Checking if node already exists
        return 

      if add_data < self.data:
        if self.left: #Checking if data node on the left exists
          self.left.add_child(add_data)
        else:
          self.left = BinaryTreeSearch(add_data) #This creates a new object (node)

      else:
        if self.right:
          self.right.add_child(add_data)
        else:
          self.right = BinaryTreeSearch(add_data)

  """ IN-ORDER TRAVERSAL"""
  """---------------------------------------------------------------------------------------------"""
  def in_order(self): #Now defining a method to traverse the binary tree in order (i.e.,starting from the left most node)
    elements = [] # Defining an empty array to house the Binary Tree elements
    #visit left tree first
    if self.left:
      elements += self.left.in_order()

    #visit the base node next
    elements.append(self.data)

    #visit right subtree next
    if self.right:
      elements += self.right.in_order()

    return elements


  """ SEARCH THE BINARY TREE"""
  """--------------------------------------------------------------------------------------------"""
  def search(self,val): # Defining a method to search for a value in the binary tree
    if self.data == val: #If the search number is the same as the root node
      return True

    if val < self.data: #Need to search left subtree
      if self.left:
        return self.left.search(val) #Recursively looking for the value
      else:
        return False

    else:
      if self.right:
        return self.right.search(val)
      else:
        return False

  """ FINDING THE MIN ELEMENT IN A BINARY TREE """
  """-------------------------------------------------------------------------------------------"""
  def min(self):
    minimum = min(self.in_order())
    return minimum

  """ FINDING THE MIN ELEMENT IN A BINARY TREE """
  """-------------------------------------------------------------------------------------------"""
  def max(self):
    maximum = max(self.in_order())
    return maximum

  """ CALCULATE THE SUM OF ALL THE ELEMENTS IN THE BINARY TREE """
  """----------------------------------------------------------"""
  def sum_tree(self): #Note this can be done in simpler manner by looping through the array, but here we are going to add the elements as we traverse the tree for practice. 
    sum = 0 #initializing sum to 0

    if self.left:
      sum += self.left.sum_tree()

    sum += self.data #Adding the number if it is the base node    

    if self.right:
      sum += self.right.sum_tree()

    return sum

  """ DEFINING A METHOD FOR POST ORDER TRAVERSAL """
  """-------------------------------------------------------------------------------------------"""
  def post_order(self): #Post order traversal basically means print left subtree, then right then base node
    elements_post = []
    
    if self.left: #Adding left subtree elements first
      elements_post+=self.left.post_order()

    if self.right:
      elements_post += self.right.post_order()

    elements_post.append(self.data)
    
    return elements_post


  """ DEFINING A METHOD FOR PRE ORDER TRAVERSAL """
  """-------------------------------------------------------------------------------------------"""
  def pre_order(self): #Post order traversal basically means print left subtree, then right then base node
    elements_pre = []

    elements_pre.append(self.data)
    
    if self.left: #Adding left subtree elements first
      elements_pre+=self.left.pre_order()

    if self.right:
      elements_pre += self.right.pre_order()

    
    
    return elements_pre


  """ DEFINING A FUNCTION TO DELETE A NODE FROM THE BINARY TREE """
  """-----------------------------------------------------------"""









  

  """ -------------- END OF CLASS DEFINTION --------------------"""
 




def build_tree(elements): #Defining a function that will take a list and build a tree out of it. Note, this is a function and not a method within the class
  root = BinaryTreeSearch(elements[0]) #Defining the root node as the first item in elements 
  for i in range(1,len(elements)):
    root.add_child(elements[i])
  return root #returning the tree as an object



  
""" THIS PART BELOW IS THE MAIN CALLING FUNCTION """
"""----------------------------------------------"""
numbers = [17,4,1,20,9,23,18,34,18,4]
numbers_tree = build_tree(numbers)
print("Binary Tree In-order Traversal:\n", numbers_tree.in_order())
print("The number exists:", numbers_tree.search(10))
print("The minimum and maximum value of the tree are:\n",numbers_tree.min(),",", numbers_tree.max())
print("The sum of the elements of the tree is:", numbers_tree.sum_tree())
print("Binary Tree in post order\n", numbers_tree.post_order())
print("Binary Tree in pre order\n", numbers_tree.pre_order())     
        
    
 
    

  