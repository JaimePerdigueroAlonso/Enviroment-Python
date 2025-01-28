import pandas as pd

class StatisticsCollector:
    def __init__(self):
        self.data = []
        self.money = []

    # Function to add data about each boat to the collector
    def add_data(self, name:int, type:str, crew:int , arrival_time:int, 
                 start_unloading_time :int, end_unloading_time:int,
                 start_loading_time :int, end_loading_time:int, price : float, error : str, error_delay : int, port : str) -> None:
        """
        Add data about a boat to the collector.

        Args:
            name (int): Boat number
            type (str): Type of boat
            crew (int): Extra crew on the boat
            arrival_time (int): Time when the boat arrives
            start_unloading_time (int): Time when unloading starts
            end_unloading_time (int): Time when unloading ends
            start_loading_time (int): Time when loading starts
            end_loading_time (int): Time when loading ends
            price (float): Total price incurred
            error (str): Type of error (if any)
            error_delay (int): Delay caused by error
            port (str): Name of the port
        """
        dict_data = {
            'Boat': name, 
            'Type': type,
            'Extra Crew' : crew,
            'Arrival Time' : arrival_time,
            'Start Unloading Time' : start_unloading_time,
            'End Unloading Time' : end_unloading_time,
            'Start Loading Time' : start_loading_time,
            'End Loading Time' : end_loading_time,
            'Total Price' : price,
            'Error' : error,
            'Error Delay' : error_delay,
            'Port' : port
        }
        
        self.data.append(dict_data)

    # Function to convert collected data to a pandas DataFrame
    def to_dataframe(self):
        """
        Convert collected data to a pandas DataFrame.

        Returns:
            pd.DataFrame: DataFrame containing collected data.
        """
        return pd.DataFrame(self.data)


