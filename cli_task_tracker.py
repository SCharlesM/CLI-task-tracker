#cli_tasker_tracker.py
#from the roadmap.sh project suggestions page
#
#from datetime import datetime
from time import strftime, gmtime, localtime
import json

#task_list = []
formatted_timestamp = strftime("%X %x", localtime())       #shorten timestamp?
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
    next_id = 1
    task_list = []

    #read the data from the JSON file, if its empty append the data with index 1 and write to JSON,
    # if the file exists, find the biggest ID and append the data with the next ID/index
    data = read_from_json()
    if data == None :
        pass
    else :
        for i in data :
            max_id = i['id']

        next_id = max_id + 1
        #task_dictionary = dict(id = next_id, description = task, status = 'todo', createdAt = formatted_timestamp, updatedAt = formatted_timestamp)
        #data.append(task_dictionary)

    task_dictionary = dict(id = next_id, description = task, status = 'todo', createdAt = formatted_timestamp, updatedAt = formatted_timestamp)
    data.append(task_dictionary)
    write_to_json(data)
    print('Task added successfully (ID: ', next_id, ')')


#a function to print the task by status
#read the json file, iterate through dictionaries to find correct status and print
# *calling this causes error if the list is empty..
def print_by_status(*status_reference):

    #retrieve the JSON data 
    stripped_reference = str(status_reference).strip("(,')")
    data = read_from_json()
 
    if stripped_reference == '' :           #if empty string print all tasks
        print("\nListing all tasks...")
        print("\nTask ID, description, status, date and time created, date and time updated")
        for extract in data :
            print(extract['id'], ". ", extract['description'], ", ", extract['status'], ", ", extract['createdAt'], ". ", extract['updatedAt'])

    elif stripped_reference == ('todo' or 'in progress' or 'done') :
        print("\nListing all tasks that are status: ", stripped_reference)
        for extract in data :
            if extract['status'] == stripped_reference :
                print(extract['id'], ". ", extract['description'], ", ", extract['status'], ", ", extract['createdAt'], ". ", extract['updatedAt'])
    else :
        print("this is not a valid input, input can be 'todo' 'in progress' or 'done'")


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
