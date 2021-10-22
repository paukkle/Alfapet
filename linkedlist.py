class Player:
    def __init__(self, name):
        self.__name = name
        self.__points = 0
        self.next = None

    def __repr__(self):
        return self.__name

    @property
    def name(self):
        return self.__name

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, amount):
        self.__points = amount


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        self.tail = None
        if nodes is not None:
            node = Player(name=nodes.pop(0))
            self.head = node
            if len(nodes) == 0:
                self.tail = node
                node.next = node
            for i, elem in enumerate(nodes):
                node.next = Player(name=elem)
                node = node.next
                if i == len(nodes) - 1:
                    self.tail = node
                    self.tail.next = self.head

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.name)
            if node.next != self.head:
                node = node.next
            else:
                break
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

