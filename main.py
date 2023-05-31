# importacao de bibliotecas 
import speech_recognition as sr 
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence

# criar um objeto de reconhecimento de fala
r = sr.Recognizer()

with sr.Microphone() as source:
    # ler os dados de áudio do microfone padrão
    audio_data = r.record(source, duration=5)
    print("Reconhecendo...")
    # converter fala em texto
    text = r.recognize_google(audio_data, language="pt-BR")

    hasElevator = text.find("elevador") # retorna -1 se não encontrar

    # se tiver elevador na frase
    if hasElevator != -1:
        print("Elevador")

    # se nao tiver elevador na frase
    else:
      print("Não é elevador")

    # print(text)
