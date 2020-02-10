# Raspicam

Raspicam code will help you if you own a Raspberry Pi with an integrated camera to record actions based on movement detection. The results of these detections will be visible through the raspicam website. The good news: it's totally free for a camera with 48 hours of historical recording.

If you feel you want to try it, you have two options to start using Raspicam on your Raspberry Pi<br/><br/>
Option 1<br/>What do you need:
- Raspberry Pi with camera
- Internet connection always available

Instructions:
- Register your account at https://www.edatasoluciones.com/raspicam/registration
- Obtain your Raspicam Activation Key once you login for the first time at https://www.edatasoluciones.com/raspicam/login
- Download Edatasoluciones folder from Github (https://github.com/FreakFrakFrok/Raspicam) and save it on a USB stick
- Install Raspbian OS on your Raspberry Pi
- After finishing the installation and turning on your raspberry, make sure you have your Internet connection already set
- From a console window run the following script to enable your camera: "sudo raspi-config". On your Raspberry configuration go to interfacing options and make sure camera option is enabled
- From a console window install M4Box: "sudo apt-get install -y gpac"
- From a console window run the following script to open a file explorer with admin privileges: "sudo pcmanfm"
- Within the file explorer copy Edatasoluciones folder from your USB stick and paste it on root folder: "/" 
- Within the file explorer move files with .service extension from "/Edatasoluciones/" and paste them on the following folder: "/lib/systemd/system/"
- From a console window run the following script: "sudo python3 /Edatasoluciones/Edata_CamValidation.py"
- You will be asked to insert your Raspicam Activation Key
- You're ready to start browsing the movement detection on the website:<br/<br/>

Option 2<br/>What do you need:
- Raspberry Pi with camera
- Internet connection always available
- 32GB Micro SD

Instructions:
- Register your account at https://www.edatasoluciones.com/raspicam/registration
- Obtain your Raspicam Activation Key once you login for the first time at https://www.edatasoluciones.com/raspicam/login
- Download the 32GB image of Raspbian with the preconfiguration of the Raspicam python code from one of the following URL:
    - https://www.edatasoluciones.com/raspicam/media/32GB_Raspicam.img
    - https://drive.google.com/drive/folders/14nZC6Qvx1dawEartg2oVAVSE1XjW3wtC?usp=sharing
- Install Raspicam image on your 32GB Micro SD Card. If you use Windows then you can use Win32DiskImager for this task:
    - http://sourceforge.net/projects/win32diskimager/files/latest/download
- After finishing the installation and turning on your raspberry, make sure you have your Internet connection already set 
- From a console window run the following script to enable your camera: "sudo raspi-config". On your Raspberry configuration go to interfacing options and make sure camera option is enabled
- From a console window run the following script: "sudo python3 /Edatasoluciones/Edata_CamValidation.py"
- You will be asked to insert your Raspicam Activation Key
- You're ready to start browsing the movement detection on the website:<br/<br/>
