#cli_tasker_tracker.py
#from the roadmap.sh project suggestions page
#
#from datetime import datetime
from time import strftime, gmtime, localtime
import json

task_list = []
formatted_timestamp = strftime("%c", localtime())
data = ("empty string")

def add_to_list(task):

    #make a dictionary and add a unique id, task description, status, createdAt and updatedAt
    id = len(task_list) + 1
    task_dictionary = dict(id= id, description = task, status = "to do", createdAt = formatted_timestamp, updatedAt = formatted_timestamp)

    #add the dictionary to the task_list,
    task_list.append(task_dictionary)

    #open an file and append the task list
    with open("list_data.json", "w") as output_file:
        json.dump(task_list, output_file, indent = 2)

    print("\nTask added successfully (ID: " + str(id) + ")")

def print_task_list():

    #open JSON file as 'read'
    with open('list_data.json', 'r') as openfile:
        
        #reading from JSON file
        #data = json.load(openfile)
        pass

    #access and process the retrieved JSON data
    print(data)

   

def update_list(task_id, new_description):
    
    #find the dictionary with id = task_id
    #change the description to new_descrption
    for x in task_list :
        temp_dictionary = task_list[x]
        if temp_dictionary['id'] == 2 :
            print("this is id 2")

def delete_from_list(task_id) :
    task_list.pop(task_id-1)
    print("\ndeleted task ID: " + str(task_id))

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