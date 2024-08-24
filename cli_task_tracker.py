#cli_tasker_tracker.py
#from the roadmap.sh project suggestions page
#
#from datetime import datetime
from time import strftime, gmtime, localtime

task_list = []
formatted_timestamp = strftime("%c", localtime())

def add_to_list(task):

    id = len(task_list) + 1
    task_dictionary = dict(id= id, description = task, status = "to do", createdAt = formatted_timestamp, updatedAt = formatted_timestamp)
    task_list.append(task_dictionary)
    print("\nTask added successfully (ID: " + str(id) + ")")
    print(task_list)

def update_list(task_id, new_description):
    
    
    print(new_description)



def delete_from_list(task_id) :
    task_list.pop(task_id-1)
    print(task_list)

def end() :
    print('end of cli-task')

def format_task(string_to_be_formatted):
    task = string_to_be_formatted.replace('"', '')
    return task

"""
print('\nWelcome to cli task tracker....what would you like to do?')
loop = False

while (loop) :
    user_command = input("\ncommand: ")
    command_list = user_command.split(" ", 2)
    #print(command_list)
    
    if command_list == [] :
        print("not a task-cli command, commands are:\n")
        print('task-cli add <task name>\ntask-cli delete <task ID>\nend')
        pass
    
    elif command_list[0] == 'end' :
        end()
        break

    elif command_list[0] != "task-cli" :
        print("not a task-cli command, commands are:\n")
        print('task-cli add <task name>\ntask-cli delete <task ID>\nend')

    elif command_list[1] == 'add' :
        task = format_task(command_list[2])
        add_to_list(task)

    elif command_list[1] == 'delete' :
        #print('deleting from JSON file')
        delete_from_list()

    else :
        print('incorrect input')
        print('commands are: task-cli add <task name>\ntask-cli delete <task ID>\nend')

"""