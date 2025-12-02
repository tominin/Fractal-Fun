#!/home/tom/snap/miniconda3/envs/fractal/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from pylab import imshow, show

dpi = 500
image_save_dpi = 1200

def mandel(x, y, max_iters):
	c = complex(x, y)
	z = 0.0j
	for i in range(max_iters):
		z = z*z + c
		if (z.real*z.real + z.imag*z.imag) >= 4:
			return i
	return max_iters

def create_fractal(ax, iters=200, width=1086, height=1086):
	min_x, max_x = ax.get_xlim()
	min_y, max_y = ax.get_ylim()

	xs = np.linspace(min_x, max_x, width)
	ys = np.linspace(min_y, max_y, height)
	img = np.zeros((height, width), dtype=np.uint8)

	for ix, x in enumerate(xs):
		for iy, y in enumerate(ys):
			img[iy, ix] = mandel(x, y, iters)

	return img


fig, ax = plt.subplots()
ax.set_xlim(-2.0, 1.0)
ax.set_ylim(-1.0, 1.0)

img = create_fractal(ax)
im = ax.imshow(img, origin="lower", extent=ax.get_xlim() + ax.get_ylim(), cmap="inferno")

def on_zoom(event):
	global im
	img = create_fractal(ax)
	im.set_data(img)
	im.set_extent(ax.get_xlim() + ax.get_ylim())
	plt.draw()
ax.callbacks.connect("xlim_changed", on_zoom)
ax.callbacks.connect("ylim_changed", on_zoom)
plt.show()
