class NodeList:
    def __init__(self, cap=0):
        self.first = None
        self.last = None
        self.cap = cap
        self.size=0
    
    def put_node_to_first(self, node):
        if node == self.first:
            return
        if node == self.last:
            self.last=self.last.pre
        node.pre.next = node.next
        if node.next:
            node.next.pre = node.pre
        self.first.pre=node
        node.next=self.first
        node.pre=None
        self.first=node
    
    def put_new_node(self, node):
        if self.cap == 0:
            return node.key
        if self.first is None:
            self.first = node
            self.last = node
            self.size+=1
            return None
        else:
            self.first.pre=node
            node.next=self.first
            self.first=node
            if self.size == self.cap:
                self.last.pre.next=None
                key = self.last.key
                self.last=self.last.pre
                return key
            self.size+=1
            return None
class Node:
    def __init__(self, val=0, key=None):
        self.val = val
        self.key = key
        self.next = None
        self.pre = None
    
class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.nodelist=NodeList(cap=capacity)
        self.cmap={}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cmap:
            self.nodelist.put_node_to_first(self.cmap[key])
            return self.cmap[key].val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cmap:
            self.cmap[key].val = value
            self.nodelist.put_node_to_first(self.cmap[key])
        else:
            self.cmap[key]=Node(val=value, key=key)
            dkey = self.nodelist.put_new_node(self.cmap[key])
            if dkey:
                self.cmap.pop(dkey)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)