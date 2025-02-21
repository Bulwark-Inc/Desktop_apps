class NumberConverter:
    @staticmethod
    def decimal_to_other(decimal_number):
        """Converts a decimal number to binary, hexadecimal, and octal."""
        try:
            decimal_number = int(decimal_number)  # Ensure it's an integer
            return {
                "decimal": decimal_number,
                "binary": bin(decimal_number)[2:],  # Remove '0b'
                "hexadecimal": hex(decimal_number)[2:].upper(),  # Remove '0x' & uppercase
                "octal": oct(decimal_number)[2:]  # Remove '0o'
            }
        except ValueError:
            return "Invalid Decimal Input"

    @staticmethod
    def binary_to_other(binary_number):
        """Converts a binary number to decimal, hexadecimal, and octal."""
        try:
            decimal = int(binary_number, 2)
            return NumberConverter.decimal_to_other(decimal)
        except ValueError:
            return "Invalid Binary Input"

    @staticmethod
    def hexadecimal_to_other(hex_number):
        """Converts a hexadecimal number to decimal, binary, and octal."""
        try:
            decimal = int(hex_number, 16)
            return NumberConverter.decimal_to_other(decimal)
        except ValueError:
            return "Invalid Hexadecimal Input"

    @staticmethod
    def octal_to_other(octal_number):
        """Converts an octal number to decimal, binary, and hexadecimal."""
        try:
            decimal = int(octal_number, 8)
            return NumberConverter.decimal_to_other(decimal)
        except ValueError:
            return "Invalid Octal Input"

if __name__ == "__main__":
    converter = NumberConverter()
    
    # Example conversions
    print(converter.decimal_to_other(25))  
    print(converter.binary_to_other("1101"))  
    print(converter.hexadecimal_to_other("1A"))  
    print(converter.octal_to_other("31"))  
