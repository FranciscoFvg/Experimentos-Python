#Necessita do download da extensão pypiwin32 através de:
#pip install pypiwin32
#Possibilita acessar diversar APIs dentro do windows.

#Importamos o módulo necessário:
import win32com.client

#Chama-se o método Dispatch para usar a API reponsável por "falar/ler texto"
#e executa-se o método speak.
speaker = win32com.client.Dispatch('SAPI.SpVoice')

def faleIsso(t):
    #next = True

    #while next:
        #t = input('Digite algum texto:\n')
        #Digite 'exit' para encerrar a execução
        #if t == 'exit':
        #    next = False
        #    speaker.speak('Saindo')
        #else:
            speaker.speak(t)