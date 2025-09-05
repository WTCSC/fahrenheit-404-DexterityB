print("Hello, I am the temperature conversion robot")
convert_yn = input("Would you like to convert some temperature measurements? [yes/no] ").lower()

while convert_yn != "yes":
    print("Ok, type yes if you change your mind")
    convert_yn = input("")
    convert_yn = convert_yn.lower()

again = "yes"
while again == "yes":
    input_unit = input("What unit are you converting from? [fahrenheit/celsius/kelvin] ").capitalize()
    while input_unit != "Fahrenheit" and input_unit != "Celsius" and input_unit != "Kelvin":
        print("That's not one of the options. Perhaps you mispelled something?")
        print("")
        input_unit = input("What unit are you converting from? [fahrenheit/celsius/kelvin] ").capitalize()

    output_unit = input("What unit are you converting to? [fahrenheit/celsius/kelvin] ").capitalize()
    while output_unit != "Fahrenheit" and output_unit != "Celsius" and output_unit != "Kelvin":
        print("That's not one of the options. Perhaps you mispelled something?")
        print("")
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
    if input_unit == output_unit:
        output_value = input_value

    output_value = round(output_value, 3)

    print("")
    print(f"{input_value} degrees {input_unit} is equal to {output_value} degrees {output_unit}")

    again = input("Would you like to convert some more temperature measurements? [yes/no] ").lower()
    print("")