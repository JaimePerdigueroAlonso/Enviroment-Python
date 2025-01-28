import csv
from Terminal_Exit.formats import format

class csv_analizer:
    
    # CSV parsers for TGport
    def TGport_MoneyAnalizer(fileCSV):
        """Analyze money data for Tankers and Bulk Carriers at TGport."""
        name1 = "Tankers"
        name2 = "Bulk Carriers"
        csv_analizer.money_analizer(fileCSV, name1, name2)

    def TGport_timeAnalizer(fileCSV):
        """Analyze time data for Tankers and Bulk Carriers at TGport."""
        name1 = "Tankers"
        name2 = "Bulk Carriers"
        csv_analizer.time_analizer(fileCSV, name1, name2)
    
    
    # CSV parsers for CGRR PORT
    def CGRRport_MoneyAnalizer(fileCSV):
        """Analyze money data for General Cargo Vessels and RoRo Vessels at CGRRport."""
        name1 = "General Cargo Vessels"
        name2 = "RoRo Vessels"
        csv_analizer.money_analizer(fileCSV, name1, name2)
          
    def CGRRport_timeAnalizer(fileCSV):
        """Analyze time data for General Cargo Vessels and RoRo Vessels at CGRRport."""
        name1 = "General Cargo Vessels"
        name2 = "RoRo Vessels"
        csv_analizer.time_analizer(fileCSV, name1, name2)
    

    # CSV parsers for CTP PORT
    def CTPport_MoneyAnalizer(fileCSV):
        """Analyze money data for Cruise Ships and Passenger Ships at CTPport."""
        name1 = "Cruise Ships"
        name2 = "Passenger Ships"
        csv_analizer.money_analizer(fileCSV, name1, name2)
           
    def CTPport_timeAnalizer(fileCSV):
        """Analyze time data for Cruise Ships and Passenger Ships at CTPport."""
        name1 = "Cruise Ships"
        name2 = "Passenger Ships"
        csv_analizer.time_analizer(fileCSV, name1, name2)
       
       
    # CSV parsers for PC PORT
    def PCport_MoneyAnalizer(fileCSV):
        """Analyze money data for Container ships at PCport."""
        name1 = "Container ships" 
        name2 = "Container ships" 
        csv_analizer.money_analizer(fileCSV, name1, name2)
      
    def PCport_timeAnalizer(fileCSV):
        """Analyze time data for Container ships at PCport."""
        name1 = "Container ships" 
        name2 = "Container ships" 
        csv_analizer.time_analizer(fileCSV, name1, name2)
    

    def TOTALMoneyAnalizer(fileCSV):
        """Analyze total money data for all ships."""
        # List to store boat prices
        price_list = []
        total_simulation_amount = 0

        # Open the CSV file in reading mode
        with open(fileCSV, mode='r') as file:
            # Create a CSV reader
            csv_analizer = csv.reader(file)
            
            # Skip the first row (headers)
            next(csv_analizer) 
            
            for row in csv_analizer:
                # Add the price to the price list
                price_list.append(float(row[8]))  
            
            for prices in price_list:
                # Sum up all the prices of the boats
                total_simulation_amount += prices 
            
            # Number of items (boats) in the list
            number_of_elements_on_list = len(price_list) 

            # Calculate average money per boat
            average_price = total_simulation_amount / number_of_elements_on_list 
            
            print('1. Total number of ships with load and unload completed:', number_of_elements_on_list,'\n') 
            print('2. Average money invoiced per boat:', format.format_money(average_price), '€\n')
            print('3. Total money invoiced:', format.format_money(total_simulation_amount), '€\n')
    
    
    def TOTALtimeAnalizer(fileCSV):
        """Analyze total time data for all ships."""
        end_times_list = []
        unload_time_list = []
        delay_time_list = []

        # Total time variables
        total_unload_time = 0 
        total_delay_time = 0
        
        with open(fileCSV, mode='r') as file:
            csv_analizer = csv.reader(file)
            next(csv_analizer)
            
            
            for row in csv_analizer: 
                # End unloading Time - Start Unloading Time
                unload_time = float(row[7]) - float(row[4]) 
                unload_time_list.append(unload_time)
                
                delay_time = float(row[10])
                delay_time_list.append(delay_time)

                end_time = float(row[7])
                end_times_list.append(end_time)
                
            # Calculate total unload time and total delay time
            total_unload_time = sum(unload_time_list)
            total_delay_time = sum(delay_time_list)
            
            # Number of items (boats) in the list
            number_of_elements_on_list = len(unload_time_list)
            # Calculate average unload time per ship
            average_unload_time = total_unload_time / number_of_elements_on_list
            max_time = end_times_list[-1] 
            # Calculate average delay time per ship
            average_delay_time = total_delay_time / number_of_elements_on_list
            
            print('4. The duration of the simulation has been:', format.format_time_statistics(max_time),'\n')
            print('5. The total time used by all ships in the simulation has been:', format.format_time_statistics(total_unload_time),'\n')
            print('6. The average unloading time per ship has been:', format.format_time_statistics(average_unload_time),'\n')
            print('7. The average delay time per ship has been:', format.format_time_statistics(average_delay_time),'\n')


    def time_analizer(fileCSV, name1, name2):
        """Analyze time data for specific ship types."""
        unload_time_list = []
        final_unload_time_list = []
        delay_time_list = []
        
        end_times_list = []
        final_end_times_list = []
        final_delay_time_list = []
        
        total_unload_time = 0 
        total_delay_time = 0
        name_list = []
        
        with open(fileCSV, mode='r') as file:
            csv_analizer = csv.reader(file)
            next(csv_analizer)
            
            
            for row in csv_analizer: 
                unload_time = float(row[5]) - float(row[4])
                unload_time_list.append(unload_time)
                
                end_time = float(row[5])
                end_times_list.append(end_time)

                delay_time = float(row[10])
                delay_time_list.append(delay_time)
                
                name_list.append(row[1].strip())
                
            # Iterate through name_list and check if any name matches "Tankers" or "Bulk Carriers"
            for i, name in enumerate(name_list):
                if name == name1 or name == name2:
                    final_unload_time_list.append(unload_time_list[i])
                    final_end_times_list.append(end_times_list[i])
                    final_delay_time_list.append(delay_time_list)

                        
            # Calculate total unload time and total delay time
            total_unload_time = sum(final_unload_time_list)
            total_delay_time = sum(delay_time_list)
            
            # Number of items (boats) in the list
            number_of_elements_on_list = len(final_unload_time_list)
            # Calculate average unload time per ship
            average_unload_time = total_unload_time / number_of_elements_on_list
            max_time = final_end_times_list[-1]
            # Calculate average delay time per ship
            average_delay_time = total_delay_time / number_of_elements_on_list
    
            print('4. The duration of the simulation has been:', format.format_time_statistics(max_time),'\n')
            print('5. The total time used by all ships in the simulation has been:', format.format_time_statistics(total_unload_time),'\n')
            print('6. The average unloading time per ship has been:', format.format_time_statistics(average_unload_time),'\n')
            print('7. The average delay time per ship has been:', format.format_time_statistics(average_delay_time),'\n')


       
    def money_analizer(fileCSV, name1, name2):
        """Analyze money data for specific ship types."""
        price_list = []
        name_list = []
        final_price_list = []
        total_simulation_amount = 0

        with open(fileCSV, mode='r') as file:
            csv_analizer = csv.reader(file)
            next(csv_analizer)
        
            for row in csv_analizer:
                price_list.append(float(row[6])) 
                name_list.append(row[1].strip())  

            # Iterate through name_list and check if any name matches "Tankers" or "Bulk Carriers"
            for i, name in enumerate(name_list):
                if name == name1 or name == name2:
                    final_price_list.append(price_list[i])
                
            # Calculate total simulation amount
            total_simulation_amount = sum(final_price_list)
     
            # Number of items (boats) in the list
            number_of_elements_on_list = len(final_price_list)
            # Calculate average money per boat
            average_price = total_simulation_amount / number_of_elements_on_list 

            print('1. Total number of ships with load and unload completed:', number_of_elements_on_list,'\n') 
            print('2. Average money invoiced per boat:', format.format_money(average_price), '€\n')
            print('3. Total money invoiced:', format.format_money(total_simulation_amount), '€\n')
