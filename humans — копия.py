"""Напишите класс Human (Человек). Экземпляр класса инициализируется
 с аргументами: имя, произвольное количество сущностей,
 именованный аргумент – уровень магии со значением по умолчанию 0.

Класс обеспечивает выполнение методов (hm – экземпляр класса):

hm.change_name() – изменить имя – к имени через пробел добавляется
строка-аргумент;
экземпляру класса можно прибавить строку: hm += line – строка
дописывается к списку сущностей, уровень магии увеличивается на
 длину строки, нацело деленную на 4;
экземпляры класса можно вычитать друг из друга: hm2 = hm - hm1 –
возвращается новый экземпляр класса с атрибутами – имя составленное
 из первых трёх букв первого и последних трёх второго, обе части с
 большой буквы, сущности только те, что есть у первого, но нет у второго,
 порядок алфавитный, уровень магии по умолчанию;
экземпляр класса можно вызвать с аргументом-числом: возвращается
список из указанного числа сущностей с начала;
экземпляры класса можно сравнивать: сначала по уровню магии,
затем по количеству сущностей, затем по имени по алфавиту;
для печати возвращается строка вида: Human by name <name>
(<entities>, <magic>) Человек по имени <имя> (<сущности через запятую и пробел>, <уровень магии>)
Пример:
Ввод
hm = Human('Illmarrannen', 'Forgiving', 'Forgiven', magic=2)
hm.change_name('Rual')
id_hm = id(hm)
hm += 'Skyman'
print(hm, hm(2), sep='\n')
print(id_hm == id(hm))
Вывод:
Human by name Illmarrannen Rual (Forgiving, Forgiven, Skyman, 3)
['Forgiving', 'Forgiven']
True

Bвод:     hm = Human('Marran', 'Hanger', 'Stick', 'Wizzard', magic=10)
hm1 = Human('Lart', 'Wizzard')
print(hm, hm1, sep='\n')
print(hm > hm1, hm <= hm1, hm == hm1)
hm2 = hm - hm1
print(hm2)
print(hm2 > hm1, hm2 <= hm, hm2 != hm)

Вывод:
Human by name Marran (Hanger, Stick, Wizzard, 10)
Human by name Lart (Wizzard, 0)
True False False
Human by name MarArt (Hanger, Stick, 0)
True True True
"""


class Human:
    def __init__(self, name, *entities, magic=0):
        self.name = name
        self.entities = list(entities)
        self.magic = magic

    def change_name(self, name):
        if not isinstance(name, str):
            raise TypeError('Аргумент должен быть "строкой"')
        self.name = f'{self.name} {name}'

    def __add__(self, other):
        if not isinstance(other, str):
            raise TypeError('Аргумент должен быть "строкой"')

        self.entities.append(other)
        self.magic += (len(other) // 4)
        return self

    def __sub__(self, other):
        if not isinstance(other, Human):
            raise TypeError('Аргумент должен быть объектом класса Human')
        name = self.name[:3].capitalize() + other.name[-3:].capitalize()
        entities = list(set(self.entities) - set(other.entities))
        entities.sort()
        return Human(name, *entities)

    def __call__(self, number):
        return self.entities[:number]

    def __eq__(self, other):
        return (self.magic == other.magic and
                len(self.entities) == len(other.entities) and
                self.name == other.name)

    def __gt__(self, other):
        if self.magic > other.magic:
            return True
        if self.magic == other.magic:
            if len(self.entities) > len(other.entities):
                return True
            if len(self.entities) == len(other.entities):
                if self.name > other.name:
                    return True
        return False

    def __lt__(self, other):
        if self.magic < other.magic:
            return True
        if self.magic == other.magic:
            if len(self.entities) < len(other.entities):
                return True
            if len(self.entities) == len(other.entities):
                if self.name < other.name:
                    return True
        return False

    def __ge__(self, other):
        if self.magic >= other.magic:
            return True
        return False

    def __le__(self, other):
        if self.magic <= other.magic:
            return True
        return False

    def __ne__(self, other):
        return (self.magic != other.magic or
                len(self.entities) != len(other.entities) or
                self.name != other.name)


    def __str__(self):
        return (f'Human by name {self.name} ({", ".join(self.entities)}, '
                f'{self.magic})')


# hm = Human('Illmarrannen', 'Forgiving', 'Forgiven', magic=2)
# hm.change_name('Rual')
# id_hm = id(hm)
# hm += 'Skyman'
# print(hm, hm(2), sep='\n')
# print(id_hm == id(hm))

hm = Human('Marran', 'Hanger', 'Stick', 'Wizzard', magic=10)
hm1 = Human('Lart', 'Wizzard')
print(hm, hm1, sep='\n')
print(hm > hm1, hm <= hm1, hm == hm1)
hm2 = hm - hm1
print(hm2)
print(hm2 > hm1, hm2 <= hm, hm2 != hm)
