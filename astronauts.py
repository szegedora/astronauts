honapok = []


def kiolvasas():
    with open('astronauts.csv', 'r', encoding='utf-8') as forrasfajl:
        forrasfajl.readline()
        for sor in forrasfajl:
            adatok = sor.strip().split(',')
            szulinap = adatok[-1].split('/')
            honap = szulinap[0]
            honapok.append(honap)


def szamolas():
    db = []
    osszeg = 0
    for number in range(1, 13):
        db.append([honapok.count(str(number)), number])
        osszeg += honapok.count(str(number))
    db.sort()
    db.reverse()
    return db, osszeg


def kiiratas(db, osszeg):
    for index in range(3):
        szazalek = db[index][0] / osszeg * 100
        print(f'A {db[index][1]}. hónap a {index + 1}. leggyakoribb hónap az űrhajósoknál. {round(szazalek, 2)}%')


def main():
    kiolvasas()
    db, osszeg = szamolas()
    kiiratas(db, osszeg)


main()
