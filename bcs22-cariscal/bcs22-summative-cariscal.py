from collections import defaultdict

class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class Queue:
    # Initializes the Queue with capacity, front, rear, size, and a list to store items
    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.QList = [None] * capacity
        self.capacity = capacity

    # Checks if the Queue is full
    def isFull(self):
        return self.size == self.capacity

    # Checks if the Queue is empty
    def isEmpty(self):
        return self.size == 0

    # Adds an item to the Queue
    def enqueue(self, item):
        if self.isFull():
            print("The list is full or overflow")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.QList[self.rear] = item
        self.size = self.size + 1

    # Removes and returns an item from the Queue
    def dequeue(self):
        if self.isEmpty():
            print('The list is empty or underflow')
            return None
        item = self.QList[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size = self.size - 1
        return item


def verticalTraversal(root):
    if not root:
        return []

    # Dictionary to store nodes at each vertical level
    vertical_levels = defaultdict(list)

    # Creates a queue for level-order traversal
    queue_capacity = 100  # Adjust the capacity based on your tree size
    queue = Queue(queue_capacity)
    queue.enqueue((root, 0))  # (node, vertical level)

    while not queue.isEmpty():
        node, level = queue.dequeue()

        # Adds the node to the corresponding vertical level
        vertical_levels[level].append(node.val)

        # Enqueues left child with updated level
        if node.left:
            queue.enqueue((node.left, level - 1))

        # Enqueues right child with updated level
        if node.right:
            queue.enqueue((node.right, level + 1))

    # Result is a list of nodes at each vertical level
    result = []
    for level in range(max(vertical_levels.keys()), min(vertical_levels.keys()) - 1, -1):
        result.extend(vertical_levels[level])

    return result

# Constructs a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.right.left = TreeNode(8)
root.right.right.right = TreeNode(9)

# Outputs the vertical traversal
result = verticalTraversal(root)
print(result)