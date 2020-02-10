# Raspicam

Raspicam code will help you if you own a Raspberry Pi with an integrated camera to record actions based on movement detection. The results of these detections will be visible through the raspicam website. The good news: it's totally free for a camera with 48 hours of historical recording.

If you feel you want to try it, you have two options to start using Raspicam on your Raspberry Pi

Option 1<br/>
What do you need:
- 32gb micro sd
- Raspberry Pi with camera
- Internet connection always available

Instructions:
- Register your account at https://www.edatasoluciones.com/raspicam/Login
- Obtain your Raspicam Activation Key once you login for the first time.
- Download the 32GB image of Raspbian with the preconfiguration of the Raspicam python code from one of the following URL:
    - https://www.edatasoluciones.com/raspicam/media/32GB_Raspicam.img
- Install Raspbicam image on your 32GB Micro SD Card. If you use Windows then you can use Win32DiskImager for this task:
    - http://sourceforge.net/projects/win32diskimager/files/latest/download
- Make sure your Raspberry Pi has an internet connection
- Make sure you have a camera installed and enabled on your Raspberry Pi
- From a console window run the following script: "sudo python3 /Edatasoluciones/Edata_CamValidation.py"
- You will be asked to insert your Raspicam Activation Key
- You're ready to start browsing the movement detection on our website

Option 2<br/>
What do you need:
- Raspberry Pi with camera
- Internet connection always available

Instructions:
- Register your account at https://www.edatasoluciones.com/raspicam/Login
- Obtain your Raspicam Activation Key once you login for the first time.
- Download Edatasoluciones folder from Github (https://github.com/FreakFrakFrok/Raspicam) and save it on a USB stick
- Install Raspbian OS on your Raspberry Pi
- Make sure your Raspberry Pi has an internet connection
- From a console window run the following script to enable your camera: "sudo raspi-config"
- Go to interfacing options and make sure the camera option is enabled
- From a console window install M4Box: "sudo apt-get install -y gpac"
- From a console window run the following script to open a file explorer with admin privileges: "sudo pcmanfm"
- Within the file explorer copy Edatasoluciones folder from your USB stick and paste it on root folder: "/" 
- Within the file explorer move files with .service extension from "/Edatasoluciones/" and paste them on the following folder: "/lib/systemd/system/"
- From a console window run the following script: "sudo python3 /Edatasoluciones/Edata_CamValidation.py"
