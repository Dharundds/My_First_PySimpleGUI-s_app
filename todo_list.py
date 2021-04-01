import PySimpleGUI as sg


def add():
    item = values['do']
    todo.append(item)
    window.FindElement('items').Update(values=todo)
    window.FindElement('do').Update("")


def delete():
    item = values['items'][0]
    todo.remove(item)
    window.FindElement('items').Update(values=todo)


def edit():
    item = values['items'][0]
    todo.remove(item)
    window.FindElement('items').Update(values=todo)
    window.FindElement('do').Update(item)
    window.FindElement('add_save').Update("save")
    if event == "add_save":
        window.FindElement('add_save').Update("Add")


todo = []

layout = [
    [sg.InputText('', size=(40, 1), font=('Arial', 16), key='do'),
     sg.Button("Add", font=('Arial', 16), key="add_save")],
    [sg.Listbox(values=todo, size=(40, 10), font=('Arial', 16), key='items'), sg.Button('Delete', font=(
        'Arial', 16), key="delete"), sg.Button('Edit', font=('Arial', 16), key="edit")]
]

window = sg.Window("ToDO App", layout)

while True:
    event, values = window.Read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'add_save':
        add()
    elif event == 'delete':
        delete()
    elif event == 'edit':
        edit()
