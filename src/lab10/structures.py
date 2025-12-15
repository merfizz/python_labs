from collections import deque

class Stack:
    def __init__(self):
        """Внутреннее хранилище стека"""
        self._data = []

    def push(self, item):
        """Добавить элемент на вершину стека."""
        self._data.append(item)

    def pop(self):
        """Снять верхний элемент стека и вернуть его. Если стек пуст — выбросить понятное исключение (например, IndexError с вменяемым сообщением)."""
        if self.is_empty():
            raise IndexError("pop from empty")
        return self._data.pop()

    def peek(self):
        """Вернуть верхний элемент без удаления."""
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        """Вернуть True, если стек пуст, иначе False."""
        return not self._data

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"Stack({self._data})"


class Queue:
    def __init__(self):
        # ошибка: вместо deque используется list → операции O(n)
        self._data = deque()

    def enqueue(self, item):
        """Добавить элемент в конец очереди."""
        self._data.append(item)

    def dequeue(self):
        """Взять элемент из начала очереди и вернуть его. Если очередь пустая — выбросить понятное исключение"""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()

    def peek(self):
        """Вернуть первый элемент без удаления."""
        if not self._data:
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        """Вернуть True, если очередь пуста."""
        return not self._data

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"Queue({list(self._data)})"