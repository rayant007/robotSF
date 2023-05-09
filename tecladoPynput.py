#librerias
import serial
import time
from pynput import keyboard as kb

#--------------------------------------
#se realiza la conexion a arduino
try:
    arduino = serial.Serial('/dev/ttyACM0',9600,timeout=2)
    print('conexion exitosa')
    print('puerto valido')
except:
    print('no se establecio conexion')
    print('puerto invalido')
#--------------------------------------

"""def pulsa(tecla):
    #print('se ha pulsado la tecla: ' + str(tecla))
    if (tecla == kb.KeyCode.from_char('w')):
        print('w')
    else:
        if (tecla == kb.KeyCode.from_char('s')):
            print('s')
        else:
            if (tecla == kb.KeyCode.from_char('a')):
                print('a')
            else:
                if (tecla == kb.KeyCode.from_char('d')):
                    print('d')
                else:
                    if (tecla == kb.KeyCode.from_char('o')):
                        print('o')
                    else:
                        if (tecla == kb.KeyCode.from_char('l')):
                            print('l')
                        else:
                            if (tecla == kb.KeyCode.from_char('q')):
                                return False"""



def pulsa(tecla):
    valores = {'w': 1, 's': 2, 'a': 3, 'd': 4, 'o': 5, 'l': 6}
    if tecla.char in valores:
        print(valores[tecla.char])
        return valores[tecla.char]
    else:
        return False

escuchador = kb.Listener(pulsa)
escuchador.start()

while escuchador.is_alive():
    pass

function_pulsa = pulsa
#with kb.Listener(pulsa) as escuchador:
#    escuchador.join()