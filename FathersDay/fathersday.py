# Father's Day code 2021
import vlc
import time
check1 = check2 = check3 = check4 = check5 = True

while check1:
    a1 = "d"
    q1 = input("\nPergunta 1: Qual...?\na) a\nb) b\nc) c\nd) d\n\nDigite a letra correta: ")
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
    q2 = input("\nPergunta 2: Qual...?\na) a\nb) b\nc) c\nd) d\n\nDigite a letra correta: ")
    check2 = (q2 != a2)
    if check2 is True:
        print("\nTente novamente.\n")
    else:
        print("\nYes!\n")
        p = vlc.MediaPlayer("C:/Users/Guilherme Duarte/Google Drive/Documents/SW/GitHub/Python/FathersDay/ofcourse.mp3")
        p.play()
        time.sleep(3)

while check3:
    a3 = "d"
    q3 = input("\nPergunta 3: Qual...?\na) a\nb) b\nc) c\nd) d\n\nDigite a letra correta: ")
    check3 = (q3 != a3)
    if check3 is True:
        print("\nTente novamente.\n")
    else:
        print("\nAí sim!\n")
        p = vlc.MediaPlayer("C:/Users/Guilherme Duarte/Google Drive/Documents/SW/GitHub/Python/FathersDay/itsok.mp3")
        p.play()
        time.sleep(3)

while check4:
    a4 = "c"
    q4 = input("\nPergunta 4: Qual...?\na) a\nb) b\nc) c\nd) d\n\nDigite a letra correta: ")
    check4 = (q4 != a4)
    if check4 is True:
        print("\nTente novamente.\n")
    else:
        print("\nAham!\n")
        p = vlc.MediaPlayer("C:/Users/Guilherme Duarte/Google Drive/Documents/SW/GitHub/Python/FathersDay/wuw.mp3")
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
        p = vlc.MediaPlayer("C:/Users/Guilherme Duarte/Google Drive/Documents/SW/GitHub/Python/FathersDay/auu.mp3")
        p.play()
        time.sleep(3)

q6 = input("\nPergunta 6: Qual é o tema do seu presente?\na) Michael Jackson\nb) Michael Jackson\nc) Michael Jackson\nd) Michael Jackson\n\nDigite a letra correta: ")
print("\nSo let's start something...\n")
time.sleep(1)
while True:
    p = vlc.MediaPlayer("C:/Users/Guilherme Duarte/Google Drive/Documents/SW/GitHub/Python/FathersDay/audio.mp3")
    p.play()
    time.sleep(360)


