import time
print ("Vítej ve hře!\nRozhodl jsi se utéct ze školy, tak uvidíme jestli se ti to podaří.")
print ("Pravidla a základní ovládání:\nVždy budeš mít na výběr možnosti, za uvedenou možností bude číslo v závorce.")
print ("např. Chceš jít do prvních dveří (1) či do druhých (2) ? ")
print ("Až se rozhodneš, napiš jednoduše číslo do příslušného okýnka! ")
print ("Může se stát že narazíš na nějakou otázku od učitele, na tu stačí, že odpovíš, Ve tvé odpovědí nesmí být překlepy, jinak se ti hra spustí od začátku!")
print ("Pojďme si to vyzkoušet, když zadáš své jméno.")
name = input ("Zadej své jméno :\n")
print (f"Vítej ve hře ÚNIK Z BOŽETĚŠKY!")
print (f"Je tvé jméno {name}?")
print (f"Ano/Ne")
ch1 = "Ano"
ch2 = "Ne"
A1 = input ()

if A1 == ch1:
    print(f"Výborně, můžeme začít s útěkem!")

if A1 ==ch2:
    print(f"Ojoj, začni znovu a zadej správně své jméno.")

print("Vytáhni si plánek třetího patra.")
time.sleep(5)
print (f"Tvůj příběh začíná v UC9. Sedíš v lavici po škole, zůstal jsi tam sám a pracuješ na tvém ročníkovém projektu.\nNajednou se rozezní nefunkční rozhlas a ty uslysíš podivným hlasem.")
time.sleep(3)
print ("Vím, že tu někde jsi. Jdu si pro Tebe. Boj se.\nV hlavě si říkáš. JAK JE MOŽNÉ ŽE TEN ROZHLAS FUNGUJE? KDO TO JE? PROČ PO MNĚ JDE?\nMUSÍM IHNED UTÉCT!!! ")
time.sleep(3)
print (f"Rychle si sbalíš věci a otevřeš dveře z UC9. Kam se vydáš?\nBude to doleva k linux učebně (1), půjdeš za tvojí třídní, paní Gébovou, ji zachránit do kabinetu a budeš doufat, že se ti nic nestane (2) či se rozhodneš jít o patro níž rovnou a nebudeš nic riskovat (3)? ")
time.sleep(3)
Ch1 = int(input ("Jak jsi se rozhodl? : "))
if Ch1 == 1:
    print (f"Utíkáš doleva kolem UC10 a slyšíš hlasy, vydáš se tam?(Ano/Ne)")
    Ch2 = input ()
    if Ch2 == "Ano":
        A1 = "Der"
        A2 = "Ich wohne in Olomouc."
        A3 = "Božena Němcová"
        A4 = "PH"
        znamka = 5
        print("Vejdeš dovnitř a tam uvidíš paní Křepelkovou zkoušet a ihned tě vyvolá k tabuli.")
        time.sleep(2)
        print("Protože jsi narušil moji hodinu, budeš zkoušený u tabule. V hlavě si řekneš. Ale NEEE, já nic neumím, já mám celou dobu Johna a nedávám pozor.")
        time.sleep(3)
        print("Paní Křepelková říká: Položím ti první otázku: Jaký člen má pes, Hund (Der/Die/Das)")
        YA1 = input()
        if YA1 == A1:
            print ("Správně")
            znamka = znamka -1
        else:
            print("CHYBA pokračujeme dále, správná odpověď je Der.") 
         
        print("Druhá otázka zní: Jak bys přeložil, Já bydlím v Olomouci.")
        YA2 = input()
        if A2 == YA2:
            print ("Působivé")
            znamka = znamka -1
        else :
            print(f"Špatně, jak jinak, správná odpověď je {A2}.")
    
        print("Protože učím i čj, začnu se ptát i na otázky z českého jazyka. Kdo napsal Babičku, poporsím celé jméno.")
        YA3 = input()
        if YA3 == A3:
            print ("Ohromující")
            znamka = znamka -1
        else:
            print(f"Vy nedáváte pozor ani v českém jazyce??? Toto jsou základy! Správná odpověď je {A3}.")
    
        print("Která písmena jsou velká v sousloví PRAŽŠKÝ HRAD?")
        YA4 = input()
        if YA4 == A4:
            print (f"správně")
            znamka = znamka -1
        else:
            print (f"Já už opravdu nevím co s vámi, je to {A4}.")

        print(f"V dálce uslyšíš podivné výkřiky a zvuky, tak se rozhodnete utéct z UC10 pryč.")
        time.sleep(2)
        print(f"Paní Křepelková na vás volá: DOSTAL JSTE ZA {znamka}, NEBOJTE SE, VŠE SI PÍŠU.")
        time.sleep(2)
        print("Mezitím jsi utekl a zadním schodištěm seběhl do druhého patra.")
    
    elif Ch2 == "Ne":
        print("Pokračuješ dál a doběhneš k zadnímu schodišti, kterým se vydáš do druhého patra.")
elif Ch1 == 2:
    print("Doběhl jsi do kabinetu paní Gébové a pana Stejskala. Oba byli vevnitř, ty jsi jim popsal situaci a oba dva začali utíkat s tebou.")
    time.sleep(2)
    print("Společně jste seběhli do druhého patra.")
elif Ch1 == 3:
    print("Seběhneš do druhého patra, z vrchu slyšíš křičet paní Gébovou s panem Stejskalem a ty jsi rád, že jsi té neznáme věci unikl a žiješ.")

print("Vytáhni si plánek druhého patra.")
time.sleep(5)
print(f"Dostal jsi se do druhé patra, co tě tu může asi čekat jiného než POSLUCHÁRNA?")
time.sleep(2)
print(f"Blížíš se k posluchárně a samozřejmě, že tam někdo je. Je tam pan Ženčiča s elektronikou (1) nebo Pan Losert se zaečkem(2) ?")
time.sleep(2)
A1= int(input("Co myslíš? : "))
if A1 == 1:
    print("Máš pravdu!! Je tam pan Ženčica a aby tě pustil pryč, musíš mu vypočítat kvadratickou rovnici.")
    time.sleep(2)
    print("Zadánní tvé kvadratické rovnice je a = 5, b = 57, c = 6")
    time.sleep(2)
    print("Ty máš ale naštěstí u sebe kvadratickou kalkulačku z dřívějška tak ji použiješ, POZOR ať tě pan Ženčica nevidí.")
    from math import sqrt, pow

    a = int(input("Zadej kořen a : "))
    b = int(input("Zadej kořen b : "))
    c = int(input("Zadej kořen c : "))

    D = (pow(b,2) - 4 *a*c)
    print (f"{D}") 
    if D > 0:

        x1 = (-b + sqrt(D))/ (2 *a)
        print(f"Kořen x1 je {x1}")
        x2 = (-b - sqrt(D))/ (2 *a)
        print(f"Kořen x2 je {x2}")
    else :
        print("Diskriminant je záporný, rovnice nemá řešení.")
    print("Máš štěstí! Pan Ženčica tě neviděl, je spokojený a můžeš pokračovat zase o patro níže.")    
if A1 == 2:
    print("Máš pravdu!! Je tam pan Losert, BÝT TEBOU TAK SI RADĚJI NACHYSTÁM PISÁTKO, KALKULAČKU A PAPÍR,\n aby tě pustil pryč, musíš mu vypočítat jeden ze šesti příkladů, který si náhodně vybereš pomocí jeho oblíbené kostky.")
    time.sleep(2)
    starter = int(input("Až budeš psychicky připraven hodit napiš číslo 13, oblíbené číslo pana Loserta.\n"))
    time.sleep(2)
    from random import randint
    priklad = randint (1,6)
    print (f"Vylosoval jsi si příklad číslo {priklad}")


    if priklad == 1 :
        vysl = 7000
        print("Uslyšíš známou větu: Všechno ze stolu, pisátko, kalkulačka a máš na to pět minut, můžeš začít.")
        time.sleep(2)
        print("Tvé zadání zní:\n Stanovte odpor vodiče, kterým prochází proud 25mA při napětí 175V. Výsledek zadej v ohmech.")
        time.sleep(2)
        Yvysl = int(input("Kolik ohmů : " ))
        if vysl == Yvysl:
            print(f"Výborně, můžeš domů!")
        else:
            print(f"Raději mi zmiz z očí! Správný výsledek je {vysl}.")


    if priklad == 2 :
        vysl = 30
        print("Uslyšíš známou větu: Všechno ze stolu, pisátko, kalkulačka a máš na to pět minut, můžeš začít.")
        time.sleep(2)
        print("Tvé zadání zní:\n Určete napětí na spotřebiči, jehož odpor je 1,5kΩ a kterým prochází proud 20mA. Výsledek zadej ve voltech.")
        time.sleep(2)
        Yvysl = int(input("Kolik voltů : " ))
        if vysl == Yvysl:
            print(f"Výborně, můžeš domů!")
        else:
            print(f"Raději mi zmiz z očí! Správný výsledek je {vysl}.")


    if priklad == 3 :
        vysl = 800
        print("Uslyšíš známou větu: Všechno ze stolu, pisátko, kalkulačka a máš na to pět minut, můžeš začít.")
        time.sleep(2)
        print("Tvé zadání zní:\n Stanovte výkon, vykonaný elektrickým proudem za 2 hodiny. Proud 10A prochází vodičem o odporu 8 ohmů. Výsledek zadej ve wattech.")
        time.sleep(2)
        Yvysl = int(input("Kolik wattů : " ))
        if vysl == Yvysl:
            print(f"Výborně, můžeš domů!")
        else:
            print(f"Raději mi zmiz z očí! Správný výsledek je {vysl}.")


    if priklad == 4 :
        vysl = 40
        print("Uslyšíš známou větu: Všechno ze stolu, pisátko, kalkulačka a máš na to pět minut, můžeš začít.")
        time.sleep(2)
        print("Tvé zadání zní:\n Vypočítejte, kolik hodin může svítit žárovka o příkonu 25W, než spotřebuje energii 1 kWh. Výsledek zadej v hodinách.")
        time.sleep(2)
        Yvysl = int(input("Kolik hodin : " ))
        if vysl == Yvysl:
            print(f"Výborně, můžeš domů!")
        else:
            print(f"Raději mi zmiz z očí! Správný výsledek je {vysl}.")

        
    if priklad == 5 :
        vysl = 20
        print("Uslyšíš známou větu: Všechno ze stolu, pisátko, kalkulačka a máš na to pět minut, můžeš začít.")
        time.sleep(2)
        print("Tvé zadání zní:\n Elektrická kamna jsou připojena na napětí 220V a mají příkon 4,4kW. Určete proud, který odebírají. Výsledek zadej v ampérách.")
        time.sleep(2)
        Yvysl = int(input("Kolik ampér : " ))
        if vysl == Yvysl:
            print(f"Výborně, můžeš domů!")
        else:
            print(f"Raději mi zmiz z očí! Správný výsledek je {vysl}.")
        
    if priklad == 6:
        print("Dnes máš štěstí, protože jsi hodil šestku a na šestku pan Losert nezkouší a pustil tě dále.")

vys1 = "receipt-invoice-customer"
vys3 = "school-goose-shark"


print("Vytáhni si plánek prvního patra.")
time.sleep(5)
print("Fuuha ten příklad mi dal zabrat, pomyslíš si. Chceš jít k hlavnímu vchodu, ale schodiště je zablokované, musíš tedy kolem kabinetu jazykářů.")
time.sleep(3)
print("Nejobávanější TRIO na škole, paní Matlerová, paní Heglasová a pan Deutsch, doufáš, že tě už nic nepotká a můžeš co nejrychleji utéct.")
time.sleep(3)
print("Přece jen ti jde o život a máš v patách neznámou identitu, která opravila rozhlas a jde si pro tebe.")
time.sleep(3)
print("Dojdeš ke kabinetu a nakonec se rozhodneš je varovat také. Zaťukáš a čekáš, kdo ti otevře, protože po většinu času je tam pani Matlerová.")
from random import randint
tvujucitel = randint(1,3)
    


if tvujucitel == 1:
    print("Paní Heglasová na tebe vytáhne její Business English a musíš ji přeložit tato slovíčka: ")
    time.sleep(2)
    print("Podle následující předlohy přelož:  účtenka-faktura-zákazník ")
    A1 = input("účtenka-faktura-zákazník ")
    if A1 == vys1:
        print("Potřebovala jsem si jen ověřit zda-li jste to vy, teď vás mohu ukrýt do bezpečí a počkat na mého manžela, který nám pomůže utéct.")
        time.sleep(3)
        print("Počkali jste společně na manžela, který vás oba dva protáhl oknem a vy jste přežili.")
        time.sleep(4)
        print("TOTO JE ÚSPĚŠNÝ KONEC HRY, GRATULUJI K ÚTĚKU")
    else:
        print("Bohužel toto není správna odpověď a nemohu vás připustit do našeho kabinetu.")
        time.sleep(3)
        print("Zabouchla za vámi a mezitím jste ztratil moc času. Duch pana Lorence vás dostihl a zavlékl do měření a co se s vámi stalo nechcete vědět.")
        time.sleep(4)
        print("TOTO JE NEÚSPĚŠNÝ KONEC HRY, PROHRAL JSI, MŮŽEŠ SE POKUSIT ZNOVU.")


if tvujucitel == 2:
    print("Paní Matlerová na tebe vytáhne její filozofii a chce po tobě slyšet smysl života : ")
    time.sleep(3)
    print("Řekni mi alespoň 50 slov o smyslu života : ")
    A2 = input("Smysl života : \n ")
    print("Paní Matlerové je jedno co jsi řekl, ona je spokojená a vezme tě do bezpečí jejich kabinetu, kde spolu počkáte na příjezd Policie, která vás bezpečně eskortuje ven ze školy.")
    time.sleep(5)
    print("TOTO JE ÚSPĚŠNÝ KONEC HRY, GRATULUJI K ÚTĚKU")

    
if tvujucitel == 3:
    print("Pan Deutsch na tebe vytáhne jeho anglickou konverzaci a chce po tobě přeložit tato slovíčka : ")
    time.sleep(2)
    print("Podle následující předlohy přelož:  škola-husa-žralok ")
    A3 = input("škola-husa-žralok : ")
    if A3 == vys3:
        print("Potřeboval jsem si jen ověřit zda-li jste to vy, teď vás mohu ukrýt do bezpečí mého kabinetu.")
        time.sleep(3)
        print("Šli jste spolu do jeho kabinetu a po cestě vás doběhl duch pana Lorence,který vás zavlékl do měření a co se s vámi stalo nechcete vědět. ")
        time.sleep(4)
        print("TOTO JE NEÚSPĚŠNÝ KONEC HRY, PROHRAL JSI, MŮŽEŠ SE POKUSIT ZNOVU.")
    else:
        print("Bohužel toto není správna odpověď a nemohu vás připustit do našeho kabinetu.")
        time.sleep(3)
        print("Zabouchl za vámi a mezitím jste ztratil moc času. Duch pana Lorence vás dostihl a zavlékl do měření a co se s vámi stalo nechcete vědět.")
        time.sleep(4)
        print("TOTO JE NEÚSPĚŠNÝ KONEC HRY, PROHRAL JSI, MŮŽEŠ SE POKUSIT ZNOVU.")











