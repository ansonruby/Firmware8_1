import commands
import sys
import time

from crontab import CronTab

import lib.Control_Archivos2  as Ca
import lib.Control_Automatico  as Cus


"""
#Log_Actualizador('4. Cambiar nombre de firmware en ejecucion')
res = commands.getoutput('[ -d /home/pi/FirmwareBK2 ] && echo "Existe" || echo "NO_existe"')
print res
"""


def Fecha_Actual():
	tiempo_segundos = time.time()
	print(tiempo_segundos)
	tiempo_cadena = time.ctime(tiempo_segundos) # 1488651001.7188754 seg
	tiempo_cadena = time.strftime("%d/%m/%y %I:%M:%S%p")
	print(tiempo_cadena)
	return tiempo_cadena

def Hora_Actual():
	tiempo_segundos = time.time()
	#print(tiempo_segundos)
	#tiempo_cadena = time.ctime(tiempo_segundos) # 1488651001.7188754 seg
	tiempo_cadena = time.strftime("%I:%M %p")
	#print(tiempo_cadena)
	return tiempo_cadena

def T_Actual():
	return str(int(time.time()*1000.0))
antes=0

while 1:
    tiempo =time.time()
    actual = str(int(tiempo*1000.0))
   
	
    print tiempo
    print actual
    print 'antes'
    print antes
    print int(actual)-antes
    int(actual)-antes
    antes=int(actual)
    time.sleep(5.01)
    seconds = 1596146599#1545925769.9618232
    local_time = time.ctime(seconds).strftime("%d/%m/%y %I:%M:%S%p")
    tiempo_cadena = time.strftime("%d/%m/%y %I:%M:%S%p")
    print("Local time:", local_time)
    print("Local time:", tiempo_cadena)
    
    
    
    
