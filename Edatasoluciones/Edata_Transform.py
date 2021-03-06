# Escribe tu código aquí :-)
import os
from pathlib import Path
from time import sleep
from PIL import Image

try:
    for filename in os.listdir('/dev/tmp/Uploads/'):
        if filename.endswith("_Thumbnail.jpg"):
            print(currentfilename)
        elif filename.endswith(".jpg"):
            #print(os.path.splitext(filename)[0])
            try:
                currentfilename = os.path.splitext(filename)[0]
                #Verificar existencia de la imagen
                csvfile = Path("/dev/tmp/Uploads/"+currentfilename+".jpg")
                if csvfile.is_file():
                    os.system("sudo MP4Box -fps 60 -add /dev/tmp/Uploads/"+currentfilename+".h264 /dev/tmp/Uploads/"+currentfilename+".mp4")
                    os.system("sudo rm -f /dev/tmp/Uploads/"+currentfilename+".h264")
                    #Generar Thumbnail del video
                    foo = Image.open("/dev/tmp/Uploads/"+currentfilename+".jpg")
                    foo = foo.resize((150,150),Image.ANTIALIAS)
                    foo.save("/dev/tmp/Uploads/"+currentfilename+"_Thumbnail.jpg")
            except:
                    os.system("sudo rm -f /dev/tmp/Uploads/"+currentfilename+".h264")
                    os.system("sudo rm -f /dev/tmp/Uploads/"+currentfilename+".mp4")
                    os.system("sudo rm -f /dev/tmp/Uploads/"+currentfilename+".jpg")
                    os.system("sudo rm -f /dev/tmp/Uploads/"+currentfilename+"_Thumbnail.jpg")
except Exception as e:
    print("Error encontrado" + str(e))
    file = open("/Edatasoluciones/log_error.csv","a")
    file.write("*** Edata_Transform *** \n")
    file.write(str(e))
    file.flush()
finally:
    #Finalizar el proceso y reinciarlo a los 20 segundos al no existir el archivo de seguimiento
    print("Finalizar proceso: Transform")
    os.system("sudo pkill -f Edata_Send.py")
    os.system("sudo python3 /Edatasoluciones/Edata_Send.py")




