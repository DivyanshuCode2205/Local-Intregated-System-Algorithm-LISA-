import os

my_files = {"downloads": os.path.normpath("D:\Downloads"),
    "documents": os.path.normpath("D:\Documents"),
    "vs code":os.path.normpath(r"C:\Users\Divyanshu xd\AppData\Local\Programs\Microsoft VS Code\Code.exe"),
    "quick share":os.path.normpath(r"C:\Program Files\Google\NearbyShare\nearby_share.exe"),
    "desktop": os.path.normpath(os.path.join(os.path.expanduser("~"), "Desktop")),
    "pictures": os.path.normpath("D:\Pictures"),
    "saved pictures":os.path.normpath(os.path.join("D:\Pictures", 'Saved Pictures')),
    "screenshots":os.path.normpath(os.path.join("D:\Pictures", 'Screenshots')),
    "wallpapers":os.path.normpath(os.path.join("D:\Pictures", "Wallpapers")),
    "c drive":os.path.normpath("C:/"), "d drive":os.path.normpath("D:/"),
    "password generator":os.path.normpath(r"D:\Python Programming\Chapter 7 Practice-set\password_generator.py")}