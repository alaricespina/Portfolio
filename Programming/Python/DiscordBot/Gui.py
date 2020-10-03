import sys
import os
import tkinter as tk

#From filename import funcname

from ServerOpen import ServerOpen

#FOR OPENING ON COMMAND: function from file
def server_on():
    ServerOpen()

def server_off():
    #FOR OPENING OFF COMMAND: Replace with function from file
    os.system ('tkinter.filedialog.askopenfilename')

def restart_server():
    #FOR OPENING OFF COMMAND: Replace with function from file
    os.system ('tkinter.filedialog.askopenfilename')
 
def reset_stat():
    label.update_idletasks()

status = str('Server Status:' + " ") #place server status variable here
 
root = tk.Tk()
root.title("Server Controller")
root.geometry('300x300')

label = tk.Label(root, text = status, fg="black", font = ("Helvetica", 15))
label.pack()
label.place(x = '0', y='0')

reset = tk.Button(root, text='Reset Status', width=20, command= reset_stat, bg = 'pink', activebackground = 'gray', font='white')
reset.pack()
reset.place(x = '50', y ='50', height = '25', width = '150')

button1 = tk.Button(root, text='Turn On Server', width=20, command= server_on, font = 'white', bg = 'green', activebackground = 'gray')
button1.pack()
button1.place(x = '50', y ='100', height = '25', width = '200')

button2 = tk.Button(root, text='Turn Off Server', width=20, command= server_off, font = 'white', bg = 'red', activebackground = 'gray')
button2.pack()
button2.place(x = '50', y ='150', height = '25', width = '200')

button3 = tk.Button(root, text='Restart Server', width=20, command= restart_server, font = 'white', bg = 'white', activebackground = 'gray')
button3.pack()
button3.place(x = '50', y ='200', height = '25', width = '200')

root.mainloop()