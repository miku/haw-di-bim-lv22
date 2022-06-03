import imageio.v3 as iio
import matplotlib.pyplot as plt
import numpy as np

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

n = 60
gif_path = "out.gif"
frames = []

for v in range(n):
    data = np.random.randint(0, 255, size=(200, 200))
    mask = np.fromfunction(lambda i, j: ((i + v) % 20) > 15 * (j + v % 4 > 2), (200, 200), dtype=int)
    data[mask] = 0
    frames.append(data)


frames = np.stack(
    frames,
    axis=0
)

iio.imwrite(gif_path, frames, mode="I", loop=10)
