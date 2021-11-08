import speech_recognition as sr
import subprocess
import tempfile
import pyttsx3
from googletrans import Translator
from generate_image import generate
import time
#from chat.chat import respond
from chat2.chat2 import chat2







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

def respons(flag,text):
    tr = Translator()
    if flag==1:
        #画像生成
        TextToSpeech_pyttsx3('生成中です')
        print(tr.translate(text=text, src="ja", dest="en").text)
        generate(tr.translate(text=text, src="ja", dest="en").text)
        TextToSpeech_pyttsx3(text+'を生成しました')
        return 0
    elif flag==2:
        #会話
        '''
        res=respond(tr.translate(text=text, src="ja", dest="en").text)
        print(tr.translate(text=res, src="en", dest="ja").text)
        TextToSpeech_pyttsx3(tr.translate(text=res, src="en", dest="ja").text)
        '''
        res=chat2(text)
        print(res)
        TextToSpeech_pyttsx3(res)
        return 2

def speach_txt(path):
    fileobj = open(path, "r", encoding="utf-8_sig")
    while True:
        line = fileobj.readline()
        if line:
            print(line)
            TextToSpeech_pyttsx3(line)

        else:
            break

def print_speach(text):
    print(text)
    TextToSpeech_pyttsx3(text)



        



def voice_rec():
    flag=0
    
    print_speach('人間を検出しました')

    #TextToSpeech_pyttsx3('起動します')
    
    
    print_speach('いらっしゃいませ！私はオープンキャンパス案内AIです')
    
    #print_speach('どんなことを知りたいですか？以下の中から教えて下さい。')
    print_speach('こんにちはと話しかけて下さい。')
    print('(音声入力受付中)')
    

    while True :
        r = sr.Recognizer()
        with sr.Microphone() as source:
            #print("ハロー")
            audio = r.listen(source)

        try:
            # Google Web Speech APIで音声認識
            text = r.recognize_google(audio, language="ja-JP")
        except sr.UnknownValueError:
            #print("Google Web Speech APIは音声を認識できませんでした。")
            #print("もう一回言って下さい。")
            #TextToSpeech_pyttsx3("もう一回言ってください。")
            continue
        except sr.RequestError as e:
            print("GoogleWeb Speech APIに音声認識を要求できませんでした;"
                " {0}".format(e))
        else: 
            if text=='こんにちは':
                print_speach('こんにちは!　東京電機大学、人工知能研究室へようこそ。')
                print_speach('どんなことを知りたいですか？以下の3つの中のどれかを読み上げて下さい。')
                print_speach('・東京電機大学について')
                print_speach('・人工知能研究室について')
                print_speach('・私について')
                print('　　　　')

                #print_speach('上の3つのうちどれかを読み上げて下さい。')

                break



    
    

    # 音声入力
    while True:
        print('(音声入力受付中)')
    

        r = sr.Recognizer()
        with sr.Microphone() as source:
            #print("ハロー")
            audio = r.listen(source)

        try:
            # Google Web Speech APIで音声認識
            text = r.recognize_google(audio, language="ja-JP")
        except sr.UnknownValueError:
            #print("Google Web Speech APIは音声を認識できませんでした。")
            print("もう一回言って下さい。")
            TextToSpeech_pyttsx3("もう一回言ってください。")
            continue
        except sr.RequestError as e:
            print("GoogleWeb Speech APIに音声認識を要求できませんでした;"
                " {0}".format(e))
        else:


            print('入力音声:',text)

            if text == "ありがとう":
                print_speach('ご利用、ありがとうございました')
                print_speach('来客検出モードに戻ります。')

                break

            if text == "終了":
                TextToSpeech_pyttsx3('プログラムを終了します')
                exit()
            
            if text=='東京電機大学について':
                t_path="./text/text.txt"
                speach_txt(t_path)

                print_speach('ほかに知りたいことはありますか？以下のどれかを読み上げて下さい。')

                print('・東京電機大学について')
                print('・人工知能研究室について')
                print('・私について')
                print('　　　　')

                #print('上の3つのうちどれかを読み上げて下さい。')



            if text=='人工知能 研究室について':
                t_path="./text/text1.txt"
                speach_txt(t_path)
                print_speach('ほかに知りたいことはありますか？以下のどれかを読み上げて下さい。')

                print('・東京電機大学について')
                print('・人工知能研究室について')
                print('・私について')
                print('　　　　')

                #print_speach('上の3つのうちどれかを読み上げて下さい。')

            if text=='私について':
                t_path="./text/text2.txt"
                speach_txt(t_path)
                print('・会話モードを開始：　AIと雑談することができます。')
                print('・会話モードを終了：　会話モードを終了します。')
                print('・人の画像を生成　：　指定した特徴の顔画像を生成します。')
                print('・ありがとう　　　：　案内を終了します。')





            if '人の画像を生成' == text:
                flag=1
                print_speach('どんな人を生成しますか？')
                continue

            if '会話モードを開始' == text:
                flag=2
                print_speach('会話モードに移行します')
                continue

            if '会話モードを終了' == text:
                if flag!=2:
                    print_speach('会話モードはまだ開始していません。')
                    continue
                else:
                    print_speach('会話モードを終了します')
                    flag=0
                    continue

        
            if 'ぬるぽ' == text:
                t_path="./text/text3.txt"
                speach_txt(t_path)
                continue

            if 'クレジット' == text:
                print('作成者：Ryunosuke Ikeda')
                print('会話API：https://www.chaplus.jp/')
                print('画像生成:http://cedro3.com/ai/styleclip-g/')
                continue

            flag=respons(flag,text)


            #TextToSpeech_pyttsx3(text)

    #print("正常に終了しました")



#voice_rec()