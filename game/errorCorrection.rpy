label correctNames(expectedNumber):
    $ expect = expectedNumber
    call names_errCorrect
    return


label names_errCorrect():
    python:
            for i in range(0,expect):
                try:
                    testNameSet = character[i][CharName]
                except:
                    charactersFailed += 1
    if charactersFailed > 0:
        call screen dialog(message="There was a problem defining the characters\nand [charactersFailed] more need to be made", ok_action=Return())
        call createCharacters(charactersFailed)
        jump correctNames
    return

label resetVariables():
        $ autoFillPrompts = False
        $ autoFillRejected = False