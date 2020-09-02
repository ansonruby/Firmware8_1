import urllib2 #librerio para control web
import os
import requests
import commands
import Control_Archivos2  as Ca


Generar		         = Ca.Generar_ID_Tarjeta

#local prueba equipo
CE_V=1   # 0: servidor de prueba 1: las direciones del aplicativo
CE_url = "http:+++++++"

#------------------------------------------------
#               constantes del aplicativo
#------------------------------------------------

IP_servidorP    = 'http://18.237.109.221'                # Pruebas
#IP_servidorP    = 'http://192.168.0.4'                # Pruebas
IP_servidor     = 'http://34.220.121.133'                 # Servidor

#MAC_DIRC        = 'cat /sys/class/net/eth0/address'
MAC_DIRC        = 'cat /sys/class/net/wlan0/address'
MAC             = commands.getoutput(MAC_DIRC)
MAC             = MAC.replace(":","")
ID_Tarjeta      = Generar(MAC)                             # ID
#ID_Tarjeta      = '23'  #'19' #ID de prueba #ID_Tarjeta      = ''
#------		Directorio
CE_rl =[        "/api/access/keyboard_access",      # Enviar Teclado
                "/api/access/grant",                # Enviar QR
                "/api/access/get_granted_users_pi", # Resivir usuarios
                "/api/access/set_in_out_activity",  # Enviar E/S sin Internet
                "/api/access/verify_conection",     # Verificar conexion
                "/api/firmware/review_update",      # Peticion Actualizacion
                "/api/firmware/confirm_update"      # Confirmacion Actualizacion
        ]
"""
CE_rl =[        "/api/access/keyboard_access/index.php",      # Enviar Teclado
                "/api/access/grant/index.php",                # Enviar QR
                "/api/access/get_granted_users_pi/index.php", # Resivir usuarios
                "/api/access/set_in_out_activity/index.php",  # Enviar E/S sin Internet
                "/api/access/verify_conection/index.php",     # Verificar conexion
                "/api/firmware/review_update/index.php",      # Peticion Actualizacion
                "/api/firmware/confirm_update/index.php"      # Confirmacion Actualizacion
        ]
"""
#print ID_Tarjeta
def Confimacion_Firmware(T_actual, vercion_Actual_Firmware,LOG):
    global CE_url
    global CE_url_Teclado
    global CE_rl
    global CE_rlP
    global ID_Tarjeta

    CE_peticion='NO'
    CE_cabeceras = {
        "Content-Type" : "application/json",
        "Fuseaccess-Id" : ID_Tarjeta,
        "Time-Scan" : T_actual
    }

    #CE_url = "http://35.161.178.60/api/firmware/confirm_update"

    if CE_V != 0	: CE_url = IP_servidor+CE_rl[6]         #CE_rl[4]
    else		: CE_url = IP_servidorP+CE_rl[6]        #CE_rlP[4]

    #print CE_url


    if len(LOG)>=2:
        CE_datos ='{"version":"'+vercion_Actual_Firmware+'","updated":"0","log":"'+LOG+'"}'
    else :
        CE_datos ='{"version":"'+vercion_Actual_Firmware+'","updated":"1"}'
    print CE_datos
    #CE_datos ='{"version":"2019.12.3.0","update":"1"}'#Formato actualisacion correcta
    #CE_datos ='{"version":"2019.12.3.0","update":"0","log":"2.3 herror ...."}' #Formato herror

    try:
        CE_peticion = requests.post(CE_url, data=CE_datos, headers=CE_cabeceras, timeout=2)
        return CE_peticion
    except:
        return CE_peticion


def Veri_Firmware(T_actual, vercion_Actual_Firmware):
    global CE_url
    global CE_url_Teclado
    global CE_rl
    global CE_rlP
    global ID_Tarjeta

    CE_peticion='NO'
    CE_cabeceras = {
        "Content-Type" : "application/json",
        "Fuseaccess-Id" : ID_Tarjeta,
        "Time-Scan" : T_actual
    }

    #CE_url = "http://35.161.178.60/api/firmware/review_update"

    if CE_V != 0	: CE_url = IP_servidor+CE_rl[5]         #CE_rl[4]
    else		: CE_url = IP_servidorP+CE_rl[5]        #CE_rlP[4]

    #print CE_url

    CE_datos ='{"data":"'+vercion_Actual_Firmware+'"}'#ya con la vercion del dispsotivo
    print CE_datos
    #CE_datos ='{"data":"2019.12.3.0"}' #firmware actual
    #CE_datos ='{"data":"2020.2.10.0"}' # firmware a actualizar

    try:
        CE_peticion = requests.get(CE_url, data=CE_datos, headers=CE_cabeceras, timeout=2)
        return CE_peticion
    except:
        return CE_peticion


def ping ():

        global CE_url
        global IP_servidorP
        global IP_servidor

        CE_peticion='NO'

        if CE_V != 0	: CE_url = IP_servidor+CE_rl[4]         #CE_rl[4]
        else		: CE_url = IP_servidorP+CE_rl[4]        #CE_rlP[4]

        try:
                CE_peticion = requests.get(CE_url, timeout=1)
                return CE_peticion.text
        except:
                return CE_peticion



def envio(dat,T_actual,QR_Te):

        global CE_url
        global CE_url_Teclado
        global CE_rl
        global CE_rlP
        global ID_Tarjeta

        CE_peticion='NO'
        CE_cabeceras = {
        "Content-Type" : "application/json",
        "Fuseaccess-Id" : ID_Tarjeta,
        "Time-Scan" : T_actual
        }

        QR_ruta = QR_Te

        #print QR_Te
        #print QR_Te == 2
        
        if QR_Te == 0:  QR_ruta = 0 # para rut
        if QR_Te == 1:  QR_ruta = 1 # para qr
        if QR_Te == 2:  QR_ruta = 0 # para pin

        #print QR_ruta

        if CE_V != 0	: CE_url = IP_servidor+CE_rl[QR_ruta]         #CE_rl[4]
        else		: CE_url = IP_servidorP+CE_rl[QR_ruta]        #CE_rlP[4]


        
        
        
        if QR_Te == 0: # enviar lo digitado
                CE_datos ='{"rut":"'+dat+'"}'	#'{"rut":"99158441"}'
        if QR_Te == 1:
                CE_datos ='{"data":"'+dat+'"}'	#'{"data":"991584411234"}'
        if QR_Te == 2:
                CE_datos ='{"rut":"'+dat+'"}'	#'{"pin":"'+dat+'"}'	#'{"pin":"99158441"}' los cuatro ultimos son el pin
        if QR_Te == 3:
                CE_datos = dat					# datos leidos para enviar
        #print CE_datos
        #print CE_url
        try:
                CE_peticion = requests.post(CE_url, data=CE_datos, headers=CE_cabeceras, timeout=2)#2
                #print CE_peticion
                #print CE_peticion.text
                return CE_peticion
        except:
                #print 'que pasa'
                #print CE_peticion
                return CE_peticion

def Usuarios_Activos(T_actual):

        global ID_Tarjeta

        CE_peticion='NO'
        CE_cabeceras = {
        "Content-Type" : "application/json",
        "Fuseaccess-Id" : ID_Tarjeta,
        "Time-Scan" : T_actual
        }

        if CE_V != 0	: CE_url = IP_servidor+CE_rl[2]         #CE_rl[4]
        else		: CE_url = IP_servidorP+CE_rl[2]        #CE_rlP[4]

        try:
                CE_peticion = requests.get(CE_url, headers=CE_cabeceras, timeout=2)
                return CE_peticion
        except:
                return CE_peticion
