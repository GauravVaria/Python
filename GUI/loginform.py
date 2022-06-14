# Write tkinter program to design a login form and validate the credentials
import tkinter as tk
window = tk.Tk()
window.geometry('1920x1080')
window.title("Login Form")
username = 'Gaurav'
password = 'Varia'
enter_label = tk.Label(text="Enter Username and Password")
enter_label.pack()
user_label = tk.Label(text = "Username")
user_label.pack()
entry1 = tk.Entry()
entry1.pack()
pass_label = tk.Label(text = "Password")
pass_label.pack()
entry2 = tk.Entry()
entry2.pack()
def check():
    input_username = entry1.get()
    input_password = entry2.get()
    if input_username == username and input_password == password:
        enter_label.configure(text = 'Valid Credentials')
    else:
        enter_label.configure(text = 'Invalid Credentials')
button = tk.Button(text = "Check", command = check)
button.pack()
user_textbox = tk.Text()
window.mainloop()