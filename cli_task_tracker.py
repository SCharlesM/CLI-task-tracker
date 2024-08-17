#cli_tasker_tracker.py
#from the roadmap.sh project suggestions page
#

print('\nWelcome to cli task tracker....')
loop = True

while (loop) :
    command = input('\ntask-cli:')

    if command == 'add' :
        print('add to JSON file')

    elif command == 'delete' :
        print('deleting from JSON file')
    
    elif command == 'end' :
        break

    else :
        print('incorrect input')

print('end of cli-task')