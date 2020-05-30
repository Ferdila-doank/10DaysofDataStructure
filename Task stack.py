class Stack(): 
    def __init__(self):
        self.items = []
        self.top_item = None
        self.item_to_remove = None
        self.size = 0
        self.limit = 1000

    def push(self, item):
        if self.has_space() == True:
            self.items.append(item)
            self.size = self.size + 1
            print('size of stacks = ' + str(self.size))
        else:
            print('All out of space!')

    def pop(self):
        if not self.is_empty():
            self.top_item = self.items[-1]
            self.item_to_remove = self.top_item
            self.items.pop()
            self.size = self.size - 1
            return(self.item_to_remove)
        else:
            print ('Stack is empty')

    def peek(self): 
        if not self.is_empty():
            self.top_item = self.items[-1]
            print ('Stack is not empty')
            return self.top_item
        else: 
            print ('Stack is empty')

    def set_next_node(self):
        if not self.is_empty():
            self.top_item = self.items[-1]
            self.push(self.top_item)
        else:
            print('Please Add vaue to stacks first')    

    def has_space(self):
        if self.limit > self.size:
            return True          

    def is_empty(self):
        if self.size == 0:
            return True     

Node = Stack() 
Node.push("A")
Node.push("B")
print(Node.items)

print(Node.peek())

Node.set_next_node()
print(Node.items)

Node.pop()
print(Node.item_to_remove)
print(Node.items)

pizza_stack = Stack()
pizza_stack.pop()
pizza_stack.push('Meat Lovers')
