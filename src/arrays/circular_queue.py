class CircularQueue:
    """
    Implement a queue using a circular buffer.

    We keep two private indices, head and tail. The head
    points to the element at the head of the queue. The
    tail points to the next free slot at the end of the
    queue. The head and tail chase each other around the
    circular buffer as elements are added and removed.

    The queue is considered empty when the head and the tail
    point to the same element. The queue is considered full
    when the next element after the tail is the head. Since
    the tail always points to the next free slot, a full
    queue contains exactly one free, and unusable, slot.
    Thus, the capacity of a buffer of length n is actually
    (n - 1).
    """

    def __init__(self, capacity):
        self.buf = [None] * (capacity + 1)
        self.head = 0
        self.tail = 0

    def add(self, element):
        """
        Append an element to the queue.

        :param element: The element to be appended.
        :return: True if the append operation was successful,
            false otherwise.
        """
        if self.is_full():
            return False
        self.buf[self.tail] = element
        self.tail = (self.tail + 1) % len(self.buf)
        return True

    def poll(self):
        """
        Remove an element from the front of the queue.

        :return: The element that was removed from the
            front of the queue, or None if the queue is empty.
        """
        if self.is_empty():
            return None
        element = self.buf[self.head]
        self.head = (self.head + 1) % len(self.buf)
        return element

    def is_full(self):
        """
        Determine whether the queue is full.

        :return: True if the queue is full, false otherwise.
        """
        return (self.tail + 1) % len(self.buf) == self.head

    def is_empty(self):
        """
        Determine whether the queue is empty.

        :return: True if the queue is empty, false otherwise.
        """
        return self.head == self.tail
