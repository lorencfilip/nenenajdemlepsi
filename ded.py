# Funkce pro přidání hodnoty do pole, pokud splňuje určitou podmínku
def pridat_do_pole(pole, hodnota):
    if isinstance(hodnota, int) and hodnota > 0:  # Podmínka, aby byla hodnota kladné celé číslo
        pole.append(hodnota)
        return True
    return False

# Hlavní funkce
def hlavni_funkce():
    # Inicializace pole
    pole = []
    
    # Cyklus s pevným počtem opakování (např. 5 opakování)
    for i in range(5):
        # Vstup od uživatele s přetypováním
        vstup = input("Zadej kladné celé číslo: ")
        try:
            cislo = int(vstup)
        except ValueError:
            print("To není platné číslo!")
            continue
        
        # Přidání hodnoty do pole pomocí funkce
        if pridat_do_pole(pole, cislo):
            print(f"Hodnota {cislo} byla přidána do pole.")
        else:
            print(f"Hodnota {cislo} nesplňuje podmínky a nebyla přidána.")
        
    # Práce s podmínkami a logickými operátory AND, OR, NOT
    print("Kontrola pole:")
    if len(pole) > 0 and not (len(pole) % 2 == 0):  # Podmínka pro lichý počet prvků v poli
        print("Pole má lichý počet prvků.")
    elif len(pole) == 0 or (len(pole) % 2 == 0):
        print("Pole je buď prázdné nebo má sudý počet prvků.")
    
    # Odebrání prvního prvku z pole, pokud nějaký existuje
    if len(pole) > 0:
        odstranena_hodnota = pole.pop(0)
        print(f"První hodnota {odstranena_hodnota} byla odebrána z pole.")
    
    # Výstup výsledného pole
    print("Konečné pole:", pole)

# Spuštění hlavní funkce
hlavni_funkce()