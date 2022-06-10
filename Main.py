from os import name, times
from sys import path
from tkinter import *
from tkinter import font
from tkinter import filedialog
import subprocess
import os



root=Tk()
root.title("Tafsut Compiler(T++) @Maroua_Rhita")
root.geometry("1200x600")
#root.resizable(height = None, width = None)
root.resizable(0, 0)

global open_file_name
open_file_name=False

global dir_path
dir_path=os.path.abspath(".")


def new_file():
    my_text.delete("1.0",END)
    root.title("Fichier Jdid ")
    global open_file_name
    open_file_name=False

def open_file():
    my_text.delete("1.0",END)
    global dir_path
    text_file=filedialog.askopenfilename(initialdir=dir_path,title="Open File",filetypes=(("Text","*.txt"),("Python file","*.py")))
    if text_file:
        global open_file_name
        open_file_name=text_file
    name=text_file
    name=name.replace(dir_path,"")
    root.title(f'{name} ')
    text_file=open(text_file,'r')
    stuff=text_file.read()
    my_text.insert(END,stuff)
    text_file.close()

def save_file():
    global open_file_name
    if open_file_name:
        text_file=open(open_file_name,'w')
        text_file.write(my_text.get(1.0,END))
        text_file.close()
    else:
        global dir_path
        text_file=filedialog.asksaveasfilename(defaultextension=".*",initialdir=dir_path,title="Save File",filetypes=(("Text","*.txt"),("Python file","*.py")))
        if text_file:
            name=text_file
            name=name.replace(dir_path,"")
            root.title(f'{name} ') 
            text_file=open(text_file,'w')
            text_file.write(my_text.get(1.0,END))
            
            open_file_name=name
            text_file.close()
            

def execute_file():
    if open_file_name:
        proc = subprocess.Popen('cmd.exe', stdin = subprocess.PIPE, stdout = subprocess.PIPE)
        os.chdir(dir_path)
        comd='python TParser.py {}   '.format(open_file_name)
        comd=comd.encode('utf-8')
        proc.stdin.write(comd)
        stdout = proc.communicate(proc.stdout.readline())
        execute_text.insert(END,stdout)



my_frame=Frame(root)
my_frame.pack(pady=5)

text_scroll=Scrollbar(my_frame)
text_scroll.pack(side=RIGHT,fill=Y)

my_text=Text(my_frame,width=1200,height=20,font=("verdana",11), background="#EBE8F9", selectbackground="#C4E5F6",selectforeground="black",undo=True,yscrollcommand=text_scroll.set)
my_text.pack()


execute_text=Text(my_frame,width=1200,height=15,font=("verdana",11),foreground="white",background="#4B0082",selectbackground="#DED8FB",selectforeground="white",undo=True,yscrollcommand=text_scroll.set)
execute_text.pack()

text_scroll.config(command=my_text.yview)
text_scroll.config(command=execute_text.yview)

my_menu=Menu(root)
root.config(menu=my_menu)

file_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Fichier",menu=file_menu)
file_menu.add_command(label="Jdid",command=new_file)
file_menu.add_command(label="Ft7",command=open_file)
file_menu.add_command(label="Sjl",command=save_file)

execute_menu=Menu(my_menu,tearoff=False)
my_menu.add_command(label="Tb9",command=execute_file)




root.mainloop()