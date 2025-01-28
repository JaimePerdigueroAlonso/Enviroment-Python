import random

class Weather:
    
    def weather_delay():
        """
        Simulate weather conditions and calculate the delay caused by bad weather.

        Returns:
            float: Total delay caused by bad weather.
        """
        
        wheather_type = [('Rain', random.uniform(1, 2)), ('Wind', random.uniform(0, 1)), ('Sun', random.uniform(0, 0)),
                     ('Snow', random.uniform(1, 4)), ('Fog', random.uniform(0, 1))] 

        weather_number = random.randint(1, 5)
        #Same as 'choice' but I tell it to randomly select multiple elements from a list I specify.
        random_weather = random.sample(wheather_type, weather_number) 

        lista = [] 
        #Bad Weather Delay Counter
        total_delay = 0  

        for item in random_weather:
            lista.append(item[0])
            #Adding the second element of the tuple to the counter.
            total_delay += item[1]  


        return total_delay
        
        
        
