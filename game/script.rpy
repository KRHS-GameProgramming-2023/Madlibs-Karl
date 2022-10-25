


# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



label ifDebug(output):
    if config.developer:
        "Debug" "[output]"
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
            

# The game starts here.
label start():
    scene bg_start
    $ swearsImport = renpy.file("hell.txt", encoding="utf-8")
    python:
        swears = []
        for i in swearsImport:
            tempList = i.strip()
            swears.append(tempList)
        for i in range(0, len(swears)):
            swears[i] = swears[i].lower()
        del i
    $ del swearsImport

    if sotry == 1:
        call createCharacters(10) from _call_createCharacters
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

    return
