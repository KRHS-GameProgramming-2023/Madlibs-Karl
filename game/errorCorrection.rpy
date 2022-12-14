label createCharsWithErrorC(num):
    call createCharacters(num) from _call_createCharacters
    call correctNames(num) from _call_correctNames
    return

label correctNames(expectedNumber):
    python:
        if config.developer:
            renpy.notify("Checking for correct number of names.")
            renpy.pause(1)
    $ expect = expectedNumber
    $ charactersFailed = 0
    call names_errCorrect from _call_names_errCorrect
    return

label names_reCheck():
    python:
        if config.developer:
            renpy.notify("Rechecking names.")
            renpy.pause(1)
    $ charactersFailed = 0
    call names_errCorrect from _call_names_errCorrect_1
    return

label names_errCorrect():
    python:
            for i in range(0, expect):
                if config.developer:
                    renpy.notify("Checking name " + str(i))
                    # freeze for .5 seconds
                    renpy.pause(0.1)
                try:
                    testNameSet = character[i][CharName]
                except:
                    if config.developer:
                        renpy.notify("Name " + str(i) + " failed.")
                        renpy.pause(1)
                    charactersFailed += 1
    if charactersFailed > 0:
        $ renpy.notify("Something went wrong while defining the characters. " + str(charactersFailed) + " characters will now be created.")
        $ charsToCreate = charactersFailed
        call createCharacters(charsToCreate) from _call_createCharacters_1
        jump names_reCheck
    if config.developer == True:
        $ renpy.notify("All characters passed\nProgressing to next scene.")
        pause 3
    return

label resetVariables():
        $ autoFillPrompts = False
        $ autoFillRejected = False