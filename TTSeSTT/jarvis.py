# importing pyttsx3
import pyttsx3
# importing speech_recognition
import speech_recognition as sr
# criando função take_commands() que
# pode pegar um pouco de audio, reconhecer e retornar
# se não houver erros
def take_commands():
    # Inicializando speech_recognition
    r = sr.Recognizer()
    # abrindo microfone físico do computador
    with sr.Microphone() as source:
        print('Escutando')
        r.pause_threshold = 0.7
        # armazenando audio/som em uma variável
        audio = r.listen(source)
        try:
            print("Reconhecendo")
            # Reconhecendo áudio usando api da google
            Query = r.recognize_google(audio)
            print("A consulta impressa é = '", Query, "'")
        except Exception as e:
            print(e)
            print("Diga isso novamente: ")
            # Não retorna nada se houver erros
            return "Nenhum"
    # retornando audio como texto
    return Query
    
# criando função speak() para poder dar fala
# ao nosso assistente de voz
def Speak(audio):
    # inicializando pyttsx3 modulo
    engine = pyttsx3.init()
    # qualquer coisa passada em engine.say()
    # será falada pelo assistente
    engine.say(audio)
    engine.runAndWait()


# Código do driver
if __name__ == '__main__':
    # usando while para se comunicar infinitamente
    while True:
        command = take_commands()
        if "exit" in command:
            Speak("Sure sir! as your wish, bai")
            break
        if "insta" in command:
            Speak("Best python page on instagram is pythonhub")
        if "learn" in command:
            Speak("copyassignment website is best to learn python")
        if "code" in command:
            Speak("You can get this code from copyassignment website")