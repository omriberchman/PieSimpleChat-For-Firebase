def main_func(name):
    from cgitb import text
    import PySimpleGUI as sg
    import requests
    import time


    url = "https://maadaniya-870cb-default-rtdb.europe-west1.firebasedatabase.app/messages.json"
    sg.theme('Dark Red')
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple) #need to use time_string


    layout = [
        [sg.Text("Welcome " +name+ ","),sg.Text("Login Time : " + time_string)],
        [sg.HorizontalSeparator()],
        [sg.Multiline('', size=(50, 15), reroute_cprint=True, key='-multi-')],
        [sg.InputText(key="text",justification='l'), sg.Button("send"),sg.Button("Refresh")]
        ]
    textwindow = sg.Window("PieSimpleChat - Login", layout , icon='Images/icon.ico',element_justification='c')
    def read_messages(url):
        response = requests.get(url)
        data = response.json()
        return data



    while True:
        event,values = textwindow.read()

        if event == sg.WIN_CLOSED:
            break

        elif event == "send":
            message = values["text"]
            dict = {"name":name,"message":message,"time":time_string}
            requests.post(url,json=dict)
            sg.cprint(dict["name"],": ",dict["message"])

        elif event == "Refresh":        
            db = read_messages(url)
            for key in db.keys():
                print(db[key])
                sg.cprint(db[key]["name"],": ",str(db[key]["message"]))
