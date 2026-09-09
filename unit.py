def convert_length(value, from_unit, to_unit):
    conversions = {
        'm': 1, 'cm': 0.01, 'km': 1000,
        'in': 0.0254, 'ft': 0.3048, 'yd': 0.9144
    }
    return value * conversions[from_unit] / conversions[to_unit]

value = float(input("Value: "))
from_unit = input("From (m, cm, km, in, ft, yd): ")
to_unit = input("To (m, cm, km, in, ft, yd): ")

result = convert_length(value, from_unit, to_unit)
print(f"{value} {from_unit} = {result} {to_unit}")