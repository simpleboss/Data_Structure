from node import Node


class Queue:
    def __init__(self, max_size=None):
        self.size = 0
        self.max_size = max_size
        self.head = None
        self.tail = None

    def enqueue(self, value):
        if self.has_space():
            item_to_add = Node(value)
            if self.is_empty():
                self.head = item_to_add
                self.tail = item_to_add
            elif self.size == 1:
                self.head.set_next_node(item_to_add)
                self.tail = item_to_add
            else:
                self.tail.set_next_node(item_to_add)
                self.tail = item_to_add
            self.size += 1
        else:
            print("No more room.")

    def peek(self):
        if not self.is_empty():
            return self.head.get_value()
        else:
            print("The queue is empty.")

    def dequeue(self):
        if not self.is_empty():
            item_to_remove = self.head
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = item_to_remove.get_next_node()
            return item_to_remove.get_value()

    def has_space(self):
        if not self.max_size:
            return True
        elif self.size < self.max_size:
            return True
        else:
            return False

    # 왜 꼭 간단한 코드도 helper method로 만들어야 하나?
    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False


gelato_queue = Queue(10)
gelato_queue.enqueue("Gichan")
gelato_queue.enqueue("Gimoon")
gelato_queue.enqueue("MK")
gelato_queue.enqueue("Andy")
print(gelato_queue.dequeue())
print(gelato_queue.dequeue())
