import matplotlib.pyplot as plt
import numpy as np

def y(a = 1, b = 1, c = 0, title='NoName Parabola'):
    x = np.arange(-10, 10, 0.01)
    y = a * x ** 2 + b * x + c

    plt.plot(x, y, label='NoName Parabola')
    plt.savefig('pic_2.png')
y()