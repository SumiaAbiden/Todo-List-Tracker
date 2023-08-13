def show_todo_list():
    todo = open('todo.txt', 'r')
    
    i = 1
    while True:
        line = todo.readline()
        if not line:
            break
        line = line.strip()
        print("(" + str(i) + ") " + line)
        i += 1
        
    todo.close()


def add_to_todo_list(item):
    todo = open('todo.txt', 'a')
    todo.write("\n" + item)
    todo.close()


def remove_from_todo_list(num):
    todo = open('todo.txt', 'r')
    new_todo = ''
    index = 1
    
    for line in todo:
        if index != num:
            new_todo += line
        index += 1
        
    todo.close()
    todo = open('todo.txt', 'w')
    todo.write(new_todo)
    todo.close()

        
    



def main():
    '''
    This is the main function!
    It handles the command loop logic, and calls the other functions when necessary.
    '''
    command = ''
    while command != 'exit':
        command = input('show, add, remove, or exit? ')
        if command == 'show':
            show_todo_list()
        elif command == 'add':
            task = input('What task needs to be added? ')
            add_to_todo_list(task)
        elif command == 'remove':
            number = int(input('What item number should be removed? '))
            remove_from_todo_list(number)
    print('Goodbye!')

  
main()