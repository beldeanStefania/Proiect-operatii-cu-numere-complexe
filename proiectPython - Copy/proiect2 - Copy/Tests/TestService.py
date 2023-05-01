from Domain.Complex import createComplexNr, getReal, getImag
from Service.Service import addComplexNrToList, modifyComplexNrOnPos, getNrOnPos, getABS, insertComplexNr, \
    deleteComplexNrFromPos, deleteIntervalOfComplexNr, replaceComplexNr, popNrPrim


def testService():
    listaNrComplexe = []
    nrTest = createComplexNr(6, 8)
    assert len(listaNrComplexe) == 0

    listaNrComplexe.append(nrTest)
    assert len(listaNrComplexe) == 1

    listaNrComplexe.append(nrTest)
    assert len(listaNrComplexe) == 2

    addComplexNrToList(listaNrComplexe, 10, -5)
    assert len(listaNrComplexe) == 3

    modifyComplexNrOnPos(listaNrComplexe, 2, 6, 8)
    assert getReal(getNrOnPos(listaNrComplexe, 2)) == 6
    assert getImag(getNrOnPos(listaNrComplexe, 2)) == 8
    assert getNrOnPos(listaNrComplexe, 0) == nrTest

    assert getABS(getNrOnPos(listaNrComplexe, 2)) == 10

    insertComplexNr(listaNrComplexe, 1, createComplexNr(1337, 7331))
    assert getReal(getNrOnPos(listaNrComplexe, 1)) == 1337
    assert getImag(getNrOnPos(listaNrComplexe, 1)) == 7331
    assert len(listaNrComplexe) == 4

    deleteComplexNrFromPos(listaNrComplexe, 1)
    assert getReal(getNrOnPos(listaNrComplexe, 1)) != 1337
    assert getImag(getNrOnPos(listaNrComplexe, 1)) != 7331
    assert len(listaNrComplexe) == 3

    deleteIntervalOfComplexNr(listaNrComplexe, 0, 2)
    assert len(listaNrComplexe) == 0

    listaNrComplexe.append(nrTest)
    listaNrComplexe.append(nrTest)
    listaNrComplexe.append(nrTest)
    assert len(listaNrComplexe) == 3

    replaceComplexNr(listaNrComplexe, nrTest, createComplexNr(1337, 7331))
    assert len(listaNrComplexe) == 3
    assert getReal(getNrOnPos(listaNrComplexe, 0)) == 1337
    assert getImag(getNrOnPos(listaNrComplexe, 0)) == 7331
    assert getReal(getNrOnPos(listaNrComplexe, 1)) == 1337
    assert getImag(getNrOnPos(listaNrComplexe, 1)) == 7331
    assert getReal(getNrOnPos(listaNrComplexe, 2)) == 1337
    assert getImag(getNrOnPos(listaNrComplexe, 2)) == 7331

    popNrPrim(listaNrComplexe)
    assert len(listaNrComplexe) == 3
    assert getReal(getNrOnPos(listaNrComplexe, 0)) == 1337
    assert getImag(getNrOnPos(listaNrComplexe, 0)) == 7331
    assert getReal(getNrOnPos(listaNrComplexe, 1)) == 1337
    assert getImag(getNrOnPos(listaNrComplexe, 1)) == 7331
    assert getReal(getNrOnPos(listaNrComplexe, 2)) == 1337
    assert getImag(getNrOnPos(listaNrComplexe, 2)) == 7331
