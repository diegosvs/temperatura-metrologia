'''

parametros do indicador
    system optoins --
        auto id - off
        autoid annunciator - off
        auto zero a - on
        com address - 111
        baudrate 19,2k
        com line feed - add line feeds
        retain tare - on
        rs232 eot char - on
        auto tare - off

'''

import visa,time, csv, os, _thread as t
from visa import constants


def conectarInterface():

    porta_comunicacao=visa.ResourceManager()   
    instrumentos_conectados=porta_comunicacao.list_resources()
    print(instrumentos_conectados)
    global indicador,dp

    try:
        indicador = porta_comunicacao.open_resource('ASRL4::INSTR',
                                                    parity=constants.Parity.none,
                                                    baud_rate=9600,
                                                    data_bits=8,
                                                    stop_bits=constants.StopBits.one,
                                                    )
        
        dp=indicador.query("*IDN?")
        return ("instrumento conectado",dp)
        
    except:
        return ("falha na conexão")

def listarPortasCom():    
    porta_com = visa.ResourceManager()
    ports = ['ASRL%s' % i for i in range(100)]      
    for port in ports:        
        try:
            ind = porta_com.open_reso
            urce(port)
            ind.close()            
        except:
            pass     

def desconectarInterface(): 
    indicador.close()
    print("DESCONECTADO")
    
def salvarValores():
    try:
        arquivo_calibracao = open ("C:\\calibrações\\arquivo.txt","a")     
        v=indicador.query('@111V00081').replace('.',',')[14:22]
        #'@111V00081' [13:22]
        arquivo_calibracao.writelines(v+'\n')
        #time.sleep(1)
        arquivo_calibracao.close()

    except:
        print("erro")

def aquisitarInterface():

    try:
               
        #return indicador.query('@111P1').replace(".",",")[13:22]
        return indicador.query('AID?\r')
    except:
        return ('erro')

def iniciarExecucaoParalela(caminho,permissao):

    def deletarArquivoReady(caminho,permissao):

        while (permissao=='ok'):
            try:
                os.remove(caminho)
                arquivo_calibracao = open ("C:\\calibrações\\arquivo.txt","a")                 
                v=indicador.query('@111V00081').replace('.',',')[14:22]
                
                arquivo_calibracao.writelines(v+'\n')
                #time.sleep(1)
                arquivo_calibracao.close()
                
            except:
                pass
        else:
            pass
     
    t.start_new_thread(deletarArquivoReady,(caminho,permissao))   
    


def zerarInterface():

    try:
        indicador.write('@111R1000000')
    except:
        return ("erro ao zerar")          


listarPortasCom()
print(conectarInterface())
caminho="C:\\KRATOS\\MPM\\READY.DAT"

comuMaq=input(print('comunicar com maquina? '))
if (comuMaq!=''):
    continuar_comunic='ok'
    iniciarExecucaoParalela(caminho,continuar_comunic)
    
else:
    pass

while (input(print('aquisitar? '))==''):
    salvarValores()

else:
    desconectarInterface()
