import math as m


s = "9191906840-9191941337,7671-13230,2669677096-2669816099,2-12,229599-392092,48403409-48523311,96763-229430,1919163519-1919240770,74928-96389,638049-668065,34781-73835,736781-819688,831765539-831907263,5615884-5749554,14101091-14196519,7134383-7169141,413340-625418,849755289-849920418,7745350-7815119,16717-26267,4396832-4549887,87161544-87241541,4747436629-4747494891,335-549,867623-929630,53-77,1414-3089,940604-1043283,3444659-3500714,3629-7368,79-129,5488908-5597446,97922755-98097602,182-281,8336644992-8336729448,24-47,613-1077"

# s = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

rs = list(map(lambda r: (int(r.split('-')[0]), int(r.split('-')[1])), s.split(',')))


antifa = [[], [], [1], [1], [1, 2], [1], [1, 2, 3], [1], [1, 2, 4], [1, 3], [1, 2, 5]]

def spracuj_r(od, do):
    od_dlzka = len(str(od))
    do_dlzka = len(str(do))
    if od_dlzka != do_dlzka:
        return spracuj_r(od, 10 ** od_dlzka - 1) + spracuj_r(10 ** od_dlzka, do)

    dlzka = od_dlzka

    antifa_pocitadlo = [1 for _ in range(dlzka)]

    sucet = 0
    for r in range(dlzka - 1, 0, -1):
    # for r in ([dlzka // 2] if dlzka % 2 == 0 else []):
        if dlzka % r != 0:
            continue

        for i in antifa[r]:
            antifa_pocitadlo[i] -= 1

        r_pocet = dlzka // r
        krok = 10 ** r
        krok = sum(krok ** rr for rr in range(0,r_pocet))
        zaciatok = m.ceil(od / krok)
        koniec = m.floor(do / krok)
        pocet = koniec - zaciatok + 1
        # print(zaciatok, koniec, pocet, krok)
        sucet += antifa_pocitadlo[r] * (pocet * zaciatok * krok + pocet * (pocet - 1) * krok // 2)

    return sucet


x = sum(spracuj_r(od, do) for (od, do) in rs)

21139440284
17763127244
        
print(x)
