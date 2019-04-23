import matplotlib.pyplot as plt

from utils.plot_kinds import kinds


class Plot:
    # visualize and save
    def __init__(self, *args, kind='normal', **kwargs):
        self.args = args
        self.kind = kind
        self.kwargs = kwargs

    def visualize(self, filename='', show=True):
        plotter = kinds[self.kind](*self.args, **self.kwargs)
        plotter.visualize()
        if filename != '':
            plt.savefig(filename)
        if show:
            plt.show()
        plt.close()


class Data:
    pass


def visualize_data():
    pass


