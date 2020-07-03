from stack import Stack

# Create Three robs Stacks
left_rob = Stack("Left rob", 100)
middle_rob = Stack("Middle rob", 100)
right_rob = Stack("Right rob", 100)

robs_list = [left_rob, middle_rob, right_rob]

# input the number of disks
the_number_of_disks = 5
# the_number_of_disks = int(input("How many disks?\n"))
while the_number_of_disks < 3:
    print("The number of disks must be greater than 2")
    the_number_of_disks = int(input("How many disks?\n"))

# put disks in left rob
for i in range(the_number_of_disks, 0, -1):
    left_rob.push(i)


# display current position of disks on a rob
def display_current_position_of_disks(rob):
    print('{:10}'.format(rob.name), end=" ")
    print(": "+str(rob.list_of_nodes()))


for rob in robs_list:
    display_current_position_of_disks(rob)