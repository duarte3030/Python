# Father's Day code 2021
import vlc
import time


check1 = check2 = check3 = check4 = check5 = True
while check1:
    a1 = "d"
    q1 = input("\nPergunta 1: Qual figura pública abaixo gostava de beber a água \"Evian\" durante seus principais trabalhos/performances?\na) Hugo Hoyama\nb) Robbie Williams\nc) Albert Einstein\nd) Nenhum acima\n\nDigite a letra correta: ")
    check1 = (q1 != a1)
    if check1 is True:
        print("\nTente novamente.\n")
    else:
        print("\nBoa!\n")
        p = vlc.MediaPlayer("C:/Users/Guilherme Duarte/Google Drive/Documents/SW/GitHub/Python/FathersDay/itstrue.mp3")
        p.play()
        time.sleep(3)
while check2:
    a2 = "a"
    q2 = input("\nPergunta 2: Onde fica a nascente da água Evian?\na) Alpes franceses\nb) Fiordes Noruegueses\nc) Serra do Curral\nd) Rio onde o Stephen Hawking nadava\n\nDigite a letra correta: ")
    check2 = (q2 != a2)
    if check2 is True:
        print("\nTente novamente.\n")
    else:
        print("\nYes!\n")
        p = vlc.MediaPlayer("C:/Users/Guilherme Duarte/Google Drive/Documents/SW/GitHub/Python/FathersDay/ofcourse.mp3")
        p.play()
        time.sleep(3)
while check3:
    a3 = "c"
    q3 = input("\nPergunta 3: Por quê estou perguntando tanto dessa Evian?\na) À toa\nb) Vai ganhar só uma água de presente\nc) Medo de dar muitas dicas da resposta\nd) Nenhuma acima\n\nDigite a letra correta: ")
    check3 = (q3 != a3)
    if check3 is True:
        print("\nTente novamente.\n")
    else:
        print("\nAí sim!\n")
        p = vlc.MediaPlayer("C:/Users/Guilherme Duarte/Google Drive/Documents/SW/GitHub/Python/FathersDay/itsok.mp3")
        p.play()
        time.sleep(3)
while check4:
    a4 = "d"
    q4 = input("\nPergunta 4: Quem é essa pessoa que tá falando?\na) Filho do Robbie Williams\nb) Justin Bieber\nc) Eu\nd) Nenhuma acima\n\nDigite a letra correta: ")
    check4 = (q4 != a4)
    if check4 is True:
        print("\nTente novamente.\n")
    else:
        print("\nAham!\n")
        p = vlc.MediaPlayer("C:/Users/Guilherme Duarte/Google Drive/Documents/SW/GitHub/Python/FathersDay/auu.mp3")
        p.play()
        time.sleep(3)
while check5:
    a5 = "d"
    q5 = input("\nPergunta 5: Quem é o Rei do Pop?\na) Justin Bieber\nb) Phil Collins\nc) Robbie Williams\nd) Michael Jackson\n\nDigite a letra correta: ")
    check5 = (q5 != a5)
    if check5 is True:
        print("\nTente novamente.\n")
    else:
        print("\nMas é por pouco né? #sqn\n")
        p = vlc.MediaPlayer("C:/Users/Guilherme Duarte/Google Drive/Documents/SW/GitHub/Python/FathersDay/wuw.mp3")
        p.play()
        time.sleep(3)
q6 = input("\nPergunta 6: Qual é o tema do seu presente?\na) Michael Jackson\nb) Michael Jackson\nc) Michael Jackson\nd) Michael Jackson\n\nDigite a letra correta: ")
print("\n      So let's start something new...\n      (Então vamos começar algo novo...)\n")
time.sleep(2)
import webbrowser
import win32com.client as comctl
while True:
    p = vlc.MediaPlayer("C:/Users/Guilherme Duarte/Google Drive/Documents/SW/GitHub/Python/FathersDay/audio.mp3")
    p.play()
    time.sleep(3)
    url = 'https://docs.google.com/presentation/d/1K-RNLdqdncs3JsoVbm_X5Hax-RCCL9lzhJgOn9ZFp9U/present'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
    wsh = comctl.Dispatch("WScript.Shell")
    # Google Chrome window title
    wsh.AppActivate("icanhazip.com")
    time.sleep(1)
    wsh.SendKeys("{F11}")

    time.sleep(360)
