#LOOPS

temps = [9.9,8.8,7.6]
temps[0]


for each_temperature in temps:
     print(round(each_temperature))



colors = [11, 34, 98, 43, 45, 54, 54]

for i in colors:
    if i > 50:
        print(i)




#Looping through a dictionary
st_grades = {"Carlton": 91,"Dem people":90}

for i in st_grades.items():
    print(i)

for i in st_grades.keys():
    print(i)


for i in st_grades.values():
    print(i)



#WHILE LOOPS

while True:
    username = input("Enter your username: ")
    if username == "Carlton":
        break
    else:
        continue

password = input("Enter your password: ")

print("Thank you for logging in!")