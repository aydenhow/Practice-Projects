# 1d_kinematics.py #
# Calculates various 1D kinematic parameters and saves any input for future calculations. #

from time import sleep

def welcome():
    print('Welcome to the 1D Kinematic Calculator!')
    sleep(1)
    print('By Ayden Howarth.\n')
    sleep(1)
    print('What would you like to calculate?')
    sleep(1)
    print('Parameters: V for Final Velocity, U for Initial Velocity, A for acceleration, S for Displacement, T for Time\n'
          'F for Force, W for Work, PE for Potential Energy, KE for Kinetic Energy, WT for Weight.')
    print('Enter P to print stored values or X to exit')
    sleep(1)
    print('Please use SI units!\n')
    sleep(1)

def start_calculator():
    welcome()
    start = True
    while start:
        user_choice = input('Enter parameter to calculate: ')
        user_choice.upper()
        if user_choice == 'F':
            if parameters['Mass'] is None:
                parameters['Mass'] = float(input('Enter mass (kg): '))
            if parameters['Acceleration'] is None:
                parameters['Acceleration'] = float(input('Enter acceleration (m/s/s): '))
            parameters['Force'] = parameters['Mass'] * parameters['Acceleration']
            print('Force: ' + str(round(parameters['Force'], 2)) + 'N\n')
        elif user_choice == 'W':
            if parameters['Force'] is None:
                parameters['Force'] = float(input('Enter Force (N): '))
            if parameters['Displacement'] is None:
                parameters['Displacement'] = float(input('Enter displacement (m): '))
            parameters['Work'] = parameters['Force'] * parameters['Displacement']
            print('Work: ' + str(round(parameters['Work'], 2)) + ' N*m\n')
        elif user_choice == 'KE':
            if parameters['Mass'] is None:
                parameters['Mass'] = float(input('Enter mass (kg): '))
            if parameters['Final Velocity'] is None:
                parameters['Final Velocity'] = float(input('Enter velocity (m/s): '))
            parameters['Kinetic Energy'] = 0.5 * parameters['Mass'] * parameters['Final Velocity']**2
            print('Kinetic Energy: ' + str(round(parameters['Kinetic Energy'], 2)) + ' J\n')
        elif user_choice == 'WT':
            if parameters['Mass'] is None:
                parameters['Mass'] = float(input('Enter mass (kg): '))
            parameters['Weight'] = parameters['Mass'] * parameters['Gravity']
            print('Weight: ' + str(round(parameters['Weight'], 2)) + ' kg\n')
        elif user_choice == 'PE':
            if parameters['Mass'] is None:
                parameters['Mass'] = float(input('Enter mass (kg): '))
            if parameters['Height'] is None:
                parameters['Height'] = float(input('Enter height (m): '))
            parameters['Potential Energy'] = parameters['Mass'] * parameters['Gravity'] * parameters['Height']
            print('Potential Energy: ' + str(round(parameters['Potential Energy'], 2)) + ' J\n')
        elif user_choice == 'V':
            if parameters['Final Velocity'] is not None:
                print('Final Velocity: ' + str(round(parameters['Final Velocity'], 2)) + ' m/s\n')
            else:
                print('Method 1: initial velocity, acceleration, time\n'
                      'Method 2: initial velocity, acceleration, displacement')
                method = input('Select method to calculate: ')
                if parameters['Initial Velocity'] is None:
                    parameters['Initial Velocity'] = float(input('Enter initial velocity (m/s): '))
                if parameters['Acceleration'] is None:
                    parameters['Acceleration'] = float(input('Enter acceleration (m/s/s): '))
                if method == '1':
                    if parameters['Time'] is None:
                        parameters['Time'] = float(input('Enter time (s): '))
                    parameters['Final Velocity'] = (parameters['Initial Velocity'] +
                                                    parameters['Acceleration'] * parameters['Time'])
                else:
                    if parameters['Displacement'] is None:
                        parameters['Displacement'] = float(input('Enter displacement (m): '))
                    parameters['Final Velocity'] = (parameters['Initial Velocity']**2 + 2 * parameters['Acceleration']
                                                    * parameters['Displacement']) ** 0.5
                print('Final Velocity: ' + str(round(parameters['Final Velocity'], 2)) + ' m/s\n')
        elif user_choice == 'U':
            if parameters['Initial Velocity'] is not None:
                print('Initial Velocity: ' + str(round(parameters['Initial Velocity'], 2)) + ' m/s\n')
            else:
                print('Method 1: final velocity, acceleration, time\n'
                      'Method 2: final velocity, acceleration, displacement')
                method = input('Select method to calculate: ')
                if parameters['Final Velocity'] is None:
                    parameters['Final Velocity'] = float(input('Enter final velocity (m/s): '))
                if parameters['Acceleration'] is None:
                    parameters['Acceleration'] = float(input('Enter acceleration (m/s/s): '))
                if method == '1':
                    if parameters['Time'] is None:
                        parameters['Time'] = float(input('Enter time (s): '))
                    parameters['Initial Velocity'] = (parameters['Final Velocity'] -
                                                          parameters['Acceleration'] * parameters['Time'])
                else:
                    if parameters['Displacement'] is None:
                        parameters['Displacement'] = float(input('Enter displacement (m): '))
                    parameters['Initial Velocity'] = abs((parameters['Final Velocity']**2 - 2 * parameters['Acceleration']
                                                    * parameters['Displacement']) ** 0.5)
                print('Initial Velocity: ' + str(round(parameters['Initial Velocity'], 2)) + ' m/s\n')
        elif user_choice == 'A':
            if parameters['Acceleration'] is not None:
                print('Acceleration: ' + str(round(parameters['Acceleration'], 2)) + ' m/s/s\n')
            else:
                print('Method 1: initial and final velocity, time\n'
                      'Method 2: initial and final velocity, displacement\n'
                      'Method 3: initial velocity, displacement, time')
                method = input('Select method to calculate: ')
                if parameters['Initial Velocity'] is None:
                    parameters['Initial Velocity'] = float(input('Enter initial velocity (m/s): '))
                if method == '1':
                    if parameters['Final Velocity'] is None:
                        parameters['Final Velocity'] = float(input('Enter final velocity (m/s): '))
                    if parameters['Time'] is None:
                        parameters['Time'] = float(input('Enter time (s): '))
                    parameters['Acceleration'] = (parameters['Final Velocity']-parameters['Initial Velocity'])/parameters['Time']
                elif method == '2':
                    if parameters['Final Velocity'] is None:
                        parameters['Final Velocity'] = float(input('Enter final velocity (m/s): '))
                    if parameters['Displacement'] is None:
                        parameters['Displacement'] = float(input('Enter displacement (m): '))
                    parameters['Acceleration'] = (parameters['Final Velocity']**2 - parameters['Initial Velocity']**2)/(2*parameters['Displacement'])
                else:
                    if parameters['Displacement'] is None:
                        parameters['Displacement'] = float(input('Enter displacement (m): '))
                    if parameters['Time'] is None:
                        parameters['Time'] = float(input('Enter time (s): '))
                    parameters['Acceleration'] = (2*parameters['Displacement']-parameters['Initial Velocity']*parameters['Time'])/parameters['Time']**2
                print('Acceleration: ' + str(round(parameters['Acceleration'], 2)) + ' m/s/s\n')
        elif user_choice == 'S':
            if parameters['Displacement'] is not None:
                print('Displacement: ' + str(round(parameters['Displacement'], 2)) + ' m\n')
            else:
                print('Method 1: initial and final velocity, acceleration\n'
                      'Method 2: initial velocity, acceleration, time')
                method = input('Select method to calculate: ')
                if parameters['Initial Velocity'] is None:
                    parameters['Initial Velocity'] = float(input('Enter initial velocity (m/s): '))
                if parameters['Acceleration'] is None:
                    parameters['Acceleration'] = float(input('Enter acceleration (m/s/s): '))
                if method == '1':
                    if parameters['Final Velocity'] is None:
                        parameters['Final Velocity'] = float(input('Enter final velocity (m/s): '))
                    parameters['Displacement'] = (parameters['Final Velocity']**2 - parameters['Initial Velocity']**2)/(2*parameters['Acceleration'])
                else:
                    if parameters['Time'] is None:
                        parameters['Time'] = float(input('Enter time (s): '))
                    parameters['Displacement'] = parameters['Initial Velocity']*parameters['Time'] + 0.5*parameters['Acceleration']*parameters['Time']**2
                print('Displacement: ' + str(round(parameters['Displacement'], 2)) + ' m\n')
        elif user_choice == 'T':
            if parameters['Time'] is not None:
                print('Time: ' + str(round(parameters['Time'], 2)) + ' s\n')
            else:
                if parameters['Initial Velocity'] is None:
                    parameters['Initial Velocity'] = float(input('Enter initial velocity (m/s): '))
                if parameters['Final Velocity'] is None:
                    parameters['Final Velocity'] = float(input('Enter final velocity (m/s): '))
                if parameters['Acceleration'] is None:
                    parameters['Acceleration'] = float(input('Enter acceleration (m/s/s): '))
                parameters['Time'] = (parameters['Final Velocity']-parameters['Initial Velocity'])/parameters['Acceleration']
                print('Time: ' + str(round(parameters['Time'], 2)) + ' s\n')
        elif user_choice == 'P':
            print(parameters)
            print('')
        elif user_choice == 'X':
            print('Exiting application...')
            start = False
            sleep(2)
        else:
            print('Invalid command entered!\n')


parameters = {'Initial Velocity': None, 'Final Velocity': None, 'Acceleration': None, 'Displacement': None,
              'Time': None, 'Mass': None, 'Gravity': 9.81, 'Work': None, 'Weight': None, 'Potential Energy': None,
              'Kinetic Energy': None, 'Force': None, 'Height': None}
start_calculator()
