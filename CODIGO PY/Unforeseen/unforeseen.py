import random
 
class Unforeseen():
    def __init__(self) -> None:
        """Initialize an Unforeseen object.

        This object is used to simulate unforeseen events that may occur, such as breakdowns, customs checks, or strikes.
        """
        self.error_type = ""
        pass
    
    # Breakdowns
    @staticmethod
    def breakdowns(): 
        """Simulate a possible breakdown.

        Returns:
            Tuple[int, str]: A tuple containing the added time due to the breakdown and the type of breakdown.
        """
        probability = random.randint(1,100)
        added_time = 0
        error_type = ""

        if(probability == 50):
            added_time = random.randint(6,48)
            error_type = "Motor Breakdown "

        return added_time, error_type

    # Custom Control (Customs)
    @staticmethod
    def aduanes(): 
        """Simulate a customs control.

        Returns:
            Tuple[int, str]: A tuple containing the added time due to the customs control and the type of control.
        """
        probability = random.randint(1,70)
        added_time = 0
        error_type = ""
        
        if(probability == 50):
            added_time = random.randint(12,24)
            error_type = "Customs "

        return added_time, error_type
        
    # Strikes
    @staticmethod
    def strike(): 
        """Simulate a strike.

        Returns:
            Tuple[int, str]: A tuple containing the added time due to the strike and the type of strike.
        """
        probability = random.randint(1,200)
        added_time = 0
        error_type = ""

        if(probability == 50):
            added_time = random.randint(24,72)
            error_type = "Strike "

        return added_time, error_type


    def total_added_time(self): 
        """Calculate the total added time due to unforeseen events.

        Returns:
            Tuple[int, str]: A tuple containing the total added time and the type of unforeseen event that caused the delay.
        """
        added_time1, error_type1 = self.breakdowns()
        added_time2, error_type2 = self.aduanes()
        added_time3, error_type3 = self.strike()

        if error_type1 != "":
            self.error_type = error_type1
        elif error_type2 != "":
            self.error_type = error_type2
        elif error_type3 != "":
            self.error_type = error_type3

        return (added_time1 + added_time2 + added_time3), self.error_type 

    
