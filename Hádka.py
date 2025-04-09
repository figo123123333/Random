import random

prodej = ["telefon","počítač","jablko","televize","porsche"]
for i in range(10):
    osoba1 = random.choice(prodej)
    osoba2 = random.choice(prodej)
    if osoba1 == osoba2:
        print(f"Kupme {osoba1} \n Ne kupme {osoba2}")
    else:
        print(f"Kupme {osoba1} \n Ne kupme {osoba2}")
