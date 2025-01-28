import simpy
from Terminal_Exit.formats import format

class Port:
    def __init__(self, env: simpy.Environment):
        """Initialize a Port object.

        Args:
            env (simpy.Environment): SimPy simulation environment.
        """
        
        self.env = env
        # Number of docks in the port
        self.TGport = simpy.Resource(env, capacity=2) 
        self.CGRRport = simpy.Resource(env, capacity=1)
        self.CTPport = simpy.Resource(env, capacity=3)
        self.PCport = simpy.Resource(env, capacity=2)


    # Mooring/dock usage time
    def DockOccupation(self, boat: object): 
        """Simulate dock occupation by a boat.

        Args:
            boat (object): Boat object.

        Yields:
            Generator: SimPy event.
        """

        if boat.type in ["Tankers              ", "Bulk Carriers        "]:
            yield from self.dock_interface(boat, self.TGport) 
               
        elif boat.type in ["General Cargo Vessels", "RoRo Vessels         "]:
            yield from self.dock_interface(boat, self.CGRRport) 
        
        elif boat.type in ["Cruise Ships         ", "Passenger Ships      "]:
            yield from self.dock_interface(boat, self.CTPport) 
        
        elif boat.type in ["Container ships      "]:
            yield from self.dock_interface(boat, self.PCport) 
            
        
    def dock_interface(self, boat, port):
        """Interface for handling boat docking and undocking at a specific port.

        Args:
            boat (object): Boat object.
            port (simpy.Resource): SimPy resource representing the port.

        Yields:
            Generator: SimPy event.
        """

        request = port.request()
        yield request
        print("Boat", boat.name, "Type:", boat.type, "--> Start unloading time:", format.format_time(self.env.now))
        boat.start_unloading_time = self.env.now
        yield self.env.timeout(boat.unload_time)
        print("Boat", boat.name, "Type:", boat.type, "--> Finished unloading time:", format.format_time(self.env.now))
        boat.end_unloading_time = self.env.now

        print("Boat", boat.name, "Type:", boat.type, "--> Start loading time:", format.format_time(self.env.now))
        boat.start_loading_time = self.env.now

        yield self.env.timeout(boat.load_time)
        print("Boat", boat.name, "Type:", boat.type, "--> Finished loading time:", format.format_time(self.env.now).ljust(29), Port.leavingPort(boat))
        boat.end_loading_time = self.env.now
        port.release(request)   

    
    # Function that tells us which port has been assigned
    def portDestination(boat: object):
        """Get the destination port for a boat.

        Args:
            boat (object): Boat object.

        Returns:
            str: Destination port.
        """

        if boat.type in ["Tankers              ", "Bulk Carriers        "]:
            return f" --> Assigned to TGport"
        
        elif boat.type in ["General Cargo Vessels", "RoRo Vessels         "]:
            return f" --> Assigned to CGRRport"
        
        elif boat.type in ["Cruise Ships         ", "Passenger Ships      "]:
            return f" --> Assigned to CTPport"
        
        elif boat.type in ["Container ships      "]:
            return f" --> Assigned to PCport"
    

    # Function that tells us which port is being abandoned
    def leavingPort(boat: object):
        """Get the port being abandoned by a boat.

        Args:
            boat (object): Boat object.

        Returns:
            str: Departing port.
        """

        if boat.type in ["Tankers              ", "Bulk Carriers        "]:
            return f" --> Leaving TGport"
        
        elif boat.type in ["General Cargo Vessels", "RoRo Vessels         "]:
            return f" --> Leaving CGRRport"
        
        elif boat.type in ["Cruise Ships         ", "Passenger Ships      "]:
            return f" --> Leaving CTPport"
        
        elif boat.type in ["Container ships      "]:
            return f" --> Leaving PCport"
