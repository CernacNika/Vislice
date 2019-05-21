import random

#Definiramo konstante
STEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = '-'
NAPACNA_CRKA = 'O'

ZACETEK = 'S'
#pove, da igra še ni začela, da še nč ne izriše
ZMAGA = 'W'
PORAZ = 'X'

# ABECEDA = 'ABCČDEFGHIJKLMNOPRSŠTUVZŽ'
#to lahko še dodatno definiraš pa potli popraviš pri vnosu

#Definiramo logični model igre

class Igra: 

    def __init__(self, geslo, crke):
        self.geslo = geslo.upper() #string
        self.crke = crke #list
        return 

    # def napacne_crke(self):
    #     sez = []
    #     for crka in crke:
    #         if crka not in geslo:
    #             sez.append(crka)
    #     return seznam

    def napacne_crke(self):
        napacne = []
        for crka in self.crke:
            if crka not in self.geslo:
               napacne.append(crka)
        return napacne

    def pravilne_crke(self):
        sez = []
        for crka in self.crke:
            if crka in self.geslo:
                sez.append(crka)
        return sez

    # def pravilne_crke(self):
    #     return [c for c in self.crke if c in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    # def zmaga(self):
    #     for crka in geslo:
    #         if crka not in pravilne_crke(self):
    #             return False
    #     return True

    def zmaga(self):
        if self.poraz():
            return False
        else:
            for crka in self.geslo:
                if crka not in self.crke:
                    return False
            return True
            
    # def poraz(self):
    #     return len(napacne_crke(self)) > STEVILO_DOVOLJENIH_NAPAK

    def poraz(self):
        return self.stevilo_napak() >  STEVILO_DOVOLJENIH_NAPAK

    # def pravilni_del_gesla(self):
    #     niz = ""
    #     for crka in geslo:
    #         if crka in pravilne_crke(self):
    #             niz += crka
    #         else:
    #             niz += '_'
    #     return niz

    def pravilni_del_gesla(self):
        niz = ""
        for crka in self.geslo:
            if crka in self.crke:
                niz+= " " + crka
            else: niz += " _"
        niz = niz.strip() #počistimo presledke
        return niz


    # def nepravilni_ugibi(self):
    #     niz = ""
    #     for crka in napacne_crke(self):
    #         niz += crka + ", "
    #     niz = niz.strip().strip(',')
    #     return niz
    
    # def nepravilni_ugibi(self):
    #     return napacne_crke(self).join(", ")
    
    def nepravilni_ugibi(self):
        return " ".join(self.napacne_crke())

    # ne briši presledkov z niz[::-1], raje s strip() 
    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        elif crka in self.geslo:
            self.crke.append(crka)
            if self.zmaga():
                return ZMAGA
            else: 
                return PRAVILNA_CRKA
        else:
            self.crke.append(crka)
            if self.poraz():
                return PORAZ
            else: 
                return NAPACNA_CRKA

# Izluščimo vse slovenske besede
bazen_besed = []

with open("besede.txt", 'r', encoding='utf-8') as datoteka:
    for vrstica in datoteka.readlines():
        beseda = vrstica.strip()
        bazen_besed.append(beseda)

#Funkcije za generiranje iger

def nova_igra():
    geslo = random.choice(bazen_besed)
    return Igra(geslo, [])

class Vislice:

    def __init__(self):

        #v slovarju igre ima vsaka igra svoj ID
        #ID je celo število
        self.igre = {}
        
        return

    def prost_id_igre(self):
        if self.igre == {}:
            return 0
        else: 
            #preverimo katero od 'n + 1' števil še ni uporavljeno za if 'n' iger
            for i in range(len(self.igre) + 1):
                if i not in self.igre.keys():
                    return i
        # lahko bi tudi takoj za else:
        #                            return max(self.igre.keys()) + 1
    def nova_igra(self):
        # Ustvari novo igro in nov ID
        igra = nova_igra()
        nov_id = self.prost_id_igre()

        #Dodaj v slovar iger
        self.igre[nov_id] = (igra, ZACETEK)

        return nov_id

        #Naredi novo igro z naključnim geslom

        #shrani (ZACeTEK, igra) v slovar z novim ID

    def ugibaj(self, id_igre, crka):
        #Pridobi igro
        (igra, _) = self.igre[id_igre]
        #ugibaj
        nov_poskus = igra.ugibaj(crka)
        #Shrani rezultat poskusa v slovar
        self.igre[id_igre] = (igra, nov_poskus)
        return

#Nič posebnega ne rabmo vračat ker itak vse kar smo že naredl je shranjen v slovarju. Vse kar shraniš v podčrtaj, python vrže stran in tega ne morš več nazaj dobit