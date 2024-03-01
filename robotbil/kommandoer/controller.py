from Hardware import motorstyrring as motor

def controller(x,y,speed):
    if x != 1: 
        y = int(y)
        if x == 5:
            print("state1 - forward / backward")
            if y <= 10:
                motor.stop()
                print("stop")
            else:
                speed = y

        elif x == 4:
            print("state1 backward")
            if y <= 5:
                speed = 0
                motor.stop()
                print("stop")
            else:
                speed = y
    
    elif x == 1:
        print("state2 - d-pad")
        x,y = map(int,y.split('_'))
        if x == -1:
            if y == 0:
                motor.VariableSpeed(speed*-1,speed) 
            else:
                motor.VariableSpeed(0, speed*y)
        elif x == 1:
            if y == 0:
                motor.VariableSpeed(speed,-1*speed) 
            else:
                motor.VariableSpeed(speed*y, 0)
        else:
            if y == 0:
                motor.stop() 
            else:
                motor.VariableSpeed(speed*y, speed*y)
    
    return speed