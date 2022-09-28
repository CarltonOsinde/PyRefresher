#FUNCTIONS - always starts with def (Cannot start with a # or math operator)

def mean(mylist):
    the_mean = sum(mylist)/len(mylist)

    return the_mean

grades = [100,90,55]

print(mean(grades)) #DO NOT use the . operator with a function


#PRINT VS RETURN
#If there's no return statement then Python defaults to None

def means(mylist):
    the_mean = sum(mylist)/len(mylist)

    print(the_mean)

grades = [100,90,55]
print(means(grades)) #THE OUTPUT WILL BE NONE


#CONDITIONALS ~ If/Else

#If statements MUST end with :

#Else statements MUST begin with :



def mean3(value):
    if type(value) == dict: #isinstance(value, dict) is a better and more efficient way to do this
        the_mean = sum(value.values()) / len(value)

    else:
        the_mean = sum(value)/len(value)

    return the_mean


temps = [2.0,3.0,4.0,5.0]

gradesA= {"Carlton": 100, "J": 99.5, "Laur": 97, "Upy":86}

print(mean3(gradesA))
print(mean3(temps))

#Quiz question
def password(value):
    if len(value) >= 8:
        return True
    
    else:
        return False 

#You can return a False & True without putting them in " "


