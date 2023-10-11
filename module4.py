# loops
# loops can be made with for or while keyword

# will print numbers from whatever you have in i to 5, with a step of one
for i in range(5):  # will output numbers from 0 to 4
    print(i)

a = 0

print("-----------SEPARATOR-------------")

# here, after while keyword you have to put some kind of statement, in this case, it's while a is lower than 5
# increase a by one and print the value
while a < 5:  # will output from 1 to 5
    a = a + 1
    print(a)

print("-----------SEPARATOR-------------")
a = 0  # resetting the value

while a < 5:  # will output from 0 to 4, because the order of commands is different
    print(a)
    a = a + 1

print("-----------SEPARATOR-------------")

# clock simulator of one day

minute = 0
hour = 0

# This is an example of a so called nested loop

for hour in range(24):
    for minute in range(60):
        print("Hour:", hour, "|| Minute:", minute)
