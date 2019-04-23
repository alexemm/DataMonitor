import matplotlib.pyplot as plt

# Maybe super class?
#
# class

class NormalPlot:
    def __init__(self, *args, **kwargs):
        self.x = args[0]
        self.y = args[1]

    def visualize(self):
        plt.plot(self.x, self.y)


# todo
class ScatterPlot:
    pass


# todo
class Hist:
    pass


class PolarPlot:
    def __init__(self, *args, **kwargs):
        self.x = args[0]
        self.y = args[1]

    def visualize(self):
        plt.polar(self.x, self.y)

kinds = {'normal': NormalPlot,
         'scatter': ScatterPlot,
         'hist': Hist,
         'polar': PolarPlot}
