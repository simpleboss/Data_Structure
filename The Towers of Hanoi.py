from stack import Stack

# Create Three robs Stacks
left_rob = Stack(100)
middle_rob = Stack(100)
right_rob = Stack(100)

robs_list = [left_rob, middle_rob, right_rob]

# Input the number of disks
the_number_of_disks = 5
# the_number_of_disks = int(input("How many disks?\n"))
while the_number_of_disks < 3:
    print("The number of disks must be greater than 2")
    the_number_of_disks = int(input("How many disks?\n"))

# put disks in left rob
for i in range(the_number_of_disks, 0, -1):
    left_rob.push(i)

