'''Assignment 1: Smart Home Appliance Control'''

class SmartThermostat:
    MIN_TEMP = 10.0
    MAX_TEMP = 35.0

    def __init__(self,appliance_name,initial_temp):
        self.__appliance_name=appliance_name
        self.__target_temp=22.0
        if self.MIN_TEMP<=initial_temp<=self.MAX_TEMP:
            self.target_temp=initial_temp

    @property
    def target_temp(self):
        """Getter property."""
        return self.__target_temp

    @target_temp.setter
    def target_temp(self,new_temp):
        if new_temp>self.MAX_TEMP or new_temp<self.MIN_TEMP:
            raise ("Temperature must be between 10.0 and 35.0 degrees.")
        else:
            self.__target_temp=new_temp

    @property
    def appliance_name(self):
        """Getter property"""
        return self.__appliance_name
        
def main():
    thermostat = SmartThermostat("Living Room AC", 24.0)
    print(thermostat.appliance_name)  # Output: Living Room AC
    print(thermostat.target_temp)     # Output: 24.0
    thermostat.target_temp = 28.0     # Updates successfully
    print(thermostat.target_temp)     # Output: 28.0
main()
