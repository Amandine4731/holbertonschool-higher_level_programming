#!/usr/bin/python3
"""
Python program
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ return a sentence """
        return ("[Square] ({}) {}/{} - {}".format
                (self.id, self.x, self.y, self.size))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ travel in a tuple """
        if len(args) > 0:
            for i in range(len(args)):
                if i >= 1:
                    self.size = args[1]
                if i >= 2:
                    self.x = args[2]
                if i >= 3:
                    self.y = args[3]
                else:
                    self.id = args[0]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
