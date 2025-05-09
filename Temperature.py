temperature = float(input("What's the temperature for you right now: "))
unit = input("Fahrenheit (F) or Celsius (C): ")

if unit.upper() == "F":
    converted = (temperature - 32) * 5/9
    print("Temperature in Celsius: " + str(round(converted, 2)))
elif unit.upper() == "C":
    converted = (temperature * 9/5) + 32
    print("Temperature in Fahrenheit: " + str(round(converted, 2)))
else:
    print("Invalid unit. Please enter 'F' or 'C'.")
