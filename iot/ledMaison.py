import network   #import des fonction lier au wifi
import urequests #import des fonction lier au requetes http
import utime #import des fonction lier au temps
import ujson #import des fonction lier aà la convertion en Json
from machine import Pin, PWM # importe dans le code la lib qui permet de gerer les Pin de sortie et de modulation du signal
import time # importe dans le code la lib qui permet de gerer le temps

wlan = network.WLAN(network.STA_IF) # met la raspi en mode client wifi
wlan.active(True) # active le mode client wifi

# Paramètres de connexion au réseau
ssid = ''
password = ''
wlan.connect(ssid, password) # connecte la raspi au réseau
url = "http://192.168.177.183:3000/iot/lastVisited"

# On définit les couleurs des maisons
maison = {
    "Gryffindor" : [255,0,0],
    "Slytherin" : [0,255,0],
    "Hufflepuff" : [200,200,0],
    "Ravenclaw" : [0,0,255]
}

led =[PWM(Pin(18,mode=Pin.OUT)), PWM(Pin(17,mode=Pin.OUT)),PWM(Pin(16,mode=Pin.OUT))]

for i in led:
    i.freq(1_000) 

# On attend que la connexion soit établie
while not wlan.isconnected():
    print("pas co")
    utime.sleep(1)
    pass

# Fonction pour récupérer la maison
def recupMaison():
    try:
        print("GET")
        r = urequests.get(url) # lance une requete sur l'url
        house = r.json()["lastVisited"]
        r.close() # ferme la demande
        print(house)
        utime.sleep(1)
    
        return house
    
    except Exception as e:
        print(e)


# Fonction pour allumer les leds
def couleurs(tableau):
    for i in range(3):
        led[i].duty_u16(tableau[i]*256)
        
# On récupère la maison et on allume les leds
while True:
    house = recupMaison()
    if not house:
        house = "Gryffindor"
        couleurs([255, 255, 255])
    else:
        couleurs(maison[house])