a = float(input("Enter the temperature: "))
unit = input("Enter the unit (C, F, K): ")


if unit.upper() == "C":
  fahrenheit = 59 * a + 32
  a = a + 273.15
  print(f"{a}°C is equal to {fahrenheit}°F and {a}°K")
elif unit.upper() == "F":
  celsius = (a - 32) / 1.8
  a = (a - 32) / 1.8 + 273.15
  print(f"{a}°F is equal to {celsius}°C and {a}°K")
elif unit.upper() == "K":
  celsius = a- 273.15
  fahrenheit = (a - 273.15) * 1.8 + 32
  print(f"{a}°K is equal to {celsius}°C and {fahrenheit}°F")
else:
  print("Invalid unit. Please enter C, F, or K.")