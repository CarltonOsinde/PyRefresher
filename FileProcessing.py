#Reading a file in Python

#NOTE: When opening a file always declare it to a myfile variable


#OPENING
myfile = open("Jobs.txt")

#READING
companies = myfile.read()

#NOTE: Due to the position of the cursor it is adviced to declare the read() to a variable

print(companies)



#CLOSING
myfile.close()


#USING the with statement/ context manager
with open("Jobs.txt") as myfile:
    companies = myfile.read()

print(companies)


#Writing to a Text file

with open("family.txt","w") as myfile:
    content = myfile.write("Carlton Osinde\nPapa Osinde\nOwen Osinde")



#QUIZ - Read the Jobs.txt file, and print out the first 90 characters of its content.


file = open("Jobs.txt")
contents = file.read()
print(contents[:90]) #EXTRACTING THE FIRST 90 CHARACTERS



#QUIZ#2 Create a first.txt file that contains the first 90 characters of bear.txt.

#Note that you should read the content of bear.txt with Python, extract its first 90 characters with Python, and write those characters in first.txt with Python.

bear_file = open("family.txt")
text = bear_file.read()
copied_text = text[:90]


with open("Jobs.txt", "w") as myfile:
    content = myfile.write(copied_text)




#Appending to an existing file







