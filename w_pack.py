'''
from math import sin
a = 71
b = 171
c = 108
d = 218
h = 109
s1 = a * b
s2 = c * d
v = h / 3 *(s1 + (s1 * s2) ** 0.5 + s2)
print(s1, s2, v)
v1 = (s1 + s2) / 2 * h
print(v1)
depth = 30
h1 = h- depth * sin(109 / 111)
print(h1)
'''
from tkinter import *

root = Tk()

class StrVar(StringVar):
    def __init__(self, func):
        super().__init__(self)
        self.func = func

    def get(self):
        a = super().get()
        return_value = self.func(a) * 5
        return return_value


s = StrVar()
s.set(5)
out = s.get()
print(out)

for i, func in (("5", int),):
    print(func(i) * 3)
