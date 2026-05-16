class Animal:
    def __init__(self,name=str):
        self.name=name
    def make_sound(self):
        return 'generic sound'
    def describe(self):
        return f'Tôi là {self.name}, tiếng kêu: {self.make_sound()}'
class Dog(Animal):
    def __init__(self,name=str):
        super().__init__(name)
    def make_sound(self):
        return f'Gâu!'
class Cat(Animal):
    def __init__(self,name=str):
        super().__init__(name)
    def make_sound(self):
        return f'Meo!'