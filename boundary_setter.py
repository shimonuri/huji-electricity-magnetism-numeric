import numpy as np
from dataclasses import dataclass
import space


@dataclass
class Ball:
    r: int
    z: int
    potential: int
    radius: int


BALL = Ball(r=0, z=4, radius=2, potential=10)

FAR_POTENTIAL = 5


def set_boundary(current_space: space.Space):
    _set_ball_boundary(current_space)
    _set_far_boundary(current_space)


def _set_ball_boundary(current_space):
    for r in np.arange(BALL.r, BALL.r + BALL.radius + 0.1, 0.1):
        current_radius = BALL.radius * np.sqrt(1 - r / BALL.radius)
        for z in np.arange(BALL.z - current_radius, BALL.z + current_radius + 0.1, 0.1):
            current_space.set_point(
                r=np.round(r, decimals=1),
                z=np.round(z, decimals=1),
                val=BALL.potential,
                is_changeable=False,
            )


def _set_far_boundary(current_space):
    for r in np.arange(0, current_space.rmax + 0.1, 0.1):
        current_space.set_point(
            r, current_space.zmax, BALL.potential, is_changeable=False
        )

    for z in np.arange(0, current_space.zmax + 0.1, 0.1):
        current_space.set_point(
            current_space.rmax, z, BALL.potential, is_changeable=False
        )
