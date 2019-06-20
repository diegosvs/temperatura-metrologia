
import visa
import time, csv, os, _thread as t

def conectarMultimetroAgilent():

    portas_conectadas=visa.ResourceManager() #instancia a classe VISA

    instrumentos_conectados=portas_conectadas.list_resources()
    print(instrumentos_conectados)
    
    global multimetro1,multimetro2

    try:
        
        multimetro1=portas_conectadas.open_resource('USB0::2391::19736::MY53310004::0::INSTR') #conecta o multimetro agilent U3606A pela GPIB
        multimetro2=portas_conectadas.open_resource('USB0::2391::2567::MY48005210::0::INSTR')
        #multimetro2=portas_conectadas.open_resource('GPIB0::22::INSTR')

        return ("instrumentos conectados "+'\n')
        
        #CONFIGURAÇÃO INICIAL PADRÃO
        multimetro1.write("CONF")
        multimetro1.write("SOUR:VOLT:RANG 30")
        multimetro1.write("INIT:CONT ON")
        #multimetro1.write("OUTP OFF")
    
    except:

        return ("falha na conexão")
    

def fonte(valor_tensao):    

    try:        
        multimetro.write("VOLT ", valor_tensao)
        time.sleep(1)
        multimetro.write("OUTP ON")
    except:
        pass

def salvarValores():
    arquivo_calibracao = open ("C:\\calibrações\\arquivo.txt","a")
 
    v='\n'+multimetro1.query("FETC?").replace(".",",")[:13].replace("\n","")+'\t'+multimetro2.query("MEAS?").replace(".",",")[:15].replace("\r","")
    arquivo_calibracao.writelines(v)
    
    #time.sleep(1)
    arquivo_calibracao.close()
    
    

       
def desconectarMultimetros():

    multimetro1.close()
    
    multimetro2.close()
    print("desconectado")

def aquisitarMultimetros():

    try:
        return '\n'+multimetro1.query("MEAS?").replace(".",",")[:15].replace("\n","") + '\n'+multimetro2.query("FETC?").replace(".",",")[:13].replace("\n","")
        
    except:
        return ("Erro na aquisição")

     
def iniciarExecucaoParalela(caminho,permissao):

    def deletarArquivoReady(caminho,permissao):

        while (permissao=='ok'):
            try:
                os.remove(caminho)
                arquivo_calibracao = open ("C:\\calibrações\\arquivo.txt","a")
                v='\n'+multimetro1.query("FETC?").replace(".",",")[:13].replace("\n","")+'\t'+multimetro2.query("MEAS?").replace(".",",")[:15].replace("\r","")
                arquivo_calibracao.writelines(v)
                time.sleep(1)
                arquivo_calibracao.close()
            except:
                pass
        else:
            pass
     
    t.start_new_thread(deletarArquivoReady,(caminho,permissao))

print(conectarMultimetroAgilent())

caminho="C:\\KRATOS\\MPM\\READY.DAT"

comuMaq=input(print('comunicar com maquina? '))
if (comuMaq=='s'):
    continuar_comunic='ok'
    iniciarExecucaoParalela(caminho,continuar_comunic)
else:
    pass

while (input(print('aquisitar? '))==''):    
    salvarValores()
    

else:
    desconectarMultimetros()
          
