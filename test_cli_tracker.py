#test file whilst working on cli_task_tracker.py
from cli_task_tracker import add_to_list, delete_from_list, update_list, print_task_list, change_status, print_by_status

#test add_to_list by adding 4 tasks to the list
add_to_list("make a list")
add_to_list("go to shops")
add_to_list("buy groceries")
add_to_list("cook dinner")

#test print function
print_task_list()

#test update function. Change status to: done, in-progress or todo
update_list(1, "make a list and do the pantry list")
update_list(2, "go to the Aldi and Lidl")

print_task_list()

#need to add to methos for id's not found.
delete_from_list(3)

print_task_list()

#test status change
change_status(2, 'done')
change_status(1, 'in progress')

print_task_list()

#test print by status function
print_by_status("done")

#add another task
add_to_list('re-write add to list function with JSON')

print_by_status