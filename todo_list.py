import PySimpleGUI as sg


def add():
    item = values['do']
    todo.append(item)
    window.FindElement('items').Update(values=todo)
    with open('list.txt', 'a') as f1:
        f1.writelines('\n'+item)
    window.FindElement('do').Update("")


def delete():
    item = values['items'][0]
    todo.remove(item)
    with open('list.txt', 'r') as f2:
        lines = f2.readlines()
    with open('list.txt', 'w') as f:
        for line in lines:
            if not (line.startswith(str(item))):
                f.write(line)
    window.FindElement('items').Update(values=todo)


def edit():
    item = values['items'][0]
    todo.remove(item)
    window.FindElement('items').Update(values=todo)
    window.FindElement('do').Update(item)
    window.FindElement('add_save').Update("save")
    if event == "add_save":
        window.FindElement('add_save').Update("Add")
    with open('list.txt', 'r') as f2:
        lines = f2.readlines()
    with open('list.txt', 'w') as f:
        for line in lines:
            f.write(line)


def remove_empty_lines():
    with open('list.txt', 'r') as f3:
        lines = f3.readlines()
    with open('list.txt', 'w') as f4:
        line = str(lines).split("\n")
        non_empty = [line for line in lines if line.strip() != ""]
        a = ""
        for line in non_empty:
            a += line+'\n'
        f4.write(a)


todo = []

layout = [
    [sg.InputText('', size=(40, 1), font=('Arial', 16), key='do'),
     sg.Button("Add", font=('Arial', 16), key="add_save")],
    [sg.Listbox(values=todo, size=(40, 10), font=('Arial', 16), key='items'), sg.Button('Delete', font=(
        'Arial', 16), key="delete"), sg.Button('Edit', font=('Arial', 16), key="edit")]
]
window = sg.Window("ToDO App", layout)
with open('list.txt', 'r')as f:
    for lines in f:
        line_stripper = lines.strip()
        tasks = line_stripper.split()
        todo.append(tasks)


while True:
    event, values = window.Read()
    if event == sg.WINDOW_CLOSED:
        remove_empty_lines()
        break
    if event == 'add_save':
        add()
    elif event == 'delete':
        delete()
        remove_empty_lines()
    elif event == 'edit':
        edit()
