from Domain.Complex import createComplexNr, getReal, getImag, setReal, setImag, toString


def testDomain():
    nrTest = createComplexNr(6, 8)
    assert getReal(nrTest) == 6
    assert getImag(nrTest) == 8

    setReal(nrTest, 7331)
    assert getReal(nrTest) == 7331

    setImag(nrTest, 1337)
    assert getImag(nrTest) == 1337

    assert toString(nrTest) == "7331 + 1337i"

    nrTest2 = createComplexNr(25, 11)
    assert getReal(nrTest2) == 25
    assert getImag(nrTest2) == 11

    setReal(nrTest2, 0)
    assert getReal(nrTest2) == 0

    setImag(nrTest2, 525)
    assert getImag(nrTest2) == 525

    assert toString(nrTest2) == "525i"
