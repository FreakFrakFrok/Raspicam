# Escribe tu código aquí :-)
import os
from datetime import datetime
from time import sleep
from PIL import Image, ImageChops
import math
import shutil
#Comentar las siguientes 2 lineas para instalaciones sin chip RTC3231
#os.system("sudo hwclock -s")
#os.system("sudo hwclock -r")

def image_entropy(img):
    """calculate the entropy of an image"""
    # this could be made more efficient using numpy
    histogram = img.histogram()
    histogram_length = sum(histogram)
    samples_probability = [float(h) / histogram_length for h in histogram]
    return -sum([p * math.log(p, 2) for p in samples_probability if p != 0])

try:
    os.system("sudo raspistill -n -ex sports -t 500 -w 640 -h 480 -q 10 -th none -o /Edatasoluciones/Detection/MDetection1.jpg")
    img1 = Image.open('/Edatasoluciones/Detection/MDetection1.jpg').convert('LA')
    img2 = img1
    while True:
        # No Difference = 1
        # Small Difference = 5
        # Large Difference = 8
        img = ImageChops.difference(img1,img2)
        x = image_entropy(img)
        print(x)
        #img = img.convert('RGB')
        #img.save("/Edatasoluciones/Detection/Difference.jpg")
        if x > 5.2:
            try:
                #Obtener el tiempo en instalaciones con I2C modulo RTC3231 sin internet
                time = str(os.system("sudo hwclock -r").strftime('%Y_%m_%d_%H_%M_%S'))
            except:
                #Obtener el tiempo en instalaciones con internet siempre activo
                time = str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))
            #print(time)
            print("Start Raspi Image")
            os.system("sudo raspistill -n -ex sports -t 300 -w 1366 -h 768 -q 10 -th none -o /Edatasoluciones/Detection/MDetection2.jpg")
            print("Start Raspi Video")
            os.system("sudo raspivid -n -ex sports -w 1280 -h 720 -fps 60 --bitrate 2100000 -t 60000 -o /Edatasoluciones/Uploads/"+time+".h264")
            
            shutil.move("/Edatasoluciones/Detection/MDetection2.jpg","/Edatasoluciones/Uploads/"+time+".jpg")
            #print("Finalizado: "+ str(datetime.now().strftime('%Y/%m/%d %H:%M:%S')))

            os.system("sudo raspistill -n -ex sports -t 300 -w 640 -h 480 -q 10 -th none -o /Edatasoluciones/Detection/MDetection2.jpg")
            img2 = Image.open('/Edatasoluciones/Detection/MDetection2.jpg').convert('LA')
            img1 = img2
            
            #os.system("sudo pkill raspivid")
            #os.system("sudo pkill mmal-vchiq")
        else:
            os.system("sudo raspistill -n -ex sports -t 300 -w 640 -h 480 -q 10 -th none -o /Edatasoluciones/Detection/MDetection1.jpg")
            img1 = Image.open('/Edatasoluciones/Detection/MDetection1.jpg').convert('LA')
            #os.system("sudo pkill raspistill")
            #os.system("sudo pkill mmal-vchiq")

except Exception as e:
    print("Error encontrado" + str(e))
    file = open("/Edatasoluciones/log_error.csv","a")
    file.write("*** Edata_Detection *** \n")
    file.write(str(e))
    file.flush()
finally:
    print("Reiniciando en 5 min")
    sleep(300)
    os.system("sudo reboot")

