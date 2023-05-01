from Domain.Complex import createComplexNr, getReal, getImag, toString
from Service.Service import  addComplexNrToList, insertComplexNr, deleteIntervalOfComplexNr, replaceComplexNr, \
    printImagPartOfNrsFromSec, printComplexNrsWithAbsLowerThanTen, printComplexNrsWithAbsEqualToTen, \
    modifyComplexNrOnPos, printSumSubsequence, printProdSubsequence, printSortedArray, popNrPrim, filtrareModul


def printMenu():
    print("0. Afiseaza lista de numere complexe")
    print("1. Adauga numar complex la sfarsitul listei")
    print("2. Modifica un numar complex de pe o pozitie data")
    print("3. Inserare numar complex pe o pozitie data")
    print("4. Stergere numere complexe dintr-un interval dat")
    print("5. Inlocuieste aparitiile unui element cu un alt numar complex")
    print("6. Afiseaza partea imaginara a numerelor dintr-un interval dat")
    print("7. Afiseaza numerele din lista care au modulul mai mic decat 10")
    print("8. Afiseaza numerele din lista care au modulul egal cu 10")
    print("9. Afiseaza suma numerelor din subsecventa data")
    print("10. Afiseaza produsul numerelor din subsecventa data")
    print("11. Afiseaza lista sortata descrescator dupa partea imaginara")
    print("12. Elimina din lista numerele complexe la care partrea reala este prim")
    print("13.Elimina din lista numerele complexe la care modulul este <,=,> decat un numar dat")
    print("u. Undo")
    print("x. Termina programul")
    print()


def runMenu():

    undoList = []
    listaNrComplexe = []

    while True:
        printMenu()
        option = input("Dati numarul optiunii: ")

        if option == "0":
            showAll(listaNrComplexe)

        elif option == "1":
            try:
                real = int(input("Dati partea reala: "))
                imag = int(input("Dati partea imaginara: "))
                undoList.append([i for i in listaNrComplexe])
                addComplexNrToList(listaNrComplexe, real, imag)
            except ValueError:
                print("Introduceti un numar real!")

        elif option == "2":
            try:
                real = int(input("Dati noua parte reala: "))
                imag = int(input("Dati noua parte imaginara: "))
                pos = input("Dati pozitia numarului pe care doriti sa il modificati: ")
                undoList.append([createComplexNr(getReal(i), getImag(i)) for i in listaNrComplexe])
                modifyComplexNrOnPos(listaNrComplexe, pos, real, imag)
            except ValueError as e:
                print(e)

        elif option == "3":
            try:
                real = int(input("Dati partea reala: "))
                imag = int(input("Dati partea imaginara: "))
                numar = createComplexNr(real, imag)
                pos = int(input("Dati pozitia pe care doriti sa fie inserat numarul: "))
                undoList.append([i for i in listaNrComplexe])
                insertComplexNr(listaNrComplexe, pos, numar)
            except ValueError as e:
                print(e)

        elif option == "4":
            try:
                lower = int(input("Dati capatul de jos al intervalului: "))
                upper = int(input("Dati capatul de sus al intervalului: "))
                undoList.append([i for i in listaNrComplexe])
                deleteIntervalOfComplexNr(listaNrComplexe, lower, upper)
            except ValueError as e:
                print(e)

        elif option == "5":
            try:
                realReplaced = int(input("Dati partea reala a numarului inlocuit: "))
                imagReplaced = int(input("Dati partea imaginara a numarului inlocuit: "))
                numarReplaced = createComplexNr(realReplaced, imagReplaced)
                realReplacer = input("Dati partea reala a noului numar: ")
                imagReplacer = input("Dati partea imaginara a noului numar: ")
                numarReplacer = createComplexNr(realReplacer, imagReplacer)
                undoList.append([i for i in listaNrComplexe])
                replaceComplexNr(listaNrComplexe, numarReplaced, numarReplacer)
            except ValueError as e:
                print(e)

        elif option == "6":
            try:
                lower = int(input("Dati capatul de jos al intervalului: "))
                upper = int(input("Dati capatul de sus al intervalului: "))
                rezultat=printImagPartOfNrsFromSec(listaNrComplexe, lower, upper)
                for numar in rezultat:
                    print(getImag(numar))
                #print(rezultat)
            except ValueError as e:
                print(e)

        elif option == "7":
            try:
                print("Numerele complexe care au modulul mai mic decat 10 sunt:")
                rezultat = printComplexNrsWithAbsLowerThanTen(listaNrComplexe)
                if rezultat==0:
                    print("Nu exista nr complexe care sa iaba modulul egal cu 10")
                else:
                    print(rezultat)
            except ValueError as e:
                print(e)

        elif option == "8":
            try:
                print("Numerele complexe care au modulul egal cu 10 sunt:")
                rezultat=printComplexNrsWithAbsEqualToTen(listaNrComplexe)
                if rezultat==0:
                    print("Nu exista nr complexe care sa aiba modulul egal cu 10")
                else:
                    print(rezultat)
            except ValueError as e:
                print(e)

        elif option == "9":
            try:
                lower = int(input("Dati capatul de jos al intervalului: "))
                upper = int(input("Dati capatul de sus al intervalului: "))
                rezultat=printSumSubsequence(listaNrComplexe, lower, upper)
                print(rezultat)
            except ValueError as e:
                print(e)

        elif option == "10":
            try:
                lower = int(input("Dati capatul de jos al intervalului: "))
                upper = int(input("Dati capatul de sus al intervalului: "))
                printProdSubsequence(listaNrComplexe, lower, upper)
            except ValueError as e:
                print(e)

        elif option == "11":
            undoList.append([i for i in listaNrComplexe])
            rezultat=printSortedArray(listaNrComplexe)
            print(rezultat)


        elif option == "12":
            undoList.append([i for i in listaNrComplexe])
            popNrPrim(listaNrComplexe)

        elif option == "13":
            try:
                nr_dat = int(input("Dati numarul: "))
                semn = input("Scrieti semnul: ")
                undoList.append([i for i in listaNrComplexe])
                filtrareModul(listaNrComplexe, nr_dat, semn)
            except ValueError as e:
                print(e)

        elif option == "u":
            if len(undoList) > 0:
                listaNrComplexe = undoList.pop()
                print("Operatia Undo s-a executat cu succes!")
            else:
                print("Nu se poate executa operatia de undo!")

        elif option == "x":
            break

        else:
            print("Ati ales o optiune gresita!")
        print()

def showAll(listaNrComplexe):
    '''
    Afiseaza lista de numere complexe
    :param listaNrComplexe: lista de numere complexe
    :return: NONE
    '''
    for nrComplex in listaNrComplexe:
        print(toString(nrComplex))