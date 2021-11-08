
import speech_recognition as sr
import subprocess
import tempfile
import pyttsx3
 
# 音声合成
def TextToSpeech_pyttsx3(ph):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    rate = engine.getProperty('rate')
    #声質
    engine.setProperty("voice", voices[0].id)
    #速さ
    engine.setProperty('rate', rate-50)
    engine.say(ph)
    engine.runAndWait()
 


TextToSpeech_pyttsx3('起動します')
print("ハロー") 

# 音声入力
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #print("ハロー")
        audio = r.listen(source)
 
    try:
        # Google Web Speech APIで音声認識
        text = r.recognize_google(audio, language="ja-JP")
    except sr.UnknownValueError:
        #print("Google Web Speech APIは音声を認識できませんでした。")
        print("もう一回言って？")
        TextToSpeech_pyttsx3("もう一回言って？")
        continue
    except sr.RequestError as e:
        print("GoogleWeb Speech APIに音声認識を要求できませんでした;"
              " {0}".format(e))
    else:
        
        print(text)
        #TextToSpeech_pyttsx3(text)
    if text == "終了":
        TextToSpeech_pyttsx3('終了します')
        break

    TextToSpeech_pyttsx3(text)

print("正常に終了しました")