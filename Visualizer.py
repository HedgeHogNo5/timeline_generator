import numpy as np
import matplotlib.pyplot as plt

flubber = (
    1  # This is a dump variable that I am using to switch which graphb is produced
)

if flubber == 0:
    fig = plt.figure()
    axs = plt.axes()

    x = np.linspace(0, 10, 1000)
    axs.plot(x, np.cos(x))

    plt.show()  # This is my first attempt to produce a graph. It should produce a Cos(x) graph between 0 and 10


if flubber == 1:
    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True

    x = np.linspace(-10, 10, 50)
    y = np.sin(x)

    plt.axhline(y=0, c="green", linestyle="dashdot", label="y=0")
    plt.plot(x, y, c="red", lw=5, linestyle="dashdot", label="y=sin(x)")
    plt.grid(False)
    plt.axis("off")
    plt.legend("off")
    plt.show()  # This is a snippet of code that I took from www.tutorialspoint.com. (n.d.). How to hide axes and
    # gridlines in Matplotlib. [online] Available at:
    # https://www.tutorialspoint.com/how-to-hide-axes-and-gridlines-in-matplotlib [Accessed 2 Oct. 2023]. I am using it
    # to help me understand the intricacies of using Matplotlib.pyplot

if flubber == 2:
    plt.rcParams["figure.autolayout"] = True
