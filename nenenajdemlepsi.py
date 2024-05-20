
def pridat_do_pole(pole, hodnota): #definuje funkci pridat_do_pole
    if isinstance(hodnota, int) and hodnota > 0: # podmínka na to aby byla hodnota kladné a celé číslo
        pole.append(hodnota) #přidá vybrané číslo
        return True # jestliže podmínka je prvadivá, funkce se vyhodnotí s hodnotou True
    return False # jestliže podmínka je neprvadivá, funkce se vyhodnotí s hodnotou False

def hlavni_funkce(): # definuje hlavní_funkci
    pole = [] # vytvoření pole
    
    for i in range(5): # cyklus který se opakuje 5x díky funkci for i in

        vstup = input("Zadej kladné celé číslo: ") # zadání vztupní hodnoty
        try: # vyzkouší blok kodu a pokud se vyskytne error , daný blok kodu neproběhne
            cislo = int(vstup) # přetypuje proměnou číslo na datový typ z int na str
        except ValueError: # jestliže se vyskytne v bloku try error kod přeskocí a provede se 2. kod ve bloku expect do ktereho napiseme typ erroru
            print("To není platné číslo!") # vytiskne to co je v závorce
            continue # pokracování v kodu

        if pridat_do_pole(pole, cislo): # přidání hodnoty do pole pomocí funkce
            print(f"Hodnota {cislo} byla přidána do pole.") # vytiskne to co je v závorce
        else: # jestliže podminka vyjde false probehne blok kodu v else
            print(f"Hodnota {cislo} nesplňuje podmínky a nebyla přidána.") # vytiskne to co je v závorce
        
    print("Kontrola pole:") # vytiskne to co je v závorce
    if len(pole) > 0 and not (len(pole) % 2 == 0): # Podmínka pro lichý počet prvků v poli
        print("Pole má lichý počet prvků.") # vytiskne to co je v závorce
    elif len(pole) == 0 or (len(pole) % 2 == 0): # podmínka pro to jestli se to rovná nule
        print("Pole je buď prázdné nebo má sudý počet prvků.") # vytiskne to co je v závorce
    
    if len(pole) > 0: # pokud je pole delší než 0
        odstranena_hodnota = pole.pop(0) # odstraní prví hodnotu pomocí pop
        print(f"První hodnota {odstranena_hodnota} byla odebrána z pole.") # vytiskne to co je v závorce
    
    print("Konečné pole:", pole) # vytiskne to co je v závorce

hlavni_funkce() # vyvolá hlavní funkci