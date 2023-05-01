from Tests.TestDomain import testDomain
from Tests.TestService import testService
from Tests.testUndo import testUndo
from UserInterface.UserInterface import runMenu


def main():
    testDomain()
    testService()
    testUndo()
    runMenu()


if __name__ == '__main__':
    main()
    exit(0)
