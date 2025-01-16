class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create a singly linked list
if __name__ == '__main__':
    head = Node("Fatima Marie")
    second = Node("Kenneth Joshua")
    third = Node("Arjonel")

    head.next = second
    second.next = third

    # Traverse and print the elements of the linked list
    print("Linked list: ")
    current = head
    while current:
        if current.next is None:
            print(current.data)
        else:
            print(current.data, end=' -> ')
        current = current.next
