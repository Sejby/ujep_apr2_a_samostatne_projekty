""" 
seznam = [1,4,3,2,8,1,7,5,10]

def vyhledej(seznam, prvek: int):
    for idx in range(len(seznam)):
        if seznam[idx] == prvek:
            return f"Prvek je v seznamu! Jeho index je: {idx}"


print(vyhledej(seznam=seznam, prvek=4))
 """

k = [1,4,3,2,9,1,8,7,4,3,5]
prvek = 3

# binární vyhledávání / moje verze
""" def vyhledej_v_serazenem_seznamu(k, prvek):
    k.sort()
    print(k)
    while True:
        prostredek = len(k) // 2
        if prvek < k[prostredek]:
            for j in range(0, prostredek):
                k[prostredek] //= 2
                if k[j] == prvek:
                    return f"Hledaný prvek je na pozici {k[j]}"
                if k[j] > prvek:
                    continue
                if k[j] < prvek:
                    continue
        
        elif prvek > k[prostredek]:
            for j in range(0, prostredek):
                k[prostredek] //= 2
                if k[j] == prvek:
                    return f"Hledaný prvek je na pozici {k[j]}"
                if k[j] > prvek:
                    continue
                if k[j] < prvek:
                    continue
        
        elif prvek == k[prostredek]:
            return f"Hledaný prvek je na pozici {k[prostredek]}"

print(vyhledej_v_serazenem_seznamu(k=k, prvek=prvek)) """

""" # správně binární vyhledávání / beránkovo verze
def binarni_vyhledavani(serazeny_seznam, prvek):
    i = len(serazeny_seznam) // 2
    while serazeny_seznam[i] != prvek:
        if serazeny_seznam[i] < prvek:
            serazeny_seznam = serazeny_seznam[i+1:]
        else:
            serazeny_seznam = serazeny_seznam[:i]
        i = len(serazeny_seznam)//2
    return i #chybně vrací jedničku / ideálně opravit

seznam = [1,4,3,2,9,1,8,7,4,3,5]
print(sorted(seznam))
print(binarni_vyhledavani(sorted(seznam), 3)) """

""" # vyhledání k-extrémů
seznam = [1,4,3,2,9,1,8,7,4,3,5]
def najdi_extremy(seznam, k):
    extremy = seznam[:k]
    min_extrem = min(extremy)
    index_min_extrem = extremy.index(min_extrem)
    for i in range(k, len(seznam)):
        if seznam[i] > min_extrem:
            extremy[index_min_extrem] = seznam[i]
            min_extrem = min(extremy)
            index_min_extrem = extremy.index(min_extrem)
    return extremy    

print(najdi_extremy(seznam, k=3))

# vyhledání globálního extrému
def globalni_maximum(seznam):
    index_maxima = 0
    maximum = seznam[index_maxima]
    for i in range(1, len(seznam)):
        if seznam[i] > maximum:
            index_maxima = i
            maximum = seznam[index_maxima]
    return index_maxima

seznam = [1,4,3,2,9,1,8,7,4,3,5]
print(globalni_maximum(seznam))

# sumační formule
def nalezni_chybejici_sumaci(seznam):
    n = len(seznam)+1
    suma = n*(n+1)/2
    akumulator = 0
    for i in range(n-1):
        akumulator += seznam[i]
    return suma - akumulator

seznam = [1, 3, 5, 2] #chybí 3, n = 4
print(nalezni_chybejici_sumaci(seznam))
4.0
seznam = [1, 3, 5, 2] #chybí 3, n = 4
n = len(seznam) + 1

print(n*(n+1)/2 - sum(seznam)) """
""" 
seznam = [1,1,2,2,2,3,4,4,4,5]
k = 3

def opakujici_se(seznam, k):
    seznam.sort()
    pocet_opakovani = 1
    hledane_prvky = []
    fixed = seznam[0]
    for i in range(1, len(seznam)):
        if fixed == seznam[i]:
            pocet_opakovani += 1
        else:
            if pocet_opakovani > k:
                hledane_prvky.append(fixed)
                fixed = seznam[i]
                break 
                  
    return f"Hledané prvky jsou {hledane_prvky}"
            
    
print(opakujici_se(seznam=seznam, k=k)) """

# Naleznete v řetězci podřetězec
retezec = "ABBABABBADADAADADA"
podretezec = "ABBA"

def nalezni_podretezec(retezec, podretezec):
    delka = len(retezec) - len(podretezec)
    hledane_hodnoty = []
    for i in range(0, delka):
        for j in range(0, len(podretezec)):
            if retezec[i+1] == podretezec[j]:
                hledane_hodnoty.append(retezec[i])
            else:
                continue

    print("".join(hledane_hodnoty))
    if "".join(hledane_hodnoty) == podretezec:
        return f"Ano je tam!"
    else:
        return "Joke"
    
    
    
print (nalezni_podretezec(retezec=retezec, podretezec=podretezec))