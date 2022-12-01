

# This program changes temp celsius to farenheit

def temp_convt(celsius):
    return (celsius * 9 / 5 ) + 32

celsius = float(input("Enter temperature in celsius: "))

print(str(celsius) + "  Celsius in Fahrenheit is " + str(temp_convt(celsius)))    