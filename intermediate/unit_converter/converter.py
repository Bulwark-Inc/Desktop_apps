class UnitConverter:
    """Handles unit conversions for length, weight, volume, temperature, area, and speed."""

    # Conversion factors based on meters (length), kilograms (weight), and liters (volume)
    length_factors = {
        "meters": 1,
        "kilometers": 0.001,
        "centimeters": 100,
        "millimeters": 1000,
        "miles": 0.000621371,
        "yards": 1.09361,
        "feet": 3.28084,
        "inches": 39.3701
    }

    weight_factors = {
        "kilograms": 1,
        "grams": 1000,
        "milligrams": 1_000_000,
        "pounds": 2.20462,
        "ounces": 35.274
    }

    volume_factors = {
        "liters": 1,
        "milliliters": 1000,
        "cubic meters": 0.001,
        "gallons": 0.264172,
        "quarts": 1.05669,
        "pints": 2.11338,
        "cups": 4.16667
    }

    area_factors = {
        "square meters": 1,
        "square kilometers": 0.000001,
        "acres": 0.000247105,
        "hectares": 0.0001,
        "square miles": 3.861e-7,
        "square feet": 10.7639,
        "square inches": 1550.003
    }

    speed_factors = {
        "meters per second": 1,
        "kilometers per hour": 3.6,
        "miles per hour": 2.23694,
        "knots": 1.94384
    }

    recent_conversions = []  # Stores last 5 conversions

    @staticmethod
    def convert(value, from_unit, to_unit, category):
        """Converts a value from one unit to another within a given category."""
        # Handle temperature separately
        if category == "Temperature":
            converted_value = UnitConverter.convert_temperature(value, from_unit, to_unit)
        else:
            factors = UnitConverter.get_factors(category)
            if from_unit not in factors or to_unit not in factors:
                raise ValueError("Invalid unit selected.")

            # Convert to base unit first, then to target unit
            base_value = value / factors[from_unit]
            converted_value = base_value * factors[to_unit]

        rounded_value = round(converted_value, 4)
        UnitConverter.store_conversion(value, from_unit, rounded_value, to_unit)
        return rounded_value

    @staticmethod
    def convert_temperature(value, from_unit, to_unit):
        """Handles temperature conversions using formulas."""
        if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                return (value * 9/5) + 32
            elif to_unit == "Kelvin":
                return value + 273.15
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                return (value - 32) * 5/9
            elif to_unit == "Kelvin":
                return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                return value - 273.15
            elif to_unit == "Fahrenheit":
                return (value - 273.15) * 9/5 + 32
        return value  # If same unit is selected

    @staticmethod
    def get_factors(category):
        """Returns the correct factor dictionary based on category."""
        category_map = {
            "Length": UnitConverter.length_factors,
            "Weight": UnitConverter.weight_factors,
            "Volume": UnitConverter.volume_factors,
            "Area": UnitConverter.area_factors,
            "Speed": UnitConverter.speed_factors
        }
        return category_map.get(category, None)

    @staticmethod
    def store_conversion(value, from_unit, converted_value, to_unit):
        """Stores the last 5 conversions."""
        UnitConverter.recent_conversions.append(f"{value} {from_unit} -> {converted_value} {to_unit}")
        if len(UnitConverter.recent_conversions) > 5:
            UnitConverter.recent_conversions.pop(0)  # Keep only last 5 records
