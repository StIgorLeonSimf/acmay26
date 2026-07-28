class People:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.lang = ['English', 'French', 'Swedish','Russian']
        # self.cnt = None

    def __iter__(self):
        self.cnt = 0
        return self

    def __next__(self):
        # obj = (self.name, self.surname, self.age)
        obj = self.lang
        if self.cnt < len(obj):
            res = obj[self.cnt]
            self.cnt += 1
            return res
        raise StopIteration

    def __str__(self):
        return f' {self.name},  {self.surname},  {self.age}'


p1 = People('Dasha', 'Petrova', 18)
car = ['GAZ', 'VAZ', 'MAZ']
lst = [car, p1]

for i in lst:
    for j in i:
        print(j)
# it = iter(car)
# print(next(it))
# print(next(it))
print(car[0])
print(p1.lang[-1])