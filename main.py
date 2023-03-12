from tkinter import *
import os, shutil, datetime, distutils

SAVES_LIST = os.listdir(r'SAVES\SAVES')
SAVES_LISTB = os.listdir(r'SAVES\SAVES\\')

def switch_SAVE(path):
    clear_SAVE()

    TARGET = os.path.expandvars(r'%LOCALAPPDATA%\UNDERTALE\file0')
    FILE = 'SAVES\SAVES\\' + path + '\\file0'
    shutil.copyfile(FILE, TARGET)

    TARGET = os.path.expandvars(r'%LOCALAPPDATA%\UNDERTALE\undertale.ini')
    FILE = 'SAVES\SAVES\\' + path + '\\undertale.ini'
    shutil.copyfile(FILE, TARGET)

    try:
        TARGET = os.path.expandvars(r'%LOCALAPPDATA%\UNDERTALE\file9')
        FILE = 'SAVES\SAVES\\' + path + '\\file9'
        shutil.copyfile(FILE, TARGET)
    except:
        pass

    try:
        TARGET = os.path.expandvars(r'%LOCALAPPDATA%\UNDERTALE\file8')
        FILE = 'SAVES\SAVES\\' + path + '\\file8'
        shutil.copyfile(FILE, TARGET)
    except:
        pass

def backup():
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    times = str(datetime.datetime.now())
    times = times.replace(':', '-')
    patha = f"SAVES\BACKUPS\\{times}"
    os.makedirs(patha)

    TARGET = os.path.expandvars(r'%LOCALAPPDATA%\UNDERTALE\file9')
    TARGET = os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'UNDERTALE')
    distutils.dir_util.copy_tree(TARGET, patha)

def clear_extra():
    try:
        TARGET = os.path.expandvars(r'%LOCALAPPDATA%\UNDERTALE\file8')
        os.remove(TARGET)
        TARGET = os.path.expandvars(r'%LOCALAPPDATA%\UNDERTALE\system_information_962')
        os.remove(TARGET)
        TARGET = os.path.expandvars(r'%LOCALAPPDATA%\UNDERTALE\system_information_963')
        os.remove(TARGET)
    except:
        pass

def clear_SAVE():
    backup()
    clear_extra()

    try:
        TARGET = os.path.expandvars(r'%LOCALAPPDATA%\UNDERTALE\file9')
        os.remove(TARGET)
        TARGET = os.path.expandvars(r'%LOCALAPPDATA%\UNDERTALE\file0')
        os.remove(TARGET)
        TARGET = os.path.expandvars(r'%LOCALAPPDATA%\UNDERTALE\undertale.ini')
        os.remove(TARGET)
    except:
        pass


LOADED = os.listdir(os.path.expandvars(r'%LOCALAPPDATA%\UNDERTALE'))

root = Tk()
root.title("Flowey's SAVE Loader")
root.geometry("500x320")
icon = PhotoImage(file='ASSETS\Pictures\icon.png')
root.iconphoto(True, icon)
root.config(bg="black")

for i in SAVES_LIST:
    Button(text=i, bg="black", fg="#ff8903", command=lambda i=i: switch_SAVE(i)).grid(column=0)
Button(text="CLEAR SAVE", bg="black", fg="#ff8903", command=lambda: clear_SAVE()).grid(row=0, column=1)
Button(text="BACKUP SAVE", bg="black", fg="#ff8903", command=lambda: backup()).grid(row=1, column=1)
Label(text="LOADED FILES IN %APPDATALOCAL%\\UNDERTALE", bg="black", fg="#ff8903").grid(row=0, column=2)
for i in LOADED:
    Label(text=i, bg="black", fg="#ff8903").grid(column=2)


root.mainloop()