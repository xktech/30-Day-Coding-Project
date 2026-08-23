# Money, metric, distance, measurement converter
#
# GBP -> USD (22/08/26) = 1 : 1.36
# MPH -> KPH = 1 : 1.60~
# cm -> mm = 1 : 10
# more

import pint

ureg = pint.UnitRegistry()

def convert(value, from_unit, to_unit):
    result = (value * ureg(from_unit)).to(to_unit)
    return result.magnitude


def convert_config():
    print("Converter - (value -> from_unit -> to_unit)")
    print("Example:")
    print("60, mph, kph")
    print("Prints 60mph in kph.")
    value = int(input("Enter the number: "))
    from_unit = input("Enter the unit you want to convert from: ")
    to_unit = input("Enter the unit you want to convert to: ")

    print(f"Converted {value}{from_unit}(s) to {convert(value=value, from_unit=from_unit, to_unit=to_unit)} {to_unit}(s)")

while True:
    print("1. Convert")
    print("2. EXIT")

    choice = input("[arch@xktech ~]$  ")

    if choice == "1":
        convert_config()
    elif choice == "2":
        break

