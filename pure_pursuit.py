import numpy as np
import math
import modelito
import move

Kp = 0.2  
Lf = 0.01 
animation = False



def PIDControl(target, current):
    a = Kp * (target - current)
    return a


def pure_pursuit_control(state, cx, cy, pind):

    ind = calc_target_index(state, cx, cy)

    if pind >= ind:
        ind = pind

    if ind < len(cx):
        tx = cx[ind]
        ty = cy[ind]
    else:
        tx = cx[-1]
        ty = cy[-1]
        ind = len(cx) - 1

    alpha = math.atan2(ty - state.y, tx - state.x) - state.yaw

    if state.v < 0:  # back
        alpha = math.pi - alpha
    delta = math.atan2(2.0 * modelito.L * math.sin(alpha) / Lf, 1.0)

    return delta, ind


def calc_target_index(state, cx, cy):
    dx = [state.x - icx for icx in cx]
    dy = [state.y - icy for icy in cy]

    d = [abs(math.sqrt(idx ** 2 + idy ** 2)) for (idx, idy) in zip(dx, dy)]

    ind = d.index(min(d))

    L = 0.0

    while Lf > L and (ind + 1) < len(cx):
        dx = cx[ind + 1] - cx[ind]
        dy = cx[ind + 1] - cx[ind]
        L += math.sqrt(dx ** 2 + dy ** 2)
        ind += 1

    return ind


def closed_loop_prediction(cx, cy, cyaw, speed_profile, goal):	

    T = 15000.0  # max simulation 
    goal_dis = 0.2
    stop_speed = 0.1

    state = modelito.State(x=0.15, y=0.15, yaw=6, v=0.0)

    time = 0.0
    x = [state.x]
    y = [state.y]
    yaw = [state.yaw]
    v = [state.v]
    t = [0.0]
    target_ind = calc_target_index(state, cx, cy)

    while T >= time:
        di, target_ind = pure_pursuit_control(state, cx, cy, target_ind)
        ai = PIDControl(speed_profile[target_ind], state.v)
        state = modelito.update(state, ai, di)

        if abs(state.v) <= stop_speed:
            target_ind += 1

        time = time + modelito.dt

        dx = state.x - goal[0]
        dy = state.y - goal[1]
        if math.sqrt(dx ** 2 + dy ** 2) <= goal_dis:
            print("Logrado")
            break

        x.append(state.x)
        y.append(state.y)
        yaw.append(state.yaw)
        v.append(state.v)

	move.forward(100*abs(state.v),100*abs(state.v*np.cos(state.yaw)))
        t.append(time)

    return t, x, y, yaw, v


def set_stop_point(target_speed, cx, cy, cyaw):
    speed_profile = [target_speed] * len(cx)
    forward = True

    d = []

    # Set stop point
    for i in range(len(cx) - 1):
        dx = cx[i + 1] - cx[i]
        dy = cy[i + 1] - cy[i]
        d.append(math.sqrt(dx ** 2.0 + dy ** 2.0))
        iyaw = cyaw[i]
        move_direction = math.atan2(dy, dx)
        is_back = abs(move_direction - iyaw) >= math.pi / 2.0

        if dx == 0.0 and dy == 0.0:
            continue

        if is_back:
            speed_profile[i] = - target_speed
        else:
            speed_profile[i] = target_speed

        if is_back and forward:
            speed_profile[i] = 0.0
            forward = False
        elif not is_back and not forward:
            speed_profile[i] = 0.0
            forward = True
    speed_profile[0] = 0.0
    speed_profile[-1] = 0.0

    d.append(d[-1])

    return speed_profile, d


def calc_speed_profile(cx, cy, cyaw, target_speed, a):

    speed_profile, d = set_stop_point(target_speed, cx, cy, cyaw)

    nsp = len(speed_profile)

    for i in range(nsp - 1):

        if speed_profile[i + 1] >= 0:  # forward
            tspeed = speed_profile[i] + a * d[i]
            if tspeed <= speed_profile[i + 1]:
                speed_profile[i + 1] = tspeed
        else:
            tspeed = speed_profile[i] - a * d[i]
            if tspeed >= speed_profile[i + 1]:
                speed_profile[i + 1] = tspeed

    for i in range(nsp - 1):
        if speed_profile[- i - 1] >= 0:  # forward
            tspeed = speed_profile[-i] + a * d[-i]
            if tspeed <= speed_profile[-i - 1]:
                speed_profile[-i - 1] = tspeed
        else:
            tspeed = speed_profile[-i] - a * d[-i]
            if tspeed >= speed_profile[-i - 1]:
                speed_profile[-i - 1] = tspeed


    return speed_profile


def extend_path(cx, cy, cyaw):

    dl = 0.1
    dl_list = [dl] * (int(Lf / dl) + 0)

    move_direction = math.atan2(cy[-1] - cy[-2], cx[-1] - cx[-2])
    is_back = abs(move_direction - cyaw[-1]) >= math.pi / 2.0

    for idl in dl_list:
        if is_back:
            idl *= -1
        cx = np.append(cx, cx[-1] + idl * math.cos(cyaw[-1]))
        cy = np.append(cy, cy[-1] + idl * math.sin(cyaw[-1]))
        cyaw = np.append(cyaw, cyaw[-1])

    return cx, cy, cyaw


def main():
    #  target course
    import numpy as np
    cx = np.arange(0, 50, 0.1)
    cy = [math.sin(ix / 5.0) * ix / 2.0 for ix in cx]

    target_speed = 10.0 / 3.6

    T = 15.0  # max simulation time

    state = modelito.State(x=-0.0, y=-3.0, yaw=0.0, v=0.0)

    lastIndex = len(cx) - 1
    time = 0.0
    x = [state.x]
    y = [state.y]
    yaw = [state.yaw]
    v = [state.v]
    t = [0.0]
    target_ind = calc_target_index(state, cx, cy)
    print("Holi")

    while T >= time and lastIndex > target_ind:
        ai = PIDControl(target_speed, state.v)
        di, target_ind = pure_pursuit_control(state, cx, cy, target_ind)
        state = modelito.update(state, ai, di)

        time = time + modelito.dt

        x.append(state.x)
        y.append(state.y)
        yaw.append(state.yaw)
        v.append(state.v)

        t.append(time)

def main2():

    import pandas as pd
    data = pd.read_csv("rrt_course.csv")
    cx = np.array(data["x"])
    cy = np.array(data["y"])
    cyaw = np.array(data["yaw"])

    target_speed = 10.0 / 3.6
    a = 0.1

    goal = [cx[-1], cy[-1]]

    cx, cy, cyaw = extend_path(cx, cy, cyaw)

    speed_profile = calc_speed_profile(cx, cy, cyaw, target_speed, a)



    t, x, y, yaw, v = closed_loop_prediction(cx, cy, cyaw, speed_profile, goal)

    v=np.asarray(v)


if __name__ == '__main__':
    print("Seguimiento de trayectoria iniciado")
    main2()
