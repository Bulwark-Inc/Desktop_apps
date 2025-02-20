# logic.py - Temperature Conversion Logic using OOP

class TemperatureConverter:
    def __init__(self, value, from_unit, to_unit):
        self.value = float(value)
        self.from_unit = from_unit
        self.to_unit = to_unit
    
    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32
    
    def celsius_to_kelvin(self, celsius):
        return celsius + 273.15
    
    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9
    
    def fahrenheit_to_kelvin(self, fahrenheit):
        return (fahrenheit - 32) * 5/9 + 273.15
    
    def kelvin_to_celsius(self, kelvin):
        return kelvin - 273.15
    
    def kelvin_to_fahrenheit(self, kelvin):
        return (kelvin - 273.15) * 9/5 + 32
    
    def convert(self):
        """Converts temperature from one unit to another."""
        if self.from_unit == self.to_unit:
            return self.value  # No conversion needed
        
        conversion_functions = {
            ('Celsius', 'Fahrenheit'): self.celsius_to_fahrenheit,
            ('Celsius', 'Kelvin'): self.celsius_to_kelvin,
            ('Fahrenheit', 'Celsius'): self.fahrenheit_to_celsius,
            ('Fahrenheit', 'Kelvin'): self.fahrenheit_to_kelvin,
            ('Kelvin', 'Celsius'): self.kelvin_to_celsius,
            ('Kelvin', 'Fahrenheit'): self.kelvin_to_fahrenheit,
        }
        
        if (self.from_unit, self.to_unit) in conversion_functions:
            return round(conversion_functions[(self.from_unit, self.to_unit)](self.value), 2)
        else:
            raise ValueError("Invalid conversion request")
