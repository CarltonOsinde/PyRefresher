#Easier way of buildng Lists - Iterating(for loops) quickly

temps = [220,240,321,300]

new_temps=[]

for temp in temps:
    new_temps.append(temp/10)

print (new_temps)




#IN-LINE COMPREHENSIONS

new_temps2 = [temp/10 for temp in temps]

print(new_temps2)