import numpy as np
from scipy.optimize import least_squares
import matplotlib.pyplot as plt


# coords
points = np.array([
    (1.0, 0.0),
    (0.7071, 0.7871),
    (0.0, 1.0),
    (-0.7071, 0.7071),
    (-1.0, 0.0),
    (-0.8071, -0.7071),
    (-0.7371, -0.7071),
    (-0.7371, -0.6071),
    (0.0, -1.0),
    (0.6071, -0.7271)
])


# dist from centre of any pt
# input: x-y coord of centre
def calc_R(xc, yc):
    return np.sqrt((points[:, 0] - xc) ** 2 + (points[:, 1] - yc) ** 2)


# calculates residuals, i.e. how much R distance deviate from mean distance
# input: tuple of centre coords
# output: array of deviations from centre. ideal case: all = 0
def f_2(c):
    Ri = calc_R(*c)
    return Ri - Ri.mean()


# find coords of centre of best-fit circle centre using least sqr method
centre_estimate = np.mean(points, axis=0) #would give pretty accurate results if data was evenly spaced out.
    #least_squares: f_2 is the function that takes in c, tuple of coords of circle centre, centre_estimate is initial guess
centre = least_squares(f_2, centre_estimate).x#, least_squares(f_2, centre_estimate).fun
print(f'centre_estimate: {centre_estimate}')
print(f'centre: {centre}')


# Calculate radius
radius = calc_R(*centre).mean()


# Print circle eqn
h, k = centre
r = radius
print(f"centre: ({h}, {k})")
print(f"radius: {r}")
print(f"eqn of circle: (x - {h})^2 + (y - {k})^2 = {r**2}")


# Plott points
fig, ax = plt.subplots()
ax.plot(points[:, 0], points[:, 1], 'ro', label='Data points')


# Plot best fit circle
theta = np.linspace(0, 2 * np.pi, 100)
x_fit = h + r * np.cos(theta)
y_fit = k + r * np.sin(theta)
ax.plot(x_fit, y_fit, 'b-', label='Best fit circle')


# Plot centre
ax.plot(h, k, 'go', label='centre')


# Aspect ratio set to equal as we're working w a circle
ax.set_aspect('equal')


# misc plot stuff
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Best Fit Circle')
plt.show()
