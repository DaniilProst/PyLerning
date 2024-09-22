class Vehicle:
    __COLOR_VARIANTS = ['black', 'white', 'blue', 'red', 'green']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return print(f'Модель: {self.__model}')

    def get_horsepower(self):
        return print(f'Мощность двигателя:{self.__engine_power}')

    def get_color(self):
        return print(f'Цвет:{self.__color}')

    def print_info(self):
        return self.get_model(), self.get_horsepower(), self.get_color(), print(f'Владелец:{self.owner}')

    def set_color(self, new_color):

        for i in self.__COLOR_VARIANTS:
            if new_color.upper() == i.upper():
                self.__color = new_color

        if self.__color != new_color:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()
