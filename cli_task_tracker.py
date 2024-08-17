#cli_tasker_tracker.py
#from the roadmap.sh project suggestions page
#

def add_to_list():
    print('added to list')

def delete_from_list() :
    print('deleted from list')

def end() :
    print('end of cli-task')

print('\nWelcome to cli task tracker....')
loop = True

while (loop) :
    user_command = input('\ntask-cli:')
    command_list = [user_command]
    print(command_list)

    if command_list[0] == 'add' :
        #print('add to JSON file')
        add_to_list()

    elif user_command == 'delete' :
        #print('deleting from JSON file')
        delete_from_list()
    
    elif user_command == 'end' :
        end()
        break

    else :
        print('incorrect input')


