import functions
import PySimpleGUI as Sg


label = Sg.Text("Type in a to-do:")
input_box = Sg.InputText(tooltip="enter text", key='todo')
add_button = Sg.Button("Add",
                       button_color='#d5f6ff',
                       border_width=2,
                        )
lst = Sg.Listbox(values=functions.get_todos(),
                 size=(50, 10),
                 font=('Arial Bold', 14),
                 enable_events=True,
                 key='todos')

edit_button = Sg.Button("Edit", key='Edit')


window = Sg.Window("My To-Do app",
                   layout=[[label, input_box, add_button], [lst, edit_button]],
                   font=('Arial', 20),)


while True:
    event, values = window.read()
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
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case Sg.WIN_CLOSED:
            break


window.close()