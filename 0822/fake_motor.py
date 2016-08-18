#!/usr/bin/env python
""" Fake motor class
See main() for example use.

@author  Kyohei Otsu <kyon@ac.jaxa.jp>
@date    2016-08-18

Usage of sample code:
    $ python fake_motor.py
"""

import time
import threading
import numpy as np
import matplotlib.pyplot as plt


class FakeMotor(threading.Thread):
    ''' 
        Fake motor class
    '''

    def __init__(self):
        '''
            Initialize the class
        '''
        threading.Thread.__init__(self)

        ### Timing params ###
        self.system_freq = 100  # [Hz]
        self.max_time = 5  # [sec]
        self.max_tics = self.max_time * self.system_freq  # [cnt]

        ### Motor state ###
        self.time_list = 1.0 * np.arange(self.max_tics) / self.system_freq
        self.angle_list = np.nan * np.ones(self.max_tics)  # [deg]
        self.velocity_list = np.nan * np.ones(self.max_tics)  # [deg / sec]
        self.angle_list[0] = 0
        self.velocity_list[0] = 0
        self.p = 0  # pointer to current data

        ### PWM setting ###
        self.duty = 0  # -100...100 [%]


    def run(self):
        '''
            Start main loop
        '''
        k = 3
        for i in range(1, self.max_tics):
            ### update ###
            self.p = i
            self.velocity_list[i] = k * self.duty  # fake motor
            self.angle_list[i] = self.angle_list[i - 1] + 1. * self.velocity_list[i] / self.system_freq
            
            ### adjust frequency ###
            wait_time = 1. / self.system_freq
            time.sleep(0.8 * wait_time)
            

    def set_pwm_duty(self, duty=0):
        '''
            Set PWM Duty (-100 ... 100[%])
        '''
        self.duty = duty
        self.duty = min(max(self.duty, -100), 100)  # bound range to -100..100
        print 't={:.2f}:  Set PWM duty = {:.1f}'.format(self.get_time(), self.duty)


    def get_time(self):
        return self.time_list[self.p]


    def get_angle(self):
        return self.angle_list[self.p]


    def get_velocity(self):
        return self.velocity_list[self.p]


    def show_profiles(self):
        '''
            Plot time series data for angle and velocity
        '''
        ti  = self.time_list
        ang = self.angle_list
        vel = self.velocity_list

        ### Plot angle ###
        plt.subplot(2, 1, 1)
        plt.xlim(0, ti[-1])
        #plt.ylim()
        #plt.xlabel('Time [s]')
        plt.ylabel('Angle [deg]')
        plt.plot(ti, ang)

        ### Plot angle velocity ###
        plt.subplot(2, 1, 2)
        plt.xlim(0, ti[-1])
        #plt.ylim()
        plt.xlabel('Time [s]')
        plt.ylabel('Angle Velocity [deg/s]')
        plt.plot(ti, vel)

        plt.ion()
        plt.show()


    def show_animation(self):
        '''
            Show animation for motor behavior
        '''
        ti  = self.time_list
        ang = self.angle_list
        vel = self.velocity_list

        plt.figure()
        plt.ion()
        plt.show()

        an = np.linspace(0, 2 * np.pi, 100)
        skips = 5
        for i in range(len(ti)):
            if not i % skips:
                plt.clf()
                plt.title('Time = {:.2f} [s]'.format(ti[i]))
                plt.plot(np.cos(an), np.sin(an), 'k-')  # plot circle
                plt.axis('equal')
                plt.plot([0, np.cos(ang[i] / 180. * np.pi)], [0, np.sin(ang[i] / 180. * np.pi)], 'b-')
                plt.pause(0.01)
            


def main():
    ### Display setting ###
    display_profiles  = True
    display_animation = True


    ### Initialize ###
    print '[1] Start initialization'
    motor = FakeMotor()
    motor.daemon = True


    ### Motor simulation ###
    print '[2] Starting motor simulation'
    motor.start()

    time.sleep(1)            # wait 1 sec
    motor.set_pwm_duty(10)   # set pwm duty to 10%
    time.sleep(1)            # wait 1 sec
    motor.set_pwm_duty(50)   # set pwm duty to 50%
    time.sleep(1)            # wait 1 sec
    motor.set_pwm_duty(-50)  # set pwm duty to -50%

    # wait until simulation stops
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

