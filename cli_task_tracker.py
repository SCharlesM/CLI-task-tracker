#cli_tasker_tracker.py
#from the roadmap.sh project suggestions page
#
#from datetime import datetime
from time import strftime, gmtime, localtime
import json

#task_list = []
formatted_timestamp = strftime("%c", localtime())
data = ("")
global loop
loop = True

#function to write the list of dictionaries to JSON file list_data.json
def write_to_json(input_list) :
    
    #open an file and write the new_list to the file
    with open("list_data.json", "w") as output_file:
        json.dump(input_list, output_file, indent = 2)

#function to read a list of dictionaries from JSON file list_data.json
def read_from_json() :

    output_list = []
    
    #open a file and read the contents into 'output_list
    with open('list_data.json', 'r') as openfile:
        try:
            output_list = json.load(openfile)
        except  json.decoder.JSONDecodeError:
            print ('this is JSON decode error, is the JSON file empty?')

    if output_list == [] :
        pass
    else :
        return(output_list)

"""
add_to_list - a function to make add a task to list
make a dictionary, add the next ID, task description, status, createdAt and updatedAt
"""
def add_to_list(task):

    max_id = 0
    current_id = 1
    task_list = []

    data = read_from_json()

    #read the data from the JSON file, find the biggest ID
    #if the file is empty start with ID 1
    if data == None :
        task_dictionary = dict(id = 1, description = task, status = 'todo', createdAt = formatted_timestamp, updatedAt = formatted_timestamp)
        task_list.append(task_dictionary)
        write_to_json(task_list)
    else :
        i = 0 
        while i <len(data) :    #len() may be wrong when id's get deleted
            extract = data[i]
            max_id = extract['id']
            i += 1
    
        current_id = max_id + 1
        task_dictionary = dict(id = current_id, description = task, status = 'todo', createdAt = formatted_timestamp, updatedAt = formatted_timestamp)
        data.append(task_dictionary)

    write_to_json(data)
    print('Task added successfully (ID: ', current_id, ')')

def print_task_list():

    data = read_from_json()

    print("\nTask ID, description, status, date and time created, date and time updated")
    
    i = 0
    while i < len(data) :
        extract = data[i]
        print(extract['id'], ". ", extract['description'], ", ", extract['status'], ", ", extract['createdAt'], ". ", extract['updatedAt'])
        i += 1

#a function to print the task by status
#read the json file, iterate through dictionaries to find correct status and print
def print_by_status(*status_reference):

    #status_reference
    stripped_reference = str(status_reference).strip("(,')")
    data = read_from_json()

    #access and process the retrieved JSON data
    i = 0

    #if stripped_reference is empty string, print_task_list
    #else print below...

    print("\nListing all tasks that are status: ", status_reference)

    while i < len(data) :       #change this while loop to 'for extract in data'
        extract = data[i]

        if extract['status'] == stripped_reference :
            print(extract['id'], ". ", extract['description'], ", ", extract['status'], ", ", extract['createdAt'], ". ", extract['updatedAt'])
        i += 1

def update_list(task_id, new_description):
    
    print('\nupdating task', task_id)
    #read the JSON file, iterate through the IDs, change the description
    data = read_from_json()
    
    i = 0 
    while i < len(data) :
        extract = data[i]
        if extract['id'] == int(task_id) :
            extract['description'] = new_description
            extract['updatedAt'] = formatted_timestamp #does this timestamp need to change?
            data[i] = extract
        
        i += 1    

    write_to_json(data)

#a function to remove a task. in practice, it removes a dictionary from a list.
# read the json file, iterate through the ids to find the task/dictionary to delete,
# then pop() from the list 
def delete_from_list(task_id) :

    print('\ndeleting task', task_id, 'from list')
    data = read_from_json()

    x = 0
    while x < len(data) :
        extract = data[x]
        if extract['id'] == int(task_id) :
            data.pop(x)
        x += 1

    write_to_json(data)

#a function to change the status of the task
#read the json file, find the id and change the status
# I need to add a check for the correct status' <todo, in progress, done>
def change_status(task_id, status) :

    print('\nchanging status of task', task_id)

    data = read_from_json()

    x = 0
    while x < len(data) :
        extract = data[x]
        if extract['id'] == int(task_id) :
            extract['status'] = status
        x += 1
    
    write_to_json(data)

def end() :
    print('end of cli-task')
    global loop
    loop = False

def format_task(string_to_be_formatted):
    task = string_to_be_formatted.replace('"', '')
    return task

if __name__ == "__main__":

    valid_inputs = {
        'add' : add_to_list,
        'update' : update_list,
        'delete' : delete_from_list,
        'mark-in-progress' : change_status,
        'mark-done' :change_status,
        'list' : print_by_status ,
    }
    
    input_error_message = 'not a task-cli command, commands are:\ntask-cli add <task name>\ntask-cli update <ID> <task name>\ntask-cli delete <task ID>\ntask-cli mark-in-progress <ID>\ntask-cli mark-done <ID>\ntask-cli list <todo/in-progress/done>\nend'

    print('\nWelcome to cli task tracker....what would you like to do?')

    while (loop) :

        user_command = input("\nCommand: ")

        command_list = user_command.split(' ', 2)
        
        if command_list[0] == 'task-cli' :
            if command_list[1] in valid_inputs :
                if len(command_list) > 2 :
                    x = command_list[2]
                    valid_inputs[command_list[1]](x)
                else :
                    valid_inputs[command_list[1]]()
            else :
                print(input_error_message)
        elif command_list[0] == 'end' :
            end()
        else :
            print(input_error_message)
