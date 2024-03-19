class Order:
    def __init__(self, qtty, customer):
        self.customer = customer
        self.qtty = qtty

    def print_order(self):
        print("     Customer:", self.get_customer())
        print("     Quantity:", self.get_qtty())
        print("     ------------")

    def get_qtty(self):
        return self.qtty

    def get_customer(self):
        return self.customer


class QueueInterface:
    def size(self):
        pass

    def is_empty(self):
        pass

    def front(self):
        pass

    def enqueue(self, info):
        pass

    def dequeue(self):
        pass


class Node:
    def __init__(self, order):
        self.order = order
        self.next = None

top = None  
node = top
while node is not None:
    print("** Element")
    node.order.print_order()
    print()
    node = node.next

