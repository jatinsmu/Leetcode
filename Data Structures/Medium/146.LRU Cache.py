class Node:
    # create a Node of linked list
    def __init__(self, key: int, val: int):
        self.val = val
        self.key = key  # to keep track of the key in cache with which this node is linked
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity  # max capacity allowed
        self.cache = {}  # {key: Node, key: Node}

        # create a dummy node in the front and the last to make accessing easier
        # create dummy oldest node
        self.oldest = Node(0, 0)
        # create dummy latest node
        self.latest = Node(0, 0)

        # link the oldest and latest nodes together
        self.oldest.next = self.latest  # next of oldest point to latest
        self.latest.prev = self.oldest  # prev of latest point to oldest

    def remove(self, node) -> None:
        # remove the given Node in place.

        # take refereces for current node's prev and next
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node  # next of prev_node will point to next node (we bypass the current Node)
        next_node.prev = prev_node  # prev of next_node will point to prev node (we bypass the current Node)

    def insert(self, node) -> None:
        # insert the node at the last. Use the dummy latest node for looking up the last node
        prev_end_node = self.latest.prev  # take reference of the end node
        dummy_node = self.latest  # take reference of the next node

        prev_end_node.next = node  # next of previous end node will point to the current node that we are inserting
        dummy_node.prev = node  # now latest dummy node points to the recent node that we inserted

        node.prev = prev_end_node  # prev of current node will point to the previous end node.
        node.next = dummy_node  # next of current node point to the latest dummy node

    def get(self, key: int) -> int:
        # check if the key is in cache
        if key in self.cache:
            # remove the key from cache
            self.remove(self.cache[key])
            # insert the key at the end
            self.insert(self.cache[key])
            # return the value of key from cache
            return self.cache[key].val

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # check if the key is already in cache, then update it. To update, first remove the key, update its value in cache and insert it at the end
        if key in self.cache:
            self.remove(self.cache[key])  # remove the node

        self.cache[key] = Node(key, value)  # update the value of that node
        self.insert(self.cache[key])  # insert it at the end

        # check the capacity.. if we reached the max capacity, then remove the very first node
        if len(self.cache) > self.capacity:
            # remove the first node
            first_beginning_node = self.oldest.next  # since oldest is the dummy node at the beginning, it is fast to get the first actual node of the list
            self.remove(first_beginning_node)

            # remove the first_beginning_node from cache
            # now the 'key' from Node class will be used. Because we kept track of the key with which all nodes are linked. So it is O(1) to get the key in the cache where the first_beginning_node is stored
            del self.cache[first_beginning_node.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
