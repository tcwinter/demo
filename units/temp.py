def celsius_to_fahrenheit(c: float) -> float:
    """Convert Celsius to Fahrenheit: F = C * 9/5 + 32"""
    return c * 9.0 / 5.0 + 32.0


def fahrenheit_to_celsius(f: float) -> float:
    """Convert Fahrenheit to Celsius: C = (F - 32) * 5/9"""
    return (f - 32.0) * 5.0 / 9.0