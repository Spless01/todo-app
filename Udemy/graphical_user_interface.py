import functions
import PySimpleGUI as Sg
import time

Sg.theme("DarkTeal2")
clock = Sg.Text('', key='Clock')
label = Sg.Text("Type in a to-do:")

input_box = Sg.InputText(tooltip="enter text", key='todo')

add_button = Sg.Button("Add",
                       border_width=1
                       )

complete_button = Sg.Button("Complete",
                            key="Complete",
                            border_width=1,
                            )

lst = Sg.Listbox(values=functions.get_todos(),
                 size=(50, 10),
                 font=('Arial Bold', 14),
                 enable_events=True,
                 key='todos')

edit_button = Sg.Button("Edit", key='Edit',
                        border_width=1,
                        )

exit_button = Sg.Button("Exit", key="Exit",
                        border_width=1,
                        )

window = Sg.Window("My To-Do app",
                   layout=[[clock],
                           [label], [input_box, add_button],
                           [lst, edit_button, complete_button], [exit_button]],
                   font=('Arial', 20),)


while True:
    event, values = window.read(timeout=100)
    window['Clock'].update(value=time.strftime("%B, %A %d, %Y %H:%M:%S"))
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except Exception as ex:
                Sg.popup("Select item firstly!")
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                index = todos.index(todo_to_complete)
                todos.pop(index)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except Exception as ex:
                Sg.popup("Select item firstly!")
        case "Exit":
            break
        case "todos":
            window["todo"].update(value=values["todos"][0])

        case Sg.WIN_CLOSED:
            break
window.close()
