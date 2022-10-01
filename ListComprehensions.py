#Easier way of buildng Lists - Iterating(for loops) quickly

temps = [220,240,321,300]

new_temps=[]

for temp in temps:
    new_temps.append(temp/10)

print (new_temps)




#IN-LINE COMPREHENSIONS

new_temps2 = [temp/10 for temp in temps]

print(new_temps2)



#QUIZ QUESTIONS: Defining a function but using list comprehensions

#Define a function that takes as parameter list of numbers and returns the list containing only the numbers that are greater than 0. For example, I called your function with foo([-5, 3, -1, 101]) it should return [3, 101].


def foo(lst):
    return [i for i in lst if i>0]