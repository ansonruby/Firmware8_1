import Control_Archivos2
import time
import RPi.GPIO as GPIO #Libreria Python GPIO


Leer_ArchivoTiempo            = int (Control_Archivos2.Leer_Archivo(30))

#print Leer_ArchivoTiempo
GPIO.setmode (GPIO.BOARD)
		# Entrada, Salida
Rele =   [37,38] #16, 19 #[21,23]
Tiempo_Torniquete= Leer_ArchivoTiempo#0.5#2 #segundos de respuesta

for k in range(2):
    GPIO.setup(Rele[k], GPIO.OUT)

def Entrar():
        global Tiempo_Torniquete
        GPIO.output(Rele[0], GPIO.LOW)
        time.sleep(Tiempo_Torniquete)
        GPIO.output(Rele[0], GPIO.HIGH)
def Salir():
        global Tiempo_Torniquete
        GPIO.output(Rele[1], GPIO.LOW)
        time.sleep(Tiempo_Torniquete)	
        GPIO.output(Rele[1], GPIO.HIGH)
# mantener cerrado
def Cerrado():    
	GPIO.output(Rele[0], GPIO.HIGH)# Entrada
	GPIO.output(Rele[1], GPIO.HIGH)# Salida
	
Cerrado()
