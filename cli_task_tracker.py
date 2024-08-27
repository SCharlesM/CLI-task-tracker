#cli_tasker_tracker.py
#from the roadmap.sh project suggestions page
#
#from datetime import datetime
from time import strftime, gmtime, localtime
import json

task_list = []
formatted_timestamp = strftime("%c", localtime())
data = ("")

#function to write the list of dictionaries to JSON file list_data.json
def write_to_json(input_list) :
    
    #open an file and write the new_list to the file
    with open("list_data.json", "w") as output_file:
        json.dump(input_list, output_file, indent = 2)

#function to read a list of dictionaries from JSON file list_data.json
def read_from_json() :
    
    #open a file and read the contents into 'output_list
    with open('list_data.json', 'r') as openfile:
        output_list = json.load(openfile)

    return(output_list)

def add_to_list(task):

#I think I need to read the JSON file here, then add the data to task_list and continue
    #make a dictionary and add a unique id, task description, status, createdAt and updatedAt
    id = len(task_list) + 1
    task_dictionary = dict(id= id, description = task, status = "todo", createdAt = formatted_timestamp, updatedAt = formatted_timestamp)

    #add the dictionary to the task_list,
    task_list.append(task_dictionary)

    write_to_json(task_list)

    print("\nTask added successfully (ID: " + str(id) + ")")

def print_task_list():

    data = read_from_json()

    print("\nTask ID, description, status, date and time created, date and time updated")
    
    i = 0
    while i < len(data) :
        extract = data[i]
        print(extract['id'], ". ", extract['description'], ", ", extract['status'], ", ", extract['createdAt'], ". ", extract['updatedAt'])
        i += 1

def print_by_status(status_reference):

    data = read_from_json()

    #access and process the retrieved JSON data
    i = 0
    while i < len(data) :
        extract = data[i]

        if extract['status'] == status_reference :
            print("all tasks that are status: " + status_reference)
            print(extract['id'], ". ", extract['description'], ", ", extract['status'], ", ", extract['createdAt'], ". ", extract['updatedAt'])
    

def update_list(task_id, new_description):
    
    #read the JSON file, iterate through the IDs, change the description
    data = read_from_json()
    
    i = 0 
    while i < len(data) :
        extract = data[i]
        if extract['id'] == task_id :
            extract['description'] = new_description
            write_to_json(data)
        i += 1       
    
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