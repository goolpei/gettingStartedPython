class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def __repr__(self):
        return f'Rectangle(width={self._width}, height={self._height})'

    def set_width(self, width):
        self._width = width

    def set_height(self, height):
        self._height = height
    
    def get_area(self):
        return self._height * self._width
    
    def get_perimeter(self):
        return 2 * (self._height + self._width)
    
    def get_diagonal(self):
        return ((self._height ** 2) + (self._width ** 2)) ** 0.5

    def get_picture(self):
        if (self._width or self._height) > 50:
            return 'Too big for picture.'
        picture = []
        for i in range(self._height):
            picture.append('*' * self._width)
        return '\n'.join(picture) + '\n'

    def get_amount_inside(self, other):
        return self.get_area() // other.get_area()

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __repr__(self):
        return f'Square(side={self._height})'

    def set_width(self, side):
        self._width = side
        self._height = side

    def set_height(self, side):
        self._width = side
        self._height = side

    def set_side(self, side):
        self._width = side
        self._height = side

r = Rectangle(4,4)
print(r.get_picture())
r2 = Rectangle(2,2)
print(r.get_amount_inside(r2))
print(r2)