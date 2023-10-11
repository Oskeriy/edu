# Collection data types: the main one you need to now is list
# it is created via []

# Basically, if you think of a variable as of a box in which you can out only one value
# like:

a = 5
print(a)

# Then lists are boxes, in which you can put multiple values

box_with_numbers = [1, 2, 3, 4, 5]
print(box_with_numbers)

# You can add numbers there
box_with_numbers.append(12)
print(box_with_numbers)

# You can delete numbers from there
box_with_numbers.remove(2)
print(box_with_numbers)

# You can take numbers from list by their index
print(box_with_numbers[0]) # first number in the list, indexing goes from 0

# You can take the last item in the list like so
# len() function will print an amount of elements in a list
# or in a String, e.g the length of "Hi" is 2, since it has 2 characters
print(box_with_numbers[len(box_with_numbers) - 1])

# You can clear the list via clear
box_with_numbers.clear()
print(box_with_numbers)


