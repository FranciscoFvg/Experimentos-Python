#pip install pyttsx3
import pyttsx3

# Inicializando biblioteca
speaker=pyttsx3.init()

# Definindo atributos:
#    Lingua: portugues do Brasil
#    Velocidade: padrao (200) -45
speaker.setProperty('voice', 'brazil')
rate = speaker.getProperty('rate')
speaker.setProperty('rate', rate-45)

# Passando texto a ser dito e executando
speaker.say("Ao escrever em português as frases deverão estar acentuadas.")
speaker.say("Caso contrário a entonação de algumas palavras sairão erradas.")
speaker.runAndWait()