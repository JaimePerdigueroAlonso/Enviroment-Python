import random
import simpy
import os


from Terminal_Exit.menu import Menu
from typing import Generator
from Principal.ports import Port
from Statistics.statistics_1 import StatisticsCollector

from Principal.boats import Boat


def boatGenerator(env: simpy.Environment, port: Port, statistics: StatisticsCollector,
                  MINIMAL_ARRIVAL_TIME: int, MAXIMUM_ARRIVAL_TIME: int) -> Generator:
    """Generator function for simulating boat arrivals at the port.

    Args:
        env (simpy.Environment): SimPy simulation environment.
        port (Port): Port object.
        statistics (StatisticsCollector): Object to collect statistics.
        MINIMAL_ARRIVAL_TIME (int): Minimum time between boat arrivals.
        MAXIMUM_ARRIVAL_TIME (int): Maximum time between boat arrivals.

    Yields:
        Generator: SimPy event.
    """

    boat_type = ['Tankers', 'Bulk Carriers', 'General Cargo Vessels', 'RoRo Vessels', 'Cruise Ships',
                 'Passenger Ships', 'Container ships']
    max_len_type = max(len(x) for x in boat_type)
    probabilities = [0.05, 0.05, 0.025, 0.025, 0.35, 0.35, 0.1]
    
    for i in range(NUM_BOATS):
        # Generate the extra crew for the ship randomly (between 0 and 20)
        crew = random.randint(0, 20) 
        # Generate ONE type of ship randomly
        chosen_type = random.choices(boat_type, weights=probabilities)
        type = chosen_type[0].ljust(max_len_type) 
        # Create the ship object
        boat = Boat(env, f'{i + 1}', crew, type, port, statistics) 
        env.process(boat.waitinQueue())
        yield env.timeout(random.randint(MINIMAL_ARRIVAL_TIME, MAXIMUM_ARRIVAL_TIME))


if __name__ == '__main__':
    # Clear the terminal when running the program
    os.system('clear') 
    
    print('---------------------------------------')
    print('Welcome to the simulation of port ')
    print('---------------------------------------')
    print('The simulation time is measured in hours')
    print('The number of hours in a year is 8760')
    print('I will need you to input two parameters\n')
    
    # Input simulation parameters
    SIMULATION_TIME = int(input('Enter the number of hours you want the simulation to last:\n'))
    NUM_BOATS = int(input('Enter the number of ships you want to attempt unloading during that time:\n'))

    
    # Simulation parameters
    MINIMAL_ARRIVAL_TIME = 5
    MAXIMUM_ARRIVAL_TIME = 40
    
    # Setup simulation environment
    env = simpy.Environment() 
    port = Port(env)
    statistics = StatisticsCollector()

    # Run simulation
    env.process(boatGenerator(env, port, statistics, MINIMAL_ARRIVAL_TIME, MAXIMUM_ARRIVAL_TIME))
    env.run(until=SIMULATION_TIME)

    # Save statistics to pandas DataFrame
    archivoCSV = statistics.to_dataframe()
    archivoCSV.to_csv('./Analisis/csv/simulation.csv', index=False)
    
    # Show menu
    Menu.mostrar_menu()
