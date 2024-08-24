#test file whilst working on cli_task_tracker.py
from cli_task_tracker import add_to_list, delete_from_list, update_list

add_to_list("make a list")
add_to_list("go to shops")
add_to_list("buy groceries")
add_to_list("cook dinner")

delete_from_list(1)

update_list(2, "go to shops and post office")