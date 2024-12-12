"""
Ce module permet de lire un fichier csv et d'en manipuler les valeurs
"""

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """
    read_data() prend en argument un nom de fichier 
    et retourne son contenu sous la forme d'une liste de
    n listes d'entiers si le fichier comporte n lignes.
    """
    l=[]
    with open(filename, 'r', encoding='utf8') as f:
        for line in f:
            l.append([int(x) for x in line.strip().split(';')])
    return l

def get_list_k(l, k):
    """
    get_list_k() prend en argument la liste de listes retournée par read_data()
     et un indice k et retourne la kième liste.
    """
    return l[k]

def get_first(l):
    """
    get_first() prend en argument une liste et retourne le premier élément de cette liste
    """
    return l[0]

def get_last(l):
    """
    get_last() prend en argument une liste et retourne le dernier élément de cette liste
    """
    return l[-1]

def get_max(l):
    """
    get_max() prend en argument une liste et retourne le maximum de cette liste
    """
    m = l[0]
    for i in l:
        m = max(m,i)
    return m

def get_min(l):
    """
    get_min() prend en argument une liste et retourne le minimum de cette liste 
    """
    m = l[0]
    for i in l:
        m = min(m,i)
    return m

def get_sum(l):
    """
    get_sum() prend en argument une liste et retourne la somme de cette liste.
    """
    s = 0
    for i in l:
        s+= i
    return s


#### Fonction principale


def main():
    """
    Fait appel aux fontions différentes
    """
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
