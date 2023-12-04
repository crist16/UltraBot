
import time
from datetime import date
import msvcrt


from utils import IniciarSession, IntroducirUsuario, LastViewWrite, LeerLineas, StartClick, cerrarPestanas, pestanasRecorrer, reiniciarIp

usrInputCoords = [648,426]
usrPassworCoords = [780,550]
contador = 0
seleccion = input('\n Ingresa 1 para funcion principal \n Presione 2 para cambiar ip \n Presione 3 para cerrar ventanas')
seleccion = int(seleccion)
today = date.today()
linesArray =[]
coordPestanas = {
    "1" : [119,65],
    "2" : [343,65],
    "3" : [540,72],
    "4" : [768,72],
    "5" : [988,72],
    "6" : [1203,72],
    "7" : [1424,58]

}



botones = {
    "iniciarSesion" : [1400,230],
    "start" : [740,140]
}
#aBRIR PROGRAMA

#os.startfile(r"C:\Users\rafae\AppData\Local\Programs\Ultra\Ultra.exe")



def MainFunction():     
    
    numeroTxt = input("Agregue el nombre del txt")
    time.sleep(5)
    LastViewWrite(today, numeroTxt)
    #pestanasRecorrer(contador)
   
    #IniciarSession(coordPestanas, botones)

    lines = LeerLineas(numeroTxt)
    
    IntroducirUsuario(usrInputCoords, usrPassworCoords, coordPestanas, lines)
    StartClick(coordPestanas, botones)   
    msvcrt.getch()


if seleccion == 1:
    MainFunction()
    
elif seleccion == 2:
    reiniciarIp()
    
elif seleccion == 3:
    cerrarPestanas()

           
        