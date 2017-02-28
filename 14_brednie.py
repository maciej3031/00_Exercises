def brednie():
    from random import seed,choice
    seed()
    tekst = ""
    t1 = ["Biało-czerwona drużyno,", "Należy jasno podkreślić, że", "Sytuacja dojrzała do tego by powiedzieć wprost", "Minione lata w sposób oczywisty wręcz dowiodły, że","Każdy kto interesuje się Polską wie, że",
          "Jak na dłoni widać, że", "Naszą głęboką troskę budzi fakt, że", "Z najwyższym zaniepokojeniem obserwujemy, iż", "Niestety", "Mamy niezbite dowody, że"]
    t2 = ["koła liberalne,", "wrogie nam ośrodki niemieckie,", "sprzedające się za sowite gratyfikacje środowiska aktorskie,", "resortowe dzieci,", "agentury obcych wywiadów,", "skompromitowane do szczętu autorytety,",
          "inspirowane z zewnątrz wiadome grupy interesów,", "gender,homopolityka i walka z chrześcijaństwem,", "tysiące post-Polaków,", "skompromitowane pokolonialne pseudoelity,",
          "komunistyczne zaplecze polskiej sceny politycznej,"]
    t3 = ["odpowiedzialne za fatalną gospodarkę leśną,", "które zrujnowaly kraj,", "z satysfakcją obserwujące upadek rodzimego górnictwa,", "szargające na deskach swoich pseudoteatrzyków wszystko, co cenne,",
          "sufitujące obce nam ideowo wzorce rodem ze zdemoralizowanego Zachodu,", "pasożytujące na gospodarce narodowej,", "wyprowadzające od lat kapitał za granicę,", "które żyją z podgryzania naszych ideowych korzeni,",
          "bezpardonowo niszczące polski rynek,", "które doprowadziły do ruiny polski przemysł stoczniowy,", "które specjalizują się w erozji ideowej,", "płodzące w zaciszu swoich gabinetów aksjologiczną breję,"]
    t4 = ["odpowiedzą za swoje zbrodnie przed Bogiem i polskim narodem.", "są wytworem porządku pojałtańskiego i mrocznych czasów rewanżyzmu.", "muszą zniknąć z powierzchni polskiego życia publicznego.",
          "odcięły się od życiodajnych źródeł tradycji, kultury i myśli narodowej.", "straciły mandat do wypowiadania się na istotne dla narodu polskiego tematy.", "mamiły nas wizjami zielonej wyspy.",
          "powielają porządek Targowicy i są ideowymi prawnukami carycy Katarzyny.", "muszą szukać swego miejsca gdzie indziej.", "pozostają póki co bezkarne.", "nie ustają w nagonce na tworzący się nowy ład.",
          "ulegają podszeptom wichrzycieli oraz kłamliwej propagandy ośrodków zagranicznych.", "pod płaszczem modernizacji planują dalsze akty destrukcji."]

    t1 = choice(t1)
    t2 = choice(t2)
    t3 = choice(t3)
    t4 = choice(t4)
    return t1 + " " + t2 + " " + t3 + " " + t4


print("Naciśnij enter, aby wylosować zdanie")
while 1:
    inp = input()
    a = brednie()
    print(a)



