# queue.py
# test 3
#
# Base queue implementation for teh cs10 ADTs unit
#
# Our initial implementation will use a singly linked list. But, if you
# want to make a faster queue, you will need to implement the data structue
# in a different way. To do this, you will need to change the class definitions
# below.
#
# IMPORTANT: If you change the class constructions, make sure you DO NOT change the
# name of the Queue class. The testing harnesses expect your queue implementation to
# be named Queue in this file.

class ListElem:
    """An element of the list.
    """

    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    """A queue made from a linked list.
    """
    def __init__(self):
        self.head = None
        

    # Add your queue implementation here!
    def __getitem__(self, key):
        '''operator overload to get the item in the 
        list at a particular index.
        '''
        curr = self.head
        for i in range(key):
            try:
                curr = curr.next
            except:
                raise IndexError
        try:
            return curr.data
        except:
            raise IndexError

    def __len__(self):
        '''Returns the number of items in the queue.
        '''
        count = 0
        curr = self.head
        while curr:
           count += 1
           curr = curr.next
        return count

    def append(self, data):
        """Enqueues data into the list.
        """
        item = ListElem(data)

        if self.head:
            curr = self.head
            nxt = self.head.next
            while nxt:
                curr = nxt
                nxt = curr.next
            curr.next = item
        else:
            self.head = item

        

    def popleft(self):
        """Dequeues the first thing in the list.
        """
        if self.head:
            item = self.head.data
            self.head = self.head.next
        
        else:
            raise IndexError

    def insert(self, index, data):
        """Inserts an element into the queue at a particular
        index.
        """
        item = ListElem(data)
        prev = None
        curr = self.head
        count = 0


        while curr:
            if count == index:
                break
            prev = curr
            curr = curr.next
            count += 1
        if prev:
            prev.next = item
        else:
            self.head = item
        item.next = curr
        
    def remove(self, value):
        """Removes the first instance of a value from the queue.
        Throws an error if the value doesn't exist in the list.
        """
        prev = None
        curr = self.head

        while(curr):
            if value == curr.data:
                if prev:
                    prev.next = curr.next
                    return
                else:
                    self.head = curr.next
                    return
            prev = curr
            curr = curr.next
        raise ValueError

    def index(self, value):
        """Finds the first instance of a value within the queue and
        returns the index of the value.
        """
        curr = self.head
        count = 0
        while(curr):
            if value == curr.data:
                return count
            curr = curr.next
            count += 1
        raise ValueError

    def count(self, value):
        """Counts the number of times a value appears in the queue
        and returns the count.
        """
        curr = self.head
        count = 0
        while curr:
            if curr.data == value:
                count += 1
            curr = curr.next
        return count
