import os

my_files = {"downloads": os.path.normpath(os.path.join(os.path.expanduser("~"), "Downloads")),
    "documents": os.path.normpath(os.path.join(os.path.expanduser("~"), "Documents")),
    "vs code":os.path.normpath(r"C:\Users\DELLS\AppData\Local\Programs\Microsoft VS Code\Code.exe"),
    "desktop": os.path.normpath(os.path.join(os.path.expanduser("~"), "Desktop")),
    "pictures": os.path.normpath(os.path.join(os.path.expanduser("~"), "Pictures")),
    "saved pictures":os.path.normpath(os.path.join(os.path.expanduser('~'), 'Pictures', 'Saved Pictures')),
    "screenshots":os.path.normpath(os.path.join(os.path.expanduser('~'), 'Pictures', 'Screenshots')),
    "c drive":os.path.normpath("C:/"), "d drive":os.path.normpath("D:/")}