# importacao de bibliotecas 
import speech_recognition as sr 
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence
import serial
import time

# criar um objeto de reconhecimento de fala
r = sr.Recognizer()

# Defina a porta serial do Arduino e a taxa de transmissão (baud rate)
porta_serial = "COM3"  # Substitua pela porta serial correta do seu Arduino
baud_rate = 9600

andares = ["terreo", "primeiro", "segundo", "terceiro", "quarto", "quinto", "sexto", "setimo", "oitavo", "nono", "decimo"]

arduino = serial.Serial(porta_serial, baud_rate, timeout=1)
# Aguarde um momento para que a comunicação serial seja estabelecida
time.sleep(2)

with sr.Microphone() as source:
    # ler os dados de áudio do microfone padrão
    audio_data = r.record(source, duration=5)
    print("Reconhecendo...")
    # converter fala em texto
    text = r.recognize_google(audio_data, language="pt-BR")

    # verificar se tem a palavra elevador na frase
    hasElevator = text.find("elevador") # retorna -1 se não encontrar

    # se tiver elevador na frase
    if hasElevator != -1:
      print("has elevador")
      # separar a frase em palavras
      words = text.split(" ")
      print(words)

      # se tiver a palavra subir na frase
      if text.find("subir") != -1:
        print("subir")
        # procurar o andar
        for word in words:
          # se a palavra estiver na lista de andares
          if word in andares:
            arduino.write("subir "+word.encode('utf-8'))
            print("andar: ", word)
            break

      # se tiver a palavra descer na frase
      else:
        print("descer")
        # procurar o andar
        for word in words:
          # se a palavra estiver na lista de andares
          if word in andares:
            arduino.write("descer "+word.encode('utf-8'))
            print("andar: ", word)
            break

      
      # ['elevador', 'subir', 'o', 'quinto', 'andar']
      # ['elevador', 'descer', 'o', 'terceiro', 'andar']


    # se nao tiver elevador na frase
    else:
      print("Não é elevador")

arduino.close()