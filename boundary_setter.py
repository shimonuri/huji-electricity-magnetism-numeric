import numpy as np

BALL_CENTER_COORDINATE = (0, 4)
BALL_RADIUS = 2
BALL_POTENTIAL = 10
FAR_POTENTIAL = 5


def set_boundary(space):
    _set_ball_boundary(space)
    _set_far_boundary(space)


def _set_ball_boundary(space):
    for theta in np.linspace(0, np.pi):
        r = BALL_RADIUS * np.sin(theta) + BALL_CENTER_COORDINATE[0]
        z = BALL_RADIUS * np.cos(theta) + BALL_CENTER_COORDINATE[1]
        r = np.round(r, decimals=1)
        z = np.round(z, decimals=1)
        space.set_value(r, z, BALL_POTENTIAL, is_changeable=False)


def _set_far_boundary(space):
    for r in np.arange(0, space.rmax, 0.1):
        space.set_value(r, space.zmax, FAR_POTENTIAL, is_changeable=False)

    for z in np.arange(0, space.zmax, 0.1):
        space.set_value(space.rmax, z, FAR_POTENTIAL, is_changeable=False)
