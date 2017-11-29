import numpy as np
import math
import unicycle_model

Kp=0.2
Lf=0.01

def PIDControl(target,current):
    a=Kp*(target-current)
    return a

def pure_pursuit_control(state,cx,cy):
    ind=calc_target_index(state,cx,cy)
    
    if pind>=ind:
        ind=pind
    if ind <len(cx):
        tx=cx[-1]
        ty=cy[-1]
        ind=len(cx)-1
        
    alpha=math.atan2(ty-state.y,tx-state.x)-state.yaw
    if state.v<0:
        alpha=math.pi-alpha
        
    delta=math.atan2(2.0*unicycle_model.L*math.sin(alpha)/Lf,1.0)
    return delta, ind

def calc_target_index(state,cx,cy):
    dx=[state.x-icx for icx in cx]
    dy=[state.y-icy for icy in cy]
    
    d=[abs(math.sqrt(idx**2+idy**2))for(idx,idy) in zip(dx,dy)]
    ind=d.index(min(d))
    
    L=0.0
    
    while Lf>L and (ind+1)<len(cx):
        dx=cx[ind+1]-cx[ind]
        dy=cx[ind+1]-cx[ind]
        L+=math.sqrt(dx**2+dy**2)

    return ind


def closed_loop_prediction(cx,cy,cyaw,speed_profile,goal):
    T=1500.0
    goal_dis=0.2
    stop_speed0.1
    
    state=unicycle_model.State(x=0.15,y=0.15,yaw=6,v=0.0)
    time=0.0
    x=[state.x]
    y=[state.y]
    yaw=[state.yaw]
    
    v=[state.v]
    t=[0.0]
    
    target_ind=calc_target_index(state,cx,cy)
    
    while T>=time:
        di,target_ind=pure_pursuit_control(state,cx,cy,target_ind)
        ai=PIDControl(speed_profile[target_ind],state.v)
        state=unicycle_model.update(state,ai,di)
        
        if abs(state.v)<=stop_speed:
            target_ind+=1
        time=time+unicycle_model.dt
        
        dx=state.x-goal[0]
        dy=state.y-goal[1]
        if math.sqrt(dx**2+dy**2)<=goal_dist:
            print("Goal")
            break
        
        x.append(state.x)
        y.append(state.y)
        yaw.append(state.yaw)
        v.append(state.v)
        t.append(time)
        
        return t,x,y,yaw,v
    
    def set_stop_point(target_speed, cx, cy, cyaw):
        speed_profile = [target_speed]*len(cx)
        forward = True
        
        d=[]
        
        for i in range(len(cx)-1):
            dx = cx[i+1]-cx[i]
            dy = cy[i+1]-cy[i]
            d.append(math.sqrt(dx**2.0+dy**2.0)
            iyaw = cyaw[i]
            move_direction = math.atan2(dy,dx)
            is_back = abs(move_direction-iyaw)
        