"""
cli_tasker_tracker.py

A project idea from roadmap.sh project suggestions page

A simple program to manage tasks, functionality to add, delete, update and change status of tasks

"""
from time import strftime, localtime
import json

Loop = True

def write_to_json(input_list) :
    """function to append the list of dictionaries to JSON file list_data.json"""

    with open("list_data.json", "w", encoding="utf-8") as output_file:
        json.dump(input_list, output_file, indent = 2)


def read_from_json() :
    """function to return the list of dictionaries from list_data.json"""

    output_list = []
    with open('list_data.json', 'r', encoding="utf-8") as openfile:
        try:
            output_list = json.load(openfile)
        except  json.decoder.JSONDecodeError:
            print ('this is JSON decode error, is the JSON file empty?')

    if output_list == [] :
        return None
    return output_list


def add_to_list(task):
    """function to generate a dictionary with id, desc, status, and timestamps"""
    max_id = 0
    next_id = 1

    #if the JSON file is empty, id = 1. Otherwise find the biggest id and + 1
    data = read_from_json()
    if data is None :
        data = []
    else :
        for i in data :
            max_id = i['id']
        next_id = max_id + 1

    formatted_timestamp = strftime("%X %x", localtime())
    task = task.replace('"', '')
    task_dictionary = {
        'id' : next_id,
        'description' : task,
        'status' : 'todo',
        'created_at' : formatted_timestamp,
        'updated_at' : formatted_timestamp
    }
    data.append(task_dictionary)
    write_to_json(data)
    print('Task added successfully (ID: ', next_id, ')')

def print_by_status(*status_reference):
    """function to print all tasks, or task with given status"""

    valid_status = ('todo', 'done', 'in-progress')
    stripped_reference = str(status_reference).strip("(,')")
    data = read_from_json()

    if stripped_reference == '' :           #if empty string print all tasks
        print("\nListing all tasks...")
    elif stripped_reference in valid_status :
        print("\nListing all tasks that are status: ", stripped_reference)
    else :
        print("this is not a valid input, input should be 'todo', 'in-progress' or 'done'")

    print("\nTask ID, description, status, date and time created, date and time updated")
    for extract in data :
        for key, value in extract.items() :
            if stripped_reference == '' :
                print(value, " ", end="")
                if key == 'updated_at' :
                    print('')
            elif extract['status'] == stripped_reference :
                print(value, " ", end="")

def update_list(task_id, new_description):
    """function to change the description with the a given id"""
    print('\nupdating task', task_id)
    data = read_from_json()

    i = 0
    while i < len(data) :               #remove while Loop
        extract = data[i]
        if extract['id'] == int(task_id) :
            extract['description'] = new_description
            formatted_timestamp = strftime("%X %x", localtime())
            extract['updated_at'] = formatted_timestamp 
            data[i] = extract
        i += 1

    write_to_json(data)

def delete_from_list(task_id) :
    """function to remove the dictionary from the list with given id"""
    print('\ndeleting task', task_id, 'from task list')
    data = read_from_json()

    for item in data :
        if item['id'] == int(task_id) :
            data.pop()
    write_to_json(data)


def change_status(task_id, status) :
    """function to change the status of the task from 'todo' to 'in-progress' or 'done'"""

    print('\nchanging status of task', task_id)
    data = read_from_json()
    for entry in data :
        if entry['id'] is int(task_id) :
            entry['status'] = status
            entry['updated_at'] = strftime("%X %x", localtime())
    write_to_json(data)

def end() :
    """function to end the program by making the Loop False"""

    print('end of cli-task')
    global Loop
    Loop = False

def format_task(string_to_be_formatted):
    """function to remove speech marks"""
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
    error_message = ('\nNot a valid task-cli command, commands are:\n\ntask-cli add <task name>'
        '\ntask-cli update <ID> <task name>\ntask-cli delete <task ID>\ntask-cli mark-in-progress'
        ' <ID>\ntask-cli mark-done <ID>\ntask-cli list <todo/in-progress/done>\nend')

    print('\nWelcome to cli task tracker....what would you like to do?')

    while Loop :
        user_command = input("\nCommand: ")
        split_input_list = user_command.split(' ', 2)
        
        if split_input_list[0] == 'task-cli' :
            match split_input_list[1] :
                case 'add':
                    add_to_list(split_input_list[2])
                case 'update' :
                    new_split = split_input_list[2].split('"')
                    task_id = new_split[0].strip()
                    if task_id.isnumeric() :
                        update_list(task_id, new_split[1])
                    else :
                        print(error_message)
                case 'delete' :
                    print('delete function')
                case 'mark-in-progress' :
                    print('mark-in-progress')
                case 'mark-done' :
                    print('mark done')
                case 'list' :
                    #print('list')
                    if len(split_input_list) > 2 :
                        print_by_status(split_input_list[2])
                    else :
                        print_by_status()
                case _:
                    print(error_message)
        elif split_input_list[0] == 'end' :
            end()
        else :
            print(error_message)     


    """
    while Loop :

        user_command = input("\nCommand: ")
        split_input_list = user_command.split(' ', 2)

        if split_input_list[0] == 'task-cli' :

            if split_input_list[1] in valid_inputs :

                if split_input_list[1] == 'update' :
                    x, y = split_input_list[2].split(' ', 1)
                    y = y.replace('"', '')
                    update_list(x,y)            #need to remove '"' from the new description

                elif split_input_list[1] == 'list' :
                    if len(split_input_list) > 2 :
                        x = split_input_list[2]
                        valid_inputs[split_input_list[1]](x)
                    else :
                        valid_inputs[split_input_list[1]]()

                elif split_input_list[1] == 'delete' :
                    x = split_input_list[2]
                    delete_from_list(x)

                elif split_input_list[1] == 'mark-in-progress' :
                    index = split_input_list[2]
                    change_status(index, 'in-progress')

                elif split_input_list[1] == 'mark-done' :
                    index = split_input_list[2]
                    change_status(index, 'done')

                elif split_input_list[1] == 'add' :
                    x = split_input_list[2]
                    valid_inputs[split_input_list[1]](x)
                else :
                    print('not in valid_inputs')
            else :
                print(error_message)
        elif split_input_list[0] == 'end' :
            end()
        else :
            print(error_message)
    """