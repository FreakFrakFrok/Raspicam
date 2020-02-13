from time import sleep
from pathlib import Path
import os
import requests
from datetime import datetime
#Comentar las siguientes 2 lineas para instalaciones sin chip RTC3231
#os.system("sudo hwclock -w")
#os.system("sudo hwclock -r")
def getserial():
    #Get serial number from Raspberry
    cpuserial = ""
    try:
        f = open('/proc/cpuinfo','r')
        for line in f:
            if line[0:6] == 'Serial':
                cpuserial = line[10:26]
        f.close()
    except:
        cpuserial = ""
    return cpuserial

os.system("sudo systemctl stop Edata_Detection.service")
os.system("sudo systemctl stop Edata_Transform.service")
os.system("sudo systemctl disable Edata_Detection.service")
os.system("sudo systemctl disable Edata_Transform.service")
os.system("sudo pkill raspivid")
os.system("sudo pkill mmal-vchiq")
try:
    data01 = input("Activation Token: ")
    data02= getserial()
    #print('data01:'+data01+' data02:'+data02)
    if (data02 != '' and data01 != '' and data01 is not None):
        PARAMS = {'data01':data01,'data02':data02}
        URL = "https://www.edatasoluciones.com/api/CameraValidation"
        r = requests.get(url = URL ,params = PARAMS)
        data = r.json()
        apireturn0= data['result0']
        apireturn1= data['result1']
        #print('apireturn0:'+apireturn0+' apireturn1:'+apireturn1)
        if (apireturn0 == 'Activated'):
            #csvfile = Path("/Edatasoluciones/Token.csv")
            os.system("sudo rm -f /Edatasoluciones/Token.csv")
            file = open("/Edatasoluciones/Token.csv", "a")
            file.write(apireturn1+"\n")
            file.flush()
            os.system("sudo systemctl enable Edata_Detection.service")
            os.system("sudo systemctl enable Edata_Transform.service")
            os.system("sudo systemctl start Edata_Detection.service")
            os.system("sudo systemctl start Edata_Transform.service")
            print("Activation success")
        else:
            print("Activation door is closed")
            os.system("sudo python3 /Edatasoluciones/Edata_CamValidation.py")  
except Exception as e:
    print("Error encontrado" + str(e))
finally:
    exit()
