import os
import sys
from datetime import date


def readtodo():
    with open('todo.txt', 'r+') as todofile:
         todoarray= todofile.readlines()
    return todoarray

def readdone():
    try:
        with open('done.txt', 'r+') as donefile:
             todoarray= donefile.readlines()
        return todoarray
    except:
    	print("There are no pending todos!")

def savetodo(todoarray):
    with open('todo.txt', 'a+') as todofile:
        for item in todoarray:
            todofile.write("%s\n" % item)
    return 0

def writetodo(todoarray):
    try:
        with open('todo.txt', 'w+') as todofile:
            for item in todoarray:
                todofile.write("%s" % item)
    except:
    	print("There are no pending todos!")
    return 0

def writedone(donearray):
    with open('done.txt', 'w+') as donefile:
        for item in donearray:
            donefile.write("%s" % item)
    return 0


def todo(arg):
    if (len(arg) == 1 or arg[1] == "help"):
        print('Usage :-\n$ ./todo add "todo item"  # Add a new todo\n$ ./todo ls               # Show remaining todos\n$ ./todo del NUMBER       # Delete a todo\n$ ./todo done NUMBER      # Complete a todo\n$ ./todo help             # Show usage\n$ ./todo report           # Statistics')

    elif (arg[1] == "ls"):
        todoarray = readtodo()
        for index in range(len(todoarray)):
            print("[" + str(len(todoarray) - index) + "] " + (todoarray[len(todoarray) - (index+1)].rstrip("\n")))

    elif (arg[1] == "add"):
        if(arg[2]):
            todoarray = []
            todoarray.append(arg[2])
            savetodo(todoarray)
            print('Added todo: "{}"'.format(arg[2]))
        else:
        	print("Error: Missing todo string. Nothing added!")

    elif(arg[1] == "del"):
        if(arg[2]):
            try:
                if(arg[2] != 0):
                    todoarray = readtodo()
                    todoarray.pop(int(arg[2])-1)
                    print("Deleted todo #{}".format(arg[2]))
                    writetodo(todoarray)
                else:
                	print("Error: todo #0 does not exist. Nothing to delete.")
            except:
                print("Error: todo #{} does not exist. Nothing deleted.".format(arg[2]))
        else:
        	print("Error: Missing NUMBER for deleting todo.")

    elif(arg[1] == "done"):
        if(arg[2]):
            try:
                todoarray = readtodo()
                donearray = readdone()
                today = (date.today()).strftime("%Y-%m-%d")
                done = todoarray.pop(int(arg[2])-1)
                donearray.append("x " + today + " " + done)
                writetodo(todoarray)
                writedone(donearray)
                print("Marked todo #{} as done.".format(arg[2]))
            except:
                print("Error: todo #{} does not exist.".format(arg[2]))
        else:
        	print("Error: Missing NUMBER for marking todo as done.")

    elif(arg[1] == "report"):
        today = (date.today()).strftime("%Y-%m-%d")
        todoarray = readtodo()
        donearray = readdone()
        print("{} Pending : {} Completed : {}".format(today, len(todoarray), len(donearray)))


todo(sys.argv)
