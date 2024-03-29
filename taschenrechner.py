#Auswahl der gewünschten Rechenoperation durch den Benutzer
auswahl = input("Bitte Rechenoperation auswählen:\n1:Addieren\n2:Subtrahieren\n3:Multiplizieren\n4:Dividieren\nwähle ein: ")

#Methoden zur Addition/Subtraktion
def subtrahieren(num1, num2):
    ergebnis = num1 - num2
    return ergebnis

def addieren(num1, num2):
    ergebnis = num1 + num2
    return ergebnis

def potenzieren(base, exponent):
    ergebnis = pow(base, exponent)
    return ergebnis
#Methoden zur Multiplikation und Division
def multiplizieren(num1, num2):
    ergebnis = num1 * num2
    return ergebnis

def dividieren(num1, num2):
    ergebnis = num1 / num2
    return ergebnis
    
# Überprüfung der Richtigkeit des eingegebenen Wertes
corrects = ['1', '2', '3', '4']
if auswahl not in corrects:
    print("Ungültige Auswahl. Bitte eine Nummer von 1 bis 4 eingeben.")
    quit()

#Eingabe der Zahlen durch Benutzer
try:
    num1 = float(input("Geben Sie die erste Zahl ein: "))
    num2 = float(input("Geben Sie die zweite Zahl ein: "))
except ValueError:
    print('Bitte gebe eine Nummer ein')
    quit()

result = 0

#Kontrollstruktur, die entscheidet welche Rechenoperation durchgeführt wird
if auswahl == "1":
    result = addieren(num1, num2)
    print("Ergebnis: ", result)
elif auswahl == "2":
    result = subtrahieren(num1, num2)
    print("Ergebnis: ", result)
elif auswahl == "3":
        result = multiplizieren(num1, num2)
        print("Ergebnis: ", result)
elif auswahl == "4":
    try:
         result = dividieren(num1, num2)
         print("Ergebnis: ", result)
    except ZeroDivisionError:
         print("Man kann nicht durch 0 teilen.")
