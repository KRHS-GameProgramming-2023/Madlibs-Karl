


# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



label ifDebug(output):
    if config.developer:
        $ renpy.notify("[output]")
    return
############################################
# Character Organization
# character[ character number ][ data ][ data kwargs ] 
# [ data ]:
#   0 Name | 1 Gender | 2 Pronouns
#
#   Pronouns [ kwargs ]:
#
#       0 Subject | 1 Object | 2 Possessive | 3 Reflexive
#
############################################

    


    
label startOne:
    $ sotry = 1
    jump start

label startTwo:
    $ sotry = 2
    jump start

label startThree:
    $ sotry = 3
    jump start

label loadSwears:
    python:
        try:
            renpy.notify("Loading Swears")
            renpy.pause(.1)
            swearsImport = renpy.file("hell.txt", encoding="utf-8")
            swears = []
            for i in swearsImport:
                tempList = i.strip()
                swears.append(tempList)
            for i in range(0, len(swears)):
                swears[i] = swears[i].lower()
            del i
            del swearsImport
            ignoreSwears = True
        except:
            renpy.jump("swearsFailed")
    $ renpy.notify("Swears Loaded")
    jump start

label swearsFailed:
    if swearsFailedTimes < 10:
        $ renpy.notify("Failed to load swears. Trying again.")
        pause .5
        $ swearsFailedTimes += 1
        jump loadSwears
    else:
        call screen confirm(message="Failed to load swears.\nIgnore?", yes_action=Return(True), no_action=Return(False))
        $ swearsFailedTimes = 0
        if _return == True:
            $ renpy.notify("Swears will not be censored.")
            $ ignoreSwears = True
            jump loadSwears
        else:
            return
    $ renpy.notify("Swears failed to load.\nReturning to main menu.")
    pause(1.5)
    return

            

# The game starts here.
label start():
    scene main_menu
    pause .5 
    
    if ignoreSwears == False:
        jump loadSwears

    # if persistent.first_run == True:
    #     call first_run from _call_first_run
    # else:
    #     if config.developer == True:
    #         $ renpy.notify("first_run skipped because persistent.first_run is False")


    if sotry == 1:
        call createCharsWithErrorC(10)
        $ persistent.characters = character
        call sotry1 from _call_sotry1

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg pregen 02

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy
    # These display lines of dialogue.



    # This ends the game.
    python:
        character.clear()
        persistent.characters = character
    
    return
