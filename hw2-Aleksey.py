class Figure:
    unit = 'mm'

    def __init__(self):
        self.perimeter = 0

    def calculate_area(self):
        pass

    def info(self):
        pass


class Circle(Figure):
    def __init__(self, __radius):
        super().__init__()
        self.__radius = __radius

    def calculate_area(self): return 3.14 * (self.__radius ** 2)

    def info(self): print(f'Circle radius: {self.__radius} {self.unit}\narea: {self.calculate_area()} {self.unit}')


class RightTriangle(Figure):
    def __init__(self, __side_a, __side_b):
        super().__init__()
        self.side_a = __side_a
        self.side_b = __side_b

    def calculate_area(self): return 0.5 * self.side_b * self.side_a

    def info(self): print(f'RightTriangle side a: {self.side_a} {self.unit},'
                          f' side b: {self.side_b} {self.unit}, '
                          f'area: {self.calculate_area()} {self.unit}')


figure_list = [Circle(5), Circle(2), RightTriangle(3, 4), RightTriangle(5, 9), RightTriangle(6, 7)]
for figure in figure_list:
    figure.info()

# class Figure:
#
#     unit = 'cm'
#
#     def __init__(self):
#         self.__perimeter = 0
#
#     @property
#     def perimeter(self):
#         return self.__perimeter
#
#     @perimeter.setter
#     def perimeter(self, value):
#         if not isinstance(value, int) or value < 0:
#             raise TypeError('Wrong value type it must'
#                             ' be positive (float or integer)')
#         else:
#             self.perimeter = value
#
#     def calculate_area(self):
#         pass
#
#     def calculate_perimeter(self):
#         pass
#
#     def info(self):
#         pass
#
#
# class Square(Figure):
#     def __init__(self, side_length):
#         super().__init__()
#         self.side_length = int(side_length)
#         self.perimeter = self.calculate_perimeter()
#
#     def calculate_area(self): return self.side_length ** 2
#
#     def calculate_perimeter(self): return self.side_length * 4
#
#     def info(self): print(f'Square side length: {str(self.side_length) + self.unit}'
#                           f', perimeter:' f'{str(self.perimeter) + self.unit},'
#                           f' area: {str(self.calculate_area()) + self.unit}.')
#
#
# class Rectangle(Figure):
#     def __init__(self, length, width):
#         super().__init__()
#         self.length = int(length)
#         self.width = int(width)
#         self.perimeter = self.calculate_perimeter()
#
#     def calculate_area(self): return self.length * self.width
#
#     def calculate_perimeter(self): return self.length * 2 + self.width * 2
#
#
# def info(self):
#     print(f'Rectangle length: {str(self.length) + self.unit},'
#           f' width: {str(self.__width) + self.unit},'
#           f' ' f'perimeter: {str(self.perimeter) + self.unit},'
#           f' area: {str(self.calculate_area()) + self.unit}')
#
#
# figures = [Square(5), Square(6), Rectangle(2, 4), Rectangle(5, 8), Rectangle(7, 10)]
# for figure in figures:
#     figure.info()
