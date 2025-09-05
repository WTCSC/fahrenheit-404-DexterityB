print("Hello, I am the temperature conversion robot")
convert_yn = input("Would you like to convert some temperature measurements? [yes/no] ").lower()

#initial question error handling
while convert_yn != "yes":
    print("Ok, type yes if you change your mind")
    convert_yn = input("")
    convert_yn = convert_yn.lower()

#loop for more temperature conversions
again = "yes"
while again == "yes":
    #units with error handling
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

    #conversion value with error handling
    input_value = input("Please input the number that requires conversion ")
    while True:
        try:
            input_value = int(input_value)
            break
        except:
            print("That is not a number")
            print("")
            input_value = input("Please input the number that requires conversion ")

    output_value = None

    #The actual conversion
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

    #Prints the result
    print("")
    print(f"{input_value} degrees {input_unit} is equal to {output_value} degrees {output_unit}")

    #Asks if you want to repeat
    again = input("Would you like to convert some more temperature measurements? [yes/no] ").lower()
    print("")