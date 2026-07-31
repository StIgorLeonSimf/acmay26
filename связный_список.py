class Box:
    def __init__(self, cat=None):
        self.cat = cat
        self.next_box = None

    def __str__(self):
        return f'{self.cat} -> {self.next_box}'


class LinkedList():
    last_box = None
    def __init__(self):
        self.head = None

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
            LinkedList.last_box = self.head
            return
        # current_box = self.head
        # while current_box.next_box:
        #     current_box = current_box.next_box
        # current_box.next_box = new_box

        LinkedList.last_box.next_box = new_box
        LinkedList.last_box = new_box

    def __str__(self):
        return f'{self.head}'


ll = LinkedList()
ll.append('Барсик')
ll.append('Мурчик')
ll.append('Alisa')
print(ll)
print(ll.in_('Alisa1'))