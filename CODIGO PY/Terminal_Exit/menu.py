from Statistics.csv_analizer import csv_analizer

class Menu:
    def mostrar_menu():
        #Read the money_statistics.csv and get the average money per boat, the average money per hour, and the total money billed
        lanzarMenu = False
        while lanzarMenu == False:
            print('-----------------------------')
            print('            Menu             ')
            print('-----------------------------')
            print('1.- Summary Total Statistics')
            print('2.- Summary TGport Statistics')
            print('3.- Summary CGRRport Statistics')
            print('4.- Summary CTPport Statistics')
            print('5.- Summary PCport Statistics')
            print('6.- Exit')

            opcion = int(input('Choose an option:\n'))
            lanzarMenu = True

            if 1 <= opcion <= 6:
                    archivo = './Analisis/csv/simulation.csv'
                    if opcion == 1:
                        print('')
                        print('---------------------------------------')
                        print('       Summary Total Statistics:       ')
                        print('---------------------------------------')
                        csv_analizer.TOTALMoneyAnalizer(archivo)
                        csv_analizer.TOTALtimeAnalizer(archivo) 
                        lanzarMenu = False 
                        
                    elif opcion == 2:
                        print('')
                        print('----------------------------------------')
                        print('       Summary TGport Statistics:       ')
                        print('----------------------------------------')
                        csv_analizer.TGport_MoneyAnalizer(archivo)
                        csv_analizer.TGport_timeAnalizer(archivo)
                        lanzarMenu = False
                        
                    elif opcion == 3:
                        print('')
                        print('------------------------------------------')
                        print('       Summary CGRRport Statistics:       ')
                        print('------------------------------------------')
                        csv_analizer.CGRRport_MoneyAnalizer(archivo)
                        csv_analizer.CGRRport_timeAnalizer(archivo)
                        lanzarMenu = False
                        
                    elif opcion == 4:
                        print('')
                        print('-----------------------------------------')
                        print('       Summary CTPport Statistics:       ')
                        print('-----------------------------------------')
                        csv_analizer.CTPport_MoneyAnalizer(archivo)
                        csv_analizer.CTPport_timeAnalizer(archivo)
                        lanzarMenu = False
                        
                    elif opcion == 5:
                        print('')
                        print('----------------------------------------')
                        print('       Summary PCport Statistics:       ')
                        print('----------------------------------------')
                        csv_analizer.PCport_MoneyAnalizer(archivo)
                        csv_analizer.PCport_timeAnalizer(archivo)
                        lanzarMenu = False
                        
                    elif opcion == 6:
                        print('---------------------------------')
                        print('   EXITING STATISTICAL PROGRAM   ')
                        print('---------------------------------')
                        print('             GOODBYE             ')
                        break  

                    
            else:
                print('----------------------------------------------------')
                print('Invalid option. Please select an option from 1 to 6.')
                print('----------------------------------------------------')
                lanzarMenu = False