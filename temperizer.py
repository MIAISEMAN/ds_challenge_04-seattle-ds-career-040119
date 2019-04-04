"""An example library for converting temperatures."""

def convert_f_to_c(temp_f):
    """Convert Fahrenheit to Celsius."""
    temp_c = (temp_f - 32) * (5/9)
    return temp_c

def convert_c_to_f(temp_c):
    """Convert Celsius to Fahrenheit."""
    return ((temp_c*9/5)+32)

def convert_c_to_k(temp_c):
    """Convert Celsius to Kelvin."""
    return (temp_c) + 273.15

def convert_f_to_k(temp_f):
    """Convert Celsius to Kelvin."""
    temp_c = convert_f_to_c(temp_f)
    return convert_c_to_k(temp_c)

def convert_k_to_c(temp_k):
    """Convert Kelvin to Celsius."""
    return temp_k - 273.15  

def convert_k_to_f(temp_k):
    """Convert Kelvin to Fahrenheit."""
    temp_c = convert_k_to_c(temp_k)
    return convert_c_to_f(temp_c)

