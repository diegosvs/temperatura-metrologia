import visa,time

def conectarMultimetroAgilent():

    portas_conectadas=visa.ResourceManager() #instancia a classe VISA

    instrumentos_conectados=portas_conectadas.list_resources()

    global multimetro

    try:
        
        multimetro=portas_conectadas.open_resource(str(instrumentos_conectados[0])) #conecta o multimetro agilent U3606A pela GPIB

        return ("instrumento conectado")

        #print(multimetro.query("*IDN?")) #pede a identificacao do multimetro e imprime na tela


        '''CONFIGURAÇÃO INICIAL PADRÃO'''
        multimetro.write("CONF")
        multimetro.write("SOUR:VOLT:RANG 30")
        multimetro.write("INIT:CONT ON")
        multimetro.write("OUTP OFF")

    except:

        return ("falha na conexão")
    

def fonte(valor_tensao):    

    try:        
        multimetro.write("VOLT ", valor_tensao)
        time.sleep(1)
        multimetro.write("OUTP ON")
    except:
        pass
        

       
def desconectarMultimetroAgilent():

    multimetro.close()
    print("desconectado")

def aquisitarMultimetroAgilent():

    try:
        return multimetro.query("FETC?").replace(".",",")[:13].replace("\n","")
    except:
        return ("Erro na aquisição")
       
    
            
    
