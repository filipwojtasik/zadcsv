import csv

terytorium = []
przystapilo = []
plec = []
rok = []
liczba = []




with open('Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            terytorium.append(row[0])
            przystapilo.append(row[1])
            plec.append(row[2])
            rok.append(row[3])
            liczba.append(row[4])

            line_count += 1


class teren():
    def __init__(self, woj):
        self.woj = woj

        if self.woj == 'polska':
            self.przystmin = 0
            self.przystmax = 17
            self.zdamin = 18
            self.zdamax = 35
        elif self.woj == 'dolnoslaskie':
            self.przystmin = 36
            self.przystmax = 53
            self.zdamin = 54
            self.zdamax = 71
        elif self.woj == 'kujawsko-pomorskie':
            self.przystmin = 72
            self.przystmax = 89
            self.zdamin = 90
            self.zdamax = 107
        elif self.woj == 'lubelskie':
            self.przystmin = 108
            self.przystmax = 125
            self.zdamin = 126
            self.zdamax = 143
        elif self.woj == 'lubuskie':
            self.przystmin = 144
            self.przystmax = 161
            self.zdamin = 162
            self.zdamax = 179
        elif self.woj == 'lodzkie':
            self.przystmin = 180
            self.przystmax = 197
            self.zdamin = 198
            self.zdamax = 215
        elif self.woj == 'malopolskie':
            self.przystmin = 216
            self.przystmax = 233
            self.zdamin = 234
            self.zdamax = 251
        elif self.woj == 'mazowieckie':
            self.przystmin = 252
            self.przystmax = 269
            self.zdamin = 270
            self.zdamax = 287
        elif self.woj == 'opolskie':
            self.przystmin = 288
            self.przystmax = 305
            self.zdamin = 306
            self.zdamax = 323
        elif self.woj == 'podkarpackie':
            self.przystmin = 324
            self.przystmax = 341
            self.zdamin = 342
            self.zdamax = 359
        elif self.woj == 'podlaskie':
            self.przystmin = 360
            self.przystmax = 377
            self.zdamin = 378
            self.zdamax = 395
        elif self.woj == 'pomorskie':
            self.przystmin = 396
            self.przystmax = 413
            self.zdamin = 414
            self.zdamax = 431
        elif self.woj == 'slaskie':
            self.przystmin = 432
            self.przystmax = 449
            self.zdamin = 450
            self.zdamax = 467
        elif self.woj == 'swietokrzyskie':
            self.przystmin = 468
            self.przystmax = 485
            self.zdamin = 486
            self.zdamax = 503
        elif self.woj == 'warminsko-mazurskie':
            self.przystmin = 504
            self.przystmax = 521
            self.zdamin = 522
            self.zdamax = 539
        elif self.woj == 'wielkopolskie':
            self.przystmin = 540
            self.przystmax = 557
            self.zdamin = 558
            self.zdamax = 575
        elif self.woj == 'zachodniopomorskie':
            self.przystmin = 576
            self.przystmax = 593
            self.zdamin = 594
            self.zdamax = 611
        else:

            self.przystmin = 0
            self.przystmax = 0
            self.zdamin = 0
            self.zdamax = 0

class zad1():
    def __init__(self, woje, pocz, kon, tryb):
        woj = teren(woje)

        osoby = 0
        self.pocz = pocz
        self.kon = kon
        self.tryb = tryb

        self.lata_pocz = self.pocz - 2010
        self.indeksm_pocz = woj.przystmin + 2 * self.lata_pocz
        self.indeksk_pocz = self.indeksm_pocz + 1

        self.lata_kon = self.kon - 2010
        self.indeksm_kon = woj.przystmin + 2 * self.lata_kon
        self.indeksk_kon = self.indeksm_kon + 1



        if self.tryb == 1:
            srednia=self.srednia_cal(self.indeksm_pocz,self.indeksk_kon)

        if self.tryb == 2:  # m
            srednia=self.srednia_m(self.indeksm_pocz,self.indeksm_kon)

        if self.tryb == 3:  # kobiety
            srednia=self.srednia_k(self.indeksk_pocz,self.indeksk_kon)

        if self.lata_pocz > 2010 :
            print("zla data")
        else:
            if woj.przystmin != 0:
                print(self.pocz,"-",self.kon,"\n",srednia)
            else:
                print("zle wpisane wojewodztwo")

    def srednia_cal(self,pocz,kon):

        osoby=0
        for i in range(kon - pocz + 1):
            li = int(liczba[pocz + i])

            osoby = osoby + li
        srednia = osoby / (self.kon - self.pocz + 1)
        return srednia

    def srednia_m(self,pocz,kon):

        osoby=0
        for i in range(int((kon - pocz) / 2) + 1):
            li = int(liczba[pocz + i * 2])

            osoby = osoby + li
        srednia = osoby / (self.kon - self.pocz + 1)
        return srednia
    def srednia_k(self,pocz,kon):

        osoby=0
        for i in range(int((kon - pocz) / 2) + 1):
            li = int(liczba[pocz + i * 2])

            osoby = osoby + li
        srednia = osoby / (self.kon - self.pocz + 1)
        return srednia



class zad2():
    def __init__(self, woje, tryb):
        woj = teren(woje)

        self.tryb = tryb

        if self.tryb == 1:
            for i in range(int((woj.przystmax - woj.przystmin) / 2) + 1):
                proc=self.tr1(woj.przystmin,woj.zdamin,i)

                if woj.przystmin != 0:
                    print(rok[woj.przystmin + i * 2], "- ", proc, "%")
                else:
                    print("zle wpisane wojewodztwo")

        if self.tryb == 2:  # m
            for i in range(int((woj.przystmax - woj.przystmin) / 2) + 1):
                proc=self.tr2(woj.przystmin,woj.zdamin,i)

                if woj.przystmin != 0:
                    print(rok[woj.przystmin + i * 2], "- ", proc, "%")
                else:
                    print("zle wpisane wojewodztwo")

        if self.tryb == 3:  # kob
            for i in range(int((woj.przystmax - woj.przystmin) / 2) + 1):
                proc=self.tr3(woj.przystmin,woj.zdamin,i)

                if woj.przystmin != 0:
                    print(rok[woj.przystmin + i * 2], "- ", proc, "%")
                else:
                    print("zle wpisane wojewodztwo")

    def tr1(self,min,minz,i):

                przyst = int(liczba[min + i * 2]) + int(liczba[min + 1 + i * 2])
                zdalo = int(liczba[minz + i * 2]) + int(liczba[minz + 1 + i * 2])
                proc = int(100 * zdalo / przyst)

                return proc


    def tr2(self,min,minz,i):

                przyst = int(liczba[min + i * 2])
                zdalo = int(liczba[minz + i * 2])
                proc = int(100 * zdalo / przyst)
                return proc


    def tr3(self,min,minz,i):

                przyst = int(liczba[min + 1 + i * 2])
                zdalo = int(liczba[minz + 1 + i * 2])
                proc = int(100 * zdalo / przyst)
                return proc




class zad3():
    def __init__(self, rok, tryb):
        self.rok = rok
        self.przyst = []
        self.zdalo = []
        self.wynik = []
        self.tryb = tryb

        self.lata_pocz = self.rok - 2010
        if self.tryb == 1:
            for i in range(16):
                ind=self.t1(self.lata_pocz,i)


        if self.tryb == 2:  # m
            for i in range(16):
                ind=self.t2(self.lata_pocz,i)


        if self.tryb == 3:  # kob
            for i in range(16):
                ind=self.t3(self.lata_pocz,i)

        def switch(argument):
            switcher = {
                0: "dolnoslaskie",
                1: "kujawsko-pomorskie",
                2: "lubelskie",
                3: "lubuskie",
                4: "lodzkie",
                5: "malopolskie",
                6: "mazowieckie",
                7: "opolskie",
                8: "podkarpackie",
                9: "podlaskie",
                10: "pomorskie",
                11: "slaskie",
                12: "swietokrzyskie",
                13: "warminsko-mazurskie",
                14: "wielkopolskie",
                15: "zachodniopomorskie"
            }

            return switcher.get(argument)



        print(self.rok, "- wojewodztwo", switch(ind))


    def t1(self, lata,i):

        self.przyst.append(int(liczba[(36 * (i + 1)) + (lata * 2)]) + int(
            liczba[(36 * (i + 1)) + (lata * 2) + 1]))
        self.zdalo.append((int(liczba[(36 * (i + 1)) + (lata * 2) + 18]) + int(
            liczba[(36 * (i + 1)) + (lata * 2) + 19])))

        self.wynik.append(100 * self.zdalo[i] / self.przyst[i])
        maxx = max(self.wynik)
        ind = self.wynik.index(maxx)
        return ind

    def t2(self,lata,i):
        self.przyst.append(int(liczba[(36 * (i + 1)) + (lata * 2)]))
        self.zdalo.append((int(liczba[(36 * (i + 1)) + (lata * 2) + 18])))

        self.wynik.append(100 * self.zdalo[i] / self.przyst[i])
        maxx = max(self.wynik)
        ind = self.wynik.index(maxx)
        return ind

    def t3(self,lata,i):
        self.przyst.append(int(liczba[(36 * (i + 1)) + (lata * 2) + 1]))
        self.zdalo.append((int(liczba[(36 * (i + 1)) + (lata * 2) + 19])))

        self.wynik.append(100 * self.zdalo[i] / self.przyst[i])
        maxx = max(self.wynik)
        ind = self.wynik.index(maxx)
        return ind


class zad4():
    def __init__(self, tab, tryb):

        self.woj = []
        self.rok = rok
        self.tryb = tryb

        if tryb == 1:
            for i in range(len(tab)):
                self.woj.append(teren(tab[i]))
                self.przyst = []
                self.zdalo = []
                self.wynik = []
                reg_pocz = []
                reg_kon = []
                for j in range(9):
                    self.przyst.append(int(liczba[(self.woj[i].przystmin) + (2 * j)]) + int(
                        liczba[(self.woj[i].przystmin) + (2 * j) + 1]))
                    self.zdalo.append(
                        int(liczba[(self.woj[i].zdamin) + (2 * j)]) + int(liczba[(self.woj[i].zdamin) + (2 * j) + 1]))
                    self.wynik.append(100 * self.zdalo[j] / self.przyst[j])

                    if len(self.wynik) > 1:
                        if self.wynik[j] < self.wynik[j - 1]:
                            reg_pocz.append(j - 1)
                            reg_kon.append(j)

                print("wojewodztwo", tab[i], "  ")


                for k in range(len(reg_pocz)):

                        print("201{} -> 201{}".format(reg_pocz[k], reg_kon[k]))

        if tryb == 2:  # m
            for i in range(len(tab)):
                self.woj.append(teren(tab[i]))
                self.przyst = []
                self.zdalo = []
                self.wynik = []
                reg_pocz = []
                reg_kon = []
                for j in range(9):
                    self.przyst.append(int(liczba[(self.woj[i].przystmin) + (2 * j)]))
                    self.zdalo.append(int(liczba[(self.woj[i].zdamin) + (2 * j)]))
                    self.wynik.append(100 * self.zdalo[j] / self.przyst[j])

                    if len(self.wynik) > 1:
                        if self.wynik[j] < self.wynik[j - 1]:
                            reg_pocz.append(j - 1)
                            reg_kon.append(j)

                print("wojewodztwo", tab[i], "  ")

                for k in range(len(reg_pocz)):
                        print("201{} -> 201{}".format(reg_pocz[k], reg_kon[k]))

        if tryb == 3:  # kob
            for i in range(len(tab)):
                self.woj.append(teren(tab[i]))
                self.przyst = []
                self.zdalo = []
                self.wynik = []
                reg_pocz = []
                reg_kon = []
                for j in range(9):
                    self.przyst.append(int(liczba[(self.woj[i].przystmin) + (2 * j) + 1]))
                    self.zdalo.append(int(liczba[(self.woj[i].zdamin) + (2 * j) + 1]))
                    self.wynik.append(100 * self.zdalo[j] / self.przyst[j])

                    if len(self.wynik) > 1:
                        if self.wynik[j] < self.wynik[j - 1]:
                            reg_pocz.append(j - 1)
                            reg_kon.append(j)
                print("wojewodztwo", tab[i], "  ")

                for k in range(len(reg_pocz)):
                        print("201{} -> 201{}".format(reg_pocz[k], reg_kon[k]))


class zad5():
    def __init__(self, woj1, woj2, tryb):

        self.woj2 = teren(woj2)
        self.woj1 = teren(woj1)
        self.tryb = tryb
        self.przyst = []
        self.zdalo = []
        self.wynik = []
        self.przyst2 = []
        self.zdalo2 = []
        self.wynik2 = []
        if self.tryb == 1:
            for i in range(9):
                self.przyst.append(int(liczba[(self.woj1.przystmin) + (2 * i)]) + int(
                    liczba[(self.woj1.przystmin) + (2 * i) + 1]))
                self.zdalo.append(
                    int(liczba[(self.woj1.zdamin) + (2 * i)]) + int(liczba[(self.woj1.zdamin) + (2 * i) + 1]))
                self.wynik.append(100 * self.zdalo[i] / self.przyst[i])

                self.przyst2.append(int(liczba[(self.woj2.przystmin) + (2 * i)]) + int(
                    liczba[(self.woj2.przystmin) + (2 * i) + 1]))
                self.zdalo2.append(
                    int(liczba[(self.woj2.zdamin) + (2 * i)]) + int(liczba[(self.woj2.zdamin) + (2 * i) + 1]))
                self.wynik2.append(100 * self.zdalo2[i] / self.przyst2[i])

                if self.wynik[i] > self.wynik2[i]:
                    if self.woj1.przystmin != 0:
                        print("201{}".format(i), "-", woj1)
                    else:
                        print("zle wpisane wojewodztwo")
                        break

                else:
                    if self.woj2.przystmin != 0:
                        print("201{}".format(i), "-", woj2)
                    else:
                        print("zle wpisane wojewodztwo")
                        break

        if self.tryb == 2:  # m
            for i in range(9):
                self.przyst.append(int(liczba[(self.woj1.przystmin) + (2 * i)]))
                self.zdalo.append(int(liczba[(self.woj1.zdamin) + (2 * i)]))
                self.wynik.append(100 * self.zdalo[i] / self.przyst[i])

                self.przyst2.append(int(liczba[(self.woj2.przystmin) + (2 * i)]))
                self.zdalo2.append(int(liczba[(self.woj2.zdamin) + (2 * i)]))
                self.wynik2.append(100 * self.zdalo2[i] / self.przyst2[i])

                if self.wynik[i] > self.wynik2[i]:
                    if self.woj1.przystmin != 0:
                        print("201{}".format(i), "-", woj1)
                    else:
                        print("zle wpisane wojewodztwo")
                        break

                else:
                    if self.woj2.przystmin != 0:
                        print("201{}".format(i), "-", woj2)
                    else:
                        print("zle wpisane wojewodztwo")
                        break

        if self.tryb == 3:  # kob
            for i in range(9):
                self.przyst.append(int(liczba[(self.woj1.przystmin) + (2 * i) + 1]))
                self.zdalo.append(int(liczba[(self.woj1.zdamin) + (2 * i) + 1]))
                self.wynik.append(100 * self.zdalo[i] / self.przyst[i])

                self.przyst2.append(int(liczba[(self.woj2.przystmin) + (2 * i) + 1]))
                self.zdalo2.append(int(liczba[(self.woj2.zdamin) + (2 * i) + 1]))
                self.wynik2.append(100 * self.zdalo2[i] / self.przyst2[i])

                if self.wynik[i] > self.wynik2[i]:
                    if self.woj1.przystmin != 0:
                        print("201{}".format(i), "-", woj1)
                    else:
                        print("zle wpisane wojewodztwo")
                        break

                else:
                    if self.woj2.przystmin != 0:
                        print("201{}".format(i), "-", woj2)
                    else:
                        print("zle wpisane wojewodztwo")
                        break


class start():
    def __init__(self):
        while(True):
            tryb=1
            x=0
            if x==0:
                print(
                    "Wybierz zadanie (liczba od 1 do 5)"
                    "\n zad 1 obliczenie sredniej liczby osob, ktore przystapily do egzaminu dla danego wojewodztwa "
                    "\n zad 2 obliczenie procentowej zdawalnosci dla danego wojewodztwa na przestrzeni lat "
                    "\n zad 3 podanie wojewodztwa o najlepszej zdawalnosci w konkretnym roku "
                    "\n zad 4 wykrycie wojewodztw, ktore zanotowaly regresje "
                    "\n zad 5 porownanie dwoch wojewodztw"
                    "\n 'z' zakonczenie programu \n"
                     )
                x = input()

            if x=="1":
                print("podaj wojewodztwo: (male litery i bez polskich znakow)")
                x1=input()
                print("\npodaj przedzial lat oddzielony znakiem '-' (od 2010 do 2018)")
                x2=input()
                buf=0
                x21=[]
                x22=[]
                for i in range(len(x2)):
                    if x2[i]=="-":
                        buf=1
                    if buf==0 and x2[i]!="-":
                        x21.append(x2[i])
                    if buf==1 and x2[i]!="-":
                        x22.append(x2[i])
                x23=int(''.join(x21))
                x24=int(''.join(x22))
                print(x23,x24)
                print("dla jakiej grupy chcesz przeprowadziić zadanie?"
                      "\n dla znaku 'm' grupa mezczyzn"
                      "\n dla 'k' grupa kobiet \n kazdy inny oznacza osoby bez rozrozniania na plec")
                x3=input()
                if x3=='m':
                    tryb=2
                elif x3=='k':
                    tryb=3
                else:
                    tryb=1
                zad1(x1,x23,x24,tryb)
                x=0
            if x=="2":
                print("podaj wojewodztwo: (male litery i bez polskich znakow)")
                x1 = input()
                print("dla jakiej grupy chcesz przeprowadziić zadanie?"
                      "\n dla znaku 'm' grupa mezczyzn"
                      "\n dla 'k' grupa kobiet \n kazdy inny oznacza osoby bez rozrozniania na plec")
                x3 = input()
                if x3 == 'm':
                    tryb = 2
                elif x3 == 'k':
                    tryb = 3
                else:
                    tryb = 1

                zad2(x1, tryb)
                x=0

            if x=="3":
                print("podaj rok (od 2010 do 2018)")
                x1 = input()

                print("dla jakiej grupy chcesz przeprowadziić zadanie?"
                      "\n dla znaku 'm' grupa mezczyzn"
                      "\n dla 'k' grupa kobiet \n kazdy inny oznacza osoby bez rozrozniania na plec")
                x3 = input()
                if x3 == 'm':
                    tryb = 2
                elif x3 == 'k':
                    tryb = 3
                else:
                    tryb = 1
                try:
                    zad3(int(x1), tryb)
                except:
                    print("wpisana zla wartosc jako rok")
                x=0

            if x=="4":
                l=[]
                print("podaj wojewodztwo (male litery i bez polskich znakow)")
                x1 = input()
                x23=[]
                x23 = (''.join(x1))
                l.append(x23)


                for i in range (16):           #poprawic
                    print("aby dodac kolejne litera 'a' aby zakonczyc dodawanie 'b'")
                    x2=input()
                    x23=[]

                    if x2=="a":
                        print("podaj wojewodztwo (male litery i bez polskich znakow)")
                        x1 = input()
                        x23 = []
                        x23= (''.join(x1))
                        l.append(x23)

                    if x2=="b":
                        break

                print("dla jakiej grupy chcesz przeprowadziić zadanie?"
                      "\n dla znaku 'm' grupa mezczyzn"
                      "\n dla 'k' grupa kobiet \n kazdy inny oznacza osoby bez rozrozniania na plec")
                x3 = input()
                if x3 == 'm':
                    tryb = 2
                elif x3 == 'k':
                    tryb = 3
                else:
                    tryb = 1

                zad4(l, tryb)
                x=0

            if x=="5":
                print("podaj pierwsze wojewodztwo: (male litery i bez polskich znakow)")
                x1 = input()
                print("podaj drugie wojewodztwo: (male litery i bez polskich znakow)")
                x2 = input()
                print("dla jakiej grupy chcesz przeprowadziić zadanie?"
                      "\n dla znaku 'm' grupa mezczyzn"
                      "\n dla 'k' grupa kobiet \n kazdy inny oznacza osoby bez rozrozniania na plec")
                x3 = input()
                if x3 == 'm':
                    tryb = 2
                elif x3 == 'k':
                    tryb = 3
                else:
                    tryb = 1

                zad5(x1,x2, tryb)
                x=0
            if x=="z":
                break






#zad1("opolskie",2011,2013,3)
# zad2("kujawsko-pomorskie",1)
# zad3(2010, 1)
# l = ["pomorskie", "opolskie"]
# zad4(l, 1)
# zad5("opolskie","pomorskie",3)
start()
