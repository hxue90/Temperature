def askTmp():
    return int(input("Please enter temperature in Fahrenheit: "))

def convertTmp(temperature):
    return (temperature-32)*(5/9)

def askConvert():
    temperature = askTmp()
    convertTemperature = convertTmp(temperature)

    print("The temperature F is '" + str(temperature) + "' and C is '" + str(convertTemperature) +"'")

def main():
    contTmp = "y"
    while contTmp == "y":
        askConvert()
        contTmp = input("Would you like to continue (y/n): ")

if __name__ == "__main__":
    main()