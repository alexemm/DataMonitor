from Equation import Expression

import numpy as np


def text2lambda(text):
    return Expression(text, 'x')


def create_data_from_function(f, begin, end, steps=69):
    x = np.linspace(begin, end, steps)
    y = np.array(list(map(f, x)))
    return x, y
