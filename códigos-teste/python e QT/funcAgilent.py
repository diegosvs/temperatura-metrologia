import visa
from visa import constants
import time, csv, os, _thread as t

def conectarMultimetroAgilent():

    portas_conectadas=visa.ResourceManager() #instancia a classe VISA

    instrumentos_conectados=portas_conectadas.list_resources()
    print(instrumentos_conectados)
    
    global multimetro,b

       


    try:
        
        #multimetro=portas_conectadas.open_resource(instrumentos__conectados[0]) #conecta o multimetro agilent U3606A pela GPIB
        multimetro=portas_conectadas.open_resource('ASRL4::INSTR',
                                                   parity=constants.Parity.none,
                                                   data_bits=8,
                                                   baud_rate=9600,
                                                   stop_bits=constants.StopBits.one
                                                   )
        #print(multimetro.query("*IDN?")) #pede a identificacao do multimetro e imprime na tela
        #multimetro.write("F1")
        #multimetro.write("SW0")
        b=multimetro.query('*IDN?')
        
        
        return ("instrumento conectado",b)

    except:

        return ("falha na conexão")
    



def aquisitarMultimetroAgilent():

    try:
        return multimetro.query("FETC?").replace(".",",")[:13].replace("\n","")
    except:
        return ("Erro na aquisição")
       
    
print(conectarMultimetroAgilent())         
    
