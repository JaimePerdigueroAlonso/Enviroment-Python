#We create this class to format the output through the console
class format:
    
    def format_time(hours):
        """
        Format time in hours into days, hours, and minutes.

        Args:
            hours (int): Time in hours.

        Returns:
            str: Formatted time string.
        """
        days, remaining_hours = divmod(hours, 24)
        remaining_hours, remaining_minutes = divmod(remaining_hours * 60, 60)
        return f"Day {int(days)} at {int(remaining_hours)} and {int(remaining_minutes)} minutes"
    

    def format_money(money):
        """
        Format money into a readable format.

        Args:
            money (float): Money amount.

        Returns:
            str: Formatted money string.
        """
        # Format the money rounded to the second decimal place
        formatted_number = str(round(money, 2)).replace('.', ',') 
        parts = formatted_number.split(",")
        int_part = parts[0]
        decimal_part = parts[1]
        
        # Separate the parts, add points every 3 digits, and replace the comma
        formatted_integer_part = "{:,.0f}".format(float(int_part)).replace(",", ".")
        
        # Concatenate the parts to form the final formatted number
        final_number = formatted_integer_part + "," + decimal_part
     
        # Return the number in money format
        return final_number
    
 
    def format_time_statistics(hours):
        """
        Format time in hours into days, hours, and minutes for statistics.

        Args:
            hours (int): Time in hours.

        Returns:
            str: Formatted time string for statistics.
        """
        days, remaining_hours = divmod(hours, 24)
        remaining_hours, remaining_minutes = divmod(remaining_hours * 60, 60)
        return f"{int(days)} Days {int(remaining_hours)} hours and {int(remaining_minutes)} minutes"


