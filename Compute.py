import matplotlib.pyplot as plt
import numpy as np
import os, time, glob
from numpy import *


def compute(a, b, c):
    # this is where you give range
    if c == 'Yes' or c == 'yes':
        # this is where you give range
        domain = eval(b)

        x = np.arange(domain[0], domain[1], .001)

        namespace = np.__dict__.copy()
        namespace.update({'x': x})
        formula = eval(a, namespace)

        fig, ax = plt.subplots()
        ax.plot(x, formula)

        ax.set(xlabel='X Axis ', ylabel='Y Axis',
               title='Kick some tail')
        ax.grid()

        fig.savefig("test.png")

        if not os.path.isdir('static'):
            os.mkdir('static')
        else:
            # Remove old plot files
            for filename in glob.glob(os.path.join('static', '*.png')):
                os.remove(filename)
            # Use time since Jan 1, 1970 in filename in order make
            # a unique filename that the browser has not chached
        plotfile = os.path.join('static', str(time.time()) + '.png')
        plt.savefig(plotfile)
        return plotfile
    elif c == 'No' or c == 'no':
        domain = eval(b)

        x = np.arange(domain[0], domain[1], .001)

        namespace = np.__dict__.copy()
        namespace.update({'x': x})
        formula = eval(a, namespace)

        plt.plot(x, formula)
        plt.title("Exercise Three Graph")
        plt.legend()
        if not os.path.isdir('static'):
            os.mkdir('static')
        else:
            # Remove old plot files
            for filename in glob.glob(os.path.join('static', '*.png')):
                os.remove(filename)
            # Use time since Jan 1, 1970 in filename in order make
            # a unique filename that the browser has not chached
        plotfile = os.path.join('static', str(time.time()) + '.png')
        plt.savefig(plotfile)
        return plotfile
    else:
        return


