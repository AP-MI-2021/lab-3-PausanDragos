# Problema 3 : Numerele au semne alternante.
def afisare_get_longest_alternating_signs(lst: list[int], inceput, lungime):
    for i in range(inceput, inceput+lungime):
        print(lst[i], " ", end='')
    print("")


def semn(n):
    if n < 0:
        return -1
    return 1


def get_longest_alternating_signs(lst: list[int]):
    """
    Daca lista este goala rezultatul va fi tot o lista goala
    In caz contrar vom parcurge lista pe care o avem de la primul element pana la penultimul si vom verifica daca
    oricare doua elemente consecutive au semn diferit ajutandu-ne de funcita semn() care returneaza valoarea 1 daca
    numarul este >=0, iar in caz contrar returneaza -1
    Cat timp avem numere de semn contrar vom mari valoarea variabilei nr (variabila care retine lungimea subsecventei
    cu proprietatea dorita)
    Cand doua numere consecutive au acelasi semn sau ajungem la capatul listei vom compara variabila nr cu nrmax
    (variabila care mentine lungimea celei mai lungi subsecvente cu proprietatea ceruta), iar daca aceasta este mai mare
    decat nrmax atunci nrmax va lua valoarea lui nr, iar pozitia primului element al noii subsecventa va fi retinut in
    variabila pos
    Dupa aceea se copiaza elementele din cea mai lunga subsecventa cu proprietatea ceruta in lista lstcorect, iar apoi
    aceasta lista este returnata
    :param lst: Lista cu care dorim sa lucram
    :return: Lista formata din cea mai lunga subsecventa care are proprietatea ceruta
    """
    if not lst:
        return lst
    lstcorect = []
    nr = 1
    pos = 0
    nrmax = 1
    for i in range(len(lst)-1):
        if semn(lst[i]) != semn(lst[i+1]):
            nr += 1
        else:
            if nr > nrmax:
                nrmax = nr
                pos = i - nr + 1
            nr = 1
    if nr > nrmax:
        nrmax = nr
        pos = len(lst) - nr
    afisare_get_longest_alternating_signs(lst, pos, nrmax)
    for i in range(pos, pos+nrmax):
        lstcorect.append(lst[i])
    return lstcorect


def test_get_longest_alternating_signs():
    assert get_longest_alternating_signs([3, -5, -7, 4, 0, -2]) == [3, -5]
    assert get_longest_alternating_signs([]) == []
    assert get_longest_alternating_signs([-4, -5]) == [-4]
    assert get_longest_alternating_signs([-4, 3, -4, 3, -5]) == [-4, 3, -4, 3, -5]


def nr_div(n):
    n = abs(n)
    nr = 0
    if n == 0:
        return -1
    if n == 1:
        return 2
    for i in range(1, n):
        if i * i > n:
            break
        if n % i == 0:
            nr += 1
            if n // i != i:
                nr += 1
    return nr * 2


def afisare_get_longest_same_div_count(lst, inceput, lungime):
    for i in range(inceput, lungime+inceput):
        print(lst[i], " ", end='')
    print("")


# Problema 12: Toate numerele același număr de divizori.
def get_longest_same_div_count(lst: list[int]):
    """
    Daca lista este goala rezultatul va fi tot o lista goala
    In caz contrar vom crea si vom parcurge o noua lista ver care va mentine pe pozitia i numarul de divizori ai
    elementului de pe pozitia i in lista lst (ne folosim de functia nrdiv() care ne da numarul de divizori ai unui
    numar, pentru a atribui in lista ver valorile corect)
    Cat timp avem aceeasi valoare pentur doua numere consecutive vom mari valoarea variabilei nr (variabila care retine
    lungimea subsecventei cu proprietatea dorita)
    Cand doua numere consecutive au valori diferite sau ajungem la capatul listei vom compara variabila nr cu nrmax
    (variabila care mentine lungimea celei mai lungi subsecvente cu proprietatea ceruta), iar daca aceasta este mai mare
    decat nrmax atunci nrmax va lua valoarea lui nr, iar pozitia primului element al noii subsecventa va fi retinut in
    variabila pos
    Dupa aceea se copiaza elementele din cea mai lunga subsecventa cu proprietatea ceruta in lista lstcorect, iar apoi
    aceasta lista este returnata
    :param lst: Lista cu care dorim sa lucram
    :return: Lista formata din cea mai lunga subsecventa care are proprietatea ceruta
    """
    if not lst:
        return lst
    lstcorect = []
    ver = []
    nr = 1
    nrmax = 1
    pos = 0
    for i in range(len(lst)):
        ver.append(nr_div(lst[i]))
    for i in range(len(ver)-1):
        if ver[i] == ver[i+1]:
            nr += 1
        else:
            if nr > nrmax:
                nrmax = nr
                pos = i - nr + 1
            nr = 1
    if nr > nrmax:
        nrmax = nr
        pos = len(ver) - nr
    afisare_get_longest_same_div_count(lst, pos, nrmax)
    for i in range(pos, pos+nrmax):
        lstcorect.append(lst[i])
    return lstcorect


def test_get_longest_same_div_count():
    assert get_longest_same_div_count([]) == []
    assert get_longest_same_div_count([2, 3, 5, 7, 10]) == [2, 3, 5, 7]
    assert get_longest_same_div_count([5, 4, 5, 4, 7, 11, 13]) == [7, 11, 13]


def printMenu():
    print('1. Problema 3')
    print('2. Problema 12')
    print('3. Exit')
    n = input('Alegeti optiunea: ')
    if n == '1':
        lst_string = input('Dati lista: ')
        lst = lst_string.split()
        for i in range(len(lst)):
            lst[i] = int(lst[i])
        print('Cea mai lunga subsecventa care contine numere de semne alternante este: ')
        get_longest_alternating_signs(lst)
    elif n == '2':
        lst_string = input('Dati lista: ')
        lst = lst_string.split()
        for i in range(len(lst)):
            lst[i] = int(lst[i])
        print('Cea mai lunga subsecventa care contine numere care au acelasi numar de divizori este: ')
        get_longest_same_div_count(lst)
    elif n == '3':
        exit(0)


def main():
    """
    test_get_longest_alternating_signs()
    test_get_longest_same_div_count()
    """
    while True:
        printMenu()


if __name__ == "__main__":
    main()
