
import requests
import PySimpleGUI as sg
import tex as chat

#layout and open second window
def main():
    layout = [
    [sg.Text("Welcome to PieSimpleChat")],
    [sg.Text("Name:")], [sg.InputText(key="-username-")],
    [sg.Text("Password")], [sg.InputText(key="-password-")],
    [sg.Button("Login"), sg.Button("Exit")]
    ]

    window = sg.Window("PieSimpleChat", layout)

    while True:
        event, values = window.read()

        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Login":
           v = verify(values["-username-"],values["-password-"])
           return v
        
#open second window
def open_window():
    layout = [[sg.Text("New Window", key="new")]]
    window = chat.main_func()
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
    
#verify user and password input
def verify(u,p):
    url = "https://maadaniya-870cb-default-rtdb.europe-west1.firebasedatabase.app/users.json"
    response = requests.get(url)
    data = response.json()
    name = "placeholder"
    for key in data.keys():
        info = data[key]
        user = info["user"]
        password = info["password"]
        if user == u and password == p:
            return True
        else:
            return False

# ------------------- code -------------------

login_window = main()
if login_window == True:
    chat.main_func()
