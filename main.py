print("Hello, I am the temperature conversion robot")
convert_yn = input("Would you like to convert some temperature measurements? [yes/no] ")
convert_yn = convert_yn.lower()

while convert_yn != "yes":
    print("Ok, type yes if you change your mind")
    convert_yn = input("")
    convert_yn = convert_yn.lower()

input_unit = input("What unit are you converting from? [fahrenheit/celsius/kelvin] ").capitalize()
output_unit = input("What unit are you converting to? [fahrenheit/celsius/kelvin] ").capitalize()
input_value = int(input("Please input the number that requires conversion "))
output_value = None

match input_unit:
    case "Fahrenheit":
        match output_unit:        
            case "Celsius":
                output_value = ((input_value - 32) * 5)/9
            case "Kelvin":
                output_value = (((input_value - 32) * 5)/9) + 273.15
    case "Celsius":
        match output_unit:        
            case "Fahrenheit":
                output_value = (input_value * 1.8) + 32
            case "Kelvin":
                output_value = input_value + 273.15
    case "Kelvin":
        match output_unit:        
            case "Fahrenheit":
                output_value = ((input_value - 273.15) * 1.8) + 32
            case "Celsius":
                output_value = input_value - 273.15

print(input_value, "degrees", input_unit, "is equal to", output_value, "degrees", output_unit)