def createComplexNr(real, imag):
    return {
        "parteReala": real,
        "parteImag": imag
    }


def getReal(numar):
    return numar["parteReala"]


def getImag(numar):
    return numar["parteImag"]


def setReal(numar, real):
    numar["parteReala"] = real


def setImag(numar, imag):
    numar["parteImag"] = imag


def toString(numar):
    if getReal(numar) > 0 and getImag(numar) > 0:
        return "{} + {}i".format(
            getReal(numar),
            getImag(numar)
        )
    if getReal(numar) > 0 and getImag(numar) == 0:
        return "{}".format(
            getReal(numar)
        )
    if getReal(numar) > 0 and getImag(numar) < 0:
        return "{} {}i".format(
            getReal(numar),
            getImag(numar)
        )

    if getReal(numar) == 0 and getImag(numar) > 0:
        return "{}i".format(
            getImag(numar)
        )
    if getReal(numar) == 0 and getImag(numar) == 0:
        return 0
    if getReal(numar) == 0 and getImag(numar) < 0:
        return "{}i".format(
            getImag(numar)
        )

    if getReal(numar) < 0 and getImag(numar) > 0:
        return "{} + {}i".format(
            getReal(numar),
            getImag(numar)
        )
    if getReal(numar) < 0 and getImag(numar) == 0:
        return "{}".format(
            getReal(numar)
        )
    if getReal(numar) < 0 and getImag(numar) < 0:
        return "{} {}i".format(
            getReal(numar),
            getImag(numar)
        )
