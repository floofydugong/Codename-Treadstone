class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    new_node = Node(data)
    new_node.next = head

    return new_node

def build_one_two_three():
    return push(push(push(None,3),2),1)