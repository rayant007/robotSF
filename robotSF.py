import serial
import time

ard = serial.Serial('/dev/ttyACM0',9600,timeout=2)
time.sleep(2)
print('puerto valido')
cadena = 'hola'
cadenaBytes = cadena.encode('utf-8')
ard.write(cadenaBytes)

ard.close
