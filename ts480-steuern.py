#!/usr/bin/python

import time
import serial
import os

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=38400,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=2
)

def schreiben(befehl):
   ser.open()
   ser.isOpen()
   ser.write(befehl)
   ser.close()


def lesen(befehl):
   ser.open()
   ser.isOpen()
   ser.write(befehl)
   x = ser.read(50)
   print x
   ser.close()

def scan(anfang,ende,weite):

   for i in range(anfang,ende,weite):
      if i < 1000:
         freq = "00"+str(i)
      elif i < 10000:
         freq = "0"+str(i)
      else:
         freq = str(i)
      ser.open()
      ser.isOpen()
      ser.write("FA000"+freq+"000;")
      ser.close()
      ser.open()
      ser.isOpen()
      ser.write("FA;")
      x = ser.read(14)
      menue()
      print "Aktuelle Frequenz: "+x[5:7]+"."+x[7:10]+","+x[10:13]+" kHz"
      time.sleep(1)
      ser.close()

def menue():
   os.system("clear")
   print "\t\t\t\tSteuerprogramm TS-480\n"
   print "(1) Frequenz eingeben"
   print "(2) Frequenzbereich scannen"
   print "(3) Bandumschaltung"
   print "(x) Programm beenden\n"

while True:
   menue()
   auswahl = raw_input("Bitte treffen Sie Ihre Auswahl: ")
   if auswahl == "1":
     freq = int(raw_input("\nBitte die einzustellende Frequenz in kHz eingeben: "))
     if freq < 1000:
        schreiben("FA00000"+str(freq)+"000;")
     elif freq < 10000:
        schreiben("FA0000"+str(freq)+"000;")   
     else:
        schreiben("FA000"+str(freq)+"000;")
   elif auswahl == "2":
      fmin = int(raw_input("Bitte die untere Frequenz in kHz eingeben: "))
      fmax = int(raw_input("Bitte die obere Frequenz in kHz eingeben: "))
      step = int(raw_input("Jetzt noch die Schrittweite: "))
      print "Und los geht es mit dem Scan-Vorgang"
      scan(fmin,fmax,step)
   elif auswahl == "3":
      richtung = raw_input("Soll (h)och oder (r)untergeschaltet werden? ")
      if richtung == "h":
         schreiben("BU;")
      elif richtung == "r":
         schreiben("BD;")
      else:
         print "Falsche Auswahl, bitte erneut aus dem Menue auswaehlen!"
         time.sleep(2)
   elif auswahl == "x":
      print "\nHiermit verlassen Sie das tolle Programm in 4 Sekunden!"
      time.sleep(4)
      exit()
   else:
      print "Sie haben eine falsche Eingabe vorgenommen,\nbitte in 2 Sekunden erneut auswaehlen!"
      time.sleep(2)
