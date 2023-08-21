'''
Adam Roy
CSCI 161
Assignment 12
'''
#ver 2.4

class BMW:
    def _init_(self, make, model, year):
        make = 'none'
        model = 'none'
        year = 0
    
    def startEngine():
        engine_on = True
        return engine_on
        
    def stopEngine():
        engine_on = False
        return engine_on
    
    class ThreeSeries(BMW):
        BMW._init_(self, cruiseControlEnabled, make, model, year, attribute)
        cruiseControlEnabled = bool(False)
        def display(car1, cruiseControlEnabled):
            #print state of cruiseControlEnabled
            print('Three Series')
            print('This', car1.make, 'is a', car1.model, 'of', car1.year)            
            if super(BMW).startEngine() is True:
                inp = input('Is cruise control on? (y or n)')
                if inp == 'y':
                    cruiseControlEnabled = bool(True)
                    print('Button start is on')
                    print('The engine is now on')
                    print('Cruise Control is Enabled:', cruiseControlEnabled)
                else:
                    cruiseControlEnabled = bool(False)
                    print('Button start is on')
                    print('The engine is now on')
                    print('Cruise Control is Enabled:', cruiseControlEnabled)                    
            else:
                print('Button start is off')
                print('The engine is off')
                print('Cruise Control is Enabled:', cruiseControlEnabled)
            
    class FiveSeries(BMW):
        super(BMW)._init_(parkingAssistEnabled, make, model, Year)
        parkingAssistEnabled = bool(False)
        def display(car2, parkingAssistEnabled):        
            #print state of parkingAssistEnabled
            print('Five Series')
            print('This', car2.make, 'is a', car2.model, 'of', car2.year)
            if super(BMW).startEngine() is True:
                inp = input('Is the parking assist enabled? (y or n)')
                if inp == 'y':
                    parkingAssistEnabled = bool(True)
                    print('Button start is on')
                    print('The engine is now on')
                    print('Parking Assist Is Enabled:', parkingAssistEnabled)
                else:
                    parkingAssistEnabled = bool(False)
                    print('Button start is on')
                    print('The engine is now on')
                    print('Parking Assist Is Enabled:', parkingAssistEnabled)                    
            else:
                print('Button start is off')
                print('The engine is off')
                print('Parking Assist Is Enabled:', parkingAssistEnabled)
                    
            
def main():
    car = BMW()
    car1 = BMW().ThreeSeries(car1)
    car1.make = input('Enter the threeseries make: \n')
    car1.model = input('Enter the model: \n')
    car1.year = input('Enter the year: \n')
    car2 = BMW().FiveSeries(car2)
    car2.make = input('Enter the fiveseries make: \n')
    car2.model = input('Enter the model: \n')
    car2.year = input('Enter the year: \n')
    BMW.startEngine()
    BMW.ThreeSeries.display
    BMW.FiveSeries.display

main()

    
            
        