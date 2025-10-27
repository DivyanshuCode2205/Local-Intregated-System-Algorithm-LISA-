import os

my_files = {"downloads": os.path.normpath(os.path.join(os.path.expanduser("~"), "Downloads")),
    "documents": os.path.normpath(os.path.join(os.path.expanduser("~"), "Documents")),
    "vs code":os.path.normpath(r"C:\Users\DELLS\AppData\Local\Programs\Microsoft VS Code\Code.exe"),
    "desktop": os.path.normpath(os.path.join(os.path.expanduser("~"), "Desktop")),
    "pictures": os.path.normpath(os.path.join(os.path.expanduser("~"), "Pictures")),
    "saved pictures":os.path.normpath(os.path.join(os.path.expanduser('~'), 'Pictures', 'Saved Pictures')),
    "notes": os.path.normpath(os.path.join(os.path.expanduser('~'), "Desktop", "PW Class Notes")),
    "screenshots":os.path.normpath(os.path.join(os.path.expanduser('~'), 'Pictures', 'Screenshots')),
    "c drive":os.path.normpath("C:/"), "d drive":os.path.normpath("D:/"),
    "password generator":os.path.normpath(r"D:\Python Programming\Chapter 7 Practice-set\password_generator.py")}