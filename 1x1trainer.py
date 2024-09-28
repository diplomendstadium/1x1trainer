
# https://github.com/diplomendstadium/1x1trainer

import random
import time
from datetime import datetime

def malaufgabe():
    faktor1 = random.randint(1,10)
    faktor2 = random.randint(1,10)
    ergebnis = faktor1 * faktor2

    print(f"Was ist {faktor1} mal {faktor2}?")
    antwort = input("Lösung: ")

    feedback = 0

    try:
        if int(antwort) == ergebnis:
            print("Stimmt! Gut gemacht")
            feedback = 1
        else:
            print(fehler)
            print(f"Richtig wäre gewesen: {ergebnis}.")
            with open("1x1trainer.fehler.txt", "a") as datei:
                datei.write(f"{datum}: {faktor1} * {faktor2} = {ergebnis}\
(≠ {antwort}) | {username}\n")
            
    except:
        print("Irgendwas stimmt mit deiner Eingabe nicht...")

    return feedback


def divisionsaufgabe():
    faktor1 = random.randint(1,10)
    faktor2 = random.randint(1,10)
    ergebnis = faktor1 * faktor2

    print(f"Was ist {ergebnis} geteilt durch {faktor1}?")
    antwort = input("Lösung: ")

    feedback = 0

    try:
        if int(antwort) == faktor2:
            print("Stimmt! Gut gemacht")
            feedback = 1
        else:
            print(fehler)
            print(f"Richtig wäre gewesen: {faktor2}.")
            with open("1x1trainer.fehler.txt", "a") as datei:
                datei.write(f"{datum}: {ergebnis} / {faktor1} = {faktor2}\
(≠ {antwort}) | {username}\n")
            
    except:
        print("Irgendwas stimmt mit deiner Eingabe nicht...")

    return feedback



logo = r"""
 ____        _______________              __ 
/_   |__  __/_   \__    ___/___________  |__| ____   ___________ 
 |   \  \/  /|   | |    |  \_  __ \__  \ |  |/    \_/ __ \_  __ \
 |   |>    < |   | |    |   |  | \// __ \|  |   |  \  ___/|  | \/
 |___/__/\_ \|___| |____|   |__|  (____  /__|___|  /\___  >__|   
           \/Version1.0                \/        \/     \/       
"""

fehler = r"""
 ____  ____  _  _  __    ____  ____ 
(  __)(  __)/ )( \(  )  (  __)(  _ \
 ) _)  ) _) ) __ (/ (_/\ ) _)  )   /
(__)  (____)\_)(_/\____/(____)(__\_)
"""



"""
Ab hier das Programm
"""

print(logo)

username_roh = input("Gib deinen Vornamen ein: ")
username = ''.join([char for char in username_roh if char.isalpha()])

laufzeit = 1

while laufzeit==1:

    # Aktuelles Datum
    aktuelles_datum = datetime.now()
    datum = aktuelles_datum.strftime("%d.%m.%Y")

    print()
    print("Es folgen 10 Rechenaufgaben. Viel Erfolg")
    startzeit = time.time()

    punkte = 0

    # Hier die eigentlichen aufgaben
    for i in range(1,11):
        print()
        print(f"Aufgabe {i}")
        punkte += malaufgabe() if random.choice([True, False]) else divisionsaufgabe()
    print()
    print(f"Du hast {punkte} von 10 Aufgaben richtig.")

    endzeit = time.time()
    stoppuhr = endzeit - startzeit
    stoppuhr = round(stoppuhr, 1)
            

    # Ergebnis speichern
    with open("1x1trainer.ergebnisse.txt", "a") as datei:
        datei.write(f"{datum};{punkte};{stoppuhr};{username}\n")

    print()
    fortsetzen = input("Nochmal? Dann tippe '1'. Alles andere für Abbruch: ")
    try:
        if int(fortsetzen) == 1:
            pass
        else:
            laufzeit=0
    except:
        laufzeit=0

print("\nProgramm wird beendet. Bis zum nächsten mal :)")
        
        
