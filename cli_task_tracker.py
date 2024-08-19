#cli_tasker_tracker.py
#from the roadmap.sh project suggestions page
#

def add_to_list(task):
    print('added ' + task + ' to list')
# check if there is a JSON file
#if there is get the next ID
#if there isn't a file, make 1 with ID = 1

def delete_from_list() :
    print('deleted from list')

def end() :
    print('end of cli-task')

def format_task(string_to_be_formatted):
    task = string_to_be_formatted.replace('"', '')
    return task


print('\nWelcome to cli task tracker....what would you like to do?')
loop = True

while (loop) :
    user_command = input("\ncommand: ")
    command_list = user_command.split(" ", 2)
    print(command_list)
    
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




