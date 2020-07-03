from stack import Stack

# Create Three robs Stacks
left_rob = Stack("Left rob", 100)
middle_rob = Stack("Middle rob", 100)
right_rob = Stack("Right rob", 100)

robs_list = [left_rob, middle_rob, right_rob]

# input the number of disks
# the_number_of_disks = 5
the_number_of_disks = int(input("How many disks?\n"))
while the_number_of_disks < 3:
    print("The number of disks must be greater than 2")
    the_number_of_disks = int(input("How many disks?\n"))

# put disks in left rob
for i in range(the_number_of_disks, 0, -1):
    left_rob.push(i)


# display current position of disks on a rob
def display_current_position_of_disks_on_robs():
    for rob in robs_list:
        print('{:10}'.format(rob.name), end=" ")
        print(": "+str(rob.list_of_nodes()))


# user의 input을 받는 method
def input_the_rob():
    user_input = ''
    first_letter_of_robs_list = [rob.name[0] for rob in robs_list]
    while user_input not in first_letter_of_robs_list:
        print("Input the first letter of the rob")
        user_input = input()
    for rob in robs_list:
        if user_input == rob.name[0]:
            return rob


while robs_list[-1].size != the_number_of_disks:
    display_current_position_of_disks_on_robs()

    while True:
        print("What robs do you want to pick disk from?")
        rob_chosen_for_pickup = input_the_rob()
        if not rob_chosen_for_pickup.is_empty():
            break
        print("The rob you chosen is empty.")

    while True:
        print("What robs do you want to pick disk to?")
        rob_chosen_for_push = input_the_rob()
        if rob_chosen_for_push.is_empty() or int(rob_chosen_for_push.peek()) > int(rob_chosen_for_pickup.peek()):
            rob_chosen_for_push.push(rob_chosen_for_pickup.pop())
            break
        print("The rob you chosen for pushing have the less value of disks on top")

    print("Mission Completed.")



