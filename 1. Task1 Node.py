# Task 1 of Day 1

# 1.Creating New Class Node with arguments value and link_node 
class Node:
  def __init__(self, value):
    self.value = value
    self.link_node = None

# Create Nodes Python Getters 
  def get_value(self):
    return self.value
  
  def get_link_node(self,nodepos):
    seqnode = [wacko, dot, yacko]
    i = len(seqnode) -1

    while i >= 0 :
      if seqnode[i] == nodepos: 
        return seqnode[i-1].value 
      i -= 1  
    
  def set_link_node(self,link_node):
    self.link_node = link_node

  def print_all_value_node(self):
    nodes = wacko
    x = 1 

    while nodes:
      print('node ' + str(x) + ' value : ' + str(nodes.value))
      nodes = nodes.link_node
      x = x + 1

  def name_link_node (self):
    return self.link_node.name

NodeTest = Node('testing node1')
print(NodeTest.get_value())

wacko = Node('has a penchant for hoarding snacks')
dot = Node('enjoys spending time in movie lots')
yacko = Node('likes to yak')

dot.set_link_node(yacko)
wacko.set_link_node(dot)

wacko.print_all_value_node()

dots_data = dot.get_link_node(nodepos=yacko)
print(dots_data)

wackos_data = wacko.get_link_node(nodepos=dot)
print(wackos_data)