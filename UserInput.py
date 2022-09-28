def weather_condition(temperature):
    if temperature >= 7:
        return "Warm"

    else:
        return "Cold"

user_input = int(input("Enter a temperature:"))


print(weather_condition(user_input))


#String Formating
user_input = input("Enter your name: ")
message = "What it do %s" %user_input
message = f"What's good {user_input}" # Easier way to implement String formating

print(message)