
class Figure:
    sides_count = 0
    def __init__(self, color, *sides):
        self._sides = list(sides)
        self._color = list(color)
        self.filled = False
        if len(self._sides) == 1:
            self._sides = [self._sides[0]] * self.sides_count
        elif len(list(self._sides)) != self.sides_count:
            self._sides = [1] * self.sides_count

    def get_color(self):
        return self._color

    def get_sides(self):
        return self._sides
    def _is_valid_color(self, r, g, b):
        f = True
        for i in [r, g, b]:
            if i < 0 or i > 255:
                f = False
        return f
    def set_color (self, r, g, b):
        if self._is_valid_color(r,g, b):
            self._color = [r, g, b]
    def _is_valid_sides(self, *new_sides):
        f = True
        if len(new_sides) != self.sides_count:
            f = False
        for i in new_sides:
            if i < 0 or not(isinstance(i, int)):
                f = False
        return f
    def set_sides(self, *new_sides):
        if self._is_valid_sides(*new_sides):
            self._sides =list(new_sides)

    def __len__(self):
        return sum(list(self._sides))

class Circle (Figure):
    sides_count = 1
    def __init__(self, color, len1):
        super().__init__(color, len1)
        self._radius = len1 /(2*3.14)

    def get_square(self):
        return (int(self._sides[0])**2)/(4*3.14)


class Cube(Figure):
    sides_count = 12
    def __init__(self, color, *edge):
        super().__init__(color, *edge)
    def get_volume(self):
        return (int(self._sides[0]))**3

class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, *len3):
        super().__init__(color, *len3)
        #if len(len3) != self.sides_count:
           # self._sides = [1] * self.sides_count
        #else:
            #self._sides = [self.len3[0]] * self.sides_count
    def get_square(self):
        p = sum(list(self._sides))/2
        return (p*(p-self._sides[0])**3)**0.5



circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6 )
print(cube1.get_volume())
triangle1 = Triangle ((100,100,30), 30)
# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4) # Не изменится
print(cube1.get_sides())
cube1.set_sides(5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5) # изменится

print(cube1.get_sides())
print(circle1.get_square())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())
print(circle1.get_square())
circle1.set_sides(23) # Изменится
print(circle1.get_sides())
circle1.set_sides(15, 3) # неИзменится
print(circle1.get_sides())
circle1.set_sides(15.2) # неИзменится
print(circle1.get_sides())


# Проверка объёма (куба):
print(cube1.get_volume())
#проверка площади круга
print(circle1.get_square())
#проверка площади треугольника
print(triangle1.get_square())
print(triangle1.get_sides())
print(triangle1.get_square())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))
print(len(cube1))
print(len(triangle1))