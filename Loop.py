import math
import matplotlib.pyplot as plt

# initial height
H = 100.0

# height function
h = 0.0

# used to track the maximum height
h_max = 0.0

# initial radius of curvature
# interesting (H, R) combinations to explore: (100, 0.5), (100, 10), (100, 100), (100, 200)
R = 50

# radius of curvature function
r = (R * (H - h)) / H

# horizontal distance function
x = 0.0

# change in horizontal distance
dx = 0.0

# amount height will be incremented by
# note that 10.0 ** -3 can also be used
# Using 10.0 ** -5 * (H * R / (H + R)) causes issues with R = 41 and others
incr = 10.0 ** -5 * (H * R / (H + R))

# point representing current horizontal distance and height
point = [x, h]

# point representing horizontal distance and height from the previous step
prev_point = [x - incr, h]

# direction of velocity vector for given point
vec = [point[0] - prev_point[0], point[1] - prev_point[1]]

# magnitude of the velocity vector (used to extract a unit direction from the velocity vector)
vec_len = math.sqrt(vec[0] ** 2 + vec[1] ** 2)

# where the center of rotation is for a certain point
# calculated by adding the product of the radius of curvature and a pi/2 rotation of the velocity vector to the point
center = [point[0] - (r / vec_len) * vec[1], point[1] + (r / vec_len) * vec[0]]

# used to store all calculated points
coords = [[x, h]]

# makes 3 loops
for num in range(3):
    # makes the part of the loop going up
    while r ** 2 - ((h + incr) - center[1]) ** 2 >= 0 and r ** 2 - (h - center[1]) ** 2 >= 0:
        # calculate the change in x given that h is increased by incr
        # change in x and h will occur along a circular path
        # the circle will have center at the center of rotation and radius the radius of curvature
        dx = math.sqrt(r ** 2 - ((h + incr) - center[1]) ** 2) - math.sqrt(r ** 2 - (h - center[1]) ** 2)

        # increment x and h
        x += dx
        h += incr

        # check if this is the maximum height
        if h > h_max:
            h_max = h

        # set the previous point to the non-incremented values of x and h
        prev_point = [point[0], point[1]]

        # set the current point to the incremented values of x and h
        point = [x, h]

        # find the new radius of curvature
        r = (R * (H - h)) / H

        # find the new velocity vector, normalize it, and use it to find the new center of rotation
        vec = [point[0] - prev_point[0], point[1] - prev_point[1]]
        vec_len = math.sqrt(vec[0] ** 2 + vec[1] ** 2)
        center = [point[0] - (r / vec_len) * vec[1], point[1] + (r / vec_len) * vec[0]]

        # add the new point
        coords.append([x, h])

    # makes the part of the loop going down
    while r ** 2 - ((h - incr) - center[1]) ** 2 >= 0:
        # finds the change in x for a given decrease in h by incr
        dx = math.sqrt(r ** 2 - (h - center[1]) ** 2) - math.sqrt(r ** 2 - ((h - incr) - center[1]) ** 2)

        # increments x but decrements h
        x += dx
        h -= incr

        # set the previous point and current point values
        prev_point = [point[0], point[1]]
        point = [x, h]

        # find the new radius of curvature and center of rotation
        r = (R * (H - h)) / H
        vec = [point[0] - prev_point[0], point[1] - prev_point[1]]
        vec_len = math.sqrt(vec[0] ** 2 + vec[1] ** 2)
        center = [point[0] - (r / vec_len) * vec[1], point[1] + (r / vec_len) * vec[0]]

        # add the new points
        coords.append([x, h])

# print the maximum height
print("The maximum height reached was:", h_max)

# compile the horizontal and vertical coordinates
hori = [coord[0] for coord in coords]
vert = [coord[1] for coord in coords]

# create a graph with equal axes
fig = plt.figure()
sp = fig.add_subplot(111)
plt.plot(hori, vert)
sp.set_aspect('equal', adjustable='box')

# show graph
plt.show()
