# importacao de bibliotecas 
import speech_recognition as sr 
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence

# criar um objeto de reconhecimento de fala
r = sr.Recognizer()


andares = ["terreo", "primeiro", "segundo", "terceiro", "quarto", "quinto", "sexto", "setimo", "oitavo", "nono", "decimo"]

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
            print("andar: ", word)
            break

      # se tiver a palavra descer na frase
      else:
        print("descer")
        # procurar o andar
        for word in words:
          # se a palavra estiver na lista de andares
          if word in andares:
            print("andar: ", word)
            break

      
      # ['elevador', 'subir', 'o', 'quinto', 'andar']
      # ['elevador', 'descer', 'o', 'terceiro', 'andar']


    # se nao tiver elevador na frase
    else:
      print("Não é elevador")

