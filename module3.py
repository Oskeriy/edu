# functions are defined using
# 1. def keyword
# 2. name of the function
# 3. the parameters inside the function (will discuss that later)
# 4. ends with :
# 5. don't forget the indents

def say_message_with_stars(message):
    print("*****", message, "*****")


# here "hello" is passed as an argument
say_message_with_stars("hello")

# It can also be passed as a variable

hi = "hi"
say_message_with_stars(hi)


# If the function does not end with return keyword, it means that it's return type is void
# Otherwise,

def to_the_power_of_two(number):
    return number * number


to_the_power_of_two(5)  # - won't print anything
print(to_the_power_of_two(4))  # will output 16

num = to_the_power_of_two(10)  # will not output anything
print(num)  # will output 100

# And by the way, add indent after you defined the method
#   like this
