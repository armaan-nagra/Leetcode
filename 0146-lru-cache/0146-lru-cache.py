class Node():
    def __init__(self,key=None, value=None):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.nodes = {}
        self.tail = Node()
        self.head = Node()
        self.tail.next = self.head
        self.head.prev = self.tail
        

    def get(self, key):
        if key in self.nodes:
            #remove the node from its current position
            node = self.nodes[key]
            p, n = node.prev, node.next
            p.next = n
            n.prev = p  

            last = self.head.prev
            node.prev = last
            last.next = node
            node.next = self.head
            self.head.prev = node
            return node.value
        return -1


    def put(self, key, value):
        if key in self.nodes:
            node = self.nodes[key]
            node.value = value

            p, n = node.prev, node.next
            p.next = n
            n.prev = p
        else:
            node = Node(key=key, value=value)
            self.nodes[key] = node
            
        last = self.head.prev
        last.next = node
        node.prev = last
        node.next = self.head
        self.head.prev = node
        
        #check that the number of items doesn't exceed capacity
        if len(self.nodes) > self.capacity:
            node = self.tail.next
            self.nodes.pop(node.key)
            p, n = node.prev, node.next
            p.next = n
            n.prev = p

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)