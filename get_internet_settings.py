### python script to display internet settings ######
import os
import winreg as wrg
hKey = wrg.OpenKey(wrg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings")

try:
    count = 0
    while 1:
        name, value, type = wrg.EnumValue(hKey, count)
        print (name , " : " , value),
        count = count + 1
except WindowsError as err:
    print(err)
    pass
os.system("pause")