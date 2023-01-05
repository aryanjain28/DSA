class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data

class Linked_List:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        current = self.head
        while current.next_node:
           current = current.next_node
        current.next_node = new_node


    def search(self, target):
        current = self.head
        while current:
            if current.data == target:
                return True
            current = current.next_node
        return False

    def insert(self, data, index):

        if index == 0:
            self.add(data) 

        if index > self.size() + 1:
            print("Out of index")
            return False

        new_node = Node(data)
        current = self.head
        for _ in range(0, index - 1): current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def delete(self, index):
        current = self.head
        for _ in range(0, index - 1): current = current.next_node
        current.next_node = current.next_node.next_node

    def remove(self, key):
        current = self.head

        if current.data == key:
            self.head = current.next_node
            return True

        while current:

            # Check for Tail   
            if not current.next_node:
                return current.data == key

            next_node = current.next_node
            if next_node.data == key:
                current.next_node = next_node.next_node
                print("Found data")
                return True

            current = current.next_node 
        
        print("Not Found")
        return False

    def node_at_index(self, index):

        if self.size() is 1:
            return self

        if index == 0:
            return self.head
        else:
            i = 0
            current = self.head
            while i < index:
                i += 1
                current = current.next_node
        
        return current

    def __repr__(self):

        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node

        return '-> '.join(nodes)

        








