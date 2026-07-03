class People:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    def __str__(self):
        return f'{self.__name} - {self.__age}'


class Flat:
    def __init__(self, number):
        self.__number = number
        self.people = []

    @property
    def number(self):
        return self.__number

    def add_people(self, *people):
        for p in people:
            if not isinstance(p, People):
                raise TypeError('Объект должен принадлежать классу People')
            self.people.append(p)

    def display(self):
        # mx = 0
        # for p in self.people:
        #     if len(p.name) > mx:
        #         mx = len(p.name)
        mx_obj = max(self.people, key=lambda p: len(p.name))
        mx = len(mx_obj.name)
        print(self)
        for n, p in enumerate(self.people, 1):
            print(f'{n}. {p.name:{mx}} - {p.age}')
        print()

    def __str__(self):
        return f'Квартира №{self.__number}'
    
    
class Floor:
    def __init__(self, numb):
        self.__number = numb
        self.flats = []

    @property
    def number(self):
        return self.__number

    def add_flats(self, *flats):
        for f in flats:
            if not isinstance(f, Flat):
                raise TypeError('Разрешён только объект класса Flat')
            self.flats.append(f)


    def display(self):
        mx = 0
        for f in self.flats:
            mx_obj = max(f.people, key=lambda p: len(p.name))
            if mx < len(mx_obj.name):
                mx = len(mx_obj.name)

        cnt = 1
        print(self)
        for f in self.flats:
            print('\t\t', f)
            for p in f.people:
                print(f'\t\t\t{cnt:2}. {p.name:{mx}} - {p.age}')
                cnt += 1

    def __str__(self):
        return f'\tЭтаж №{self.__number}'


class Dom:
    def __init__(self, num):
        self.__num = num
        self.floors = []

    def add_floors(self, *floors):
        for f in floors:
            if not isinstance(f, Floor):
                raise TypeError('Разрешён только объект класса Floor')
            self.floors.append(f)

    def display(self):
        mx = 0
        count_people = 0
        for fl in self.floors:
            for f in fl.flats:
                count_people += len(f.people)
                mx_obj = max(f.people, key=lambda p: len(p.name))
                if mx < len(mx_obj.name):
                    mx = len(mx_obj.name)

        cnt = 1
        print(self)
        for fl in self.floors:
            print(f'{fl}  Кол-во квартир - {len(fl.flats)}')
            for f in fl.flats:
                print(f'\t\t{f}' )
                for p in f.people:
                    print(f'\t\t\t{cnt:2}. {p.name:{mx}} - {p.age}')
                    cnt += 1

    def __str__(self):
        return f'Дом №{self.__num}'





p1 = People('Klava Koka', 30)
p2 = People('Said ibn Hattab', 80)
p3 = People('Jhone', 32)
p4 = People('Pol Maccartney', 70)

p5 = People('Klava Koka1', 30)
p6 = People('Said ibn Hattab1', 80)
p7 = People('Jhone1', 32)
p8 = People('Pol Maccartney1', 70)

kv45 = Flat(45)
kv46 = Flat(46)
kv55 = Flat(55)
kv56 = Flat(56)

fl4 = Floor(4)
fl5 = Floor(5)

dom = Dom('3, ул. Циолковского ')

# print(kv45)
kv45.add_people(p1, p3)
kv46.add_people(p2, p4)
kv55.add_people(p5, p6)
kv56.add_people(p7, p8)
# kv45.display()
# kv46.display()
fl4.add_flats(kv45, kv46)
fl5.add_flats(kv55, kv56)
# fl4.display()
# fl5.display()
dom.add_floors(fl4, fl5)
dom.display()