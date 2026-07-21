class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
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
        picture = []
        for i in range(self._height):
            if i == 0 or i == self._height - 1:
                picture.append('*' * self._width)
            else:
                picture.append('*' + (' ' * (self._width - 2)) + '*')
        return '\n'.join(picture)

    def get_amount_inside(self, other):
        return self.get_area() // other.get_area()



r = Rectangle(2,4)
print(r.get_picture())
r2 = Rectangle(2,2)
print(r.get_amount_inside(r2))