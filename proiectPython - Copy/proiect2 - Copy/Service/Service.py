from Domain.Complex import createComplexNr, getReal, getImag, toString, setReal, setImag
from math import sqrt


def addComplexNrToList(listaNrComplexe, real, imag):
    '''
    Creeaza numarul complex si il adauga in lista
    :param listaNrComplexe: lista in care se adauga numarul
    :param real: partea reala
    :param imag: partea imaginara
    :return: NONE
    '''
    numar = createComplexNr(real, imag)
    listaNrComplexe.append(numar)


def modifyComplexNrOnPos(listaNrComplexe, pos, newReal, newImag):
    '''
    Inlocuieste toate aperitiile unui numar complex cu alt numar complex
    :param listaNrComplexe: lista de numere complexe
    :param pos: pozitia, numar natural
    :param newReal: partea reala
    :param newImag: partea imaginara
    :return: NONE
    '''
    i = 0
    for nrComplex in listaNrComplexe:
        if int(i) == int(pos):
            setReal(nrComplex, newReal)
            setImag(nrComplex, newImag)
        i += int(1)


def multiplyComplexNr1Nr2(nr1, nr2):
    '''
    Calculeaza produsul a doua numere complexe
    :param nr1: numar complex
    :param nr2: numar complex
    :return: produsul celor doua numere
    '''
    real1 = getReal(nr1)  # a
    real2 = getReal(nr2)  # x
    imag1 = getImag(nr1)  # b
    imag2 = getImag(nr2)  # y
    real1 = real1 * real2 - imag1 * imag2
    imag1 = real1 * imag2 + imag1 * real2
    return createComplexNr(real1, imag1)


def getNrOnPos(listaNrComplexe, pos):
    '''
    :param listaNrComplexe: lista de numere complexe
    :param pos: pozitia din lista
    :return: numarul complex de pe pozitia data din lista
    '''
    return listaNrComplexe[int(pos)]


def getABS(numar):
    '''
    Calculeaza modulul unui numar complex
    :param numar: numar complex
    :return: modulul numarului complex
    '''
    prtReal = getReal(numar)
    prtImag = getImag(numar)
    return sqrt(prtReal * prtReal + prtImag * prtImag)


def insertComplexNr(listaNrComplexe, pos, numar):
    '''
    Insereaza un numar complex pe o pozitie data
    :param listaNrComplexe: lista de numere complexe
    :param pos: pozitia
    :param numar: numar complex
    :return: NONE
    '''
    i = int(0)
    listaNoua = []
    for nrComplex in listaNrComplexe:
        if int(i) == int(pos):
            listaNoua.append(numar)
        listaNoua.append(nrComplex)
        i += int(1)
    while len(listaNrComplexe) > 0:
        listaNrComplexe.pop()
    for nrComplex in listaNoua:
        listaNrComplexe.append(nrComplex)


def deleteComplexNrFromPos(listaNrComplexe, pos):
    '''
    Sterge un numar complex de pe o anumita pozitie
    :param listaNrComplexe: lista de numere complexe
    :param pos: pozitia din lista, numar natural
    :return: NONE
    '''
    i = int(0)
    listaNoua = []
    for nrComplex in listaNrComplexe:
        if int(i) != int(pos):
            listaNoua.append(nrComplex)
        i += int(1)
    while len(listaNrComplexe) > 0:
        listaNrComplexe.pop()
    for nrComplex in listaNoua:
        listaNrComplexe.append(nrComplex)


def deleteIntervalOfComplexNr(listaNrComplexe, lower, upper):
    '''
    Sterge un interval de numere complexe
    :param listaNrComplexe: lista de numere complexe
    :param lower: primul capat de interval
    :param upper: al doilea capat de interval
    :return: NONE
    '''
    i = int(0)
    listaNoua = []
    for nrComplex in listaNrComplexe:
        if int(i) < int(lower) or int(i) > int(upper):
            listaNoua.append(nrComplex)
        i += int(1)
    while len(listaNrComplexe) > 0:
        listaNrComplexe.pop()
    for nrComplex in listaNoua:
        listaNrComplexe.append(nrComplex)


def replaceComplexNr(listaNrComplexe, replaced, replacer):
    '''
    Inlocuieste toate aparitiile unui numar complex cu alt numar complex
    :param listaNrComplexe: lista de numere complexe
    :param replaced: numarul de inlocuit
    :param replacer: numarul nou
    :return:NONE
    '''
    listaNoua = []
    for nrComplex in listaNrComplexe:
        if getReal(nrComplex) == getReal(replaced) and getImag(nrComplex) == getImag(replaced):
            listaNoua.append(replacer)
        else:
            listaNoua.append(nrComplex)
    while len(listaNrComplexe) > 0:
        listaNrComplexe.pop()
    for nrComplex in listaNoua:
        listaNrComplexe.append(nrComplex)


def printImagPartOfNrsFromSec(listaNrComplexe, lower, upper):
    '''
    Afiseaza partea imaginara a unor numere complexe dintr-un interval
    :param listaNrComplexe: lista de numere complexe
    :param lower: primul capat de interval
    :param upper: al doilea capat de interval
    :return: NONE
    '''
    #lista
    lista=[]
    i = int(0)
    for nrComplex in listaNrComplexe:
        if int(i) >= int(lower) and int(i) <= int(upper):
            lista.append(nrComplex)
        i += int(1)
    return lista

def printComplexNrsWithAbsLowerThanTen(listaNrComplexe):
    '''
    Afiseaza lista de numere complexe a carei numere complexe au modulul mai mic decat 10
    :param listaNrComplexe: lista de numere complexe
    :return: NONE
    '''
    #lista
    lista=[]
    for nrComplex in listaNrComplexe:
        if getABS(nrComplex) < 10:
            lista.append(nrComplex)
    return lista

def printComplexNrsWithAbsEqualToTen(listaNrComplexe):
    '''
    Afiseaza lista de numere complexe a carei numere complexe au modulul egal cu 10
    :param listaNrComplexe: lista de numere complexe
    :return: NONE
    '''
    lista=[]
    for nrComplex in listaNrComplexe:
        if getABS(nrComplex) == 10:
            lista.append(nrComplex)
    return lista

def printSumSubsequence(listaNrComplexe, lower, upper):
    '''
    Afiseaza suma numerelor complexe dintr-un interval dat
    :param listaNrComplexe: lista de numere complexe
    :param lower: primul capat de interval
    :param upper: al doilea capat de interval
    :return: NONE
    '''
    i = int(0)
    suma_real = int(0)
    suma_imag = int(0)
    for nrComplex in listaNrComplexe:
        if i >= int(lower) and i <= int(upper):
            suma_real = suma_real+getReal(nrComplex)
            suma_imag = suma_imag+getImag(nrComplex)
        i = i + int(1)
    numar = createComplexNr(suma_real, suma_imag)
    #UI rezultat=
    return toString(numar)

def printProdSubsequence(listaNrComplexe, lower, upper):
    '''
    Afiseaza produsul numerelor dintr-un interval dat
    :param listaNrComplexe: lista de numere complexe
    :param lower: primul capat de interval
    :param upper: al doilea capat de interval
    :return: NONE
    '''
    i = int(0)
    prod = createComplexNr(0, 0)
    init = False
    for nrComplex in listaNrComplexe:
        if init is False:
            setReal(prod, getReal(nrComplex))
            setImag(prod, getImag(nrComplex))
            init = True
        if i >= int(lower) and i <= int(upper):
            prod = multiplyComplexNr1Nr2(prod, nrComplex)
        i = i + int(1)
    print(toString(prod))

def printSortedArray(listaNrComplexe):
    '''
    Afiseaza lista sortata descrescator
    :param listaNrComplexe: lista de numere complexe
    :return: NONE
    '''
    lista=[]
    for i in range(0, len(listaNrComplexe) - 1):
        for j in range(i, len(listaNrComplexe)):
            if int(getImag(listaNrComplexe[i])) < int(getImag(listaNrComplexe[j])):
                aux = listaNrComplexe[i]
                listaNrComplexe[i] = listaNrComplexe[j]
                listaNrComplexe[j] = aux
    #lista
    for nrComplex in listaNrComplexe:
        lista.append(toString(nrComplex))
    return lista


def verifNrPrim(x):
    '''
    Verifica daca un numar este prim
    :param x: numar intreg
    :return: True daca e prim si False daca nu este prim
    '''
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0 or x < 2:
        return False
    for i in range(5, int(sqrt(x)), 6):
        if x % (i+2) == 0 or x % i == 0:
            return False
    return True


def popNrPrim(listaNrComplexe):
    '''
    Sterge din lista numerele complexe a caror parte reala este numar prim
    :param listaNrComplexe: lista de numere complexe
    :return: None
    '''
    listaNoua = []
    i = int(0)
    while(i < len(listaNrComplexe)):
        if verifNrPrim(getReal(listaNrComplexe[i])) is False:
            listaNoua.append(listaNrComplexe[i])
        i = i + 1
    while len(listaNrComplexe) > 0:
        listaNrComplexe.pop()
    for nrComplex in listaNoua:
        listaNrComplexe.append(nrComplex)
    return listaNrComplexe


def filtrareModul(listaNrComplexe, nrDat, semn):
    '''
    Elimina din lista numerele complexe la care modulul este <, = sau > decat un numar dat
    :param listaNrComplexe: lista de numere complexe
    :param nrDat: numar complex
    :param semn: string
    :return:NONE
    '''
    listaNoua = []
    if semn == "=":
        i = int(0)
        while i < len(listaNrComplexe):
            if getABS(listaNrComplexe[i]) == nrDat:
                listaNrComplexe.remove(listaNrComplexe[i])
            i = i + int(1)
    if semn == "<":
        i = int(0)
        while i < len(listaNrComplexe):
            if getABS(listaNrComplexe[i]) < nrDat:
                listaNrComplexe.remove(listaNrComplexe[i])
            i = i + int(1)
    if semn == ">":
        i = int(0)
        while i < len(listaNrComplexe):
            if getABS(listaNrComplexe[i]) > nrDat:
                listaNrComplexe.remove(listaNrComplexe[i])
            i = i + int(1)
