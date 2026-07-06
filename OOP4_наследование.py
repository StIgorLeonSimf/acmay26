# def display(self):
#     mx = 0
#     # for fl in self.floors:
#     #     for f in fl.flats:
#     #         mx_obj = max(f.people, key=lambda p: len(p.name))
#     #         if mx < len(mx_obj.name):
#     #             mx = len(mx_obj.name)
#     # spl = max(len(p.name) for fl in self.floors for f in fl.flats for p in f.people)
#     # print(f'{spl}')
#     mx = max(len(p.name) for fl in self.floors for f in fl.flats for p in f.people)
#
#     cnt = 1
#     print(self)
#     for fl in self.floors:
#         print(f'\t{fl} Кол-во квартир - {len(fl.flats)}, '
#               f'Кол-во жителей на этаже - '
#               f'{reduce(lambda x, y: len(x.people) + len(y.people), fl.flats)}')
#         for f in fl.flats:
#             print('\t\t', f'{f} Кол-во жителей в кв-ре - {len(fl.flats)}')
#             for p in f.people:
#                 print(f'\t\t\t{cnt:2}. {p.name:{mx}} - {p.age}')
#                 cnt += 1
#
# def __str__(self):
#     return f'Дом №{self.__num}'

# class Mechanism:
#         def __init__(self, name):
#             self.__name = name
#
#         @property
#         def name(self):
#             return self.__name
#
#         @name.setter
#         def name(self, new):
#             if not isinstance(new, str):
#                 raise TypeError('Значение должно быть строкой')
#             self.__name = new
#
#         def __str__(self):
#             return self.__name
#
#
# class Car(Mechanism):
#     name = 'Автомобиль'
#     def __init__(self, model):
#             super().__init__(Car.name)
#             self.__model = model
#
#     @property
#     def model(self):
#         return self.__model
#
#     def __str__(self):
#         return f'{self.name}, {self.__model}'
#
# class Version(Car):
#     def __init__(self, model, version):
#         super().__init__(model)
#         self.__version = version
#
#     def __str__(self):
#         return f'{self.name} {self.model}-{self.__version}'
#
#
# m1 = Mechanism('Автомобиль')
# print(m1)
# car = Car('Москвич')
# car1 =Car('Toyota')
# ver = Version('Москвич', 412)
# print(car)
# print(ver)
# # print(Car.name)
# # print(car1.name)
# # print(isinstance(m1, Mechanism))
# # print(isinstance(m1, Car))
# # print(isinstance(car, Mechanism))
# # print(isinstance(car, Car))
# class PlayMixin:
#     @staticmethod
#     def play(chanal='1'):
#         match chanal:
#             case '1': print('Играет "ABBA"')
#             case '2': print('Играет "Beatles"')
#             case '3': print('Поет Лепс')
#             case _: print('Идут "Новости"')
#
#
# class Car(PlayMixin):
#     def ride(self):
#         print('Едет по дороге')
#
#     # @staticmethod
#     # def play():
#     #     print('Играет "ABBA"')
#
# class Boat(PlayMixin):
#     def swim(self):
#         print('Ходит по воде')
#
#     # @staticmethod
#     # def play():
#     #     print('Играет "ABBA"')
#
#
# class Amphibian(Car, Boat):
#     def display(self):
#         print('Amphibian')
#
#
# am = Amphibian()
# am.display()
# am.ride()
# am.swim()
# am.play('3')
# am.play()
# # print(Amphibian.mro())

class Name:
    def __init__(self, name):
        self.name = name


class Surname:
    def __init__(self, surname):
        self.surname = surname

class MiddleName:
    def __init__(self, midname):
        self.midname = midname

class FIO(Name, Surname, MiddleName):
    def __init__(self, name, midname, surname):
        super().__init__(name)
        Surname.__init__(self, surname)
        MiddleName.__init__(self,midname)

    def __str__(self):
        return f'{self.name} {self.midname} {self.surname}'


n = Name('Dasha')
m = MiddleName('Andreevna')
s = Surname('Ivanova')

p = FIO('Alina', 'Petrovna', 'Popova')
print(p)
p1 = FIO(n.name, m.midname, s.surname)
print(p1)
mn = MiddleName(p.midname)
print(mn.midname)