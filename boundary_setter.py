import numpy as np
from dataclasses import dataclass


@dataclass
class Ball:
    r: int
    z: int
    potential: int
    radius: int


BALL = Ball(r=0, z=4, radius=2, potential=10)

FAR_POTENTIAL = 5


def set_boundary(space):
    _set_ball_boundary(space)
    _set_far_boundary(space)


def _set_ball_boundary(space):
    for r in np.arange(BALL.r, BALL.r + BALL.radius + 0.1, 0.1):
        current_radius = ((2 - r) / 2) * BALL.radius
        for z in np.arange(BALL.z - current_radius, BALL.z + current_radius + 0.1, 0.1):
            space.set_value(
                r=np.round(r, decimals=1),
                z=np.round(z, decimals=1),
                value=BALL.potential,
                is_changeable=False,
            )


def _set_far_boundary(space):
    for r in np.arange(0, space.rmax, 0.1):
        space.set_value(r, space.zmax, FAR_POTENTIAL, is_changeable=False)

    for z in np.arange(0, space.zmax, 0.1):
        space.set_value(space.rmax, z, FAR_POTENTIAL, is_changeable=False)
