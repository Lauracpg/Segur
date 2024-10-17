from collections import Counter

frekuentziak_gazteleraz = ['e', 'a', 'o', 'l', 's', 'n', 'd', 'r', 'u', 'i', 't', 'c', 'p', 'm', 'y', 'q', 'b', 'h', 'g', 'f', 'v', 'j', 'ñ', 'z', 'x', 'k', 'w']

def frekuentziak_kontatu(mezua):
    letrak_soilik = ''.join(filter(str.isalpha, mezua.lower()))
    frekuentziak = Counter(letrak_soilik)
    letrak_totala = sum(frekuentziak.values())
    frekuentziak_portzentaia = {letra: (frekuentziak[letra] / letrak_totala) * 100 for letra in frekuentziak}
    return frekuentziak, frekuentziak_portzentaia

def mapaketa_egin(frekuentziak):
    letra_ordenatuak = [letra for letra, _ in frekuentziak.most_common()]
    ordezkapen_mapa = {letra_zifratua: letra_gazte for letra_zifratua, letra_gazte in zip(letra_ordenatuak, frekuentziak_gazteleraz)}
    return ordezkapen_mapa

def mezua_deszifratu(mezua, ordezkapen_mapa):
    mezua_deszifratuta = []
    for letra in mezua:
        if letra.lower() in ordezkapen_mapa:
            letra_deszifratua=ordezkapen_mapa[letra.lower()]
            mezua_deszifratuta.append(letra_deszifratua.upper() if letra.isupper() else letra_deszifratua)
        else:
            mezua_deszifratuta.append(letra)
    return ''.join(mezua_deszifratuta)

def main():
    mezu_zifratua = input("Mezua sartu: ")
    frekuentziak, frekuentziak_portzentaia = frekuentziak_kontatu(mezu_zifratua)

    print("\nFrekuentziak portzentaian mezu zifratuan: ")
    for letra, portzentaia in frekuentziak_portzentaia.items():
        print(f"{letra}: {portzentaia:.2f}%")

    ordezkapen_mapa = mapaketa_egin(frekuentziak)
    print("\nHasierako ordezkapenak: ")
    for letra_zifratua, letra_deszifratua in ordezkapen_mapa.items():
        print(f"{letra_zifratua} -> {letra_deszifratua}")

    hasierako_mezu_deszifratua = mezua_deszifratu(mezu_zifratua, ordezkapen_mapa)
    print("\nHasierako mezu deszifratua: ")
    print(hasierako_mezu_deszifratua)

    while True:
        letra_zifratua = input("\nZein letra aldatu nahi duzu?: ").lower()
        if letra_zifratua == '':
            break
        if letra_zifratua not in ordezkapen_mapa:
            print(f"'{letra_zifratua}' letra ez dago ordezkapen mapan.")
            continue

        letra_berria = input(f"Zein letragatik ordezkatu nahi duzu '{letra_zifratua}' letra?: ").lower()
        if letra_berria== '':
            break
        
        ordezkapen_mapa[letra_zifratua] = letra_berria

        mezu_desenkriptatuta = mezua_deszifratu(mezu_zifratua, ordezkapen_mapa)
        print("\nMezua eguneratuta:")
        print(mezu_desenkriptatuta)

    print("\nMezua guztiz deszifratuta:")
    print(mezu_desenkriptatuta)


if __name__=="__main__":
    main()

##2.ariketan bajar imagen carpeta porque ha cambiado algo 
