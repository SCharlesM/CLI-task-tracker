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
    command = input('\ntask-cli:')

    if command == 'add' :
        #print('add to JSON file')
        add_to_list()

    elif command == 'delete' :
        #print('deleting from JSON file')
        delete_from_list()
    
    elif command == 'end' :
        end()
        break

    else :
        print('incorrect input')


