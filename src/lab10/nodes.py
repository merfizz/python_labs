from typing import Any, Optional, Iterator

class Node:
    """
    Узел односвязного списка.
    Хранит значение и ссылку на следующий узел.
    """
    def __init__(self, value: Any, next_node: Optional['Node'] = None):
        self.value = value
        self.next = next_node
    
    def __repr__(self) -> str:
        return f"Node({self.value})"


class SinglyLinkedList:
    """
    Односвязный список (Singly Linked List).
    Поддерживает указатель на хвост (tail) для вставки за O(1).
    """
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None  # Важно явно инициализировать tail
        self._size: int = 0

    def append(self, value: Any) -> None:
        """Добавить элемент в конец списка. Сложность: O(1)."""
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            # Сразу добавляем после хвоста, без перебора всего списка
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def prepend(self, value: Any) -> None:
        """Добавить элемент в начало списка. Сложность: O(1)."""
        new_node = Node(value, next_node=self.head)
        self.head = new_node
        # Если список был пуст, новый элемент станет и хвостом тоже
        if self._size == 0:
            self.tail = new_node
        self._size += 1

    def insert(self, idx: int, value: Any) -> None:
        """Вставка по индексу. Сложность: O(n)."""
        if not (0 <= idx <= self._size):
            raise IndexError("list assignment index out of range")

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

        new_node = Node(value, next_node=current.next)
        current.next = new_node
        self._size += 1

    def remove(self, idx: int) -> None:
        """Удаление по индексу. Сложность: O(n)."""
        if not (0 <= idx < self._size):
            raise IndexError("pop index out of range")

        # Удаление головы
        if idx == 0:
            self.head = self.head.next
            if self._size == 1: # Если это был единственный элемент
                self.tail = None
            self._size -= 1
            return

        # Ищем узел ПЕРЕД удаляемым
        current = self.head
        for _ in range(idx - 1):
            current = current.next

        # Удаляемый узел — это current.next
        node_to_remove = current.next
        current.next = node_to_remove.next

        # Если удалили последний элемент, обновляем tail
        if idx == self._size - 1:
            self.tail = current

        self._size -= 1

    def __iter__(self) -> Iterator[Any]:
        """Генератор для перебора элементов в цикле for."""
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __len__(self) -> int:
        """Возвращает текущий размер списка за O(1)."""
        return self._size

    def __repr__(self) -> str:
        return f"SinglyLinkedList({list(self)})"

# Пример использования
sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.prepend(5)
sll.insert(1, 7) # Результат: [5, 7, 10, 20]
print(sll)

sll.remove(0)

print(sll)

