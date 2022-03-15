import math
import matplotlib.pyplot as plt
import sys

file_1 = open('Loop_Heights.txt', 'w')
file_2 = open('Loop_Coordinates.txt', 'w')

# initial height
H = 100.0

# maximum R to test to
R_max = 200

# used to store R vs h_max
pts_1 = []

# used to store R vs the x coordinate at h_max
pts_2 = []

# for many sets of R
for R in range(1, R_max + 1, 1):
    # height function
    h = 0.0

    # used to track the maximum height
    h_max = 0.0

    # used to track the x coordinate at the maximum height
    x_max = 0.0

    # horizontal distance function
    x = 0.0

    # change in horizontal distance
    dx = 0.0

    # point representing current horizontal distance and height
    point = [x, h]

    # radius of curvature function
    r = (R * (H - h)) / H

    # amount height will be incremented by
    incr = 10.0 ** -3

    # point representing horizontal distance and height from the previous step
    prev_point = [x - incr, h]

    # direction of velocity vector for given point
    vec = [point[0] - prev_point[0], point[1] - prev_point[1]]

    # magnitude of the velocity vector (used to extract a unit direction from the velocity vector)
    vec_len = math.sqrt(vec[0] ** 2 + vec[1] ** 2)

    # where the center of rotation is for a certain point
    center = [point[0] - (r / vec_len) * vec[1], point[1] + (r / vec_len) * vec[0]]

    # the loop going up
    while r ** 2 - ((h + incr) - center[1]) ** 2 >= 0 and r ** 2 - (h - center[1]) ** 2 >= 0:
        # calculate the change in x given that h is increased by incr
        dx = math.sqrt(r ** 2 - ((h + incr) - center[1]) ** 2) - math.sqrt(r ** 2 - (h - center[1]) ** 2)

        # increment x and h
        x += dx
        h += incr

        # check if this is the maximum height
        if h > h_max:
            h_max = h
            x_max = x

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

    # add values to list of points
    pts_1.append([R, h_max])
    pts_2.append([R, x_max])

    # print the initial radius of curvature vs maximum height
    file_1.write(str(R) + "," + str(h_max) + "\n")

    # print the horizontal and vertical coordinates of the peak of the loop
    file_2.write(str(x_max) + "," + str(h_max) + "\n")

    # print the progress left
    print("PROGRESS:", str(R) + "/" + str(R_max))

# close the files
file_1.close()
file_2.close()

# compile the horizontal and vertical coordinates
hori_1 = [pt[0] for pt in pts_1]
vert_1 = [pt[1] for pt in pts_1]
hori_2 = [pt_2[0] for pt_2 in pts_2]
vert_2 = [pt_2[1] for pt_2 in pts_2]

# create a graph with equal axes
fig = plt.figure()
sp_1 = fig.add_subplot(1, 3, 1)
sp_2 = fig.add_subplot(1, 3, 2)
sp_3 = fig.add_subplot(1, 3, 3)
sp_1.plot(hori_1, vert_1)
sp_2.plot(hori_2, vert_2)
sp_3.plot(vert_2, vert_1)
sp_1.set_aspect('equal', adjustable='box')
sp_1.set_title('Loop Height vs Initial Radius of Curvature')
sp_1.set_xlabel('Initial Radius of Curvature')
sp_1.set_ylabel('Maximum Loop Height')
sp_2.set_aspect('equal', adjustable='box')
sp_2.set_title('Peak Distance vs Initial Radius of Curvature')
sp_2.set_xlabel('Initial Radius of Curvature')
sp_2.set_ylabel('X-Coordinate of Peak of Loop')
sp_3.set_aspect('equal', adjustable='box')
sp_3.set_title('Loops with Different Radii of Curvature')
sp_3.set_xlabel('X-Coordinate of Maximum Loop Height')
sp_3.set_ylabel('Y-Coordinate of Maximum Loop Height')

# show graph
plt.show()
