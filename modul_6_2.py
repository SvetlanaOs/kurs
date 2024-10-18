class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner:str, _model:str, __engine_power:int, _color:str):
        self.owner = owner
        self.model = _model
        self.engine_power = __engine_power
        self.color = _color
    def get_model(self):
        return f'Модель: {self.model}'
    def get_horsepower(self):
         return f'Мощность двигателя: {self.engine_power}'
    def get_color(self):
        return f'Цвет: {self.color}'
    def print_info(self):
        print (self.get_model(), self.get_horsepower(),self.get_color(), f'Владелец: {self.owner}', sep = '\n')
    def set_color (self, new_color:str):
        f = True
        for i in range(len(self.__COLOR_VARIANTS)):
            if new_color.upper() == self.__COLOR_VARIANTS[i].upper():
                self.color = new_color
                f = False
        if f:
            print (f"Нельзя сменить цвет на {new_color}")

class Sedan(Vehicle):
    _PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500,'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

