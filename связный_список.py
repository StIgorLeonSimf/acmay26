class Box:
    def __init__(self, cat=None):
        self.cat = cat
        self.next_box = None

    def __str__(self):
        return f'{self.cat} -> {self.next_box}'


class LinkedList:

    def __init__(self):
        self.head = None
        self.last_box = None

    def in_(self, name):
        current_box = self.head
        while current_box:
            if name == current_box.cat:
                return True
            current_box = current_box.next_box
        return False

    def append(self, name):
        new_box = Box(name)
        if self.head == None:
            self.head = new_box
            self.last_box = self.head
            return
        # current_box = self.head
        # while current_box.next_box:
        #     current_box = current_box.next_box
        # current_box.next_box = new_box

        self.last_box.next_box = new_box
        self.last_box = new_box

    def get(self):
        current_box = self.head
        self.head = self.head.next_box
        current_box.next_box = None
        return current_box

    def remove(self, name):
        current_box = self.head
        previous_box = None
        if current_box.cat == name:
            self.head = self.head.next_box
            return

        while current_box:
            if current_box.cat == name:
                if current_box.next_box:
                    previous_box.next_box = current_box.next_box
                else:
                    previous_box.next_box = None
                break
            previous_box = current_box
            current_box = current_box.next_box
        else:
            raise ValueError(f'{name} в списке отсутствует!')

    def __str__(self):
        return f'{self.head}'


ll = LinkedList()
ll.append('Барсик')
ll.append('Мурчик')
ll.append('Alisa')
print(ll)
print(ll.in_('Alisa1'))
# print(ll.get())
ll.remove('Alisa1')
print(ll)
