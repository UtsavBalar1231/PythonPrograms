import random


class CircularLinkedList:
    """
    Circular linked list is a linked list where all nodes are connected to form a circle.
    This class implements a circular linked list.
    """

    def __init__(self, data):
        """
        Constructor for the CircularLinkedList class.
        It contains the data and the next pointer.
        """
        self.data = data
        self.next = self

    def insert(self, data):
        """
        Insert a node at the end of the circular linked list.
        """
        new_node = CircularLinkedList(data)
        new_node.next = self.next
        self.next = new_node

    def delete(self, data):
        """
        Delete a node from the circular linked list.
        The node to be deleted is the first node that contains the data.
        """
        # If the head node contains the data, then delete the head node.
        if self.data == data:
            return self.next
        # If the head node does not contain the data, then delete the node that contains the data.
        else:
            current = self
            while current.next != self:
                if current.next.data == data:
                    current.next = current.next.next
                    return self
                current = current.next
            return self

    def traverse(self):
        """
        Traverse the circular linked list and print the data of each node.
        """
        current = self
        while current.next != self:
            print(current.data, end=" ")
            current = current.next
        print(current.data, end=" ")
        print()

    def search(self, data):
        """
        Search for a node in the circular linked list that contains the data.
        Return True if the node is found. Otherwise, return False.
        """
        current = self
        while current.next != self:
            if current.data == data:
                return True
            current = current.next
        return False


class SecondChanceReplacement:
    """
    Second Chance Replacement Algorithm (SCRA) is a page replacement algorithm that is used in operating systems.
    this class initializes the size of the linked list, the head, tail, current, and victim.
    """

    def __init__(self, size):
        self.size = size
        self.head = None
        self.tail = None
        self.current = None
        self.victim = None

    def create(self):
        """
        create the linked list with random values of 0 or 1
        """
        for i in range(self.size):
            self.insert(random.randint(0, 1))

    def insert(self, data):
        """
        insert a new node into the linked list with the data
        """
        if self.head is None:
            self.head = CircularLinkedList(data)
            self.tail = self.head
        else:
            self.tail.insert(data)
            self.tail = self.tail.next

    def delete(self, data):
        """
        delete a node from the linked list with the data
        """
        self.head = self.head.delete(data)
        self.tail.next = self.head

    def traverse(self):
        """
        traverse the linked list and print out the data of each node
        """
        self.head.traverse()

    def search(self, data):
        """
        search the linked list for the data and return true if found
        """
        return self.head.search(data)

    def select_victim(self, victim):
        """
        select the victim from the linked list and return the victim data
        """
        self.victim = victim
        self.current = self.head
        self.print_victim()

        # if the victim is the head, then move the head to the next node
        for i in range(victim):
            self.current = self.current.next

        if self.current.data == 1:
            print("Victim", self.victim, "has a second chance")

            # give second chance to victim
            self.current.data = 0
        else:
            print("Victim", self.victim, "is free to be replaced")
            # victim is free so fill it with 1
            self.current.data = 1

    def print_victim(self):
        print("Victim: ", self.victim)


if __name__ == "__main__":
    # Create a linked list of size between 20-30 and fill it with random 0's and 1's.
    size = random.randint(20, 30)
    print("Size of the linked list: ", size)
    second_chance = SecondChanceReplacement(size)
    second_chance.create()
    second_chance.traverse()

    n = 0
    while n < 3:
        print("Enter a victim between 0 and", size - 1)
        victim = int(input("Enter victim: "))
        if victim >= 0 and victim < size:
            second_chance.select_victim(victim)
            # print out the list so the user knows what the values are.
            second_chance.traverse()
            n += 1
        else:
            print("Invalid victim number. Please try again.")
