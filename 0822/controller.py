#!/usr/bin/env python
""" Controller for Fake Motor

@author  Kyohei Otsu <kyon@ac.jaxa.jp>
@date    2016-08-19

Usage:
    $ python controller.py
"""

import fake_motor
import time


def main():
    ### Display setting ###
    display_profiles  = True
    display_animation = True


    ### Initialize ###
    print '[1] Start initialization'
    motor = fake_motor.FakeMotor()
    motor.daemon = True


    ### Motor simulation ###
    '''
        Useful Functions:
            motor.get_angle()  ... returns current angle [deg]
            motor.set_pwm_duty()  ... set pwm duty (-100...100) [%]
    '''

    print '[2] Starting motor simulation'
    motor.start()

    # Simulation params
    angref = 45  # target angle
    dt = 0.1     # sampling time

    while True:
        # get current angle
        ang = motor.get_angle()  
        
        ######################################################
        # TODO: write your controller here!

        # On/Off Control (example) 
        if abs(ang - angref) < 2.5:
            motor.set_pwm_duty(0)
        elif ang > angref:
            motor.set_pwm_duty(-25)
        else:
            motor.set_pwm_duty(25)
        
        ######################################################

        # wait for dt[sec] (do not edit this)
        time.sleep(dt)

        # break the loop if simulation finishes (do not edit this)
        if not motor.isAlive(): break

    # wait until simulation stops (do not edit this)
    motor.join()  


    ### Show results ###
    if display_profiles:
        print '[3] Displaying results'
        motor.show_profiles()
    
    if display_animation:
        print '[4] Showing animation'
        motor.show_animation()


    print 'Press enter to exit ...', raw_input()



if __name__ == '__main__':
    main()

