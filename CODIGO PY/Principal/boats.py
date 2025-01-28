import simpy
import random
from Principal.ports import Port
from typing import Generator
from Unforeseen.unforeseen import Unforeseen
from Statistics.statistics_1 import StatisticsCollector
from Terminal_Exit.formats import format
from Unforeseen.weather import Weather
 
class Boat:
    def __init__(self, env: simpy.Environment, name: int, crew: int, type: str, port: Port,
                 statistics: StatisticsCollector):
        """Initialize a Boat object.

        Args:
            env (simpy.Environment): SimPy simulation environment.
            name (int): Boat number.
            crew (int): Amount of extra crew on the boat.
            type (str): Type of boat.
            port (Port): Port object where the boat docks.
            statistics (StatisticsCollector): Object to collect statistics.
        """
        # Simulation environment
        self.env = env 
        # Boat number
        self.name = name 
        # Amount of extra crew on the boat 
        self.crew = crew 
        # Type of boat
        self.type = type  
        self.port = port
        self.statistics = statistics
        self.start_unloading_time = None
        self.end_unloading_time = None
        self.start_loading_time = None
        self.end_loading_time = None
        
        # Instantiate Unforeseen object to handle unforeseen events
        unforessen = Unforeseen()
        # Get total added time and error type due to unforeseen events
        self.added_time, self.error_type = unforessen.total_added_time()
        
        # Generate random times for different types of boats
        self.random_Tankers = random.uniform(12, 48)
        self.random_Bulk_Carriers = random.uniform(12, 72)
        self.random_General_Cargo = random.uniform(4, 48)
        self.random_RoRo_Vessels = random.uniform(6, 24)
        self.random_Cruise_Ships = random.uniform(4, 36)
        self.random_Passenger_Ships = random.uniform(1, 3)
        self.random_Container_Ships = random.uniform(6, 72)
        # Get weather delay
        self.weather_delay = Weather.weather_delay()
        # Calculate crew time
        self.crew_time = self.crew * 0.01 
        
        # Calculate unload and load time based on boat type
        if self.type == "Tankers              ":
            self.unload_time = self.random_Tankers + self.weather_delay - self.crew_time + self.added_time
            self.load_time = self.random_Tankers + self.weather_delay - self.crew_time 
            self.port_name = "TGport"
            
        elif self.type == "Bulk Carriers        ":
            self.unload_time = self.random_Bulk_Carriers + self.weather_delay - self.crew_time + self.added_time
            self.load_time = self.random_Bulk_Carriers + self.weather_delay - self.crew_time 
            self.port_name = "TGport"

        elif self.type == "General Cargo Vessels":
            self.unload_time = self.random_General_Cargo + self.weather_delay - self.crew_time + self.added_time
            self.load_time = self.random_General_Cargo + self.weather_delay - self.crew_time 
            self.port_name = "CGRRport"

        elif self.type == "RoRo Vessels         ":
            self.unload_time = self.random_RoRo_Vessels + self.weather_delay - self.crew_time + self.added_time 
            self.load_time = self.random_RoRo_Vessels + self.weather_delay - self.crew_time 
            self.port_name = "CGRRport"

        elif self.type == "Cruise Ships         ":
            self.unload_time = self.random_Cruise_Ships + self.weather_delay - self.crew_time + self.added_time 
            self.load_time = self.random_Cruise_Ships + self.weather_delay - self.crew_time 
            self.port_name = "CTPport"

        elif self.type == "Passenger Ships      ":
            self.unload_time = self.random_Passenger_Ships + self.weather_delay - self.crew_time + self.added_time 
            self.load_time = self.random_Passenger_Ships + self.weather_delay - self.crew_time
            self.port_name = "CTPport"

        elif self.type == "Container ships      ":
            self.unload_time = self.random_Container_Ships + self.weather_delay - self.crew_time + self.added_time 
            self.load_time = self.random_Container_Ships + self.weather_delay - self.crew_time 
            self.port_name = "PCport"



    def waitinQueue(self) -> Generator:
        """Simulate boat waiting in queue to dock at the port."""
        arrival_time = self.env.now
        
        print ("Boat", self.name, "Type:", self.type, "--> Arrival time:", format.format_time(arrival_time).ljust(30) + Port.portDestination(self))
        
        if(self.error_type != ""):
            print("      --> Delay caused by", self.error_type, self.added_time, "hours")
        
        price_x_hour = random.randint(500, 2000)
        price =  (self.unload_time + self.load_time) * price_x_hour
        yield from self.port.DockOccupation(self)

        # Add data to statistics and create the csv  
        self.statistics.add_data(self.name, self.type, self.crew, arrival_time, self.start_unloading_time, self.end_unloading_time,
                                  self.start_loading_time,self.end_loading_time, price, self.error_type, self.added_time, self.port_name)
 