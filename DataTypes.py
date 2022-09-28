# The Basics: Data Types/Data Structures##

################################

#Lists

student_grades = [99.0, 35.5, 88.1]

print(student_grades)

print(111111111111111111111111111111111111111111)


#Calculate the mean ofa list

grades_sum = sum(student_grades)

mean = grades_sum/ len(student_grades)

print(mean)

print(111111111111111111111111111111111111111111)

#Finding the count of 10 in a list

student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]

the_count_of_ten = student_grades.count(10.0)

print(the_count_of_ten)

print(111111111111111111111111111111111111111111)


#Dictionaries

weeks_temp = [10.0, 9.2, 5.0]
the_grades2 = {'Carlton': 10.0, 'Upy': 9.2, 'Laur': 9.3}

values_of_the_grades = the_grades2.values()
print(values_of_the_grades)

mysum = sum(the_grades2.values())
mean = mysum / len(the_grades2)

print(mean)

values_of_the_grades = the_grades2.values()



#Tuples

temp = (11,16,24)

print(temp[1])

print(111111111111111111111111111111111111111111)


#OPERATIONS WITH DATA Types


#appending to a list
monday_temp=[11.3,22,14.5,17,19]

monday_temp.append(15)

print(monday_temp)
print(111111111111111111111111111111111111111111)

#Indexing with List
#Use this to find the function .index() to get the index given the value of the list

print(monday_temp.index(14.5,1))
print(111111111111111111111111111111111111111111)

##Access using index to find the value of the list

print(monday_temp[1])
print(111111111111111111111111111111111111111111)


#SLICES - Accessing portions of the list

sl = [3,4,5,2,7,1]

print(sl[3:]) #From the 3rd index all the way to the last index

print(sl[3:5]) #From the 3rd index all the way to the 5th

print(sl[-2]) #Negative indexing - starts from the back of the list


#Chain indexing inside a LIST

sl2 = ["Carlton", 2, 4]
print(sl2[0][0])




#INDEXING WITH Dictionaries

jobs = {"Google": 120000, "Bloomberg": 1500000, "Facebook": 1700000}

print(jobs.keys()) #Access the keys of the dictionary
print(jobs.values()) #Access the values of the dictionarydictionary

print(jobs["Facebook"]) #Access the value of a key



data = {"a": [1,2,3], "b": [4,5,6], "c": [7,8,9]}

