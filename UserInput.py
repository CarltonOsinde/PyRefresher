def weather_condition(temperature):
    if temperature >= 7:
        return "Warm"

    else:
        return "Cold"

user_input = int(input("Enter a temperature:"))


print(weather_condition(user_input))


#String Formating
user_input = input("Enter your name: ")
message = "What it do %s" %user_input # Variable
message = f"What's good {user_input}" # Easier way to implement String formating

print(message)


#String Formating with multiple Variables

name = input("Enter your first name: ")
surname = input ("Enter your surname: ")

message = "Yo %s %s" %(name, surname)

print(message)


def get_username():
    user_input = input("Enter your first name: ")
    first_name = user_input.capitalize()
    message = "Hi %s" %first_name
    
    return message

print(get_username())

