#! /usr/bin/python
# -*- coding: utf-8 -*-
"""


author Atsushi Sakai
"""

import math
#import motorsito as mp


dt = 0.01 # [s]
L = 0.3  # [m]


class State:

    def __init__(self, x=0.0, y=0.0, yaw=0.0, v=0.0):
        self.x = x
        self.y = y
        self.yaw = yaw
        self.v = v


def update(state, a, delta):

    state.x = state.x + state.v * math.cos(state.yaw) * dt
    state.y = state.y + state.v * math.sin(state.yaw) * dt
    state.yaw = state.yaw + state.v / L * math.tan(delta) * dt
    state.v = state.v + a * dt

    return state


if __name__ == '__main__':
    print("start unicycle simulation")

    T = 100
    a = [1.0] * T
    delta = [math.radians(1.0)] * T
    #  print(delta)
    #  print(a, delta)

    state = State()

    x = []
    y = []
    yaw = []
    v = []

    for (ai, di) in zip(a, delta):
        state = update(state, ai, di)

        x.append(state.x)
        y.append(state.y)
        yaw.append(state.yaw)
        v.append(state.v)
	print(state.v)

#    plt.show()
