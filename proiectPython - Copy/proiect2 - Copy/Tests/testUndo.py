from Domain.Complex import createComplexNr, getReal, getImag
from Service.Service import addComplexNrToList, modifyComplexNrOnPos, getNrOnPos, getABS, insertComplexNr, \
    deleteComplexNrFromPos, deleteIntervalOfComplexNr, replaceComplexNr, popNrPrim


def testUndo():
    undoList = []
    listaNrComplexe = []

    nrTest = createComplexNr(6, 8)
    assert len(listaNrComplexe) == 0

    undoList.append([i for i in listaNrComplexe])
    listaNrComplexe.append(nrTest)
    assert len(listaNrComplexe) == 1

    undoList.append([i for i in listaNrComplexe])
    listaNrComplexe.append(nrTest)
    assert len(listaNrComplexe) == 2

    undoList.append([i for i in listaNrComplexe])
    addComplexNrToList(listaNrComplexe, 10, -5)
    assert len(listaNrComplexe) == 3

    assert len(undoList) == 3

    listaNrComplexe = undoList.pop()
    assert len(undoList) == 2

    listaNrComplexe = undoList.pop()
    assert len(undoList) == 1

    listaNrComplexe = undoList.pop()
    assert len(undoList) == 0

    undoList.append([i for i in listaNrComplexe])
    listaNrComplexe.append(nrTest)
    undoList.append([i for i in listaNrComplexe])
    listaNrComplexe.append(nrTest)
    undoList.append([i for i in listaNrComplexe])
    addComplexNrToList(listaNrComplexe, 10, -5)
    assert len(undoList) == 3
    assert len(listaNrComplexe) == 3

    undoList.append([createComplexNr(getReal(i), getImag(i)) for i in listaNrComplexe])
    assert len(undoList) == 4
    assert len(listaNrComplexe) == 3
    modifyComplexNrOnPos(listaNrComplexe, 2, 6, 8)
    assert getReal(getNrOnPos(listaNrComplexe, 2)) == 6
    assert getImag(getNrOnPos(listaNrComplexe, 2)) == 8
    assert getNrOnPos(listaNrComplexe, 0) == nrTest

    listaNrComplexe = undoList.pop()
    assert getReal(getNrOnPos(listaNrComplexe, 2)) == 10
    assert getImag(getNrOnPos(listaNrComplexe, 2)) == -5
    assert len(undoList) == 3
    assert len(listaNrComplexe) == 3

    undoList.append([createComplexNr(getReal(i), getImag(i)) for i in listaNrComplexe])
    modifyComplexNrOnPos(listaNrComplexe, 2, 6, 8)
    assert getReal(getNrOnPos(listaNrComplexe, 2)) == 6
    assert getImag(getNrOnPos(listaNrComplexe, 2)) == 8
    assert getNrOnPos(listaNrComplexe, 0) == nrTest
    assert len(undoList) == 4
    assert len(listaNrComplexe) == 3

    modifyComplexNrOnPos(listaNrComplexe, 2, 6, 8)
    assert getReal(getNrOnPos(listaNrComplexe, 2)) == 6
    assert getImag(getNrOnPos(listaNrComplexe, 2)) == 8
    assert getNrOnPos(listaNrComplexe, 0) == nrTest

    assert getABS(getNrOnPos(listaNrComplexe, 2)) == 10

    undoList.append([i for i in listaNrComplexe])
    insertComplexNr(listaNrComplexe, 1, createComplexNr(1337, 7331))
    assert len(undoList) == 5
    assert getReal(getNrOnPos(listaNrComplexe, 1)) == 1337
    assert getImag(getNrOnPos(listaNrComplexe, 1)) == 7331
    assert len(listaNrComplexe) == 4

    listaNrComplexe = undoList.pop()
    assert len(listaNrComplexe) == 3
    assert len(undoList) == 4
    assert getReal(getNrOnPos(listaNrComplexe, 1)) == 6
    assert getImag(getNrOnPos(listaNrComplexe, 1)) == 8

    undoList.append([i for i in listaNrComplexe])
    insertComplexNr(listaNrComplexe, 1, createComplexNr(1337, 7331))
    assert len(undoList) == 5
    assert getReal(getNrOnPos(listaNrComplexe, 1)) == 1337
    assert getImag(getNrOnPos(listaNrComplexe, 1)) == 7331
    assert len(listaNrComplexe) == 4

    undoList.append([i for i in listaNrComplexe])
    assert len(undoList) == 6
    deleteComplexNrFromPos(listaNrComplexe, 1)
    assert getReal(getNrOnPos(listaNrComplexe, 1)) != 1337
    assert getImag(getNrOnPos(listaNrComplexe, 1)) != 7331
    assert len(listaNrComplexe) == 3

    listaNrComplexe = undoList.pop()
    assert len(undoList) == 5
    assert len(listaNrComplexe) == 4
    assert getReal(getNrOnPos(listaNrComplexe, 1)) == 1337
    assert getImag(getNrOnPos(listaNrComplexe, 1)) == 7331

    undoList.append([i for i in listaNrComplexe])
    assert len(undoList) == 6
    deleteComplexNrFromPos(listaNrComplexe, 1)
    assert getReal(getNrOnPos(listaNrComplexe, 1)) != 1337
    assert getImag(getNrOnPos(listaNrComplexe, 1)) != 7331
    assert len(listaNrComplexe) == 3

    undoList.append([i for i in listaNrComplexe])
    assert len(undoList) == 7
    deleteIntervalOfComplexNr(listaNrComplexe, 0, 2)
    assert len(listaNrComplexe) == 0

    listaNrComplexe = undoList.pop()
    assert len(undoList) == 6
    assert len(listaNrComplexe) == 3

    undoList.append([i for i in listaNrComplexe])
    assert len(undoList) == 7
    deleteIntervalOfComplexNr(listaNrComplexe, 0, 2)
    assert len(listaNrComplexe) == 0

    undoList.append([i for i in listaNrComplexe])
    listaNrComplexe.append(nrTest)
    undoList.append([i for i in listaNrComplexe])
    listaNrComplexe.append(nrTest)
    undoList.append([i for i in listaNrComplexe])
    listaNrComplexe.append(nrTest)
    assert len(listaNrComplexe) == 3
    assert len(undoList) == 10

    undoList.append([i for i in listaNrComplexe])
    replaceComplexNr(listaNrComplexe, nrTest, createComplexNr(1337, 7331))
    assert len(listaNrComplexe) == 3
    assert getReal(getNrOnPos(listaNrComplexe, 0)) == 1337
    assert getImag(getNrOnPos(listaNrComplexe, 0)) == 7331
    assert getReal(getNrOnPos(listaNrComplexe, 1)) == 1337
    assert getImag(getNrOnPos(listaNrComplexe, 1)) == 7331
    assert getReal(getNrOnPos(listaNrComplexe, 2)) == 1337
    assert getImag(getNrOnPos(listaNrComplexe, 2)) == 7331
    assert len(undoList) == 11

    listaNrComplexe = undoList.pop()
    assert len(listaNrComplexe) == 3
    assert getReal(getNrOnPos(listaNrComplexe, 0)) == 6
    assert getImag(getNrOnPos(listaNrComplexe, 0)) == 8
    assert getReal(getNrOnPos(listaNrComplexe, 1)) == 6
    assert getImag(getNrOnPos(listaNrComplexe, 1)) == 8
    assert getReal(getNrOnPos(listaNrComplexe, 2)) == 6
    assert getImag(getNrOnPos(listaNrComplexe, 2)) == 8
    assert len(undoList) == 10

    undoList.append([i for i in listaNrComplexe])
    replaceComplexNr(listaNrComplexe, nrTest, createComplexNr(1337, 7331))
    assert len(listaNrComplexe) == 3
    assert getReal(getNrOnPos(listaNrComplexe, 0)) == 1337
    assert getImag(getNrOnPos(listaNrComplexe, 0)) == 7331
    assert getReal(getNrOnPos(listaNrComplexe, 1)) == 1337
    assert getImag(getNrOnPos(listaNrComplexe, 1)) == 7331
    assert getReal(getNrOnPos(listaNrComplexe, 2)) == 1337
    assert getImag(getNrOnPos(listaNrComplexe, 2)) == 7331
    assert len(undoList) == 11

    undoList.append([i for i in listaNrComplexe])
    popNrPrim(listaNrComplexe)
    assert len(listaNrComplexe) == 3
    assert getReal(getNrOnPos(listaNrComplexe, 0)) == 1337
    assert getImag(getNrOnPos(listaNrComplexe, 0)) == 7331
    assert getReal(getNrOnPos(listaNrComplexe, 1)) == 1337
    assert getImag(getNrOnPos(listaNrComplexe, 1)) == 7331
    assert getReal(getNrOnPos(listaNrComplexe, 2)) == 1337
    assert getImag(getNrOnPos(listaNrComplexe, 2)) == 7331
    assert len(undoList) == 12

    listaNrComplexe = undoList.pop()
    assert len(listaNrComplexe) == 3
    assert getReal(getNrOnPos(listaNrComplexe, 0)) == 1337
    assert getImag(getNrOnPos(listaNrComplexe, 0)) == 7331
    assert getReal(getNrOnPos(listaNrComplexe, 1)) == 1337
    assert getImag(getNrOnPos(listaNrComplexe, 1)) == 7331
    assert getReal(getNrOnPos(listaNrComplexe, 2)) == 1337
    assert getImag(getNrOnPos(listaNrComplexe, 2)) == 7331
    assert len(undoList) == 11

    undoList.append([i for i in listaNrComplexe])
    popNrPrim(listaNrComplexe)
    assert len(listaNrComplexe) == 3
    assert getReal(getNrOnPos(listaNrComplexe, 0)) == 1337
    assert getImag(getNrOnPos(listaNrComplexe, 0)) == 7331
    assert getReal(getNrOnPos(listaNrComplexe, 1)) == 1337
    assert getImag(getNrOnPos(listaNrComplexe, 1)) == 7331
    assert getReal(getNrOnPos(listaNrComplexe, 2)) == 1337
    assert getImag(getNrOnPos(listaNrComplexe, 2)) == 7331
    assert len(undoList) == 12

    listaNrComplexe = undoList.pop()
    listaNrComplexe = undoList.pop()
    listaNrComplexe = undoList.pop()
    listaNrComplexe = undoList.pop()
    listaNrComplexe = undoList.pop()
    listaNrComplexe = undoList.pop()
    listaNrComplexe = undoList.pop()
    listaNrComplexe = undoList.pop()
    listaNrComplexe = undoList.pop()
    listaNrComplexe = undoList.pop()
    listaNrComplexe = undoList.pop()
    listaNrComplexe = undoList.pop()
    assert len(undoList) == 0
    assert len(listaNrComplexe) == 0
