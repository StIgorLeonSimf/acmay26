class People:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__children = []
        self.__parent = None

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    name = property(get_name, set_name)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


p1 = People('Ольга Воробьева', 33)
p1.set_name('Jhoney')
print(p1.get_name())
p1.name = 'Ольга Воробьева'
print(p1.name)
