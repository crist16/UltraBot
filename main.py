
import time
import pyperclip
import subprocess
import pyautogui
import os
import msvcrt
import pyperclip

usrInputCoords = [662,531]
usrPassworCoords = [662,648]
contador = 0
numeroTxt = input("Agregue el nombre del txt")
linesArray = []
coordPestanas = {
    "1" : [132,71],
    "2" : [416,72],
    "3" : [680,72],
    "4" : [944,72],
    "5" : [1197,72],
    "6" : [1431,72],

}



botones = {
    "iniciarSesion" : [1394,278],
    "start" : [900,160]
}
""""

RECORRER PESTAÑAS 
CLICAR INICIAR SESSION
COPIAR USER 
PEGAR EN FORMULARIO
COPIAR PASSWORD 
PEGAR EN FORMULARIO
PRESIONAR ENTER
PRESIONAR INICIAR
"""

#aBRIR PROGRAMA

os.startfile(r"C:\Users\Cristobal\AppData\Local\Programs\Ultra\Ultra.exe")
time.sleep(12)
print("Fin sleep")

#ABRIR LAS PESTAÑAS 
while contador <=5:
    
    try:
        contador = contador+1
        print("CLicked here")
        pyautogui.click("images/icon.png")
    except:    
        pyautogui.click("images/addPestanaUltra.png")
        contador = contador+1
   

#Recorrer pestañar
for p in coordPestanas:
    time.sleep(2)
    pyautogui.click(x=coordPestanas[p][0],y=coordPestanas[p][1])
    time.sleep(3)
    pyautogui.click(x=botones["iniciarSesion"][0],y=botones["iniciarSesion"][1])
    time.sleep(3)
    
   
with open(f"{numeroTxt}.txt","r") as file:
        lines = file.readlines()
        lineArray = lines



    
    
for idx,line in enumerate(lines):       
    #obteniendo usr y password
    lineArray = line.split(",")
    usr = lineArray[0]
    pyperclip.copy(usr)
    pyautogui.click(x=coordPestanas[f"{idx+1}"][0],y=coordPestanas[f"{idx+1}"][1])
    pyautogui.click(x=usrInputCoords[0],y=usrInputCoords[1])
    pyautogui.hotkey ("ctrl","v")
    time.sleep(3)
    
    password = lineArray[1]
    pyperclip.copy(password)
    time.sleep(5)
    pyautogui.click(x=usrPassworCoords[0],y=usrPassworCoords[1])  
    
    time.sleep(2)
    pyautogui.hotkey("ctrl","v")
    time.sleep(2)   
    pyautogui.press('enter')


for p in coordPestanas:
    time.sleep(2)
    pyautogui.click(x=coordPestanas[p][0],y=coordPestanas[p][1])
    pyautogui.click(x=botones["start"][0], y= botones["start"][1])
    time.sleep(2)   



msvcrt.getch()




           
        