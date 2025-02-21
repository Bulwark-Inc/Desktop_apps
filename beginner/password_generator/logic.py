import random
import string

class PasswordGenerator:
    @staticmethod
    def generate(length=12, use_upper=True, use_digits=True, use_symbols=True):
        """Generates a random password with the specified criteria."""
        lower_chars = string.ascii_lowercase
        upper_chars = string.ascii_uppercase if use_upper else ''
        digit_chars = string.digits if use_digits else ''
        symbol_chars = string.punctuation if use_symbols else ''
        
        all_chars = lower_chars + upper_chars + digit_chars + symbol_chars

        if not all_chars:
            return "Error: No character set selected!"
        
        return ''.join(random.choice(all_chars) for _ in range(length))
