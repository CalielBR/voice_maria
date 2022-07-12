import pyttsx3

texto = "Mike Carvalho Barbosa, apresente-se no Consultório CT03"

# Lê o arquivo de texto ou pdf no diretorio do PC
f = open('D:/STUDY/Python/voz_maria/chamada.txt', 'r', encoding="utf8")
texto = f.read()

# Inicia serviço biblioteca
speaker = pyttsx3.init()
# metodo de voz
voices = speaker.getProperty('voices')

# Lista as vozes instaladas no PC
for voice in voices:
    # Mostra a ID dos idiomas de voz instalados em seu PC
    print(voice, voice.id)

# Define a voz padrao, no meu caso o portugues era o[0] (iniciando do zero)
speaker.setProperty('voice', voices[0].id)
rate = speaker.getProperty('rate')
# Altera velocidade da leitura, quanto menor mais lento
speaker.setProperty('rate', rate-10)

# Escreve o texto na tela
print(texto)
# Define o texto que será lido
speaker.say(texto)
# Lê o texto
speaker.runAndWait()
# Fecha o modo de leitura do arquivo txt ou pdf
f.close()
