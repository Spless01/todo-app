import functions
import time

while True:
    real_time=time.strftime("%B, %A %d, %Y %H:%M:%S")
    print(f"It`s: {real_time}")
    user_action = input("Type: add/show/edit/complete/exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo+'\n')

        functions.write_todos(todos)

        print("New item is added to your todo list")

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')

            row = f"{index + 1}. {item}"

            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()
            new_todo = input("type new todo: ")
            todos[number] = new_todo+"\n"

            functions.write_todos(todos)
        except Exception as ex:
            print(f"ERROR!!!\n{ex}")
            print("Your command is not valid, please try again")
            continue
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()
            index = number-1
            to_do_to_remove = todos[index].strip("\n")
            todos.pop(index)

            functions.write_todos(todos)
            message = f"Your program delete - {to_do_to_remove}"
            print(message)
        except Exception as ex:
            print(f"ERROR!!!\n{ex}")
            print("Your command is not valid, please try again")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is no valid")
print("your program end. Bye!")
