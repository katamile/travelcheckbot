# Importar librerias
import os
import time
import subprocess
from viaje import Viaje
# Importar desde librerias
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler, ConversationHandler, CallbackQueryHandler)
# AGREGAR A VIAJE NUMERO DE PERSONA PARA MOSTRAR AL FINAL -----
v1 = Viaje("tame","GUAYAQUIL", "QUITO", "40 minutos",400,"f1","f2","0","/GYEUIO")
v2 = Viaje("Latan","GUAYAQUIL", "GALAPAGOS","120 minutos",1555,"f1","f2","0","/GYESCY")
v3 = Viaje("Latan","GUAYAQUIL", "CUENCA", "90 minutos",900,"f1","f2","0","/GYECUE")
v4 = Viaje("Latan","GUAYAQUIL", "MANTA", "60 minutos",200,"f1","f2","0","/GYEMEC")     #---
v5 = Viaje("Latan","GUAYAQUIL", "ISLA BALTRA","145 minutos",1000,"f1","f2","0","/GYEGPS") #
v6 = Viaje("Tame","GUAYAUIL", "BUENOS AIRES","330 minutos",2000,"f1","f2","0","/GYEBHI") #
v7 = Viaje("Latan","GUAYAQUIL", "CÓRDOVA", "360 minutos",2200,"f1","f2","0","/GYECOR") #
v8 = Viaje("AZUL LINHAS","GUAYAQUIL","BRASIL","400 minutos",2000,"f1","f2","0","/GYEBR")#
v9 = Viaje("FLYBE","GUAYAQUIL","MEXICO","600 minutos",1000,"f1","f2","0","/GYEMX")#
v10 =Viaje("TAME","QUITO","COLOMBIA","600 minutos",1200,"f1","f2","0","/UIOCO")#
v11 =Viaje("LAN ECUADOR","QUITO","MEXICO","700 minutos",2000,"f1","f2","0","/UIOMX")
v12 =Viaje("AIR CANADA","QUITO","CANADA","900 minutos,",4000,"f1","f2","0","/UIOCA")
v13 =Viaje("AIR EUROPE","QUITO","RUSIA","700 minutos,",4300,"f1","f2","0","/UIORU")
v14 =Viaje("AIR EUROPE","QUITO","MURCIA","550 minutos,",3400,"f1","f2","0","/UIOMUC")
v15 = Viaje("AVIANCA","CUENCA","BRASIL","500 minutos",1300,"f1","f2","0","/CUEBR")
v16 = Viaje("LAN ECUADOR","CUENCA","VENEZUELA","400 minutos",1000,"f1","f2","0","/CUEVE")
v17 = Viaje("TAME","CUENCA","MEXICO","550 minutos",2300,"f1","f2","0","/CUEMX")
v18 = Viaje("TAME","CUENCA","CIUDAD DE MEXICO","660 minutos",3000,"f1","f2","0","/CUEMEX")
v19 = Viaje("LAN ECUADOR","CUENCA","QUITO","45 minutos",300,"f1","f2","0","/CUEUIO")#
v20 = Viaje("AMERICAN AIRLINES","GUAYAQUIL","MIAMI","500 minutos",2333,"f1","f2","0","/GYEMIA")
v21 = Viaje("AIR EUROPE","GUAYAQUIL","MENORCA","555 minutos",3400,"f1","f2","0","/GYEMAH")
v22 = Viaje("LAN ECUADOR","GUAYAQUIL","MEDALLIN","400 minutos",2300,"f1","f2","0","/GYEMDE")
v23 = Viaje("AIR EUROPE","GUAYAQUIL","MOSCU","590 minutos",5000,"f1","f2","0","/GYEMOW")
v24 = Viaje("AIR CANADA","GUAYAQUIL","MONTREAL","540 minutos",3000,"f1","f2","0","/GYEYUL")#
v25 = Viaje("LAN ECUADOR","MANTA","GUAYAQUIL","40 minutos",90,"f1","f2","0","/MECGYE")
v26 = Viaje("LAN ECUADOR","MANTA","QUITO","80 minutos",99,"f1","f2","0","/MECUIO")
v27 = Viaje("LAN ECUADOR","MANTA","CUENCA","85 minutos",89,"f1","f2","0","/MECCUE")
v28 = Viaje("LAN ECUADOR","GALAPAGOS","GUAYAQUIL","90 minutos",900,"f1","f2","0","/GPSGYE")
v29 = Viaje("LAN ECUADOR","GALAPAGOS","CUENCA","90 minutos",890,"f1","f2","0","/GPSCUE")
v30 = Viaje("LAN ECUADOR","GALAPAGOS","QUITO","89 minutos",800,"f1","f2","0","/GPSUIO")
v31 = Viaje("AIR CHINA","GUAYAQUIL","CHINA","900 minutos",3400,"f1","f2","0","/GYECN")
v32 = Viaje("AIR CHINA","CUENCA","CHINA","990 minutos",3400,"f1","f2","0","/CUECN")
v33 = Viaje("LAN ECUADOR","CUENCA","COLOMBIA","80 minutos",580,"f1","f2","0","/CUECO")
v34 = Viaje("LAN ECUADOR","CUENCA","MANTA","50 minutos",300,"f1","f2","0","/CUEMEC")
v35 = Viaje("AIR JAPON","GUAYAQUIL","JAPON","500 minutos",5000,"f1","f2","0","/GYEJP")
v36 = Viaje("AMERICAN AIRLINES","GUAYAQUIL","ESTADOS UNIDOS","200 minutos",2300,"f1","f2","0","/GYEUS")
v37 = Viaje("AMERICAN AIRLINES","CUENCA","ESTADOS UNIDOS","230 minutos",2500,"f1","f2","0","/CUEUS")
v38 = Viaje("AIR EUROPE","GUAYAQUIL","AUSTRALIA","900 minutos",5000,"f1","f2","0","/GYEAU")
v39 = Viaje("LAN ECUADOR","GUAYAQUIL","PER�","99 minutos",250,"f1","f2","0","/GYEPE")
v40 = Viaje("AIR EUROPE","GUAYAQUIL","UCRANIA","500 minutos",5000,"f1","f2","0","/GYEUA")


ncliente=""
esperando_ruta = 0

bv = False
idv=False
v=[]
of=[]
ff=[]
vtt=Viaje
c=""
tt=0
n=0

of.append(v1)
of.append(v2)
of.append(v3)
of.append(v4)
of.append(v5)
of.append(v6)
of.append(v7)
of.append(v8)
of.append(v9)
of.append(v10)
of.append(v11)
of.append(v12)
of.append(v13)
of.append(v14)
of.append(v15)
of.append(v16)
of.append(v17)
of.append(v18)
of.append(v19)
of.append(v20)
of.append(v21)
of.append(v22)
of.append(v23)
of.append(v24)
of.append(v25)

##############################

TOKEN = "1660343055:AAGEpAH8djmuFw6REpUJZ4B52tW0sBmaZns"  # A establecer por el usuario (consultar mediante @BotFather)
 # A establecer por el usuario (consultar mediante @get_id_bot)

# Comandos recibidos

# Manejador correspondiente al comando /inicio
def start(bot, update):
  # Solo hacer caso si quien le habla es el remitente correspondiente a dicha ID
    update.message.reply_text("BIENVENIDO A AL BOT DE VIAJES ....\n")
    update.message.reply_text("-Para Listar viajes pulse --> \t/Listar"+"\n-Para Buscar viajes pulse --> \t/Busqueda"
                              +"\n-Para Comprar viajes solo IDA  pulse --> \t/Ida"+"\n-Para Comprar viajes solo Ida y Vuelta pulse -->\t/IdayVuelta"
                              +"\n-Para conocer los comandos implementados consulta la /ayuda")
# Manejador correspondiente al comando /ayuda
def ayuda(bot, update):
      # Solo hacer caso si quien le habla es el remitente correspondiente a dicha ID
        update.message.reply_text(
            "Lista de comandos implementados: \n\n/inicio - Comando de inicio\n\n/ayuda - Consulta la lista de comandos implementados y la descripcion de estos\n\n/Listar - Lista todos los vuelos disponibles \n\n/Busqueda - Busca viajes por Origen\n\n/Ida - Permite comprar Vuelos de Ida\n\n/IdayVuelta - Permite comprar vuelos de Ida y Vuelta")

##############################
def Ida(bot,update):
    global idv
    idv = False
    update.message.reply_text("Para elegir un vuelo solo de click en el comando ejemplo / GYEUIO")
    for b in of:
     update.message.reply_text("Origen :"+b.origen+ "\nDestino :"+b.destino+"\nAerolínea:"+b.aerolinea+"\nPrecio:"+str(b.precio)+"$"+"\nDuracion:"+b.duracion+"\n" +b.cod)

##------------------------------- Funciones de cada viaje codigo iata ----------------------------
def GYEUIO(bot,update):
    global vtt,idv
    vtt = Viaje(of[0].aerolinea,of[0].origen,of[0].destino,of[0].duracion,of[0].precio,of[0].fecha1,of[0].fecha2,of[0].npersona,of[0].cod)
    update.message.reply_text("Origen :" +vtt.origen+ "\nDestino :" + vtt.destino+"\nAerolinea :"+vtt.aerolinea+"\nPrecio:" +str(vtt.precio)+"$" + "\nDuracion:"+vtt.duracion)
    update.message.reply_text("A continuacion escriba /fechaida (000-00-00)\n Ejemplo /fechaida 2020-10-09 ") #año -mes-dia
    if idv == True:
        update.message.reply_text("A continuacion escriba /fechavuelta (000-00-00)\n Ejemplo /fechavuelta 2020-10-09 ")  # año -mes-dia

def GYESCY(bot,update):
    global vtt,idv
    vtt = Viaje(of[1].aerolinea,of[1].origen,of[1].destino,of[1].duracion,of[1].precio,of[1].fecha1,of[1].fecha2,of[1].npersona,of[1].cod)
    update.message.reply_text("Origen :" +vtt.origen+ "\nDestino :" + vtt.destino+"\nAerolinea :"+vtt.aerolinea+"\nPrecio:" +str(vtt.precio)+"$" + "\nDuracion:"+vtt.duracion)
    update.message.reply_text("A continuacion escriba /fechaida (000-00-00)\n Ejemplo /fechaida 2020-10-09 ") #año -mes-dia
    if idv == True:
        update.message.reply_text("A continuacion escriba /fechavuelta (000-00-00)\n Ejemplo /fechavuelta 2020-10-09 ")  # año -mes-dia
def GYECUE(bot,update):
    global vtt,idv
    vtt = Viaje(of[2].aerolinea,of[2].origen,of[2].destino,of[2].duracion,of[2].precio,of[2].fecha1,of[2].fecha2,of[2].npersona,of[2].cod)
    update.message.reply_text("Origen :" +vtt.origen+ "\nDestino :" + vtt.destino+"\nAerolinea :"+vtt.aerolinea+"\nPrecio:" +str(vtt.precio)+"$" + "\nDuracion:"+vtt.duracion)
    update.message.reply_text("A continuacion escriba /fechaida (000-00-00)\n Ejemplo /fechaida 2020-10-09 ") #año -mes-dia
    if idv == True:
        update.message.reply_text("A continuacion escriba /fechavuelta (000-00-00)\n Ejemplo /fechavuelta 2020-10-09 ")  # año -mes-dia
def GYEMEC(bot,update):
    global vtt,idv
    vtt = Viaje(of[3].aerolinea,of[3].origen,of[3].destino,of[3].duracion,of[3].precio,of[3].fecha1,of[3].fecha2,of[3].npersona,of[3].cod)
    update.message.reply_text("Origen :" +vtt.origen+ "\nDestino :" + vtt.destino+"\nAerolinea :"+vtt.aerolinea+"\nPrecio:" +str(vtt.precio)+"$" + "\nDuracion:"+vtt.duracion)
    update.message.reply_text("A continuacion escriba /fechaida (000-00-00)\n Ejemplo /fechaida 2020-10-09 ") #año -mes-dia
    if idv == True:
        update.message.reply_text("A continuacion escriba /fechavuelta (000-00-00)\n Ejemplo /fechavuelta 2020-10-09 ")  # año -mes-dia


def GYEGPS(bot,update):
    global vtt,idv
    vtt = Viaje(of[4].aerolinea,of[4].origen,of[4].destino,of[4].duracion,of[4].precio,of[4].fecha1,of[4].fecha2,of[4].npersona,of[4].cod)
    update.message.reply_text("Origen :" +vtt.origen+ "\nDestino :" + vtt.destino+"\nAerolinea :"+vtt.aerolinea+"\nPrecio:" +str(vtt.precio)+"$" + "\nDuracion:"+vtt.duracion)
    update.message.reply_text("A continuacion escriba /fechaida (000-00-00)\n Ejemplo /fechaida 2020-10-09 ") #año -mes-dia
    if idv == True:
        update.message.reply_text("A continuacion escriba /fechavuelta (000-00-00)\n Ejemplo /fechavuelta 2020-10-09 ")  # año -mes-dia

def GYEBHI(bot, update):
        global vtt, idv
        vtt =Viaje(of[5].aerolinea,of[5].origen,of[5].destino,of[5].duracion,of[5].precio,of[5].fecha1,of[5].fecha2,of[5].npersona,of[5].cod)
        update.message.reply_text(
            "Origen :" + vtt.origen + "\nDestino :" + vtt.destino + "\nAerolinea :" + vtt.aerolinea + "\nPrecio:" + str(
                vtt.precio) + "$" + "\nDuracion:" + vtt.duracion)
        update.message.reply_text(
            "A continuacion escriba /fechaida (000-00-00)\n Ejemplo /fechaida 2020-10-09 ")  # año -mes-dia
        if idv == True:
            update.message.reply_text(
                "A continuacion escriba /fechavuelta (000-00-00)\n Ejemplo /fechavuelta 2020-10-09 ")  # año -mes-dia


def GYECOR(bot, update):
    global vtt, idv
    vtt =Viaje(of[6].aerolinea,of[6].origen,of[6].destino,of[6].duracion,of[6].precio,of[6].fecha1,of[6].fecha2,of[6].npersona,of[6].cod)
    update.message.reply_text(
        "Origen :" + vtt.origen + "\nDestino :" + vtt.destino + "\nAerolinea :" + vtt.aerolinea + "\nPrecio:" + str(
            vtt.precio) + "$" + "\nDuracion:" + vtt.duracion)
    update.message.reply_text(
        "A continuacion escriba /fechaida (000-00-00)\n Ejemplo /fechaida 2020-10-09 ")  # año -mes-dia
    if idv == True:
        update.message.reply_text(
            "A continuacion escriba /fechavuelta (000-00-00)\n Ejemplo /fechavuelta 2020-10-09 ")  # año -mes-dia

def GYEBR(bot, update):
    global vtt, idv
    vtt =Viaje(of[7].aerolinea,of[7].origen,of[7].destino,of[7].duracion,of[7].precio,of[7].fecha1,of[7].fecha2,of[7].npersona,of[7].cod)
    update.message.reply_text(
        "Origen :" + vtt.origen + "\nDestino :" + vtt.destino + "\nAerolinea :" + vtt.aerolinea + "\nPrecio:" + str(
            vtt.precio) + "$" + "\nDuracion:" + vtt.duracion)
    update.message.reply_text(
        "A continuacion escriba /fechaida (000-00-00)\n Ejemplo /fechaida 2020-10-09 ")  # año -mes-dia
    if idv == True:
        update.message.reply_text(
            "A continuacion escriba /fechavuelta (000-00-00)\n Ejemplo /fechavuelta 2020-10-09 ")  # año -mes-dia


def GYEMX(bot, update):
    global vtt, idv
    vtt = Viaje(of[8].aerolinea, of[8].origen, of[8].destino, of[8].duracion, of[8].precio, of[8].fecha1, of[8].fecha2,of[8].npersona, of[8].cod)
    update.message.reply_text(
        "Origen :" + vtt.origen + "\nDestino :" + vtt.destino + "\nAerolinea :" + vtt.aerolinea + "\nPrecio:" + str(
            vtt.precio) + "$" + "\nDuracion:" + vtt.duracion)
    update.message.reply_text(
        "A continuacion escriba /fechaida (000-00-00)\n Ejemplo /fechaida 2020-10-09 ")  # año -mes-dia
    if idv == True:
        update.message.reply_text(
            "A continuacion escriba /fechavuelta (000-00-00)\n Ejemplo /fechavuelta 2020-10-09 ")  # año -mes-dia

def UIOCO(bot, update):
    global vtt, idv
    vtt = Viaje(of[9].aerolinea, of[9].origen, of[9].destino, of[9].duracion, of[9].precio, of[9].fecha1, of[9].fecha2,
                of[9].npersona, of[9].cod)
    update.message.reply_text(
        "Origen :" + vtt.origen + "\nDestino :" + vtt.destino + "\nAerolinea :" + vtt.aerolinea + "\nPrecio:" + str(
            vtt.precio) + "$" + "\nDuracion:" + vtt.duracion)
    update.message.reply_text(
        "A continuacion escriba /fechaida (000-00-00)\n Ejemplo /fechaida 2020-10-09 ")  # año -mes-dia
    if idv == True:
        update.message.reply_text(
            "A continuacion escriba /fechavuelta (000-00-00)\n Ejemplo /fechavuelta 2020-10-09 ")  # año -mes-dia

def UIOMX(bot, update):
    global vtt, idv
    vtt = Viaje(of[10].aerolinea, of[10].origen, of[10].destino, of[10].duracion, of[10].precio, of[10].fecha1,
                of[10].fecha2, of[10].npersona, of[10].cod)
    update.message.reply_text(
        "Origen :" + vtt.origen + "\nDestino :" + vtt.destino + "\nAerolinea :" + vtt.aerolinea + "\nPrecio:" + str(
            vtt.precio) + "$" + "\nDuracion:" + vtt.duracion)
    update.message.reply_text(
        "A continuacion escriba /fechaida (000-00-00)\n Ejemplo /fechaida 2020-10-09 ")  # año -mes-dia
    if idv == True:
        update.message.reply_text(
            "A continuacion escriba /fechavuelta (000-00-00)\n Ejemplo /fechavuelta 2020-10-09 ")  # año -mes-dia
def UIOCA(bot, update):
    global vtt, idv
    vtt = Viaje(of[11].aerolinea, of[11].origen, of[11].destino, of[11].duracion, of[11].precio, of[11].fecha1,of[11].fecha2, of[11].npersona, of[11].cod)
    update.message.reply_text(
        "Origen :" + vtt.origen + "\nDestino :" + vtt.destino + "\nAerolinea :" + vtt.aerolinea + "\nPrecio:" + str(
            vtt.precio) + "$" + "\nDuracion:" + vtt.duracion)
    update.message.reply_text(
        "A continuacion escriba /fechaida (000-00-00)\n Ejemplo /fechaida 2020-10-09 ")  # año -mes-dia
    if idv == True:
        update.message.reply_text(
            "A continuacion escriba /fechavuelta (000-00-00)\n Ejemplo /fechavuelta 2020-10-09 ")  # año -mes-dia
def UIORU(bot, update):
    global vtt, idv
    vtt = Viaje(of[12].aerolinea, of[12].origen, of[12].destino, of[12].duracion, of[12].precio, of[12].fecha1,of[12].fecha2, of[12].npersona, of[12].cod)
    update.message.reply_text(
        "Origen :" + vtt.origen + "\nDestino :" + vtt.destino + "\nAerolinea :" + vtt.aerolinea + "\nPrecio:" + str(
            vtt.precio) + "$" + "\nDuracion:" + vtt.duracion)
    update.message.reply_text(
        "A continuacion escriba /fechaida (000-00-00)\n Ejemplo /fechaida 2020-10-09 ")  # año -mes-dia
    if idv == True:
        update.message.reply_text(
            "A continuacion escriba /fechavuelta (000-00-00)\n Ejemplo /fechavuelta 2020-10-09 ")  # año -mes-dia

def UIOMUC(bot, update):
    global vtt, idv
    vtt = Viaje(of[13].aerolinea, of[13].origen, of[13].destino, of[13].duracion, of[13].precio, of[13].fecha1,of[13].fecha2, of[13].npersona, of[13].cod)
    update.message.reply_text(
        "Origen :" + vtt.origen + "\nDestino :" + vtt.destino + "\nAerolinea :" + vtt.aerolinea + "\nPrecio:" + str(
            vtt.precio) + "$" + "\nDuracion:" + vtt.duracion)
    update.message.reply_text(
        "A continuacion escriba /fechaida (000-00-00)\n Ejemplo /fechaida 2020-10-09 ")  # año -mes-dia
    if idv == True:
        update.message.reply_text(
            "A continuacion escriba /fechavuelta (000-00-00)\n Ejemplo /fechavuelta 2020-10-09 ")  # año -mes-dia

def CUEBR(bot, update):
    global vtt, idv
    vtt = Viaje(of[14].aerolinea, of[14].origen, of[14].destino, of[14].duracion, of[14].precio, of[14].fecha1,of[14].fecha2, of[14].npersona, of[14].cod)
    update.message.reply_text(
        "Origen :" + vtt.origen + "\nDestino :" + vtt.destino + "\nAerolinea :" + vtt.aerolinea + "\nPrecio:" + str(
            vtt.precio) + "$" + "\nDuracion:" + vtt.duracion)
    update.message.reply_text(
        "A continuacion escriba /fechaida (000-00-00)\n Ejemplo /fechaida 2020-10-09 ")  # año -mes-dia
    if idv == True:
        update.message.reply_text(
            "A continuacion escriba /fechavuelta (000-00-00)\n Ejemplo /fechavuelta 2020-10-09 ")  # año -mes-dia

def CUEVE(bot, update):
    global vtt, idv
    vtt =Viaje(of[15].aerolinea,of[15].origen,of[15].destino,of[15].duracion,of[15].precio,of[15].fecha1,of[15].fecha2,of[15].npersona,of[15].cod)
    update.message.reply_text("Origen :" + vtt.origen + "\nDestino :" + vtt.destino + "\nAerolinea :" + vtt.aerolinea + "\nPrecio:" + str(
            vtt.precio) + "$" + "\nDuracion:" + vtt.duracion)
    update.message.reply_text("A continuacion escriba /fechaida (000-00-00)\n Ejemplo /fechaida 2020-10-09 ")  # año -mes-dia
    if idv == True:
        update.message.reply_text("A continuacion escriba /fechavuelta (000-00-00)\n Ejemplo /fechavuelta 2020-10-09 ")  # año -mes-dia

def CUEMX(bot, update):
    global vtt, idv
    vtt =Viaje(of[16].aerolinea,of[16].origen,of[16].destino,of[16].duracion,of[16].precio,of[16].fecha1,of[16].fecha2,of[16].npersona,of[16].cod)
    update.message.reply_text(
        "Origen :" + vtt.origen + "\nDestino :" + vtt.destino + "\nAerolinea :" + vtt.aerolinea + "\nPrecio:" + str(
            vtt.precio) + "$" + "\nDuracion:" + vtt.duracion)
    update.message.reply_text(
        "A continuacion escriba /fechaida (000-00-00)\n Ejemplo /fechaida 2020-10-09 ")  # año -mes-dia
    if idv == True:
        update.message.reply_text(
            "A continuacion escriba /fechavuelta (000-00-00)\n Ejemplo /fechavuelta 2020-10-09 ")  # año -mes-dia

def CUEMEX(bot, update):
    global vtt, idv
    vtt =Viaje(of[17].aerolinea,of[17].origen,of[17].destino,of[17].duracion,of[17].precio,of[17].fecha1,of[17].fecha2,of[17].npersona,of[17].cod)
    update.message.reply_text(
        "Origen :" + vtt.origen + "\nDestino :" + vtt.destino + "\nAerolinea :" + vtt.aerolinea + "\nPrecio:" + str(
            vtt.precio) + "$" + "\nDuracion:" + vtt.duracion)
    update.message.reply_text(
        "A continuacion escriba /fechaida (000-00-00)\n Ejemplo /fechaida 2020-10-09 ")  # año -mes-dia
    if idv == True:
        update.message.reply_text(
            "A continuacion escriba /fechavuelta (000-00-00)\n Ejemplo /fechavuelta 2020-10-09 ")  # año -mes-dia

def CUEUIO(bot, update):
    global vtt, idv
    vtt =Viaje(of[18].aerolinea,of[18].origen,of[18].destino,of[18].duracion,of[18].precio,of[18].fecha1,of[18].fecha2,of[18].npersona,of[18].cod)
    update.message.reply_text(
        "Origen :" + vtt.origen + "\nDestino :" + vtt.destino + "\nAerolinea :" + vtt.aerolinea + "\nPrecio:" + str(
            vtt.precio) + "$" + "\nDuracion:" + vtt.duracion)
    update.message.reply_text(
        "A continuacion escriba /fechaida (000-00-00)\n Ejemplo /fechaida 2020-10-09 ")  # año -mes-dia
    if idv == True:
        update.message.reply_text(
            "A continuacion escriba /fechavuelta (000-00-00)\n Ejemplo /fechavuelta 2020-10-09 ")  # año -mes-dia
def  GYEMIA(bot, update):
    global vtt, idv
    vtt = Viaje(of[19].aerolinea, of[19].origen, of[19].destino, of[19].duracion, of[19].precio, of[19].fecha1,of[19].fecha2, of[19].npersona, of[19].cod)
    update.message.reply_text(
        "Origen :" + vtt.origen + "\nDestino :" + vtt.destino + "\nAerolinea :" + vtt.aerolinea + "\nPrecio:" + str(
            vtt.precio) + "$" + "\nDuracion:" + vtt.duracion)
    update.message.reply_text(
        "A continuacion escriba /fechaida (000-00-00)\n Ejemplo /fechaida 2020-10-09 ")  # año -mes-dia
    if idv == True:
        update.message.reply_text(
            "A continuacion escriba /fechavuelta (000-00-00)\n Ejemplo /fechavuelta 2020-10-09 ")  # año -mes-dia
def GYEMAH(bot, update):
    global vtt, idv
    vtt =Viaje(of[20].aerolinea,of[20].origen,of[20].destino,of[20].duracion,of[20].precio,of[20].fecha1,of[20].fecha2,of[20].npersona,of[20].cod)
    update.message.reply_text(
        "Origen :" + vtt.origen + "\nDestino :" + vtt.destino + "\nAerolinea :" + vtt.aerolinea + "\nPrecio:" + str(
            vtt.precio) + "$" + "\nDuracion:" + vtt.duracion)
    update.message.reply_text(
        "A continuacion escriba /fechaida (000-00-00)\n Ejemplo /fechaida 2020-10-09 ")  # año -mes-dia
    if idv == True:
        update.message.reply_text(
            "A continuacion escriba /fechavuelta (000-00-00)\n Ejemplo /fechavuelta 2020-10-09 ")  # año -mes-dia
#________________________________________________________________________________________________________________________
def GYEMDE(bot, update):
    global vtt, idv
    vtt =Viaje(of[21].aerolinea,of[21].origen,of[21].destino,of[21].duracion,of[21].precio,of[21].fecha1,of[21].fecha2,of[21].npersona,of[21].cod)
    update.message.reply_text(
        "Origen :" + vtt.origen + "\nDestino :" + vtt.destino + "\nAerolinea :" + vtt.aerolinea + "\nPrecio:" + str(
            vtt.precio) + "$" + "\nDuracion:" + vtt.duracion)
    update.message.reply_text(
        "A continuacion escriba /fechaida (000-00-00)\n Ejemplo /fechaida 2020-10-09 ")  # año -mes-dia
    if idv == True:
        update.message.reply_text(
            "A continuacion escriba /fechavuelta (000-00-00)\n Ejemplo /fechavuelta 2020-10-09 ")  # año -mes-dia

def GYEMOW(bot, update):
    global vtt, idv
    vvtt =Viaje(of[22].aerolinea,of[22].origen,of[22].destino,of[22].duracion,of[22].precio,of[22].fecha1,of[22].fecha2,of[22].npersona,of[22].cod)
    update.message.reply_text(
        "Origen :" + vtt.origen + "\nDestino :" + vtt.destino + "\nAerolinea :" + vtt.aerolinea + "\nPrecio:" + str(
            vtt.precio) + "$" + "\nDuracion:" + vtt.duracion)
    update.message.reply_text(
        "A continuacion escriba /fechaida (000-00-00)\n Ejemplo /fechaida 2020-10-09 ")  # año -mes-dia
    if idv == True:
        update.message.reply_text(
            "A continuacion escriba /fechavuelta (000-00-00)\n Ejemplo /fechavuelta 2020-10-09 ")  # año -mes-dia
def GYEYUL(bot, update):
    global vtt, idv
    vtt =Viaje(of[23].aerolinea,of[23].origen,of[23].destino,of[23].duracion,of[23].precio,of[23].fecha1,of[23].fecha2,of[23].npersona,of[23].cod)
    update.message.reply_text(
        "Origen :" + vtt.origen + "\nDestino :" + vtt.destino + "\nAerolinea :" + vtt.aerolinea + "\nPrecio:" + str(
            vtt.precio) + "$" + "\nDuracion:" + vtt.duracion)
    update.message.reply_text(
        "A continuacion escriba /fechaida (000-00-00)\n Ejemplo /fechaida 2020-10-09 ")  # año -mes-dia
    if idv == True:
        update.message.reply_text(
            "A continuacion escriba /fechavuelta (000-00-00)\n Ejemplo /fechavuelta 2020-10-09 ")  # año -mes-dia
def MECGYE (bot, update):
    global vtt, idv
    vvtt =Viaje(of[24].aerolinea,of[24].origen,of[24].destino,of[24].duracion,of[24].precio,of[24].fecha1,of[24].fecha2,of[24].npersona,of[24].cod)
    update.message.reply_text(
        "Origen :" + vtt.origen + "\nDestino :" + vtt.destino + "\nAerolinea :" + vtt.aerolinea + "\nPrecio:" + str(
            vtt.precio) + "$" + "\nDuracion:" + vtt.duracion)
    update.message.reply_text(
        "A continuacion escriba /fechaida (000-00-00)\n Ejemplo /fechaida 2020-10-09 ")  # año -mes-dia
    if idv == True:
        update.message.reply_text(
            "A continuacion escriba /fechavuelta (000-00-00)\n Ejemplo /fechavuelta 2020-10-09 ")  # año -mes-dia
def MECUIO (bot, update):
    global vtt, idv
    vtt = Viaje(of[25].aerolinea, of[25].origen, of[25].destino, of[25].duracion, of[25].precio, of[25].fecha1, of[25].fecha2, of[25].npersona, of[25].cod)
    update.message.reply_text(
        "Origen :" + vtt.origen + "\nDestino :" + vtt.destino + "\nAerolinea :" + vtt.aerolinea + "\nPrecio:" + str(
            vtt.precio) + "$" + "\nDuracion:" + vtt.duracion)
    update.message.reply_text(
        "A continuacion escriba /fechaida (000-00-00)\n Ejemplo /fechaida 2020-10-09 ")  # año -mes-dia
    if idv == True:
        update.message.reply_text(
            "A continuacion escriba /fechavuelta (000-00-00)\n Ejemplo /fechavuelta 2020-10-09 ")  # año -mes-dia
def MECCUE (bot, update):
    global vtt, idv
    vtt = Viaje(of[26].aerolinea, of[26].origen, of[26].destino, of[26].duracion, of[26].precio, of[26].fecha1,of[26].fecha2, of[26].npersona, of[26].cod)
    update.message.reply_text(
        "Origen :" + vtt.origen + "\nDestino :" + vtt.destino + "\nAerolinea :" + vtt.aerolinea + "\nPrecio:" + str(
            vtt.precio) + "$" + "\nDuracion:" + vtt.duracion)
    update.message.reply_text(
        "A continuacion escriba /fechaida (000-00-00)\n Ejemplo /fechaida 2020-10-09 ")  # año -mes-dia
    if idv == True:
        update.message.reply_text(
            "A continuacion escriba /fechavuelta (000-00-00)\n Ejemplo /fechavuelta 2020-10-09 ")  # año -mes-dia
def GPSGYE (bot, update):
    global vtt, idv
    vtt =Viaje(of[27].aerolinea,of[27].origen,of[27].destino,of[27].duracion,of[27].precio,of[27].fecha1,of[27].fecha2,of[27].npersona,of[27].cod)
    update.message.reply_text(
        "Origen :" + vtt.origen + "\nDestino :" + vtt.destino + "\nAerolinea :" + vtt.aerolinea + "\nPrecio:" + str(
            vtt.precio) + "$" + "\nDuracion:" + vtt.duracion)
    update.message.reply_text(
        "A continuacion escriba /fechaida (000-00-00)\n Ejemplo /fechaida 2020-10-09 ")  # año -mes-dia
    if idv == True:
        update.message.reply_text(
            "A continuacion escriba /fechavuelta (000-00-00)\n Ejemplo /fechavuelta 2020-10-09 ")  # año -mes-dia
def GPSCUE (bot, update):
    global vtt, idv
    vtt =Viaje(of[28].aerolinea,of[28].origen,of[28].destino,of[28].duracion,of[28].precio,of[28].fecha1,of[28].fecha2,of[28].npersona,of[28].cod)
    update.message.reply_text(
        "Origen :" + vtt.origen + "\nDestino :" + vtt.destino + "\nAerolinea :" + vtt.aerolinea + "\nPrecio:" + str(
            vtt.precio) + "$" + "\nDuracion:" + vtt.duracion)
    update.message.reply_text(
        "A continuacion escriba /fechaida (000-00-00)\n Ejemplo /fechaida 2020-10-09 ")  # año -mes-dia
    if idv == True:
        update.message.reply_text(
            "A continuacion escriba /fechavuelta (000-00-00)\n Ejemplo /fechavuelta 2020-10-09 ")  # año -mes-dia
def GPSUIO (bot, update):
    global vtt, idv
    vtt =Viaje(of[29].aerolinea,of[29].origen,of[29].destino,of[29].duracion,of[29].precio,of[29].fecha1,of[29].fecha2,of[29].npersona,of[29].cod)
    update.message.reply_text(
        "Origen :" + vtt.origen + "\nDestino :" + vtt.destino + "\nAerolinea :" + vtt.aerolinea + "\nPrecio:" + str(
            vtt.precio) + "$" + "\nDuracion:" + vtt.duracion)
    update.message.reply_text(
        "A continuacion escriba /fechaida (000-00-00)\n Ejemplo /fechaida 2020-10-09 ")  # año -mes-dia
    if idv == True:
        update.message.reply_text(
            "A continuacion escriba /fechavuelta (000-00-00)\n Ejemplo /fechavuelta 2020-10-09 ")  # año -mes-dia
def GYECN (bot, update):
    global vtt, idv
    vtt =Viaje(of[30].aerolinea,of[30].origen,of[30].destino,of[30].duracion,of[30].precio,of[30].fecha1,of[30].fecha2,of[30].npersona,of[30].cod)
    update.message.reply_text(
        "Origen :" + vtt.origen + "\nDestino :" + vtt.destino + "\nAerolinea :" + vtt.aerolinea + "\nPrecio:" + str(
            vtt.precio) + "$" + "\nDuracion:" + vtt.duracion)
    update.message.reply_text(
        "A continuacion escriba /fechaida (000-00-00)\n Ejemplo /fechaida 2020-10-09 ")  # año -mes-dia
    if idv == True:
        update.message.reply_text(
            "A continuacion escriba /fechavuelta (000-00-00)\n Ejemplo /fechavuelta 2020-10-09 ")  # año -mes-dia
def CUECN (bot, update):
    global vtt, idv
    vtt =Viaje(of[31].aerolinea,of[31].origen,of[31].destino,of[31].duracion,of[31].precio,of[31].fecha1,of[31].fecha2,of[31].npersona,of[31].cod)
    update.message.reply_text("Origen :" + vtt.origen + "\nDestino :" + vtt.destino + "\nAerolinea :" + vtt.aerolinea + "\nPrecio:" + str(vtt.precio) + "$" + "\nDuracion:" + vtt.duracion)
    update.message.reply_text("A continuacion escriba /fechaida (000-00-00)\n Ejemplo /fechaida 2020-10-09 ")  # año -mes-dia
    if idv == True:
        update.message.reply_text("A continuacion escriba /fechavuelta (000-00-00)\n Ejemplo /fechavuelta 2020-10-09 ")  # año -mes-dia

def CUECO  (bot, update):
    global vtt, idv
    vtt =Viaje(of[32].aerolinea,of[32].origen,of[32].destino,of[32].duracion,of[32].precio,of[32].fecha1,of[32].fecha2,of[32].npersona,of[32].cod)
    update.message.reply_text("Origen :" + vtt.origen + "\nDestino :" + vtt.destino + "\nAerolinea :" + vtt.aerolinea + "\nPrecio:" + str(vtt.precio) + "$" + "\nDuracion:" + vtt.duracion)
    update.message.reply_text("A continuacion escriba /fechaida (000-00-00)\n Ejemplo /fechaida 2020-10-09 ")  # año -mes-dia
    if idv == True:
        update.message.reply_text("A continuacion escriba /fechavuelta (000-00-00)\n Ejemplo /fechavuelta 2020-10-09 ")
        # año -mes-dia
def CUEMEC (bot, update):
    global vtt, idv
    vtt =Viaje(of[33].aerolinea,of[33].origen,of[33].destino,of[33].duracion,of[33].precio,of[33].fecha1,of[33].fecha2,of[33].npersona,of[33].cod)
    update.message.reply_text(
        "Origen :" + vtt.origen + "\nDestino :" + vtt.destino + "\nAerolinea :" + vtt.aerolinea + "\nPrecio:" + str(
            vtt.precio) + "$" + "\nDuracion:" + vtt.duracion)
    update.message.reply_text(
        "A continuacion escriba /fechaida (000-00-00)\n Ejemplo /fechaida 2020-10-09 ")  # año -mes-dia
    if idv == True:
        update.message.reply_text(
            "A continuacion escriba /fechavuelta (000-00-00)\n Ejemplo /fechavuelta 2020-10-09 ")  # año -mes-dia
def GYEJP(bot, update):
    global vtt, idv
    vtt =Viaje(of[34].aerolinea,of[34].origen,of[34].destino,of[34].duracion,of[34].precio,of[34].fecha1,of[34].fecha2,of[34].npersona,of[34].cod)
    update.message.reply_text(
        "Origen :" + vtt.origen + "\nDestino :" + vtt.destino + "\nAerolinea :" + vtt.aerolinea + "\nPrecio:" + str(
            vtt.precio) + "$" + "\nDuracion:" + vtt.duracion)
    update.message.reply_text(
        "A continuacion escriba /fechaida (000-00-00)\n Ejemplo /fechaida 2020-10-09 ")  # año -mes-dia
    if idv == True:
        update.message.reply_text(
            "A continuacion escriba /fechavuelta (000-00-00)\n Ejemplo /fechavuelta 2020-10-09 ")  # año -mes-dia
def GYEUS (bot, update):
    global vtt, idv
    vtt =Viaje(of[35].aerolinea,of[35].origen,of[35].destino,of[35].duracion,of[35].precio,of[35].fecha1,of[35].fecha2,of[35].npersona,of[35].cod)
    update.message.reply_text(
        "Origen :" + vtt.origen + "\nDestino :" + vtt.destino + "\nAerolinea :" + vtt.aerolinea + "\nPrecio:" + str(
            vtt.precio) + "$" + "\nDuracion:" + vtt.duracion)
    update.message.reply_text(
        "A continuacion escriba /fechaida (000-00-00)\n Ejemplo /fechaida 2020-10-09 ")  # año -mes-dia
    if idv == True:
        update.message.reply_text(
            "A continuacion escriba /fechavuelta (000-00-00)\n Ejemplo /fechavuelta 2020-10-09 ")  # año -mes-dia
def CUEUS (bot, update):
    global vtt, idv
    vtt =Viaje(of[36].aerolinea,of[36].origen,of[36].destino,of[36].duracion,of[36].precio,of[36].fecha1,of[36].fecha2,of[36].npersona,of[36].cod)
    update.message.reply_text(
        "Origen :" + vtt.origen + "\nDestino :" + vtt.destino + "\nAerolinea :" + vtt.aerolinea + "\nPrecio:" + str(
            vtt.precio) + "$" + "\nDuracion:" + vtt.duracion)
    update.message.reply_text(
        "A continuacion escriba /fechaida (000-00-00)\n Ejemplo /fechaida 2020-10-09 ")  # año -mes-dia
    if idv == True:
        update.message.reply_text(
            "A continuacion escriba /fechavuelta (000-00-00)\n Ejemplo /fechavuelta 2020-10-09 ")  # año -mes-dia
def GYEAU (bot, update):
    global vtt, idv
    vtt =Viaje(of[37].aerolinea,of[37].origen,of[37].destino,of[37].duracion,of[37].precio,of[37].fecha1,of[37].fecha2,of[37].npersona,of[37].cod)
    update.message.reply_text(
        "Origen :" + vtt.origen + "\nDestino :" + vtt.destino + "\nAerolinea :" + vtt.aerolinea + "\nPrecio:" + str(
            vtt.precio) + "$" + "\nDuracion:" + vtt.duracion)
    update.message.reply_text(
        "A continuacion escriba /fechaida (000-00-00)\n Ejemplo /fechaida 2020-10-09 ")  # año -mes-dia
    if idv == True:
        update.message.reply_text(
            "A continuacion escriba /fechavuelta (000-00-00)\n Ejemplo /fechavuelta 2020-10-09 ")  # año -mes-dia

def GYEPE (bot, update):
    global vtt, idv
    vtt = Viaje(of[38].aerolinea, of[38].origen, of[38].destino, of[38].duracion, of[38].precio, of[38].fecha1,of[38].fecha2, of[38].npersona, of[38].cod)
    update.message.reply_text(
        "Origen :" + vtt.origen + "\nDestino :" + vtt.destino + "\nAerolinea :" + vtt.aerolinea + "\nPrecio:" + str(
            vtt.precio) + "$" + "\nDuracion:" + vtt.duracion)
    update.message.reply_text(
        "A continuacion escriba /fechaida (000-00-00)\n Ejemplo /fechaida 2020-10-09 ")  # año -mes-dia
    if idv == True:
        update.message.reply_text(
            "A continuacion escriba /fechavuelta (000-00-00)\n Ejemplo /fechavuelta 2020-10-09 ")  # año -mes-dia

def GYEUA (bot, update):
    global vtt, idv
    vtt =Viaje(of[39].aerolinea,of[39].origen,of[39].destino,of[39].duracion,of[39].precio,of[39].fecha1,of[39].fecha2,of[39].npersona,of[39].cod)
    update.message.reply_text(
        "Origen :" + vtt.origen + "\nDestino :" + vtt.destino + "\nAerolinea :" + vtt.aerolinea + "\nPrecio:" + str(
            vtt.precio) + "$" + "\nDuracion:" + vtt.duracion)
    update.message.reply_text(
        "A continuacion escriba /fechaida (000-00-00)\n Ejemplo /fechaida 2020-10-09 ")  # año -mes-dia
    if idv == True:
        update.message.reply_text(
            "A continuacion escriba /fechavuelta (000-00-00)\n Ejemplo /fechavuelta 2020-10-09 ")  # año -mes-dia


#___________________________________________________________ 40 ____________________________________-#
#______________________________________________________________________________________________________________________________________________####
def  IdaVuelta(bot,update):
    global idv
    idv=True
    update.message.reply_text("Para elegir un vuelo solo de click en el comando ejemplo / GYEUIO")
    for b in of:

        update.message.reply_text("Origen :" + b.origen + "\nDestino :" + b.destino + "\nPrecio:" + str(
            b.precio) + "$" + "\nDuracion:" + b.duracion + "\n" + b.cod)

def Fecha1(bot,update,args):
    global  idv
    f=args[0]
    vtt.fecha1=f
    if idv== False:
        update.message.reply_text("A continuacion escriba: /asiento (número de asientos que desea)\n -Ejemplo /asiento 4 ")

def Fecha2(bot,update,args):
    f=args[0]
    vtt.fecha2=f
    update.message.reply_text("A continuacion escriba: /asiento (número de asientos que desea)\n -Ejemplo /asiento 4 ")

def id(bot,update,args):
    global c ,tt ,n ,vtt,ncliente
    #update.message.reply_text("Ingrese su numero de cedula ")
    if len(args)==0:
        update.message.reply_text("!ingrese una cedula !!  /cedula 1234567890 ")
    else:
        id = args[0]
        if len(id)==10 and id.isdigit():
            c=id
            if idv == False:
                update.message.reply_text("------ DATOS DE SU VIAJE --------\n")
                update.message.reply_text("Su viaje :" + vtt.origen + "\nDestino:" + vtt.destino + "\nDuracion:" + vtt.duracion + "\nFecha de Ida:" + vtt.fecha1 + "\nPrecio :"+str(vtt.precio)+"\n Numero de asientos :" +str(vtt.npersona))
            if idv == True:
                pi = vtt.precio * 2
                vtt.precio = pi
                tt = n * vtt.precio
                update.message.reply_text("------ DATOS DE SU VIAJE --------\n")
                update.message.reply_text(
                    "Origen :" + vtt.origen + "\nDestino:" + vtt.destino + "\nDuracion:" + vtt.duracion + "\nFecha de Ida :" + vtt.fecha1 + "\nFecha de Regreso :" + vtt.fecha2 + "\nPrecio Base :" + str(vtt.precio)+"\nNumero de asientos :"+str(vtt.npersona))
                update.message.reply_text("Precio por Ida y vuelta" + str(pi) + "$")

            update.message.reply_text("Nombre  :" + ncliente)
            update.message.reply_text("Número de Cedula :"+c)
            update.message.reply_text("Su total a cancelar es de " + str(tt) + "$")
            update.message.reply_text("\n- /regresar")

        else:
             update.message.reply_text("! ingrese cedula valida de 10 digitos !")
             update.message.reply_text("ingrese su cedula con /cedula 0123456789")
             id(bot,update,args)


def nasiento(bot,update,args):
    global vtt,tt,n
    if len(args)==0:
        update.message.reply_text("ingresa un numero de asientos: /asiento (número de asientos que desea)\n -Ejemplo /asiento 4")
    else:
        n = int(args[0])
        vtt.npersona=n
        p=int(str(vtt.precio))
        tt=p*n
        update.message.reply_text("-Para ingresar su nombre /Nombre(Alberto Gil)")


def Busqueda(bot,update,args):
    global bv
    if len(args) == 0:
       bc(bot,update,args)
    else:
        a = args[0].upper()
        for h in of:
            if a == h.origen:
                update.message.reply_text("Origen :" + h.origen + "\nDestino :" + h.destino + "\nPrecio:" + str(
                    h.precio) + "$" + "\nDuracion:" + h.duracion + "\nAerolinea:" + h.aerolinea)
                bv=True
                update.message.reply_text("\n- /regresar")
        if bv==False:
                time.sleep(1)
                update.message.reply_text("Lo sentimos no se encontro nada ....")
                bc(bot,update,args)
                update.message.reply_text("\n- /regresar")

def Listar(bot,update):
    l=0
    update.message.reply_text("-Te muestro todos los vuelos  :")
    for t in of:
        l=l+1
        update.message.reply_text("____ Vuelo #"+str(l)+" _____")
        update.message.reply_text("Origen :" +t.origen+ "\nDestino :" + t.destino + "\nPrecio:" + str(t.precio) + "$" + "\nDuracion:" + t.duracion + "\nAerolinea:" + t.aerolinea)
    update.message.reply_text("\n- /regresar")

def bc(bot,update,args):
    update.message.reply_text("-Para buscar viajes por su origen ingrese /Busqueda(ciudad de origen)")
    update.message.reply_text("\n -Ejemplo:  /Buscar guayaquil")

def nom(bot,update):
    update.message.reply_text("-Para ingresar su nombre /Nombre(Alberto Gil)")

def Nombre(bot,update,args):
    global ncliente
    if len(args) == 0:
        update.message.reply_text("No puede dejar vacio su Nombre")
        nom(bot,update)
    else:
        ncliente=args[0]
        update.message.reply_text("ingrese su cedula con /cedula 0000000000000")






# Manejador para mensajes recibidos que no son comandos
def mensaje_nocomando(bot, update):
    global esperando_ruta
     # Solo hacer caso si quien le habla es el remitente correspondiente a dicha ID
    if esperando_ruta == 1:
            esperando_ruta = 0
            ruta = update.message.text
            subprocess.Popen(["nohup", "wget", enlace_descarga, "-P", ruta])
            update.message.reply_text(
                "Descargando en '" + ruta + "' desde el enlace " + enlace_descarga)  # Respondemos al comando con el mensaje
    else:
            update.message.reply_text("Por favor envia un comando adecuado.\n\nPara conocer los comandos implementados consulta la /ayuda")  # Respondemos al comando con el mensaje








##############################

def main():
    # Crear el manejador de eventos a partir del TOKEN del bot
    updater = Updater(TOKEN)

    # Obtener el registro de manejadores del planificador
    dp = updater.dispatcher

    # Asociamos manejadores para cada comando reconocible
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("regresar", start))
    dp.add_handler(CommandHandler("asiento", nasiento, pass_args=True))
    dp.add_handler(CommandHandler("fechaida",Fecha1, pass_args=True))
    dp.add_handler(CommandHandler("fechavuelta", Fecha2, pass_args=True))
    dp.add_handler(CommandHandler("Busqueda", bc, pass_args=True))
    dp.add_handler(CommandHandler("cedula", id, pass_args=True))
    dp.add_handler(CommandHandler("GYEUIO", GYEUIO))
    dp.add_handler(CommandHandler("GYESCY", GYESCY))
    dp.add_handler(CommandHandler("GYECUE", GYECUE))
    dp.add_handler(CommandHandler("GYEMEC", GYEMEC))
    dp.add_handler(CommandHandler("GYEGPS",GYEGPS))
    dp.add_handler(CommandHandler("GYEBHI",GYEBHI))
    dp.add_handler(CommandHandler("GYECOR",GYECOR))
    dp.add_handler(CommandHandler("GYEBR", GYEBR))
    dp.add_handler(CommandHandler("GYEMX", GYEMX))
    dp.add_handler(CommandHandler("UIOCO", UIOCO))
    dp.add_handler(CommandHandler("UIOMX", UIOMX))
    dp.add_handler(CommandHandler("UIOCA", UIOCA))
    dp.add_handler(CommandHandler("UIORU", UIORU))
    dp.add_handler(CommandHandler("UIOMUC", UIOMUC))
    dp.add_handler(CommandHandler("CUEBR", CUEBR))
    dp.add_handler(CommandHandler("CUEVE", CUEVE))
    dp.add_handler(CommandHandler("CUEMX", CUEMX))
    dp.add_handler(CommandHandler("CUEMEX", CUEMEX))
    dp.add_handler(CommandHandler("CUEUIO", CUEUIO))
    dp.add_handler(CommandHandler("GYEMIA", GYEMIA))
    dp.add_handler(CommandHandler("GYEMAH", GYEMAH))
    dp.add_handler(CommandHandler("GYEMDE", GYEMDE))
    dp.add_handler(CommandHandler("GYEMOW", GYEMOW))
    dp.add_handler(CommandHandler("GYEYUL", GYEYUL))
    dp.add_handler(CommandHandler("MECGYE", MECGYE))
    dp.add_handler(CommandHandler("MECUIO", MECUIO))
    dp.add_handler(CommandHandler("MECCUE", MECCUE))
    dp.add_handler(CommandHandler("GPSGYE", GPSGYE))
    dp.add_handler(CommandHandler("GPSCUE", GPSCUE))
    dp.add_handler(CommandHandler("GPSUIO", GPSUIO))
    dp.add_handler(CommandHandler("GYECN", GYECN))
    dp.add_handler(CommandHandler("CUECN", CUECN))
    dp.add_handler(CommandHandler("CUECO", CUECO))
    dp.add_handler(CommandHandler("CUEMEC", CUEMEC))
    dp.add_handler(CommandHandler("GYEJP", GYEJP))
    dp.add_handler(CommandHandler("GYEUS", GYEUS))
    dp.add_handler(CommandHandler("CUEUS", CUEUS))
    dp.add_handler(CommandHandler("GYEAU", GYEAU))
    dp.add_handler(CommandHandler("GYEPE", GYEPE))
    dp.add_handler(CommandHandler("GYEUA", GYEUA))
    dp.add_handler(CommandHandler("Listar",Listar))
    dp.add_handler(CommandHandler("Ida", Ida))
    dp.add_handler(CommandHandler("IdayVuelta", IdaVuelta))
#    dp.add_handler(CommandHandler("IdayVuelta", IdaV))
    dp.add_handler(CommandHandler("ayuda", ayuda))
    dp.add_handler(CommandHandler("Nombre",Nombre, pass_args=True))
    dp.add_handler(CommandHandler("Buscar", Busqueda, pass_args=True))
    # Asociamos un manejador para cualquier mensaje recibido (no comando)
    dp.add_handler(MessageHandler(Filters.text, mensaje_nocomando))
    # Iniciamos el bot
    updater.start_polling()
    # Actualizamos el estado del bot (bloquea la ejecucion a la espera de mensajes)
    updater.idle()

if __name__ == '__main__':
    main()


# Fin del Codigo