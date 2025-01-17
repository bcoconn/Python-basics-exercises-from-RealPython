# 9.1 - Tuples are Immutable Sequences
# Solutions to review exercises


# Exercise 1
# Create a tuple "cardinal_numbers" with "first", "second" and "third"
cardinal_numbers = ("first", "second", "third", "fourth", "fifth", "sixth")


# Exercise 2
# Display the second object in the tuple
print(cardinal_numbers[1])

# Display the sixth object in the tuple
print(cardinal_numbers[5])

# Exercise 3
# Unpack the tuple into three strings and display them
position1, position2, position3, position4, position5, position6 = cardinal_numbers
print(position1)
print(position2)
print(position3)
print(position4)
print(position5)
print(position6)

# Exercise 4
# Create a tuple containing the letters of your name from a string
my_name = tuple("David")

# Exercise 5
# Check whether or not x is in my_name
print("x" in my_name)

# Exercise 6
# Create tuple containing all but the first letter in my_name
print(my_name[1:])
