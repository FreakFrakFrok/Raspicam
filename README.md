# Raspicam

Raspicam code will help you if you own a Raspberry Pi with an integrated camera to record actions based on movement detection. The results of these detections will be visible through the raspicam website. The good news: it's totally free for a camera with 48 hours of historical recording.

Raspbian Buster Lite 32GB OS<br/>What do you need:
- Raspberry Pi with camera
- Raspberry Pi with Wifi or Ethernet available
- 32GB Micro SD

Instructions:
- Register your account at https://www.edatasoluciones.com/raspicam/registration
- Obtain your Raspicam Activation Key once you login for the first time at https://www.edatasoluciones.com/raspicam/login
- Download the 32GB image of Raspbian Buster Lite 32GB with the preconfiguration of the Raspicam python code from one of the following URL:
    - https://www.edatasoluciones.com/raspicam/media/32GB_Raspicam.img
    - https://drive.google.com/drive/folders/14nZC6Qvx1dawEartg2oVAVSE1XjW3wtC?usp=sharing
- Install Raspbian Buster Lite 32GB image on your 32GB Micro SD Card. 
    - If you use Windows then you can use Win32DiskImager for this task: http://sourceforge.net/projects/win32diskimager/files/latest/download
- After image installation, insert your micro SD card into your raspberry and turn it on. 
- From console window run the following script: "sudo raspi-config". 
    - Make sure you have your Wifi or ethernet is configured (Network Options - Wifi)
    - Make sure you you have your regional date time is configured. (Localisation Options - Change Timezone)
    - Make sure your camera is enabled (Interfacing Options - Camera - Enabled)
- From a console window run the following script: "sudo python3 /Edatasoluciones/Edata_CamValidation.py"
- You will be asked to insert your Raspicam Activation Key.
- You're ready to start browsing the movement detection on Raspicam by Edatasoluciones website.
