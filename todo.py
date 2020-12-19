import os
import sys
from datetime import date


def todo(arg):
    with open('todo.txt', 'w+') as todofile:
        todoarray = list(todofile.readlines.split("\n"))
    with open('done.txt', 'w+') as donefile:
        donearray = list(donefile.readlines.split("\n"))

    if (arg[2] == "help" or arg[2] == ""):
        print('Usage :-\n$ ./todo add "todo item"  # Add a new todo\n$ ./todo ls               # Show remaining todos\n$ ./todo del NUMBER       # Delete a todo\n$ ./todo done NUMBER      # Complete a todo\n$ ./todo help             # Show usage\n$ ./todo report           # Statistics')

    elif (arg[2] == "ls"):
        for task, index in reversed(list(enumerate(todoarray))):
            print("[{}] {}".format(index+1, task))

    elif (arg[2] == "add"):
        if(arg[3]):
            todoarray.append(arg[3])
            print("Added todo: {}".format(arg[3]))

    elif(arg[2] == "del"):
        if(arg[3]):
            try:
                todoarray.pop(arg[3]-1)
                print("Deleted todo #{}".format(arg[3]))
            except:
                print("Error: todo #{} does not exist. Nothing deleted.".format(arg[3]))

    elif(arg[2] == "done"):
        if(arg[3]):
            try:
                today = date.today()
                today = today.strftime("%Y-%m-%d")
                done = todoarray.pop(arg[3]-1)
                donearray.append("x " + today + " " + done)
                print("Marked todo #{} as done.".format(arg[3]))
            except:
                print("Error: todo #{} does not exist.".format(arg[3]))

    elif(arg[2] == "report"):
        today = date.today()
        today = today.strftime("%Y-%m-%d")
        print("{} Pending : {} Completed : {}".format(today, len(todoarray), len(donearray)))

    with open('todo.txt', 'w') as todofile:
        for item in todoarray:
            todofile.write("%s\n" % item)

    with open('done.txt', 'w') as donefile:
        for item in todoarray:
            donefile.write("%s\n" % item)


todo(sys.argv)
