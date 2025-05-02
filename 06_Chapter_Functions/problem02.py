def Celsius_to_Fahrenheit():#Without Parameters
    celsius = int(input("Enter Temprature in celsi..."))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} is equal to {fahrenheit}")

def Fahrenheit_to_Celsius(f):#Without Parameters
    # celsius = int(input("Enter Temprature in celsi..."))
    celsius = (f -32) * 5/9
    print(f"{f} is equal to {celsius}")

Celsius_to_Fahrenheit()
Fahrenheit_to_Celsius(68)
