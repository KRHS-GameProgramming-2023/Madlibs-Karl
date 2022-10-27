label char_name():
    label genRandName():
            $ randomName = renpy.random.choice(defaultNames)
            if randomName in names:
                jump genRandName
    $ defaulInp = randomName
    label char_name_prompt():
        call screen askForString(prompt="Enter a name", defaultInput=defaulInp)

    if _return.lower() in swears:
        $ renpy.notify('Name cannot be "' + _return + '"')
        $ defaulInp = randomName
        jump char_name_prompt
    if _return.lower() in names:
        $ renpy.notify('"' + _return + '" is already in use')
        $ defaulInp = _return
        jump char_name_prompt
    if _return.lower() == "":
        call screen dialog(message='Name cannot be blank', ok_action=Return())
        jump char_name
    if _return.lower() == " " or _return.lower() == "  " or _return.lower() == "   " or _return.lower() == "    " or _return.lower() == "     ":
        call screen dialog(message='how the fuck', ok_action=Return())
        jump char_name
    
    $ tempName = _return
    return


label char_gender():
    call screen def_charGender("Enter [tempName]'s gender")
    $ tempGender = _return
    python:
        if tempGender == "Female":
            tempPronounVar = ["She", "Her", "Hers", "Herself"]
        else:
            tempPronounVar = ["He", "Him", "His", "Himself"]

    return


label char_arrange:
    $ names.append(tempName)
    $ combinedList = [tempName, tempGender, tempPronounVar]
    $ character.append(combinedList)
    $ persistent.characters = character
    return


label chars_create():
    if autoFillRejected == False:
        if autoFillPrompts == False:
            call screen confirm("Auto fill character prompts?", yes_action=Return(True), no_action=Return(False))
        if _return == True or autoFillPrompts == True:
            $ autoFillPrompts = True

            label genRandNameAuto:
                $ randomName = renpy.random.choice(defaultNames)
                if randomName in names:
                    jump genRandNameAuto
            $ tempName = randomName
            $ tempGender = renpy.random.choice(["Female", "Male"])
            python:
                if tempGender == "Female":
                    tempPronounVar = ["She", "Her", "Hers", "Herself"]
                else:
                    tempPronounVar = ["He", "Him", "His", "Himself"]
            call char_arrange
        else:
            $ autoFillRejected = True
    else:
        call char_name from _call_char_name
        call char_gender from _call_char_gender
        call char_arrange
    python:
        charsToCreate -= 1
    if 0 < charsToCreate:
        jump chars_create
    else:
        return


label createCharacters(num, defaultName=["Hakaru","Shinomi","Kashita","Minomi","Nomuri","Zekaru","Osake","Rizoto","Chinomi","Kaguya","Asuka","Ake","Ohayou","Sayoru","Yuka","Minesa","Kazeshi","Yunomi","Shitana","Ritama","Tsunde","Yande","Demi","Zoski","Kazeshi","Nomita","Roku","Shiromi","Kasoki","Resoki","Rekezo","Shishi","Takesa","Noabeku","Taoshi","Mineme","Noshiko","Asano"]):
    $ charsToCreate = num
    $ defaultNames = defaultName
    call chars_create from _call_chars_create

    if config.developer == True:
        # list the names of the characters
        $ nameList = []
        $ i = 0
        $ numberOfChars = len(persistent.characters)
        while i < numberOfChars:
            $ tempName = persistent.characters[i][CharName]
            $ nameList.append(tempName)
            $ i += 1
        call screen dialog("Succesfully created [numberOfChars] characters.\n[nameList]", ok_action=Return())

    return


label getAColour():
    $ validInputColours = ["red", "green", "blue", "purple", "yellow", "white", "black", "orange", "pink", "purple", "brown", "grey", "gray", "silver", "gold", "cyan", "magenta", "lime"]
    call screen askForString(prompt="Enter a colour", defaultInput="White")
    $ colour = _return.lower()
    if colour in swears:
        call screen dialog(message='"[colour]" is a swear', ok_action=Return())
        jump getAColour
    else:
        if _return.lower() in validInputColours:
            return
        else:
            call screen dialog(message='Colour "[_return]" is not a known colour', ok_action=Return())
            jump getAColour


label getATime():
    call screen askForInt(prompt="Enter a time\nSeparate hours from minutes with a .", defaultInput="23.46", maxLength=24, otherAllowedCharacters=".")
    python:
        returnedFloat = float(_return)
        returnedInt = int(_return)
    $ minutesReturn = (returnedFloat - returnedInt)*100
    if minutes > 60 or returnedInt > 24 or minutes < 0 or returnedInt < 0:
        jump getATime
    $ hoursReturn = returnedInt
    return
    

