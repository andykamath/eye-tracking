from math import isnan as nan
import matplotlib.pyplot as plt
import pandas
df = pandas.read_csv('data.csv')
left_x = df['LGazePointOnDisplayX']
left_y = df['LGazePointOnDisplayY']
right_x = df['RGazePointOnDisplayX']
right_y = df['RGazePointOnDisplayY']
left = []
right = []
for lx, ly, rx, ry in zip(left_x, left_y, right_x, right_y):
	if not (nan(lx) or nan(ly) or nan(rx) or nan(ry)):
		left.append((lx, ly))
		right.append((rx, ry))
coors = zip(left, right)
lx, ly = zip(*left)
rx, ry = zip(*right)
plt.plot(lx, ly)
plt.plot(rx, ry)
plt.show()

