# --------------
# Code starts here

# Create the lists 
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']
new_class = class_1 + class_2
print(new_class)
new_class += ['Peter Warden']
print(new_class)
new_class.remove('Carla Gentry')
print(new_class)
courses = {'Math': 65,'English': 70,'History' : 80,'French': 70,'Science': 60}
total = 0
for key in courses:
    total = total + courses[key]
percentage = total / 5
print(total,percentage)

mathematics = {'Geoffrey Hinton': 78, 'Andrew Ng': 95, 'Sebastian Raschka': 65, 'Yoshua Bengio': 50, 'Hilary Mason': 70, 'Corinna Cortes': 66, 'Peter Warden': 75}

topper = max(mathematics,key = mathematics.get)
print(topper)

topper = topper.split(" ")
first_name,last_name = topper

full_name = last_name +" " + first_name
certificate_name = full_name.upper()
print(certificate_name)
# Concatenate both the strings


# Append the list

# Print updated list


# Remove the element from the list

# Print the list



# Create the Dictionary



# Slice the dict and stores  the all subjects marks in variable


# Store the all the subject in one variable `Total`

# Print the total

# Insert percentage formula

# Print the percentage




# Create the Dictionary
 



# Given string


# Create variable first_name 

# Create variable Last_name and store last two element in the list

# Concatenate the string

# print the full_name

# print the name in upper case

# Code ends here


