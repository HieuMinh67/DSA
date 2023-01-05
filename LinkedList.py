class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        self.length += 1
        new_node = Node(value)
        if self.tail is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        return True

    def pop(self):
        if self is None:
            return None
        elif self.length == 1:
            result = self.head.value
            self.head = None
            self.tail = None
        else:
            tmp = self.head
            while tmp.next.next is not None:
                tmp = tmp.next
            result = tmp.next.value
            tmp.next = None
            self.tail = tmp
        self.length -= 1
        return result

    def prepend(self, new_node: Node):
        if self.head is None and self.tail is None:
            self.tail = self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        tmp = self.head
        self.head = tmp.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return tmp.value

    def print(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.value)
            tmp = tmp.next


my_linked_list = LinkedList(4)
my_linked_list.append(5)
# my_linked_list.pop()
# my_linked_list.prepend(Node(6))
my_linked_list.pop_first()
my_linked_list.pop_first()

# print('Head:', my_linked_list.head.value)
# print('Tail:', my_linked_list.tail.value)
# print('Length:', my_linked_list.length)

my_linked_list.print()

"""
    EXPECTED OUTPUT:
    ----------------
    Head: 4
    Tail: 4
    Length: 1
    
"""
