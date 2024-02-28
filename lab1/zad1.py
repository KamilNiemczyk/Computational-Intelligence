import datetime
import math

#30minut zajęło to napisanie samemu, a jakos 5 minut zajęło to chatowi

# imie = str(input("Podaj imie: "))
# dzien = int(input("Podaj dzien urodzenia: "))
# miesiac = int(input("Podaj miesiac urodzenia: "))
# rok = int(input("Podaj rok urodzenia: "))
imie = "Kamil"
dzien = 24
miesiac = 1
rok = 2002
print("Witaj", imie)
aktualna_data = datetime.datetime.now()
ileminelo = aktualna_data - datetime.datetime(rok, miesiac, dzien)
ileminelo = ileminelo.days
print("Masz", ileminelo, "dni")

biorytmfizyczny = math.sin((ileminelo * 2 * math.pi) / 23)
biorytmemocjonalny = math.sin((ileminelo * 2 * math.pi) / 28)
biorytmintelektualny = math.sin((ileminelo * 2 * math.pi) / 33)

if biorytmfizyczny > 0.5:
    biorytmfizyczny = f"Jesteś w formie fizycznej = {biorytmfizyczny}"
elif biorytmfizyczny < -0.5:
    biorytmfizyczny = f"Jesteś w słabej formie fizycznej = {biorytmfizyczny}"
    nowybiorytmfizyczny = math.sin((ileminelo+1 * 2 * math.pi) / 23)
    if nowybiorytmfizyczny > math.sin((ileminelo * 2 * math.pi) / 23):
        biorytmfizyczny = biorytmfizyczny + " jutro bedzie lepiej"
    else:
        biorytmfizyczny = biorytmfizyczny + " jutro bedzie gorzej"

if biorytmemocjonalny > 0.5:
    biorytmemocjonalny = f"Jesteś w formie emocjonalnej = {biorytmemocjonalny}"
elif biorytmemocjonalny < -0.5:
    biorytmemocjonalny = f"Jesteś w słabej formie emocjonalnej = {biorytmemocjonalny}"
    nowybiorytmemocjonalny = math.sin((ileminelo+1 * 2 * math.pi) / 28)
    if nowybiorytmemocjonalny > math.sin((ileminelo * 2 * math.pi) / 28):
        biorytmemocjonalny = biorytmemocjonalny + " jutro bedzie lepiej"
    else:
        biorytmemocjonalny = biorytmemocjonalny + " jutro bedzie gorzej"
if biorytmintelektualny > 0.5:
    biorytmintelektualny = f"Jesteś w formie intelektualnej = {biorytmintelektualny} "
elif biorytmintelektualny < -0.5:
    biorytmintelektualny = f"Jesteś w słabej formie intelektualnej = {biorytmintelektualny}"
    nowybiorytmintelektualny = math.sin((ileminelo+1 * 2 * math.pi) / 33)
    if nowybiorytmintelektualny > math.sin((ileminelo * 2 * math.pi) / 33):
        biorytmintelektualny = biorytmintelektualny + " jutro bedzie lepiej"
    else:
        biorytmintelektualny = biorytmintelektualny + " jutro bedzie gorzej"

lista = [biorytmfizyczny, biorytmemocjonalny, biorytmintelektualny]       


for elem in lista:
    if type(elem) == str:
        print(elem)

# def oblicz_biorytmy(ileminelo, okres):
#     wartosc_biorytmu = math.sin((ileminelo * 2 * math.pi) / okres)
#     komunikat = ""
#     if wartosc_biorytmu > 0.5:
#         komunikat = f"Jesteś w formie = {wartosc_biorytmu}"
#     elif wartosc_biorytmu < -0.5:
#         komunikat = f"Jesteś w słabej formie = {wartosc_biorytmu}"
#         nowy_wartosc = math.sin(((ileminelo + 1) * 2 * math.pi) / okres)
#         if nowy_wartosc > wartosc_biorytmu:
#             komunikat += " jutro będzie lepiej"
#         else:
#             komunikat += " jutro będzie gorzej"
#     return komunikat

