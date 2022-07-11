from collections import defaultdict


# ______________________________________________________________________________________________________________________
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
#
# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
# ______________________________________________________________________________________________________________________

# Node class for doubly LL nodes
class Node:
    def __init__(self, key, val):
        # Here doubly LL node will have key and val (key,val)
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.map = defaultdict()

        # Creating a dummy head and tail LL,so that we wouldn't need to check for null.
        #       head        tail
        #        |           |
        #     [0,0]   <->  [0,0]
        #
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def removeFromTail(self):
        if len(self.map) == 0:  # if map is empty means DLL does not exists, so return
            return

        else:  # else map not empty,so get tail_node and delete it from map and DLL
            tail_node = self.tail.prev  # required tail node that has to be deleted will be present at prev of tail,because, last tail is dummy tail

            del self.map[tail_node.key]  # first delete it from map
            self.removeFromList(tail_node)  # also delete it from DLL

    def addToFront(self, node):
        # As at front there is dummy head, we need to make connection after dummy head.next
        headNext = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = headNext
        headNext.prev = node

    def removeFromList(self, node):
        # Simple, just break the connections.
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key):
        # Two conditions to get a key,
        # 1. if we have key  or 2. we don't have a key
        if key in self.map:  # 1. if we have a key
            node = self.map[key]
            # if we have a key, we will have to remove from its existing place in DLL and bring it to front

            self.removeFromList(node)  # remove from its place in DLL
            self.addToFront(node)  # insert it in front of DLL

            return node.val  # finally return required key.val
        else:  # 2. we don't have a key
            return -1

    def put(self, key, value):
        # To put a key, we have two conditions
        # 1. if key already present or , 2. if key not present
        if key in self.map:  # 1. if key already in map, remove previous key, because its value might have changed this time
            node = self.map[key]

            self.removeFromList(node)  # remove previous key from DLL
            newNode = Node(key, value)  # make new node from new key,value

            self.addToFront(newNode)  # insert newNode in DLL
            self.map[key] = newNode  # and also add it in map

        else:  # 2. else key not present, then add it
            if len(self.map) >= self.capacity:  # but check if capacity reached or not
                self.removeFromTail()  # if capacity full ,then remove LRU ,which will be present at DLL tail

            node = Node(key, value)  # make new node
            self.map[key] = node  # add it to map
            self.addToFront(node)  # add it to front of DLL


# _LIMITED TO PYTHON ONLY USING ALL INBUILT FUNCTIONALITY______________________________________________________________________________________
from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)  # Gotta keep this pair fresh, move to end of OrderedDict
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) >= self.size:
                self.cache.popitem(last=False)  # last=True, LIFO; last=False, FIFO. We want to remove in FIFO fashion.
        else:
            self.cache.move_to_end(key)  # Gotta keep this pair fresh, move to end of OrderedDict

            self.cache[key] = value


# ____________________________________________________________________________________________________________________
capacity = 2
obj = LRUCache(capacity)
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
obj.put(3, 3)
print(obj.get(2))
obj.put(4, 4)
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))
