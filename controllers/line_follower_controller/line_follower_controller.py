from controller import Robot

def run_robot(robot):

    
    # get the time step of the current world.
    timestep = 32
    max_speed = 6.28 # angular_velocity
    
    # create motor instances.
    left_motor = robot.getDevice('left wheel motor')
    right_motor = robot.getDevice('right wheel motor')
    
    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))
    
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)
    
    # create and enable IR sensor instances
    right_ir = robot.getDevice('ir0')
    right_ir.enable(timestep)
    
    left_ir = robot.getDevice('ir1')
    left_ir.enable(timestep)
    
    
    # Main loop, Step simulation
    while robot.step(timestep) != -1:
        
        # read ir sensors
        left_ir_value = left_ir.getValue()
        right_ir_value = right_ir.getValue()
        
        print("left: {} right: {}".format(left_ir_value, right_ir_value))
        
        left_speed = max_speed * 0.25
        right_speed = max_speed * 0.25
        
        if (left_ir_value > right_ir_value) and (6 < left_ir_value < 15):
            print("Go left")
            left_speed = -max_speed * 0.25
        elif (right_ir_value > left_ir_value) and (6 < right_ir_value < 15):
            print("Go right")
            right_speed = -max_speed * 0.25
                

        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)

if __name__ == "__main__":
    
    
    # create the Robot instance.
    robot = Robot()
    run_robot(robot)
    