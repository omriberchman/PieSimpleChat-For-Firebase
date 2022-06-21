import json
import requests
import PySimpleGUI as sg

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
            verify(values["-username-"],values["-password-"])
            window.close()
            open_window()
        
#open second window
def open_window():
    layout = [[sg.Text("New Window", key="new")]]
    window = sg.Window("Second Window", layout, modal=True)
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

    for key in data.keys():
        info = data[key]
        user = info["user"]
        password = info["password"]
        if user == u and password == p:
            print("login succesful")
        
            
            


            



if __name__ == "__main__":
    main()

