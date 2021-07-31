class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front == None

    def enqueue(self, element):
        new_item = Node(element)

        if self.rear == None:
            self.front = self.rear = new_item
            return
        self.rear.next = new_item
        self.rear = self.rear.next

    def dequeue(self):
        if self.is_empty():
            print("You cannot dequeue from an empty queue.")
        else:
            removed_item = self.front
            self.front = removed_item.next

            if (self.front == None):
                self.rear = None
            return removed_item.data

    def print_queue(self):                      #I made this print method to test that the queue is
        item = self.front                       #implemented correctly.
        if self.is_empty():
            print("The queue is empty.")
        else:
            queue = []
            while (item != None):
                queue.append(item.data)
                item = item.next
            print (queue)



class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    def pop(self):
        if self.is_empty():
            print ('You cannot pop from an empty stack.')
            return None
        else:
            popped_item = self.head
            self.head = self.head.next
            popped_item.next = None
            return popped_item.data

    def print_stack(self):
        item = self.head
        if self.is_empty():
            print("The stack is empty.")
        else:
            stack = []
            while (item != None):
                stack.append(item.data)
                item = item.next
            print(stack)



if __name__ == '__main__':
    #Testing the queue:
    my_queue = Queue()
    my_queue.enqueue('Jack')
    my_queue.enqueue('Christine')
    my_queue.dequeue()
    my_queue.enqueue('Harry')
    my_queue.print_queue()

    #Testing the stack:
    my_stack = Stack()
    my_stack.push(59)
    my_stack.push(90)
    my_stack.push(123)
    my_stack.push(234)
    my_stack.pop()
    my_stack.push(6  )
    my_stack.pop()
    my_stack.print_stack()
