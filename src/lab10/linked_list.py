# class Node — узел односвязного списка
class Node:
    """
    Узел односвязного списка.
    Хранит значение и ссылку на следующий узел.
    """
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
    def __repr__(self):
        return f"Node({self.value})"

# class SinglyLinkedList — односвязный список.
class SinglyLinkedList:
    """
    Односвязный список (Singly Linked List).
    Поддерживает указатель на хвост (tail) для вставки за O(1).
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, value) -> None:
        """Добавить элемент в конец списка. Сложность: O(1)."""
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1

    def prepend(self, value):
        """Добавить элемент в начало списка. Сложность: O(1)."""
        new_node = Node(value, next=self.head)
        self.head = new_node
        if self._size == 0:
            self.tail = new_node
        self._size += 1


    def insert(self, idx, value) -> None:
        """Вставка по индексу. Сложность: O(n)."""
        if idx < 0 or idx > self._size:
            raise IndexError("negative index is not supported")

        if idx == 0:
            self.prepend(value)
            return
        
        if idx == self._size:
            self.append(value)
            return
        
         # Ищем узел, который будет ПЕРЕД вставляемым
        current = self.head
        for _ in range(idx - 1):
            current = current.next

        new_node = Node(value, next=current.next)
        current.next = new_node
        self._size += 1

    def remove(self, idx: int)-> None:
        """Удаление по индексу. Сложность: O(n)."""
        if idx < 0 or idx >= self._size:
            raise IndexError("index out of range")

        if idx == 0:
            self.head = self.head.next
            if self._size == 1:
                self.tail = None
            self._size -= 1
            return

        current = self.head
        for _ in range(idx - 1):
            current = current.next

        current.next = current.next.next
        if idx == self._size - 1:
            self.tail = current

        self._size -= 1

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self):
        return self._size

    def __repr__(self):
        values = list(self)
        return f"SinglyLinkedList({values})"