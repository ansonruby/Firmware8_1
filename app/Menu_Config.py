# -*- coding: utf-8 -*-



import Tkinter
import ttk
from Tkinter import *

import socket
import fcntl
import struct
import commands


import lib.Control_Archivos2


# definiciones para el aplicativo principal -----------------


N_A_wifi                ='/etc/wpa_supplicant/wpa_supplicant.conf'
N_A_IP_Static           ='/etc/dhcpcd.conf'


Leer_Archivo            = lib.Control_Archivos2.Leer_Archivo
Borrar                  = lib.Control_Archivos2.Borrar_Archivo
Escrivir		= lib.Control_Archivos2.Escrivir_Archivo
Escrivir_Estados        = lib.Control_Archivos2.Escrivir_Estados





#-----------------------------------
#---------Variables de configuracion
#-----------------------------------


tk = Tk()
tk.geometry("320x480")
tk.geometry("+%d+%d" % (0,0))
tk.config(background='Dark gray')
tk.attributes("-fullscreen",True)


Fuente=("Arial",14,'bold')
Fuenteip=("Arial",22,'bold')
Fuentew=("Arial",20,'bold')
Fuente2=("Arial",16,'bold')

#dimenciones de botones menu principal

DX_b=100
DY_b= 20
#Ip static
textin  =StringVar()
textin2 =StringVar()
textin3 =StringVar()
textin4 =StringVar()
textin5 =StringVar()

#dimenciones de botones menu principal
DX=35#16
DY=15#2 #5
BD=1

#distancia menu principal
Disxm=55
Disym=30#39


# posicion de botones 
Ini_x=6
Ini_y=95
Disx=90#52
Disy=60#35#39

#dimenciones de botones ipstatica
DXip=33#16
DYip=10#2 #5

# posicion de botones ipstatica
Ini_xip=25
Ini_yip=115
Disxip=90#52
Disyip=60#35#39


operator=""
operator2=""
operator3=""
operator4=""
operator5=""
Mayusculas=0

# posicion de botones wifi
Ini_xw=6
Ini_yw=48 #95
Disxw=62
Disyw=46#39
#dimenciones de botones wifi
DXw=18
DYw=4 #5

# Multi torniquete
MIni_xip = 25
MDisxip  = 95
MIni_y   = 120
MDisyip  = 60


Tiempo_Torniquete = int (Leer_Archivo(30))

#-----------------------------------
#--------       funciones       ----
#-----------------------------------


def Escrivir_Archivo(Texto,a):
 
        global N_A_wifi
        global N_A_IP_Static
	
        if a==6:	arch	=	N_A_wifi
        
        archivo = open(arch, "a")
        #print(archivo.tell())
        archivo.write(Texto + "\n")
        #print(archivo.tell())
        archivo.close()


def Modificar_Archivo1(a,we):
        
        global N_A_wifi
        global N_A_IP_Static

        contador =0
        #we =2
        
        if a==0:	arch	=	N_A_wifi
        if a==1:	arch	=	N_A_IP_Static

        f = open (arch,'r')
        lineas = f.readlines()
        f.close()
        
        x=0
        T_fichero = len(lineas)
        print T_fichero
        print a

        f = open (arch,'w')
        for linea in lineas:
                
                if (linea[0]!='#') and (len(linea)>=4):
                        if (linea.find('interface')!=-1) or (linea.find('static')!=-1):
                                if (linea.find('option')==-1):
                                        if (linea.find('eth0')!=-1):
                                                contador =0
                                                wec = 1
                                                
                                        if (linea.find('wlan0')!=-1):
                                                contador =0
                                                wec = 0

                                        if contador>=0 and contador <=3:
                                                if we == wec:
                                                        print 'Eli: '+str(contador) + linea
                                                else:
                                                        #print str(contador) + linea
                                                        f.write(linea)
                                        contador =contador + 1

                                else:
                                        #print str(contador) + linea
                                        f.write(linea)
                        else:
                                #print str(contador) + linea
                                f.write(linea)
                else:
                        #print str(contador) + linea
                        f.write(linea)

        
        print 'colocando las ip statica'
        if we==0:
                f.write('interface wlan0'+'\n')
        else:
                f.write('interface eth0'+'\n')
                
        f.write('static ip_address='+ str(IP.get())+'\n')
        f.write('static routers='+ str(Gateway.get())+'\n')
        f.write('static domain_name_servers='+ str(Gateway.get())+'\n')
        
        f.close()


def Modificar_Archivo(a):
        
        global N_A_wifi
        global N_A_IP_Static


        if a==0:	arch	=	N_A_wifi
        if a==1:	arch	=	N_A_IP_Static


        
        f = open (arch,'r')
        lineas = f.readlines()
        f.close()
        
        x=0
        T_fichero = len(lineas)
        print T_fichero


        f = open (arch,'w')
        for linea in lineas:

                #f.write(linea)
                
                x+=1

                if  x >= (T_fichero -3) :
                        #if len(linea) >= 1:
                        #(linea.find('interface')!=-1) or (linea.find('static')!=-1) or 
                        if (linea[0]!='#') and (len(linea)>=2):
                                print 'Eliminar Linea:'+str(x)+': '+ linea
                                #f.write(linea)
                                
                        else:
                                print 'Linea:'+str(x)+': '+ linea
                                #print 'Linea:'+str(x)+': '+ linea + 'Ta: '+str(len(linea))
                                f.write(linea)
                else:
                        f.write(linea)


        print 'colocando las ip statica'

        
        #f.write('interface wlan0'+'\n')
        f.write('interface eth0'+'\n')
        f.write('static ip_address='+ str(IP.get())+'\n')
        f.write('static routers='+ str(Gateway.get())+'\n')
        f.write('static domain_name_servers='+ str(Gateway.get())+'\n')
        
        f.close()

   
        #return mensaje 
def clickbut_Tiempo(number):
        global Tiempo_Torniquete
        if number == '◄':
                Tiempo_Torniquete =Tiempo_Torniquete-1
                if Tiempo_Torniquete <= 1:
                        Tiempo_Torniquete =1

        else:
                Tiempo_Torniquete =Tiempo_Torniquete+1
                if Tiempo_Torniquete >= 20:
                        Tiempo_Torniquete =20

        #operator=operator+str(number)
        #textin.set(operator)
        #P_C_Tiempo_Torniquete.set("2")
        texto = StringVar()
        texto.set(str(Tiempo_Torniquete))
        P_C_Tiempo_Torniquete.config(textvariable=texto)
        #Tiempo Torniquete
        Borrar(30)      #Esatado chicharra
        Escrivir_Estados(str(Tiempo_Torniquete),30)

def clickbut(number):   #lambda:clickbut(1)

        global operator
        global operator2
        global operator3
        global operator4
        global operator5
        global Mayusculas




        #print lista.get()
        """
        if number == '+':
                if Mayusculas == 0:
                        Mayusculas=1
                            #print "Minusculas"
                else:
                        Mayusculas=0
                        #print "Mayusculas"
        """
        if number == '◄':
                print 'borrar el ultimo'
                w=tk.focus_get()
                if w is IP:
                        IP.delete(len(IP.get())-1, END)
                        operator=IP.get()
                elif w is Gateway:
                        Gateway.delete(len(Gateway.get())-1, END)
                        operator2=Gateway.get()
                if w is wifi:
                        wifi.delete(len(wifi.get())-1, END)
                        operator3=wifi.get()
                elif w is contrasena:
                        contrasena.delete(len(contrasena.get())-1, END)
                        operator4=contrasena.get()
                elif w is M_T_IP:
                        M_T_IP.delete(len(M_T_IP.get())-1, END)
                        operator5=M_T_IP.get()

            
        else:

                if Mayusculas == 0:
                    number= number.upper()
        
                w=tk.focus_get()
                #print "focus is:",w
                #print type(w)
                #print wifi
                if w is IP:
                    #print "It's wifi"
                    if len(operator) > 0:
                        operator=operator+str(number)
                        textin.set(operator)
                        #sonidoLector(Tiempo_sonido)
                    elif number != 0:
                        operator=operator+str(number)
                        textin.set(operator)
            
                elif w is Gateway:
                    #print "It's contrasena"
                    if len(operator2) > 0:
                        operator2=operator2+str(number)
                        textin2.set(operator2)
                        #sonidoLector(Tiempo_sonido)
                    elif number != 0:
                        operator2=operator2+str(number)
                        textin2.set(operator2)

                elif w is wifi:
                    #print "It's contrasena"
                    if len(operator3) > 0:
                        operator3=operator3+str(number)
                        textin3.set(operator3)
                        #sonidoLector(Tiempo_sonido)
                    elif number != 0:
                        operator3=operator3+str(number)
                        textin3.set(operator3)
                elif w is contrasena:
                    #print "It's contrasena"
                    if len(operator4) > 0:
                        operator4=operator4+str(number)
                        textin4.set(operator4)
                        #sonidoLector(Tiempo_sonido)
                    elif number != 0:
                        operator4=operator4+str(number)
                        textin4.set(operator4)
                elif w is M_T_IP:
                    #print "It's contrasena"
                    if len(operator5) > 0:
                        operator5=operator5+str(number)
                        textin5.set(operator5)
                        #sonidoLector(Tiempo_sonido)
                    elif number != 0:
                        operator5=operator5+str(number)
                        textin5.set(operator5)
                



def desplegar(event):
        Actualizar_lista()
        #print 'desplicada'
        return 0
        
def Actualizar_lista():
        lista["values"]= []
        #print 'Listado Wifis '
        res = commands.getoutput('sudo iwlist wlan0 scan | grep ESSID')
        res=res.replace('"',"")
        res=res.replace('\n',"")
        redes =res.split("ESSID:")
        
        BK_Red=0
        for x1 in range(len(redes)):
            c= redes[x1]
            c=c.replace('\n',"")
            c=c.replace(' ',"")
            #print (c)
            #lista.set(c)
            values = list(lista["values"])
            lista["values"]= values+ [c]
        
def ver_wifi_Letras_Minusculas():
        butqw.place(x=Ini_xw+(Disxw*0), y=Ini_yw+(Disyw*1))
        butww.place(x=Ini_xw+(Disxw*1), y=Ini_yw+(Disyw*1))
        butew.place(x=Ini_xw+(Disxw*2), y=Ini_yw+(Disyw*1))
        butrw.place(x=Ini_xw+(Disxw*3), y=Ini_yw+(Disyw*1))
        buttw.place(x=Ini_xw+(Disxw*4), y=Ini_yw+(Disyw*1))
        butyw.place(x=Ini_xw+(Disxw*0), y=Ini_yw+(Disyw*2))
        butuw.place(x=Ini_xw+(Disxw*1), y=Ini_yw+(Disyw*2))
        butiw.place(x=Ini_xw+(Disxw*2), y=Ini_yw+(Disyw*2))
        butow.place(x=Ini_xw+(Disxw*3), y=Ini_yw+(Disyw*2))
        butpw.place(x=Ini_xw+(Disxw*4), y=Ini_yw+(Disyw*2))
        butaw.place(x=Ini_xw+(Disxw*0), y=Ini_yw+(Disyw*3))
        butsw.place(x=Ini_xw+(Disxw*1), y=Ini_yw+(Disyw*3))
        butdw.place(x=Ini_xw+(Disxw*2), y=Ini_yw+(Disyw*3))
        butfw.place(x=Ini_xw+(Disxw*3), y=Ini_yw+(Disyw*3))
        butgw.place(x=Ini_xw+(Disxw*4), y=Ini_yw+(Disyw*3))
        buthw.place(x=Ini_xw+(Disxw*0), y=Ini_yw+(Disyw*4))
        butjw.place(x=Ini_xw+(Disxw*1), y=Ini_yw+(Disyw*4))
        butkw.place(x=Ini_xw+(Disxw*2), y=Ini_yw+(Disyw*4))
        butlw.place(x=Ini_xw+(Disxw*3), y=Ini_yw+(Disyw*4))
        butzw.place(x=Ini_xw+(Disxw*4), y=Ini_yw+(Disyw*4))
        butxw.place(x=Ini_xw+(Disxw*0), y=Ini_yw+(Disyw*5))
        butcw.place(x=Ini_xw+(Disxw*1), y=Ini_yw+(Disyw*5))
        butvw.place(x=Ini_xw+(Disxw*2), y=Ini_yw+(Disyw*5))
        butbw.place(x=Ini_xw+(Disxw*3), y=Ini_yw+(Disyw*5))
        butnw.place(x=Ini_xw+(Disxw*4), y=Ini_yw+(Disyw*5))
        butMYw.place(x=Ini_xw+(Disxw*0), y=Ini_yw+(Disyw*6))
        butmw.place(x=Ini_xw+(Disxw*1), y=Ini_yw+(Disyw*6))
        but123w.place(x=Ini_xw+(Disxw*2), y=Ini_yw+(Disyw*6))
        butabcw.place_forget()
        #butbw.place(x=Ini_xw+(Disxw*3), y=Ini_yw+(Disyw*6))
        butBow.place(x=Ini_xw+(Disxw*4), y=Ini_yw+(Disyw*6))
        butespw.place(x=Ini_xw+(Disxw*1), y=Ini_yw+(Disyw*7))

def NO_ver_wifi_Letras_Minusculas():
        butqw.place_forget()
        butww.place_forget()
        butew.place_forget()
        butrw.place_forget()
        buttw.place_forget()
        butyw.place_forget()
        butuw.place_forget()
        butiw.place_forget()
        butow.place_forget()
        butpw.place_forget()
        butaw.place_forget()
        butsw.place_forget()
        butdw.place_forget()
        butfw.place_forget()
        butgw.place_forget()
        buthw.place_forget()
        butjw.place_forget()
        butkw.place_forget()
        butlw.place_forget()
        butzw.place_forget()
        butxw.place_forget()
        butcw.place_forget()
        butvw.place_forget()
        butbw.place_forget()
        butnw.place_forget()
        butmw.place_forget()

def NO_ver_wifi_Letras_Mayusculas():
        butQw.place_forget()
        butWw.place_forget()
        butEw.place_forget()
        butRw.place_forget()
        butTw.place_forget()
        butYw.place_forget()
        butUw.place_forget()
        butIw.place_forget()
        butOw.place_forget()
        butPw.place_forget()
        butAw.place_forget()
        butSw.place_forget()
        butDw.place_forget()
        butFw.place_forget()
        butGw.place_forget()
        butHw.place_forget()
        butJw.place_forget()
        butKw.place_forget()
        butLw.place_forget()
        butZw.place_forget()
        butXw.place_forget()
        butCw.place_forget()
        butVw.place_forget()
        butBw.place_forget()
        butNw.place_forget()
        butMw.place_forget()

def NO_ver_wifi_Numeros():
        but1w.place_forget()
        but2w.place_forget()
        but3w.place_forget()
        but4w.place_forget()
        but5w.place_forget()
        but6w.place_forget()
        but7w.place_forget()
        but8w.place_forget()
        but9w.place_forget()
        but0w.place_forget()

        butA1w.place_forget()
        butS2w.place_forget()
        butD3w.place_forget()
        butF4w.place_forget()
        butG5w.place_forget()
        butH6w.place_forget()
        butJ7w.place_forget()
        butK8w.place_forget()
        butL9w.place_forget()
        butZ0w.place_forget()
        butX1w.place_forget()
        butC2w.place_forget()
        butV3w.place_forget()
        butB4w.place_forget()
        butN5w.place_forget()
        

def V_wifi_Minusculas():
        global Mayusculas
        
        if Mayusculas != 1 :
                Mayusculas=1


        No_ver_menu_principal()
        
        L_wifi.place(bordermode=OUTSIDE, height=20, width=100, y=25)
        L_password.place(bordermode=OUTSIDE, height=20, width=100, y=60)
        #wifi.place(bordermode=OUTSIDE, height=30, width=200, x=90, y=20)
        lista.place(x=Ini_xw+(Disxw*0)+83, y=Ini_yw+(Disyw*0)-35)
        contrasena.place(bordermode=OUTSIDE, height=29, width=200, x=89, y=55)

        P_Menu.place(x=Ini_x+150, y=Ini_y+330)#place(x=Ini_x+(Disx*1)+25, y=Ini_y+(Disy*9)+10)
        Aceptar_W.place(x=Ini_x, y=Ini_y+330)#place(x=Ini_x+(Disx*1)+25, y=Ini_y+(Disy*7)+33)
        #wifi
        
        #minusculas
        ver_wifi_Letras_Minusculas()
        #Maysculas
        NO_ver_wifi_Letras_Mayusculas()
        #numeros
        NO_ver_wifi_Numeros()



def  V_wifi_May_Minu():
        global Mayusculas
        if Mayusculas == 1 :
                Mayusculas=0
                V_wifi_Mayusculas()
        else:
                V_wifi_Minusculas()
                Mayusculas=1


def  V_wifi_Numeros():

        butabcw.place(x=Ini_xw+(Disxw*2), y=Ini_yw+(Disyw*6))
        
        but123w.place_forget()
        butMYw.place_forget()

        NO_ver_wifi_Letras_Mayusculas()
        
        NO_ver_wifi_Letras_Minusculas()
 

        but1w.place(x=Ini_xw+(Disxw*0), y=Ini_yw+(Disyw*1))
        but2w.place(x=Ini_xw+(Disxw*1), y=Ini_yw+(Disyw*1))
        but3w.place(x=Ini_xw+(Disxw*2), y=Ini_yw+(Disyw*1))
        but4w.place(x=Ini_xw+(Disxw*3), y=Ini_yw+(Disyw*1))
        but5w.place(x=Ini_xw+(Disxw*4), y=Ini_yw+(Disyw*1))
        but6w.place(x=Ini_xw+(Disxw*0), y=Ini_yw+(Disyw*2))
        but7w.place(x=Ini_xw+(Disxw*1), y=Ini_yw+(Disyw*2))
        but8w.place(x=Ini_xw+(Disxw*2), y=Ini_yw+(Disyw*2))
        but9w.place(x=Ini_xw+(Disxw*3), y=Ini_yw+(Disyw*2))
        but0w.place(x=Ini_xw+(Disxw*4), y=Ini_yw+(Disyw*2))

        butA1w.place(x=Ini_xw+(Disxw*0), y=Ini_yw+(Disyw*3))
        butS2w.place(x=Ini_xw+(Disxw*1), y=Ini_yw+(Disyw*3))
        butD3w.place(x=Ini_xw+(Disxw*2), y=Ini_yw+(Disyw*3))
        butF4w.place(x=Ini_xw+(Disxw*3), y=Ini_yw+(Disyw*3))
        butG5w.place(x=Ini_xw+(Disxw*4), y=Ini_yw+(Disyw*3))
        butH6w.place(x=Ini_xw+(Disxw*0), y=Ini_yw+(Disyw*4))
        butJ7w.place(x=Ini_xw+(Disxw*1), y=Ini_yw+(Disyw*4))
        butK8w.place(x=Ini_xw+(Disxw*2), y=Ini_yw+(Disyw*4))
        butL9w.place(x=Ini_xw+(Disxw*3), y=Ini_yw+(Disyw*4))
        butZ0w.place(x=Ini_xw+(Disxw*4), y=Ini_yw+(Disyw*4))
        butX1w.place(x=Ini_xw+(Disxw*0), y=Ini_yw+(Disyw*5))
        
        butC2w.place(x=Ini_xw+(Disxw*1), y=Ini_yw+(Disyw*5))
        butV3w.place(x=Ini_xw+(Disxw*2), y=Ini_yw+(Disyw*5))
        butB4w.place(x=Ini_xw+(Disxw*3), y=Ini_yw+(Disyw*5))
        butN5w.place(x=Ini_xw+(Disxw*4), y=Ini_yw+(Disyw*5))
        #butMYw.place(x=Ini_xw+(Disxw*0), y=Ini_yw+(Disyw*6))
        #butmw.place(x=Ini_xw+(Disxw*1), y=Ini_yw+(Disyw*6))
        
        
def V_wifi_Mayusculas():
        global Mayusculas
        if Mayusculas != 0 :
                Mayusculas=0
        
        L_Menu_Principal.place_forget()
        P_wifi.place_forget()
        P_IP.place_forget()
        P_salir.place_forget()
        P_Menu.place(x=Ini_x+150, y=Ini_y+330)#P_Menu.place(x=Ini_x+(Disx*1)+25, y=Ini_y+(Disy*9))
        #wifi
        NO_ver_wifi_Letras_Minusculas()
                     
        butQw.place(x=Ini_xw+(Disxw*0), y=Ini_yw+(Disyw*1))
        butWw.place(x=Ini_xw+(Disxw*1), y=Ini_yw+(Disyw*1))
        butEw.place(x=Ini_xw+(Disxw*2), y=Ini_yw+(Disyw*1))
        butRw.place(x=Ini_xw+(Disxw*3), y=Ini_yw+(Disyw*1))
        butTw.place(x=Ini_xw+(Disxw*4), y=Ini_yw+(Disyw*1))
        butYw.place(x=Ini_xw+(Disxw*0), y=Ini_yw+(Disyw*2))
        butUw.place(x=Ini_xw+(Disxw*1), y=Ini_yw+(Disyw*2))
        butIw.place(x=Ini_xw+(Disxw*2), y=Ini_yw+(Disyw*2))
        butOw.place(x=Ini_xw+(Disxw*3), y=Ini_yw+(Disyw*2))
        butPw.place(x=Ini_xw+(Disxw*4), y=Ini_yw+(Disyw*2))
        butAw.place(x=Ini_xw+(Disxw*0), y=Ini_yw+(Disyw*3))
        butSw.place(x=Ini_xw+(Disxw*1), y=Ini_yw+(Disyw*3))
        butDw.place(x=Ini_xw+(Disxw*2), y=Ini_yw+(Disyw*3))
        butFw.place(x=Ini_xw+(Disxw*3), y=Ini_yw+(Disyw*3))
        butGw.place(x=Ini_xw+(Disxw*4), y=Ini_yw+(Disyw*3))
        butHw.place(x=Ini_xw+(Disxw*0), y=Ini_yw+(Disyw*4))
        butJw.place(x=Ini_xw+(Disxw*1), y=Ini_yw+(Disyw*4))
        butKw.place(x=Ini_xw+(Disxw*2), y=Ini_yw+(Disyw*4))
        butLw.place(x=Ini_xw+(Disxw*3), y=Ini_yw+(Disyw*4))
        butZw.place(x=Ini_xw+(Disxw*4), y=Ini_yw+(Disyw*4))
        butXw.place(x=Ini_xw+(Disxw*0), y=Ini_yw+(Disyw*5))
        butCw.place(x=Ini_xw+(Disxw*1), y=Ini_yw+(Disyw*5))
        butVw.place(x=Ini_xw+(Disxw*2), y=Ini_yw+(Disyw*5))
        butBw.place(x=Ini_xw+(Disxw*3), y=Ini_yw+(Disyw*5))
        butNw.place(x=Ini_xw+(Disxw*4), y=Ini_yw+(Disyw*5))
        butMw.place(x=Ini_xw+(Disxw*1), y=Ini_yw+(Disyw*6))
        butespw.place(x=Ini_xw+(Disxw*1), y=Ini_yw+(Disyw*7))
        
        NO_ver_wifi_Numeros()

        
def V_IP():
        #Menu Principal
        No_ver_menu_principal()
        #P_Menu.place(x=Ini_x+(Disx*0)+25, y=Ini_y+(Disy*0)) # 1 9
        P_Menu.place(x=Ini_x+150, y=Ini_y+330) # 1 9
        #IP_static
        ver_IP_Static()
        
        
def ver_IP_Static():
        
        L_Ip_Static.place(bordermode=OUTSIDE, height=20, width=100, y=10, x= 115)
        L_Ip_Static_lista.place(bordermode=OUTSIDE, height=29, width=200, x=60, y=40)
        L_Ip.place(bordermode=OUTSIDE, height=20, width=100, y=80)
        L_Gat.place(bordermode=OUTSIDE, height=20, width=100, y=130)
        IP.place(bordermode=OUTSIDE, height=30, width=200, x=90, y=80)
        Gateway.place(bordermode=OUTSIDE, height=30, width=200, x=90, y=120)
        
        but1.place(x=Ini_xip+(Disxip*0), y=Ini_yip+(Disyip*1))
        but2.place(x=Ini_xip+(Disxip*1), y=Ini_yip+(Disyip*1))
        but3.place(x=Ini_xip+(Disxip*2), y=Ini_yip+(Disyip*1))
        but4.place(x=Ini_xip+(Disxip*0), y=Ini_yip+(Disyip*2))
        but5.place(x=Ini_xip+(Disxip*1), y=Ini_yip+(Disyip*2))        
        but6.place(x=Ini_xip+(Disxip*2), y=Ini_yip+(Disyip*2))
        but7.place(x=Ini_xip+(Disxip*0), y=Ini_yip+(Disyip*3))
        but8.place(x=Ini_xip+(Disxip*1), y=Ini_yip+(Disyip*3))
        but9.place(x=Ini_xip+(Disxip*2), y=Ini_yip+(Disyip*3))
        but0.place(x=Ini_xip+(Disxip*0), y=Ini_yip+(Disyip*4))
        butb.place(x=Ini_xip+(Disxip*1), y=Ini_yip+(Disyip*4))
        butp.place(x=Ini_xip+(Disxip*2), y=Ini_yip+(Disyip*4))
        Aceptar_IP.place(x=Ini_x, y=Ini_y+330)
        

                
def No_ver_IP_Static():
        L_Ip_Static.place_forget()
        L_Ip_Static_lista.place_forget()
        L_Ip.place_forget()
        L_Gat.place_forget()
        IP.place_forget()
        Gateway.place_forget()
        but1.place_forget()
        but2.place_forget()
        but3.place_forget()
        but4.place_forget()
        but5.place_forget()
        butb.place_forget()
        but6.place_forget()
        but7.place_forget()
        but8.place_forget()
        but9.place_forget()
        but0.place_forget()
        butp.place_forget()
        Aceptar_IP.place_forget()
        #Cancelar_IP.place_forget()
        
def L_menu_inicio():
        #Menu
        ver_menu_principal()        
        P_Menu.place_forget()
        #IP_static
        No_ver_IP_Static()
        #wifi
        L_wifi.place_forget()
        L_password.place_forget()
        butabcw.place_forget()
        wifi.place_forget()
        contrasena.place_forget()
        Aceptar_W.place_forget()
        lista.place_forget()

        NO_ver_wifi_Letras_Mayusculas()
        
        NO_ver_wifi_Letras_Minusculas()

        NO_ver_wifi_Numeros()

        but123w.place_forget()
        butabcw.place_forget()
        butbw.place_forget()
        butBow.place_forget()
        butespw.place_forget()
        butMYw.place_forget()

        No_ver_Restablecer()
        No_ver_Torniquete()
        No_ver_Multi_Torniquete()


def check_IP(address):
        try:
                socket.inet_aton(address)
                return address.count('.') == 3
        except socket.error:
                return False

def salir():
        
        commands.getoutput('sudo reboot')
        

def verificar_IP_Static(): #esta función verifica que este correcto usuario y contraseña digitado por el usuario
 
    Ip1=IP.get()#get es el metodo utilizado para capturar los datos de la caja de texto
    Gateway1=Gateway.get()
    Tipo_red = L_Ip_Static_lista.get()
    print Tipo_red
    print Ip1
    print Gateway1

    #Leer_Archivo(1)
    #print len(a)
    #print len(Tipo_red)
 
    

    if (len(Ip1) == 0) or (len(Gateway1)==0) or (len(Tipo_red)==0):
        top = Tk()
        top.geometry("+%d+%d" % (65,200))
        top.config(background='Red')
        top.title("Error")
        frame2 = Message(top, font='Arial', relief=RAISED, text='Los campos estan vacíos.',padx=50,pady=50,width=100, bg='Red')
        frame2.pack()
    else:
        print 'verificacion ip valida'

        if (check_IP(Ip1) == False) or (check_IP(Gateway1) == False) :
                top = Tk()
                top.geometry("+%d+%d" % (65,200))
                top.config(background='Red')
                top.title("Error")
                frame2 = Message(top, font='Arial', relief=RAISED, text='NO es una IP valida.',padx=50,pady=50,width=100, bg='Red')
                frame2.pack()
        else:
                print 'verificar una configuracion previa y guardar la nueva' 
                #Modificar_Archivo(1)
                if Tipo_red == "Ethernet":
                        Modificar_Archivo1(1,1)
                else:
                        Modificar_Archivo1(1,0)
                commands.getoutput('sudo reboot')



def verificar_wifi(): #esta función verifica que este correcto usuario y contraseña digitado por el usuario
 
    #red=wifi.get()#get es el metodo utilizado para capturar los datos de la caja de texto
    clave=contrasena.get()

    red = lista.get()
    print red
    
    #print len(a)
    #print len(b)

    if (len(red) == 0) or (len(clave)==0):
        top = Tk()
        top.geometry("+%d+%d" % (65,200))
        top.config(background='Red')
        top.title("Error")
        frame2 = Message(top, font='Arial', relief=RAISED, text='Los campos estan vacíos.',padx=50,pady=50,width=100, bg='Red')
        frame2.pack()
    else:
        print 'Test wifis '
        res = commands.getoutput('sudo iwlist wlan0 scan | grep ESSID')
        res=res.replace('"',"")
        res=res.replace('\n',"")
        redes =res.split("ESSID:")
        
        BK_Red=0
        for x1 in range(len(redes)):
            c= redes[x1]
            c=c.replace('\n',"")
            c=c.replace(' ',"")
            print (c)
            #print len(c)
            if red == c:
                #print 'Esta al alcanse la red'
                BK_Red=1
            
        if BK_Red == 0:
            top = Tk()
            top.geometry("+%d+%d" % (65,200))
            top.config(background='Red')
            top.title("Error")
            frame2 = Message(top, font='Arial', relief=RAISED, text='La red no esta disponible.',padx=50,pady=50,width=100, bg='Red')
            frame2.pack()
        else:
            print 'Configurar el archivo wifi '


            commands.getoutput('sudo chmod -R 777 /etc/wpa_supplicant/wpa_supplicant.conf')

            Nueva_wifi='\nnetwork={\n\tssid="'+red+'"\n\tpsk="'+clave+'"\n\tkey_mgmt=WPA-PSK\n\n}'
            print (Nueva_wifi)

            Escrivir_Archivo(Nueva_wifi,6)

            commands.getoutput('sudo reboot')

def ver_menu_principal():
        L_Menu_Principal.place(bordermode=OUTSIDE, height=20, width=150, y=10, x= 90)
        P_wifi.place(x=Ini_x+(Disxm*0)+25, y=Ini_y+(Disym*0)-60)
        P_IP.place(x=Ini_x+(Disxm*0)+24, y=Ini_y+(Disym*2)-50)
        P_Restablecer.place(x=Ini_x+(Disxm*0)+25, y=Ini_y+(Disym*4)-40)
        P_Confi_Torniquete.place(x=Ini_x+(Disxm*0)+25, y=Ini_y+(Disym*6)-30)
        P_Confi_Multi_Dispositivo.place(x=Ini_x+(Disxm*0)+25, y=Ini_y+(Disym*7)+10)
        P_salir.place(x=Ini_x+(Disxm*0)+25, y=Ini_y+(Disym*10)-0)

def No_ver_menu_principal():
        L_Menu_Principal.place_forget()
        P_wifi.place_forget()
        P_IP.place_forget()
        P_Restablecer.place_forget()
        P_Confi_Torniquete.place_forget()
        P_salir.place_forget()
        P_Confi_Multi_Dispositivo.place_forget()

def Restablecer():
        #Menu Principal
        No_ver_menu_principal()
        P_Menu.place(x=Ini_x+150, y=Ini_y+330)#P_Menu.place(x=Ini_x+(Disx*1)+25, y=Ini_y+(Disy*9))
        #Botones Restablecer
        P_R_Restablecer.place(bordermode=OUTSIDE, height=20, width=150, y=10, x= 90)
        P_R_Borrar_Historial.place(x=Ini_x+(Disx*0)+25, y=Ini_y+(Disy*0)-60)        
        P_R_Borrar_Bace_Datos.place(x=Ini_x+(Disx*0)+25, y=Ini_y+(Disy*2)-60)
        P_R_Valores_Fabrica.place(x=Ini_x+(Disx*0)+25, y=Ini_y+(Disy*4)-60)

        P_R_Aceptar_Res.place(x=Ini_x, y=Ini_y+330)
        
        #print "restableser"

def No_ver_Restablecer():
                
        #Botones Restablecer
        P_R_Restablecer.place_forget()
        P_R_Valores_Fabrica.place_forget()
        P_R_Borrar_Bace_Datos.place_forget()
        P_R_Borrar_Historial.place_forget()
        P_R_Aceptar_Res.place_forget()

def Torniquete():
        #Menu Principal
        No_ver_menu_principal()
        P_Menu.place(x=Ini_x+150, y=Ini_y+330)#P_Menu.place(x=Ini_x+(Disx*1)+25, y=Ini_y+(Disy*9))
        #Botones configuara torniquete
        P_C_Config_Torniquete.place(bordermode=OUTSIDE, height=20, width=150, y=10, x= 90)
        P_C_Salir_Izquierda.place(x=Ini_x+(Disx*0)+25, y=Ini_y+(Disy*0)-60) 
        P_C_Salir_Derecha.place(x=Ini_x+(Disx*0)+25, y=Ini_y+(Disy*1)-10)
        P_C_Aceptar_Tor.place(x=Ini_x, y=Ini_y+330)
        P_C_CTiempo_Torniquete.place(bordermode=OUTSIDE, height=20, width=150, x= Ini_x+(Disx*1)-10, y= Ini_y+(Disy*3)-40)
        texto = StringVar()
        texto.set(str(Tiempo_Torniquete))
        P_C_Tiempo_Torniquete.config(textvariable=texto)

        P_C_Tiempo_Torniquete.place(bordermode=OUTSIDE, height=20, width=150, x= Ini_x+(Disx*1)-10, y= Ini_y+(Disy*4)-40)
        P_C_Tiempo_Torniquete_incremento.place(x=Ini_x+(Disx*2)+15, y=Ini_y+(Disy*4)-60)
        P_C_Tiempo_Torniquete_decremento.place(x=Ini_x+(Disx*0)+25, y=Ini_y+(Disy*4)-60)
        
        
        #Botones torniquete

def No_ver_Torniquete():
                
        #Botones Restablecer
        P_C_Config_Torniquete.place_forget()
        P_C_Salir_Izquierda.place_forget()
        P_C_Salir_Derecha.place_forget()
        P_C_Aceptar_Tor.place_forget()
        P_C_CTiempo_Torniquete.place_forget()
        P_C_Tiempo_Torniquete.place_forget()
        P_C_Tiempo_Torniquete_incremento.place_forget()
        P_C_Tiempo_Torniquete_decremento.place_forget()

def Tor_Derecha():
        Borrar(13)
        Escrivir_Estados('D',13) #
def Tor_Izquierda():
        Borrar(13)
        Escrivir_Estados('I',13) #
        
def Valores_Fabrica():
        print 'valores de Fabrica'
        Base_Datos_Local()
        Borrar_Historial ()
        #estados de sensores y lecturas
        #led
        Borrar(10)      #led
        Escrivir_Estados('0',10)
        Borrar(3)      #Estado led
        Escrivir_Estados('0',3)
        #tecla
        Borrar(4)      #Esatado teclado
        Borrar(5)      #Teclas
        #chicharra
        Borrar(6)      #Esatado chicharra
        Escrivir_Estados('1',6)
        #Qr
        Borrar(7)      #QR
        Borrar(8)      #Estado QR
        Borrar(9)      #Estado sensor
        Escrivir_Estados('0',9)
        Borrar(11)      #Estado QR repetido
        #Torniquete
        Borrar(13)      #Direcion Torniquete
        Escrivir_Estados('D',13)
        #Tiempo Torniquete
        Borrar(30)      #Esatado chicharra
        Escrivir_Estados('1',30)
        
        #Escrivir_Estados(Estados,3)


def Base_Datos_Local():
        
        Borrar(0)       #borrar tabla servidor
        Borrar(1)       #borrar tabla lector
        Borrar(2)       #borrar tabla Enviar
        print 'Base datos borrado'

def Borrar_Historial():
       
       Borrar(12)       #Borrar Numero de lecturas
       Escrivir('0',12) #dejar en 0 las lecturas
       
       Borrar(14)       #Borrar Numero de Reinicios
       Escrivir('0',14) #dejar en 0 los reinicios
       print 'Historial borrado'

def Aceptar_reboot():
        commands.getoutput('sudo reboot')
        


def Multi_Torniquete():
        #Menu Principal
        No_ver_menu_principal()
        P_Menu.place(x=Ini_x+150, y=Ini_y+330)
        #Botones configuara torniquete

        M_T_Title.place(bordermode=OUTSIDE, height=20, width=160, x=80, y=10)
        M_T_lista.place(bordermode=OUTSIDE, height=29, width=200, x=60, y=40)
        #M_T_List.place(bordermode=OUTSIDE, height=20, width=100, y=60)

        M_T_Borrar_IP.place(bordermode=OUTSIDE, height=40, width=200, x=60, y=80)
        M_T_IPs.place(bordermode=OUTSIDE, height=20, width=30,x=15, y=135)
        M_T_IP.place(bordermode=OUTSIDE, height=30, width=200, x=60, y=130)
   
        M_T_but1.place(x=MIni_xip+(MDisxip*0), y=MIni_y+(MDisyip*1))
        M_T_but2.place(x=MIni_xip+(MDisxip*1), y=MIni_y+(MDisyip*1))
        M_T_but3.place(x=MIni_xip+(MDisxip*2), y=MIni_y+(MDisyip*1))
        M_T_but4.place(x=MIni_xip+(MDisxip*0), y=MIni_y+(MDisyip*2))
        M_T_but5.place(x=MIni_xip+(MDisxip*1), y=MIni_y+(MDisyip*2))        
        M_T_but6.place(x=MIni_xip+(MDisxip*2), y=MIni_y+(MDisyip*2))
        M_T_but7.place(x=MIni_xip+(MDisxip*0), y=MIni_y+(MDisyip*3))
        M_T_but8.place(x=MIni_xip+(MDisxip*1), y=MIni_y+(MDisyip*3))
        M_T_but9.place(x=MIni_xip+(MDisxip*2), y=MIni_y+(MDisyip*3))
        M_T_but0.place(x=MIni_xip+(MDisxip*0), y=MIni_y+(MDisyip*4))
        M_T_butb.place(x=MIni_xip+(MDisxip*1), y=MIni_y+(MDisyip*4))
        M_T_butp.place(x=MIni_xip+(MDisxip*2), y=MIni_y+(MDisyip*4))
        M_T_Aceptar_IP.place(x=MIni_xip, y=MDisyip+365)

        

def No_ver_Multi_Torniquete():
                
        #Botones Restablecer
        
        M_T_Title.place_forget()
        #M_T_List.place_forget()
        M_T_IPs.place_forget()
        M_T_IP.place_forget()
        M_T_lista.place_forget() 

        M_T_Borrar_IP.place_forget()
        M_T_but1.place_forget()
        M_T_but2.place_forget()
        M_T_but3.place_forget()
        M_T_but4.place_forget()
        M_T_but5.place_forget()
        M_T_but6.place_forget()
        M_T_but7.place_forget()
        M_T_but8.place_forget()
        M_T_but9.place_forget()
        M_T_but0.place_forget()
        M_T_butb.place_forget()
        M_T_butp.place_forget()
        M_T_Aceptar_IP.place_forget()
                
def Eliminar_IP_Dispostivos():
        
        Ip_dispostivo = M_T_lista.get()
        print Ip_dispostivo

        if (len(Ip_dispostivo)==0):
                top = Tk()
                top.geometry("+%d+%d" % (65,200))
                top.config(background='Red')
                top.title("Error")
                frame2 = Message(top, font='Arial', relief=RAISED, text='No selecciono una IP.',padx=50,pady=50,width=100, bg='Red')
                frame2.pack()
        else:
                M_T_lista["values"]= []
                IPs = Leer_Archivo(21)
                redes =IPs.split("\n")
                #print len(redes)

                for x1 in redes:                        
                        if len(x1) >= 3:
                                if x1.find(Ip_dispostivo):
                                        values = list(M_T_lista["values"])
                                        M_T_lista["values"]= values+ [x1]

                Borrar(21)
                for x1 in M_T_lista["values"]:
                        #print x1
                        Escrivir(x1,21)
                
                #Escrivir(Ip_dispostivo,21)
                #Actualizar_lista2()
                M_T_lista.select_clear()



def Agregar_IP_Dispostivos():
        Ip_dispostivo=M_T_IP.get()
        print Ip_dispostivo

        if (len(Ip_dispostivo)==0):
                top = Tk()
                top.geometry("+%d+%d" % (65,200))
                top.config(background='Red')
                top.title("Error")
                frame2 = Message(top, font='Arial', relief=RAISED, text='El campo esdta vacio.',padx=50,pady=50,width=100, bg='Red')
                frame2.pack()
        else :
                print 'verificacion ip valida'

                if (check_IP(Ip_dispostivo) == False) :
                        top = Tk()
                        top.geometry("+%d+%d" % (65,200))
                        top.config(background='Red')
                        top.title("Error")
                        frame2 = Message(top, font='Arial', relief=RAISED, text='NO es una IP valida.',padx=50,pady=50,width=100, bg='Red')
                        frame2.pack()
                else:
                        Valido =0
                        for x1 in M_T_lista["values"]:
                                print x1
                                if len(x1) >= 3:
                                        if x1.find(Ip_dispostivo) != -1:
                                                Valido = 1
                                                #print 'existe'
                        if Valido == 1:
                                top = Tk()
                                top.geometry("+%d+%d" % (65,200))
                                top.config(background='Red')
                                top.title("Error")
                                frame2 = Message(top, font='Arial', relief=RAISED, text='Existe esta IP',padx=50,pady=50,width=100, bg='Red')
                                frame2.pack()
                        else:
                                Escrivir(Ip_dispostivo,21)
                                #Actualizar_lista2()
                                M_T_lista.select_clear()
                    

def desplegar2(event):
        Actualizar_lista2()
        #print 'desplicada'
        return 0
        
def Actualizar_lista2():
        
        M_T_lista["values"]= []
        IPs = Leer_Archivo(21)
        redes =IPs.split("\n")

        
        for x1 in redes: 

                values = list(M_T_lista["values"])
                M_T_lista["values"]= values+ [x1]

def desplegar_IP_Static(event):
        L_Ip_Static_lista["values"]= []

        L_Ip_Static_lista["values"]= ["Ethernet","WIFI"]
        
        
        
        return 0
      
#-----------------------------------
#-----          Definiciones    ----
#-----------------------------------

#----------------------------------------
#-----          Pagina Menu Inicio   ----
#----------------------------------------

L_Menu_Principal = Label(tk, font='Arial', bg='Dark gray', text="MENU PRINCIPAL")
P_wifi = Button(tk,padx=DX_b-54,pady=DY_b,bd=BD,command=V_wifi_Minusculas,text="Configurar Wifi",font=Fuente)
P_IP = Button(tk,padx=DX_b-75,pady=DY_b,bd=BD,command=V_IP,text="IP Estatica Ethernet",font=Fuente)
P_Restablecer = Button(tk,padx=DX_b-95,pady=DY_b,bd=BD,command=Restablecer,text="Restablacer Dispositivo",font=Fuente)
P_Confi_Torniquete = Button(tk,padx=DX_b-89,pady=DY_b,bd=BD,command=Torniquete,text="Configurar Torniquete",font=Fuente)
P_Confi_Multi_Dispositivo = Button(tk,padx=DX_b-62,pady=DY_b,bd=BD,command=Multi_Torniquete,text="Multi Torniquete",font=Fuente)
P_salir = Button(tk,padx=DX_b-5,pady=DY_b,bd=BD,command=salir,text="Salir",font=Fuente)

P_Menu = Button(tk,padx=DX-14,pady=DY-10,bd=BD,command=L_menu_inicio,text="Menu Inicio",font=Fuente)

ver_menu_principal()

#P_IP.place(x=Ini_x+(Disx*1)+25, y=Ini_y+(Disy*9))
#-------------------------------------------
#-----          Pagina Ip Static        ----
#-------------------------------------------
L_Ip_Static = Label(tk, font='Arial', bg='Dark gray', text="IP STATIC")
L_Ip_Static_lista = ttk.Combobox(tk, font=Fuente2, width=15,height=16, state="readonly")
L_Ip_Static_lista.bind("<Button-1>",desplegar_IP_Static)
L_Ip = Label(tk, font='Arial', bg='Dark gray', text="IP: ")
L_Gat = Label(tk, font='Arial', bg='Dark gray', text="Gateway: ")
IP=Entry(tk, font='Arial',textvar=textin)
Gateway=Entry(tk, font='Arial',textvar=textin2) # , show='*'se escoge encriptar con * la contraseña
but1=Button(tk,padx=DXip,pady=DYip,bd=BD,bg='white',command=lambda:clickbut('1'),text='1',font=Fuenteip)
but2=Button(tk,padx=DXip,pady=DYip,bd=BD,bg='white',command=lambda:clickbut('2'),text='2',font=Fuenteip)
but3=Button(tk,padx=DXip,pady=DYip,bd=BD,bg='white',command=lambda:clickbut('3'),text='3',font=Fuenteip)
but4=Button(tk,padx=DXip,pady=DYip,bd=BD,bg='white',command=lambda:clickbut('4'),text='4',font=Fuenteip)
but5=Button(tk,padx=DXip,pady=DYip,bd=BD,bg='white',command=lambda:clickbut('5'),text='5',font=Fuenteip)
but6=Button(tk,padx=DXip,pady=DYip,bd=BD,bg='white',command=lambda:clickbut('6'),text='6',font=Fuenteip)
but7=Button(tk,padx=DXip,pady=DYip,bd=BD,bg='white',command=lambda:clickbut('7'),text='7',font=Fuenteip)
but8=Button(tk,padx=DXip,pady=DYip,bd=BD,bg='white',command=lambda:clickbut('8'),text='8',font=Fuenteip)
but9=Button(tk,padx=DXip,pady=DYip,bd=BD,bg='white',command=lambda:clickbut('9'),text='9',font=Fuenteip)
but0=Button(tk,padx=DXip,pady=DYip,bd=BD,bg='white',command=lambda:clickbut('0'),text='0',font=Fuenteip)
butp=Button(tk,padx=DXip+4,pady=DYip,bd=BD,bg='white',command=lambda:clickbut('.'),text='.',font=Fuenteip)
butb=Button(tk,padx=DXip-6,pady=DYip,bd=BD,bg='white',command=lambda:clickbut('◄'),text='◄',font=Fuenteip)
Aceptar_IP = Button(tk,padx=DX,pady=DY-10,bd=BD,command=verificar_IP_Static,text="Aceptar",font=Fuente)
#Cancelar_IP = Button(tk,padx=DX,pady=DY,bd=BD,command=salir,text="Cancelar",font=Fuente)


#-------------------------------------------
#-----          Pagina Wifi             ----
#-------------------------------------------




L_wifi = Label(tk, font='Arial', bg='Dark gray', text="WIFI")
L_password = Label(tk, font='Arial', bg='Dark gray', text="Password")

lista = ttk.Combobox(tk, font=Fuente2, width=15,height=16, state="readonly")
#lista.Combobox(tk, postcomand=desplagar)
lista.bind("<Button-1>",desplegar)

wifi=Entry(tk, font='Arial',textvar=textin3)
contrasena=Entry(tk, font='Arial',textvar=textin4) # , show='*'se escoge encriptar con * la contraseña
Aceptar_W = Button(tk,padx=DX,pady=DY-10,bd=BD,command=verificar_wifi,text="Aceptar",font=Fuente)

butqw=Button(tk,padx=DXw,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('q'),text='q',font=Fuentew)
butww=Button(tk,padx=DXw-1,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('w'),text='w',font=Fuentew)
butew=Button(tk,padx=DXw+1,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('e'),text='e',font=Fuentew)
butrw=Button(tk,padx=DXw+3,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('r'),text='r',font=Fuentew)
buttw=Button(tk,padx=DXw+4,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('t'),text='t',font=Fuentew)
butyw=Button(tk,padx=DXw+1,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('y'),text='y',font=Fuentew)
butuw=Button(tk,padx=DXw,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('u'),text='u',font=Fuentew)
butiw=Button(tk,padx=DXw+4,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('i'),text='i',font=Fuentew)
butow=Button(tk,padx=DXw,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('o'),text='o',font=Fuentew)
butpw=Button(tk,padx=DXw,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('p'),text='p',font=Fuentew)
butaw=Button(tk,padx=DXw+1,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('a'),text='a',font=Fuentew)
butsw=Button(tk,padx=DXw+1,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('s'),text='s',font=Fuentew)
butdw=Button(tk,padx=DXw,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('d'),text='d',font=Fuentew)
butfw=Button(tk,padx=DXw+4,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('f'),text='f',font=Fuentew)
butgw=Button(tk,padx=DXw,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('g'),text='g',font=Fuentew)
buthw=Button(tk,padx=DXw,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('h'),text='h',font=Fuentew)
butjw=Button(tk,padx=DXw+4,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('j'),text='j',font=Fuentew)
butkw=Button(tk,padx=DXw+1,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('k'),text='k',font=Fuentew)
butlw=Button(tk,padx=DXw+5,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('l'),text='l',font=Fuentew)
butzw=Button(tk,padx=DXw+1,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('z'),text='z',font=Fuentew)
butxw=Button(tk,padx=DXw+1,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('x'),text='x',font=Fuentew)
butcw=Button(tk,padx=DXw+1,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('c'),text='c',font=Fuentew)
butvw=Button(tk,padx=DXw+1,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('v'),text='v',font=Fuentew)
butbw=Button(tk,padx=DXw,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('b'),text='b',font=Fuentew)
butnw=Button(tk,padx=DXw,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('n'),text='n',font=Fuentew)
butmw=Button(tk,padx=DXw-4,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('m'),text='m',font=Fuentew)
butespw=Button(tk,padx=DXw+68,pady=DYw,bd=BD,bg='white',command=lambda:clickbut(' '),text=' ',font=Fuentew)



butMYw=Button(tk,padx=DXw-4,pady=DYw,bd=BD,bg='white',command=V_wifi_May_Minu,text='▲',font=Fuentew)
but123w=Button(tk,padx=DXw+9,pady=DYw,bd=BD,bg='white',command=V_wifi_Numeros,text='123?',font=Fuentew)
butabcw=Button(tk,padx=DXw+17,pady=DYw,bd=BD,bg='white',command=V_wifi_Minusculas,text='ABC',font=Fuentew)
#butbw=Button(tk,padx=DXw,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('b'),text='b',font=Fuente)
butBow=Button(tk,padx=DXw-4,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('◄'),text='◄',font=Fuentew)
#◄ ▲ ► ▼


butQw=Button(tk,padx=DXw-1,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('Q'),text='Q',font=Fuentew)
butWw=Button(tk,padx=DXw-2,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('W'),text='W',font=Fuentew)
butEw=Button(tk,padx=DXw,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('E'),text='E',font=Fuentew)
butRw=Button(tk,padx=DXw,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('R'),text='R',font=Fuentew)
butTw=Button(tk,padx=DXw-1,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('T'),text='T',font=Fuentew)
butYw=Button(tk,padx=DXw,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('Y'),text='Y',font=Fuentew)
butUw=Button(tk,padx=DXw,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('U'),text='U',font=Fuentew)
butIw=Button(tk,padx=DXw+4,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('I'),text='I',font=Fuentew)
butOw=Button(tk,padx=DXw-1,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('O'),text='O',font=Fuentew)
butPw=Button(tk,padx=DXw-1,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('P'),text='P',font=Fuentew)
butAw=Button(tk,padx=DXw,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('A'),text='A',font=Fuentew)
butSw=Button(tk,padx=DXw,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('S'),text='S',font=Fuentew)
butDw=Button(tk,padx=DXw,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('D'),text='D',font=Fuentew)
butFw=Button(tk,padx=DXw,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('F'),text='F',font=Fuentew)
butGw=Button(tk,padx=DXw-2,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('G'),text='G',font=Fuentew)
butHw=Button(tk,padx=DXw,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('H'),text='H',font=Fuentew)
butJw=Button(tk,padx=DXw+1,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('J'),text='J',font=Fuentew)
butKw=Button(tk,padx=DXw,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('K'),text='K',font=Fuentew)
butLw=Button(tk,padx=DXw,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('L'),text='L',font=Fuentew)
butZw=Button(tk,padx=DXw,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('Z'),text='Z',font=Fuentew)
butXw=Button(tk,padx=DXw,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('X'),text='X',font=Fuentew)
butCw=Button(tk,padx=DXw,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('C'),text='C',font=Fuentew)
butVw=Button(tk,padx=DXw,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('V'),text='V',font=Fuentew)
butBw=Button(tk,padx=DXw-1,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('B'),text='B',font=Fuentew)
butNw=Button(tk,padx=DXw-1,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('N'),text='N',font=Fuentew)
butMw=Button(tk,padx=DXw-2,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('M'),text='M',font=Fuentew)


but1w=Button(tk,padx=DXw,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('1'),text='1',font=Fuentew)
but2w=Button(tk,padx=DXw,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('2'),text='2',font=Fuentew)
but3w=Button(tk,padx=DXw,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('3'),text='3',font=Fuentew)
but4w=Button(tk,padx=DXw,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('4'),text='4',font=Fuentew)
but5w=Button(tk,padx=DXw,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('5'),text='5',font=Fuentew)
but6w=Button(tk,padx=DXw,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('6'),text='6',font=Fuentew)
but7w=Button(tk,padx=DXw,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('7'),text='7',font=Fuentew)
but8w=Button(tk,padx=DXw,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('8'),text='8',font=Fuentew)
but9w=Button(tk,padx=DXw,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('9'),text='9',font=Fuentew)
but0w=Button(tk,padx=DXw,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('0'),text='0',font=Fuentew)

butA1w=Button(tk,padx=DXw,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('#'),text='#',font=Fuentew)
butS2w=Button(tk,padx=DXw-2,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('&'),text='&',font=Fuentew)
butD3w=Button(tk,padx=DXw+3,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('/'),text='/',font=Fuentew)
butF4w=Button(tk,padx=DXw+2,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('-'),text='-',font=Fuentew)
butG5w=Button(tk,padx=DXw,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('_'),text='_',font=Fuentew)
butH6w=Button(tk,padx=DXw,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('+'),text='+',font=Fuentew)
butJ7w=Button(tk,padx=DXw+2,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('('),text='(',font=Fuentew)
butK8w=Button(tk,padx=DXw+3,pady=DYw,bd=BD,bg='white',command=lambda:clickbut(')'),text=')',font=Fuentew)
butL9w=Button(tk,padx=DXw+2,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('*'),text='*',font=Fuentew)
butZ0w=Button(tk,padx=DXw+3,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('.'),text='.',font=Fuentew)
butX1w=Button(tk,padx=DXw+3,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('!'),text='!',font=Fuentew)
butC2w=Button(tk,padx=DXw-1,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('?'),text='?',font=Fuentew)
butV3w=Button(tk,padx=DXw-3,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('@'),text='@',font=Fuentew)
butB4w=Button(tk,padx=DXw+2,pady=DYw,bd=BD,bg='white',command=lambda:clickbut(':'),text=':',font=Fuentew)
butN5w=Button(tk,padx=DXw+2,pady=DYw,bd=BD,bg='white',command=lambda:clickbut(';'),text=';',font=Fuentew)
#butMw=Button(tk,padx=DXw,pady=DYw,bd=BD,bg='white',command=lambda:clickbut('M'),text='M',font=Fuente)

#but0=Button(tk,padx=DX,pady=DY,bd=BD,bg='white',command=lambda:clickbut('0'),text='0',font=Fuente)
#butp=Button(tk,padx=DX+3,pady=DY,bd=BD,bg='white',command=lambda:clickbut('.'),text='.',font=Fuente)
#Aceptar_IP = Button(tk,padx=DX+5,pady=DY,bd=BD,command=verificar,text="Aceptar",font=Fuente)
#Cancelar_IP = Button(tk,padx=DX,pady=DY,bd=BD,command=salir,text="Cancelar",font=Fuente)


#-------------------------------------------
#-----          Pagina Restablecer      ----
#-------------------------------------------
P_R_Restablecer = Label(tk, font='Arial', bg='Dark gray', text="RESTABLECER")
P_R_Valores_Fabrica = Button(tk,padx=DX_b-65,pady=DY_b,bd=BD,command=Valores_Fabrica,text="Valores de Fabrica",font=Fuente)
P_R_Borrar_Bace_Datos = Button(tk,padx=DX_b-70,pady=DY_b,bd=BD,command=Base_Datos_Local,text="Base de datos local",font=Fuente)
P_R_Borrar_Historial = Button(tk,padx=DX_b-50,pady=DY_b,bd=BD,command=Borrar_Historial,text="Borrar Historial",font=Fuente)
P_R_Aceptar_Res = Button(tk,padx=DX,pady=DY-10,bd=BD,command=Aceptar_reboot,text="Aceptar",font=Fuente)

#-------------------------------------------
#-----          Pagina Configuracion torniquete      ----
#-------------------------------------------
P_C_Config_Torniquete = Label(tk, font='Arial', bg='Dark gray', text="Configurar Torniquete")
P_C_Salir_Izquierda = Button(tk,padx=DX_b-70,pady=DY_b,bd=BD,command=Tor_Izquierda,text="Salir por la Izquierda",font=Fuente)
P_C_Salir_Derecha = Button(tk,padx=DX_b-66,pady=DY_b,bd=BD,command=Tor_Derecha,text="Salir por la Derecha",font=Fuente)
P_C_Aceptar_Tor = Button(tk,padx=DX,pady=DY-10,bd=BD,command=Aceptar_reboot,text="Aceptar",font=Fuente)
P_C_CTiempo_Torniquete = Label(tk, font='Arial', bg='Dark gray', text="Tiempo Relevador")
P_C_Tiempo_Torniquete = Label(tk, font=Fuenteip, bg='Dark gray', text="1")
P_C_Tiempo_Torniquete_incremento=Button(tk,padx=DX-6,pady=DY,bd=BD,bg='white',command=lambda:clickbut_Tiempo('►'),text='►',font=Fuenteip)
P_C_Tiempo_Torniquete_decremento=Button(tk,padx=DX-6,pady=DY,bd=BD,bg='white',command=lambda:clickbut_Tiempo('◄'),text='◄',font=Fuenteip)

#R_but0=Button(tk,padx=DX,pady=DY,bd=BD,bg='white',command=lambda:clickbut('0'),text='0',font=Fuente)
#R_butp=Button(tk,padx=DX+3,pady=DY,bd=BD,bg='white',command=lambda:clickbut('.'),text='.',font=Fuente)


#-------------------------------------------
#-----          Pagina Multi Tornique       ----
#-------------------------------------------

M_T_Title = Label(tk, font='Arial', bg='Dark gray', text="IP, Torniquetes")
#M_T_List = Label(tk, font='Arial', bg='Dark gray', text="Listado")
M_T_IPs = Label(tk, font='Arial', bg='Dark gray', text="IP:")
M_T_lista = ttk.Combobox(tk, font=Fuente2, width=15,height=16, state="readonly")
M_T_lista.bind("<Button-1>",desplegar2)

M_T_IP=Entry(tk, font='Arial',textvar=textin5)

M_T_Borrar_IP = Button(tk,padx=DX,pady=DY-10,bd=BD,command=Eliminar_IP_Dispostivos,text="Eliminar IP",font=Fuente)
M_T_but1=Button(tk,padx=DXip,pady=DYip,bd=BD,bg='white',command=lambda:clickbut('1'),text='1',font=Fuenteip)
M_T_but2=Button(tk,padx=DXip,pady=DYip,bd=BD,bg='white',command=lambda:clickbut('2'),text='2',font=Fuenteip)
M_T_but3=Button(tk,padx=DXip,pady=DYip,bd=BD,bg='white',command=lambda:clickbut('3'),text='3',font=Fuenteip)
M_T_but4=Button(tk,padx=DXip,pady=DYip,bd=BD,bg='white',command=lambda:clickbut('4'),text='4',font=Fuenteip)
M_T_but5=Button(tk,padx=DXip,pady=DYip,bd=BD,bg='white',command=lambda:clickbut('5'),text='5',font=Fuenteip)
M_T_but6=Button(tk,padx=DXip,pady=DYip,bd=BD,bg='white',command=lambda:clickbut('6'),text='6',font=Fuenteip)
M_T_but7=Button(tk,padx=DXip,pady=DYip,bd=BD,bg='white',command=lambda:clickbut('7'),text='7',font=Fuenteip)
M_T_but8=Button(tk,padx=DXip,pady=DYip,bd=BD,bg='white',command=lambda:clickbut('8'),text='8',font=Fuenteip)
M_T_but9=Button(tk,padx=DXip,pady=DYip,bd=BD,bg='white',command=lambda:clickbut('9'),text='9',font=Fuenteip)
M_T_but0=Button(tk,padx=DXip,pady=DYip,bd=BD,bg='white',command=lambda:clickbut('0'),text='0',font=Fuenteip)
M_T_butp=Button(tk,padx=DXip+4,pady=DYip,bd=BD,bg='white',command=lambda:clickbut('.'),text='.',font=Fuenteip)
M_T_butb=Button(tk,padx=DXip-6,pady=DYip,bd=BD,bg='white',command=lambda:clickbut('◄'),text='◄',font=Fuenteip)

M_T_Aceptar_IP = Button(tk,padx=DX,pady=DY-10,bd=BD,command=Agregar_IP_Dispostivos,text="Agregar",font=Fuente)

#Cancelar_IP = Button(tk,padx=DX,pady=DY,bd=BD,command=salir,text="Cancelar",font=Fuente)
#Modificar_Archivo1(1,0)
#while 1:
#        a=0
        
#-----------------------------------
#-----  Bucle principal         ----
#-----------------------------------
tk.mainloop()
