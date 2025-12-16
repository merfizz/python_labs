# Лаба 10
## structures
```
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
```
## linked_list
```
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
```
## Тестирование
![pic 1](/image/lab10/image.png)

# Теория
### Стек (Stack)

- **Принцип:** *LIFO* — Last In, First Out.

- **Операции:**
  - `push(x)` — положить элемент сверху;
  - `pop()` — снять верхний элемент;
  - `peek()` — посмотреть верхний, не снимая.

- **Типичные применения:**
  - история действий (undo/redo);
  - обход графа/дерева в глубину (DFS);
  - парсинг выражений, проверка скобок.

- **Асимптотика (при реализации на массиве / списке):**
  - `push` — `O(1)` амортизированно;
  - `pop` — `O(1)`;
  - `peek` — `O(1)`;
  - проверка пустоты — `O(1)`.

---

### Очередь (Queue)

- **Принцип:** *FIFO* — First In, First Out.

- **Операции:**
  - `enqueue(x)` — добавить в конец;
  - `dequeue()` — взять элемент из начала;
  - `peek()` — посмотреть первый элемент, не удаляя.

- **Типичные применения:**
  - обработка задач по очереди (job queue);
  - обход графа/дерева в ширину (BFS);
  - буферы (сетевые, файловые, очереди сообщений).

- **В Python:**
  - обычный `list` **плохо подходит** для реализации очереди:
    - удаление с начала `pop(0)` — это `O(n)` (все элементы сдвигаются);
  - `collections.deque` даёт `O(1)` операции по краям:
    - `append` / `appendleft` — `O(1)`;
    - `pop` / `popleft` — `O(1)`.

- **Асимптотика (на нормальной очереди):**
  - `enqueue` — `O(1)`;
  - `dequeue` — `O(1)`;
  - `peek` — `O(1)`.


---

### Односвязный список (Singly Linked List)

- **Структура:**
  - состоит из узлов `Node`;
  - каждый узел хранит:
    - `value` — значение элемента;
    - `next` — ссылку на следующий узел или `None` (если это последний).

- **Основные идеи:**
  - элементы не хранятся подряд в памяти, как в массиве;
  - каждый элемент знает только «следующего соседа».

- **Плюсы:**
  - вставка/удаление в **начало** списка за `O(1)`:
    - если есть ссылка на голову (`head`), достаточно перенаправить одну ссылку;
  - при удалении из середины **не нужно сдвигать** остальные элементы:
    - достаточно обновить ссылки узлов;
  - удобно использовать как базовый строительный блок для других структур
    (например, для очередей, стеков, хеш-таблиц с цепочками).

- **Минусы:**
  - доступ по индексу `i` — `O(n)`:
    - чтобы добраться до позиции `i`, нужно пройти `i` шагов от головы;
  - нет быстрого доступа к предыдущему элементу:
    - чтобы удалить узел, нужно знать его предыдущий узел → часто нужен дополнительный проход.

- **Типичные оценки:**
  - `prepend` (добавить в начало) — `O(1)`;
  - `append`:
    - при наличии `tail` — `O(1)`,
    - без `tail` — `O(n)`, т.к. требуется пройти до конца;
  - поиск по значению — `O(n)`.


---

### Двусвязный список (Doubly Linked List)

- **Структура:**
  - также состоит из узлов `DNode`;
  - каждый узел хранит:
    - `value` — значение элемента;
    - `next` — ссылку на следующий узел;
    - `prev` — ссылку на предыдущий узел.

- **Основные идеи:**
  - можно двигаться как вперёд, так и назад по цепочке узлов;
  - удобно хранить ссылки на оба конца: `head` и `tail`.

- **Плюсы по сравнению с односвязным:**
  - удаление узла по ссылке на него — `O(1)`:
    - достаточно «вытащить» его, перенастроив `prev.next` и `next.prev`;
    - не нужно искать предыдущий узел линейным проходом;
  - эффективен для структур, где часто нужно удалять/добавлять элементы
    в середине, имея на них прямые ссылки (например, реализация LRU-кэша);
  - можно легко идти в обе стороны:
    - прямой и обратный обход списка.

- **Минусы:**
  - узел занимает больше памяти:
    - нужно хранить две ссылки (`prev`, `next`);
  - код более сложный:
    - легко забыть обновить одну из ссылок и «сломать» структуру;
  - сложнее отлаживать.

- **Типичные оценки (при наличии `head` и `tail`):**
  - вставка/удаление в начале/конце — `O(1)`;
  - вставка/удаление по ссылке на узел — `O(1)`;
  - доступ по индексу — `O(n)` (нужно идти от головы или хвоста);
  - поиск по значению — `O(n)`.
