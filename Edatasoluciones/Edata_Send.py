# Escribe tu código aquí :-)
from time import sleep
from pathlib import Path
import os
import requests
import csv
from time import sleep
from datetime import datetime
import binascii
import json
from base64 import b64encode

def Token01():           
    with open('/Edatasoluciones/Token.csv',mode='r') as csvfile:
        csvreader = csv.reader(csvfile)
        rows = list(csvreader)
        for line in rows[0]:
            resultado = line
    return resultado       
            
def Token02():
    with open('/Edatasoluciones/Token.csv',mode='r') as csvfile:
        csvreader = csv.reader(csvfile)
        rows = list(csvreader)
        for line in rows[1]:
            resultado = line
    return resultado  

def convertToBinaryData(filename):
    #Convert image to binary data
    with open(filename,'rb') as file:
        binaryData = file.read()
        b = bytearray(binaryData)
    return b

def checkping():
    hostname="www.edatasoluciones.com"
    response = os.system("ping -c 1 "+hostname)
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"
    return pingstatus

URL_ValidateRequest = "https://www.edatasoluciones.com/api/ValidateRequest"
URL_SubmitVideo = "https://www.edatasoluciones.com/api/SubmitFile.ashx"

#Verificar que exista conexion a internet y el server este activo
status = checkping()
print(status)
if status == "Network Active":
    try:
        for filename in os.listdir('/Edatasoluciones/Uploads/'):
            if filename.endswith("_Thumbnail.jpg"):
                data01 = Token01()
                data02 = Token02()
                if (data01 != '' and data02 != ''):
                    Params_ValidateRequest = {'data01':data01,'data02':data02}
                    r = requests.get(url = URL_ValidateRequest ,params = Params_ValidateRequest )
                    data = r.json()
                    SubmitToken = data['result0']
                    print('data01:'+data01+' data02:'+data02)
                    if SubmitToken != "":
                        try:
                            #Quitar la extension en el nombre del archivo
                            currentfilename = os.path.splitext(filename)[0]
                            #Quitar 10 strings al final para eliminar la palabra Thumbnail en el seguimiento del nombre
                            currentfilename = currentfilename[:-10]
                            #print(currentfilename)
                                
                            with open("/Edatasoluciones/Uploads/"+currentfilename+".jpg",'rb') as File01:
                                Params_File01 = {'SubmitToken':SubmitToken,'FileType':'image',
                                                    'FileSize':'1366x768','FileTime':currentfilename}
                                r = requests.post(url = URL_SubmitVideo, params = Params_File01, files={'file':File01})  
                                print(r.content)
                                print(r.text)          
                            
                            with open("/Edatasoluciones/Uploads/"+currentfilename+"_Thumbnail.jpg",'rb') as File02:
                                Params_File02 = {'SubmitToken':SubmitToken,'FileType':'image',
                                                'FileSize':'150x150','FileTime':currentfilename}
                                r = requests.post(url = URL_SubmitVideo, params = Params_File02, files={'file':File02}) 
                                print(r.content)
                                print(r.text)
                                    
                            with open("/Edatasoluciones/Uploads/"+currentfilename+".mp4",'rb') as File03:
                                Params_File03 = {'SubmitToken':SubmitToken,'FileType':'video',
                                            'FileSize':'','FileTime':currentfilename}
                                r = requests.post(url = URL_SubmitVideo, params = Params_File03, files={'file':File03}) 
                                print(r.content)
                                print(r.text)
                        finally:
                            #Eliminar archivo fuentes de imagen y video del sistema
                            os.system("sudo rm -f /Edatasoluciones/Uploads/"+currentfilename+".mp4")
                            os.system("sudo rm -f /Edatasoluciones/Uploads/"+currentfilename+".jpg")
                            os.system("sudo rm -f /Edatasoluciones/Uploads/"+currentfilename+"_Thumbnail.jpg")
    except Exception as e:
        print("Error encontrado" + str(e))
        file = open("/Edatasoluciones/log_error.csv","a")
        file.write("Edata_Send: "+str(e)+"\n")
        file.flush()
    finally:
        #Finalizar el proceso y reinciarlo a los 15 segundos al finalizar
        print("Finalizar proceso: Send")
        sleep(10)
        os.system("sudo pkill -f Edata_Transform..py")   
        os.system("sudo python3 /Edatasoluciones/Edata_Transform.py")                        
else:
    sleep(10)
    os.system("sudo pkill -f Edata_Transform..py")   
    os.system("sudo python3 /Edatasoluciones/Edata_Transform.py")                  

