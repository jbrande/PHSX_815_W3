#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import numpy as np
import matplotlib.pyplot as plt

# use a plot styling package if installed: https://github.com/dhaitz/mplcyberpunk
# if not, just plot normally
iscyberpunk = False
try:
	import mplcyberpunk
	plt.style.use("cyberpunk")
	iscyberpunk = True
except Exception as e:
	pass

# default filename
filename = "output.txt"

# if the user passes a filename, read that instead
if "-filename" in sys.argv:
    filename = sys.argv[sys.argv.index('-filename') + 1]

# array to store random numbers
myx = []

# open the specified file, read the numbers into the array
with open(filename) as f:
	for line in f.readlines():
		#line = line.split("\n")[0]
		try:
			myx.append(float(line))
		except Exception as e:
			pass
	f.close()

# make a figure of a nice aspect ratio
plt.figure(figsize=(10,6))

# if the package is installed, make the histogram fancy
if mplcyberpunk:

	# the plt.hist function already makes nice bin rectangles, so instead 
	# I'm going to manually plot the top vertices of the bins and use the 
	# fancy package's glow/drop shadow effects to show the rest of the histogram.

	# histogram of the data
	n, bins, patches = plt.hist(myx, 50, density=True, alpha=0)

	#get width of a bin to make nice rectangle tops
	dl = (bins[1] - bins[0])

	# some arrays to hold the reorganized data
	newx = []
	newy = []

	# for every bin frequency, the new x values will be every top left/right vertex of 
	# the bins, and the y values will just be two of each of the frequencies, one for each vertex
	for i in range(len(n)):
		newx.append(bins[i])
		newx.append(bins[i]+dl)
		newy.append(n[i])
		newy.append(n[i])

	# and plot
	plt.plot(newx, newy, "-C0")
	
	# and make the glowies
	mplcyberpunk.add_glow_effects()

else:
	# if no fancy plotting style package, just plot this normally
	n, bins, patches = plt.hist(myx, 50, density=True, facecolor='g', alpha=0.75)

# plot formatting options
plt.xlabel('x')
plt.ylabel('Probability')
plt.title('Random Number Histogram')
plt.grid(True)

# save the figure before we show it
plt.savefig("random_histogram.png", dpi=180)
plt.show()