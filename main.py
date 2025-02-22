import speech_recognition as sr
from gtts import gTTS
import os
import playsound
import webbrowser

def texto_fala():
    text_to_say = "Olá! tudo bem?"
    language = "pt"
    gtts_object = gTTS(text = text_to_say, lang = language, slow = False)

    from IPython.display import Audio
    gtts_object.save('1.wav')
    sound_file = '1.wav'
    Audio(sound_file, autoplay=True)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        # wait for a second to let the recognizer adjust the
        # energy threshold based on the surrounding noise level
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio, language='pt-BR')
            print(said)
        except sr.UnknownValueError:
            speak("Desculpa, não consegui entender o que disse.")
        except sr.RequestError:
            speak("Desculpa, o serviço não está disponível")
    return said.lower()

#speak converted audio to text
def speak(text):
    tts = gTTS(text=text, lang='pt')
    filename = "voice.mp3"
    try:
        os.remove(filename)
    except OSError:
        pass
    tts.save(filename)
    playsound.playsound(filename)

#function to respond to commands
def respond(text):
    print("Text from get audio " + text)
    if 'youtube' in text:
        webbrowser.open("https://www.youtube.com")
    elif 'wikipédia' in text:
        webbrowser.open("https://www.wikipedia.com")
    elif 'farmácia' in text:
        webbrowser.open("https://www.google.com.br/maps/search/farmacia/")
    elif 'sair' in text:
        speak("Tchau, até a próxima")
        exit()

#let's try it
#text = get_audio()
#speak(text)

def fala_texto():
    while True:
        print("Estou ouvindo...")
        text = get_audio()
        respond(text)

texto_fala()
fala_texto()