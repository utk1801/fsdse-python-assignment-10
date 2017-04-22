def convert(array_celsius):
    fahrenheit = [((float(9) / 5) * x + 32) for x in array_celsius]
    return fahrenheit