import functions
import PySimpleGUI as Sg


label = Sg.Text("Type in a to-do:")
input_box = Sg.InputText(tooltip="enter text")
add_button = Sg.Button("add")
window = Sg.Window("My To-Do app", layout=[[[label], input_box, add_button]])

window.read()
window.close()