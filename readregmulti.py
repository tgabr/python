# importing required module
### this script used to read  security agents registry  information ###
import winreg as wrg
import os

# Store location of HKEY_CURRENT_USER
location = wrg.HKEY_LOCAL_MACHINE
  
# Storing path in soft

soft={}
soft[0]={}
soft[1]={}
soft[0]['keyname']='SYSTEM\\CurrentControlSet\\Services\\BDProtSrv\\'
soft[0]['key']=wrg.OpenKeyEx(location,r"SYSTEM\\CurrentControlSet\\Services\\BDProtSrv\\")
soft[1]['keyname']='SYSTEM\\CurrentControlSet\\Services\\WinDefend\\'
soft[1]['key']=wrg.OpenKeyEx(location,r"SYSTEM\\CurrentControlSet\\Services\\WinDefend\\")

#soft.append(wrg.OpenKeyEx(location,r"SYSTEM\\CurrentControlSet\\Services\\BDProtSrv\\"))
#soft.append(wrg.OpenKeyEx(location,r"SYSTEM\\CurrentControlSet\\Services\\WinDefend\\"))
size = 2       #number of loops 
x=0
for x in range(size):
     soft[x]['displayname']=wrg.QueryValueEx(soft[x]['key'],"DisplayName")
     soft[x]['imagepath']=wrg.QueryValueEx(soft[x]['key'],"ImagePath")
# reading values in value_1 and value_2

#value_1=[]
#value_2=[]
x=0
for x in range(size):
    print("\nkey:\t\t\t" , soft[x]['keyname'] , "\ndisplayname:\t\t" , soft[x]['displayname'] , "\nimagepath:\t\t" , soft[x]['imagepath'])

  
os.system("pause")
  
# Printing values
#print("\nDisplayName:",value_1,"\n")
#print("\nImagePath:",value_2,"\n")
