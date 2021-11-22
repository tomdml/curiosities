from functools import partial

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def update(Z, M):
    pass


Z = np.random.randint(2, size=(300, 600))
M = np.zeros(Z.shape)

# Output logic
ySize, xSize = Z.shape
dpi = 80.0
figsize = (xSize / dpi, ySize / dpi)
fig = plt.figure(figsize=figsize, dpi=dpi)
fig.add_axes([0.0, 0.0, 1.0, 1.0], frameon=False)

im = plt.imshow(
    M,
    interpolation='nearest',
    cmap=plt.cm.gray_r,
    vmin=0,
    vmax=1)

plt.xticks([])
plt.yticks([])

func = partial(update, Z, M)

animation = FuncAnimation(
    fig,
    func,
    interval=10,
    frames=2000)

plt.show()
