FAHRENHEIT_TO_CELSIUS_FACTOR = 5.0/9.0
CELSIUS_TO_FAHRENHEIT_FACTOR =  9.0/5.0

def convert_to_celsius(temp):
    global FAHRENHEIT_TO_CELSIUS
    converted_temp = (temp - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return converted_temp

    

def convert_to_fahrenheit(temp):
    global CELSIUS_TO_FAHRENHEIT
    converted_temp = (temp * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return converted_temp

def main():
    print("Temperature Conversion Tool")

    #input valid temperature
    try:
        temperature = float(input("Enter the temperature to convert: "))
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return
    
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F) ").strip().upper()
    match unit:
        case "F":
            celsius = convert_to_celsius(temperature)
            print (f"{temperature}\u00B0F is {celsius}\u00B0C.")
        
        case "C":
            fahrenheit = convert_to_fahrenheit(temperature)
            print(f"{temperature}\u00B0C is {fahrenheit}\u00B0F")

        case _:
            print("Invalid unit. Please enter Fahrenheit or Celsius (C/F)")

if __name__ == "__main__":
    main()
